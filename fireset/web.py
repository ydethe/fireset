# Fireset
# Copyright (C) 2016-2017 Jelmer Vernooĳ <jelmer@jelmer.uk>, et al.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 3
# of the License or (at your option) any later version of
# the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.

"""Web server implementation..

This is the concrete web server implementation. It provides the
high level application logic that combines the WebDAV server,
the carddav support, the caldav support and the DAV store.
"""

from importlib import metadata
import functools
import hashlib
import logging
import os
import posixpath
import shutil
import urllib.parse
from collections.abc import Iterable, Iterator
from email.utils import parseaddr
from typing import Optional

from aiohttp import web
from aiohttp_basicauth_middleware import basic_auth_middleware
import jinja2

from . import settings

from . import (
    access,
    apache,
    caldav,
    carddav,
    infit,
    quota,
    scheduling,
    sync,
    timezones,
    webdav,
    xmpp,
)
from .store import (
    STORE_TYPE_ADDRESSBOOK,
    STORE_TYPE_CALENDAR,
    STORE_TYPE_OTHER,
    STORE_TYPE_PRINCIPAL,
    STORE_TYPE_SCHEDULE_INBOX,
    STORE_TYPE_SCHEDULE_OUTBOX,
    STORE_TYPE_SUBSCRIPTION,
    DuplicateUidError,
    File,
    InvalidCTag,
    InvalidFileContents,
    LockedError,
    NotStoreError,
    OutOfSpaceError,
)

from .icalendar import CalendarFilter, ICalendarFile
from .store.database import DatabaseStore
from .vcard import VCardFile

try:
    from asyncio import to_thread  # type: ignore
except ImportError:  # python < 3.8
    import contextvars
    from asyncio import events

    async def to_thread(func, *args, **kwargs):  # type: ignore
        loop = events.get_running_loop()
        ctx = contextvars.copy_context()
        func_call = functools.partial(ctx.run, func, *args, **kwargs)
        return await loop.run_in_executor(None, func_call)


logger = logging.getLogger("fireset_logger")
WELLKNOWN_DAV_PATHS = {
    caldav.WELLKNOWN_CALDAV_PATH,
    carddav.WELLKNOWN_CARDDAV_PATH,
}

STORE_CACHE_SIZE = 128
# TODO(jelmer): Make these configurable/dynamic
CALENDAR_HOME_SET = ["calendars"]
ADDRESSBOOK_HOME_SET = ["contacts"]

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR), enable_async=True)


async def render_jinja_page(
    name: str, accepted_content_languages: list[str], **kwargs
) -> tuple[Iterable[bytes], int, Optional[str], str, list[str]]:
    """Render a HTML page from jinja template.

    Args:
      name: Name of the page
      accepted_content_languages: List of accepted content languages
    Returns: Tuple of (body, content_length, etag, content_type, languages)
    """
    # TODO(jelmer): Support rendering other languages
    encoding = "utf-8"
    template = jinja_env.get_template(name)
    fireset_version = metadata.version("fireset")
    body = await template.render_async(
        version=fireset_version, urljoin=urllib.parse.urljoin, **kwargs
    )
    body_encoded = body.encode(encoding)
    return (
        [body_encoded],
        len(body_encoded),
        None,
        f"text/html; encoding={encoding}",
        ["en-UK"],
    )


def create_strong_etag(etag: str) -> str:
    """Create strong etags.

    Args:
      etag: basic etag
    Returns: A strong etag
    """
    return '"' + etag + '"'


def extract_strong_etag(etag: Optional[str]) -> Optional[str]:
    """Extract a strong etag from a string."""
    if etag is None:
        return etag
    return etag.strip('"')


class ObjectResource(webdav.Resource):
    """Object resource."""

    def __init__(
        self,
        store: DatabaseStore,
        name: str,
        content_type: str,
        etag: str,
        file: Optional[File] = None,
    ) -> None:
        self.store = store
        self.name = name
        self.etag = etag
        self.content_type = content_type
        self._file = file

    def __repr__(self) -> str:
        return "{}({!r}, {!r}, {!r}, {!r})".format(
            type(self).__name__,
            self.store,
            self.name,
            self.etag,
            self.get_content_type(),
        )

    async def get_file(self) -> File:
        if self._file is None:
            self._file = await to_thread(
                self.store.get_file, self.name, self.content_type, self.etag
            )
            assert self._file is not None
        return self._file

    async def get_body(self) -> Iterable[bytes]:
        file = await self.get_file()
        return file.content

    async def set_body(self, data, replace_etag=None):
        try:
            (name, etag) = await to_thread(
                self.store.import_one,
                self.name,
                self.content_type,
                data,
                replace_etag=extract_strong_etag(replace_etag),
            )
        except InvalidFileContents as exc:
            # TODO(jelmer): Not every invalid file is a calendar file..
            raise webdav.PreconditionFailure(
                "{%s}valid-calendar-data" % caldav.NAMESPACE,
                f"Not a valid calendar file: {exc.error}",
            ) from exc
        except DuplicateUidError as exc:
            raise webdav.PreconditionFailure(
                "{%s}no-uid-conflict" % caldav.NAMESPACE, "UID already in use."
            ) from exc
        except LockedError as exc:
            raise webdav.ResourceLocked() from exc
        return create_strong_etag(etag)

    def get_content_language(self) -> str:
        raise KeyError

    def get_content_type(self) -> str:
        return self.content_type

    async def get_content_length(self) -> int:
        return sum(map(len, await self.get_body()))

    async def get_etag(self) -> str:
        return create_strong_etag(self.etag)

    def get_supported_locks(self):
        return []

    def get_active_locks(self):
        return []

    def get_owner(self):
        return None

    def get_comment(self):
        raise KeyError

    def set_comment(self, comment):
        raise NotImplementedError(self.set_comment)

    def get_creationdate(self):
        # TODO(jelmer): Find creation date using store function
        raise KeyError

    def get_last_modified(self):
        # TODO(jelmer): Find last modified time using store function
        raise KeyError

    def get_is_executable(self):
        # TODO(jelmer): Retrieve POSIX mode and check for executability.
        return False

    def get_quota_used_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError

    def get_quota_available_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError

    def get_schedule_tag(self):
        # TODO(jelmer): Ask the store?
        raise KeyError


class StoreBasedCollection:
    def __init__(self, backend, relpath, store) -> None:
        self.backend = backend
        self.relpath = relpath
        self.store = store

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.store!r})"

    def set_resource_types(self, resource_types):
        # TODO(jelmer): Allow more than just this set; allow combining
        # addressbook/calendar.
        resource_types = set(resource_types)
        if resource_types == {
            caldav.CALENDAR_RESOURCE_TYPE,
            webdav.COLLECTION_RESOURCE_TYPE,
        }:
            self.store.set_type(STORE_TYPE_CALENDAR)
        elif resource_types == {
            carddav.ADDRESSBOOK_RESOURCE_TYPE,
            webdav.COLLECTION_RESOURCE_TYPE,
        }:
            self.store.set_type(STORE_TYPE_ADDRESSBOOK)
        elif resource_types == {webdav.PRINCIPAL_RESOURCE_TYPE}:
            self.store.set_type(STORE_TYPE_PRINCIPAL)
        elif resource_types == {
            caldav.SCHEDULE_INBOX_RESOURCE_TYPE,
            webdav.COLLECTION_RESOURCE_TYPE,
        }:
            self.store.set_type(STORE_TYPE_SCHEDULE_INBOX)
        elif resource_types == {
            caldav.SCHEDULE_OUTBOX_RESOURCE_TYPE,
            webdav.COLLECTION_RESOURCE_TYPE,
        }:
            self.store.set_type(STORE_TYPE_SCHEDULE_OUTBOX)
        elif resource_types == {webdav.COLLECTION_RESOURCE_TYPE}:
            self.store.set_type(STORE_TYPE_OTHER)
        elif resource_types == {
            webdav.COLLECTION_RESOURCE_TYPE,
            caldav.SUBSCRIPTION_RESOURCE_TYPE,
        }:
            self.store.set_type(STORE_TYPE_SUBSCRIPTION)
        else:
            raise NotImplementedError(self.set_resource_types)

    def _get_resource(
        self,
        name: str,
        content_type: str,
        etag: str,
        file: Optional[File] = None,
    ) -> webdav.Resource:
        return ObjectResource(self.store, name, content_type, etag, file=file)

    def _get_subcollection(self, name: str) -> webdav.Collection:
        return self.backend.get_resource(posixpath.join(self.relpath, name))

    def get_displayname(self) -> str:
        displayname = self.store.get_displayname()
        if displayname is None:
            return os.path.basename(self.store.repo.path)
        return displayname

    def set_displayname(self, displayname: str) -> None:
        self.store.set_displayname(displayname)

    def get_sync_token(self) -> str:
        return self.store.get_ctag()

    def get_ctag(self) -> str:
        return self.store.get_ctag()

    async def get_etag(self) -> str:
        return create_strong_etag(self.store.get_ctag())

    def members(self) -> Iterator[tuple[str, webdav.Resource]]:
        for name, content_type, etag in self.store.iter_with_etag():
            resource = self._get_resource(name, content_type, etag)
            yield (name, resource)
        for name, resource in self.subcollections():
            yield (name, resource)

    def subcollections(self):
        for name in self.store.subdirectories():
            yield (name, self._get_subcollection(name))

    def get_member(self, name):
        assert name != ""
        for fname, content_type, fetag in self.store.iter_with_etag():
            if name == fname:
                return self._get_resource(name, content_type, fetag)
        if name in self.store.subdirectories():
            return self._get_subcollection(name)
        raise KeyError(name)

    def delete_member(self, name, etag=None):
        assert name != ""
        self.store.delete_one(name, etag=extract_strong_etag(etag))

    async def create_member(
        self, name: str, contents: Iterable[bytes], content_type: str
    ) -> tuple[str, str]:
        try:
            (name, etag) = self.store.import_one(name, content_type, contents)
        except InvalidFileContents as exc:
            # TODO(jelmer): Not every invalid file is a calendar file..
            raise webdav.PreconditionFailure(
                "{%s}valid-calendar-data" % caldav.NAMESPACE,
                f"Not a valid calendar file: {exc.error}",
            ) from exc
        except DuplicateUidError as exc:
            raise webdav.PreconditionFailure(
                "{%s}no-uid-conflict" % caldav.NAMESPACE, "UID already in use."
            ) from exc
        except OutOfSpaceError as exc:
            raise webdav.InsufficientStorage() from exc
        except LockedError as exc:
            raise webdav.ResourceLocked() from exc
        return (name, create_strong_etag(etag))

    def iter_differences_since(
        self, old_token: str, new_token: str
    ) -> Iterator[tuple[str, Optional[webdav.Resource], Optional[webdav.Resource]]]:
        old_resource: Optional[webdav.Resource]
        new_resource: Optional[webdav.Resource]
        try:
            for (
                name,
                content_type,
                old_etag,
                new_etag,
            ) in self.store.iter_changes(old_token, new_token):
                if old_etag is not None:
                    old_resource = self._get_resource(name, content_type, old_etag)
                else:
                    old_resource = None
                if new_etag is not None:
                    new_resource = self._get_resource(name, content_type, new_etag)
                else:
                    new_resource = None
                yield (name, old_resource, new_resource)
        except InvalidCTag as exc:
            raise sync.InvalidToken(exc.ctag) from exc

    def get_owner(self):
        return None

    def get_supported_locks(self):
        return []

    def get_active_locks(self):
        return []

    def get_headervalue(self):
        raise KeyError

    def get_comment(self):
        return self.store.get_comment()

    def set_comment(self, comment):
        self.store.set_comment(comment)

    def get_creationdate(self):
        # TODO(jelmer): Find creation date using store function
        raise KeyError

    def get_last_modified(self):
        # TODO(jelmer): Find last modified time using store function
        raise KeyError

    def get_content_type(self):
        return "httpd/unix-directory"

    def get_content_language(self):
        raise KeyError

    async def get_content_length(self):
        raise KeyError

    def destroy(self) -> None:
        # RFC2518, section 8.6.2 says this should recursively delete.
        self.store.destroy()

    async def get_body(self):
        raise NotImplementedError(self.get_body)

    async def render(self, self_url, accepted_content_types, accepted_content_languages):
        content_types = webdav.pick_content_types(accepted_content_types, ["text/html"])
        assert content_types == ["text/html"]
        return await render_jinja_page(
            "collection.html",
            accepted_content_languages,
            collection=self,
            self_url=self_url,
        )

    def get_is_executable(self) -> bool:
        return False

    def get_quota_used_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError

    def get_quota_available_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError

    def get_refreshrate(self):
        # TODO(jelmer): Support setting refreshrate
        raise KeyError

    def set_refreshrate(self, value):
        # TODO(jelmer): Store refreshrate
        raise NotImplementedError(self.set_refreshrate)


class Collection(StoreBasedCollection, webdav.Collection):
    """A generic WebDAV collection."""


class ScheduleInbox(StoreBasedCollection, scheduling.ScheduleInbox):
    """A schedling inbox collection."""


class ScheduleOutbox(StoreBasedCollection, scheduling.ScheduleOutbox):
    """A schedling outbox collection."""


class SubscriptionCollection(StoreBasedCollection, caldav.Subscription):
    def get_source_url(self):
        source_url = self.store.get_source_url()
        if source_url is None:
            raise KeyError
        return source_url

    def set_source_url(self, url):
        self.store.set_source_url(url)

    def get_calendar_description(self):
        return self.store.get_description()

    def get_calendar_color(self):
        color = self.store.get_color()
        if not color:
            raise KeyError
        if color and color[0] != "#":
            color = "#" + color
        return color

    def set_calendar_color(self, color):
        self.store.set_color(color)

    def get_supported_calendar_components(self):
        return ["VEVENT", "VTODO", "VJOURNAL", "VFREEBUSY"]


class CalendarCollection(StoreBasedCollection, caldav.Calendar):
    def get_calendar_description(self):
        return self.store.get_description()

    def get_calendar_color(self):
        color = self.store.get_color()
        if not color:
            raise KeyError
        if color and color[0] != "#":
            color = "#" + color
        return color

    def set_calendar_color(self, color):
        self.store.set_color(color)

    def get_calendar_order(self):
        order = self.store.config.get_order()
        if not order:
            raise KeyError
        return order

    def set_calendar_order(self, order):
        self.store.config.set_order(order)

    def get_calendar_timezone(self):
        # TODO(jelmer): Read from config
        raise KeyError

    def set_calendar_timezone(self, content):
        raise NotImplementedError(self.set_calendar_timezone)

    def get_supported_calendar_components(self):
        return ["VEVENT", "VTODO", "VJOURNAL", "VFREEBUSY"]

    def get_supported_calendar_data_types(self):
        return [("text/calendar", "1.0"), ("text/calendar", "2.0")]

    def get_max_date_time(self):
        return "99991231T235959Z"

    def get_min_date_time(self):
        return "00010101T000000Z"

    def get_max_instances(self):
        raise KeyError

    def get_max_attendees_per_instance(self):
        raise KeyError

    def get_max_resource_size(self):
        # No resource limit
        raise KeyError

    def get_max_attachments_per_resource(self):
        # No resource limit
        raise KeyError

    def get_max_attachment_size(self):
        # No resource limit
        raise KeyError

    def get_schedule_calendar_transparency(self):
        # TODO(jelmer): Allow configuration in config
        return caldav.TRANSPARENCY_OPAQUE

    def get_managed_attachments_server_url(self):
        # TODO(jelmer)
        raise KeyError

    def calendar_query(self, create_filter_fn):
        filter = create_filter_fn(CalendarFilter)
        for name, file, etag in self.store.iter_with_filter(filter=filter):
            resource = self._get_resource(name, file.content_type, etag, file=file)
            yield (name, resource)

    def get_xmpp_heartbeat(self):
        # TODO
        raise KeyError

    def get_xmpp_server(self):
        # TODO
        raise KeyError

    def get_xmpp_uri(self):
        # TODO
        raise KeyError


class AddressbookCollection(StoreBasedCollection, carddav.Addressbook):
    def get_addressbook_description(self):
        return self.store.get_description()

    def set_addressbook_description(self, description):
        self.store.set_description(description)

    def get_supported_address_data_types(self):
        return [("text/vcard", "3.0")]

    def get_max_resource_size(self):
        # No resource limit
        raise KeyError

    def get_max_image_size(self):
        # No resource limit
        raise KeyError

    def set_addressbook_color(self, color):
        self.store.set_color(color)

    def get_addressbook_color(self):
        color = self.store.get_color()
        if not color:
            raise KeyError
        if color and color[0] != "#":
            color = "#" + color
        return color


class CollectionSetResource(webdav.Collection):
    """Resource for calendar sets."""

    def __init__(self, backend, relpath) -> None:
        self.backend = backend
        self.relpath = relpath

    @classmethod
    def create(cls, backend, relpath):
        path = backend._map_to_file_path(relpath)
        if not os.path.isdir(path):
            os.makedirs(path)
            logger.info("Creating %s", path)
        return cls(backend, relpath)

    def get_displayname(self):
        return posixpath.basename(self.relpath)

    def get_sync_token(self):
        raise KeyError

    async def get_etag(self):
        raise KeyError

    def get_ctag(self):
        raise KeyError

    def get_supported_locks(self):
        return []

    def get_active_locks(self):
        return []

    def get_owner(self):
        return None

    def members(self):
        p = self.backend._map_to_file_path(self.relpath)
        for name in os.listdir(p):
            if name.startswith("."):
                continue
            resource = self.get_member(name)
            yield (name, resource)

    def get_member(self, name):
        assert name != ""
        relpath = posixpath.join(self.relpath, name)
        p = self.backend._map_to_file_path(relpath)
        if not os.path.isdir(p):
            raise KeyError(name)
        return self.backend.get_resource(relpath)

    def get_headervalue(self):
        raise KeyError

    def get_comment(self):
        raise KeyError

    def set_comment(self, comment):
        raise NotImplementedError(self.set_comment)

    def get_content_type(self):
        return "httpd/unix-directory"

    def get_content_language(self):
        raise KeyError

    async def get_content_length(self):
        raise KeyError

    def get_last_modified(self):
        # TODO(jelmer): Find last modified time using store function
        raise KeyError

    def delete_member(self, name, etag=None):
        # This doesn't have any non-collection members.
        self.get_member(name).destroy()

    def destroy(self):
        p = self.backend._map_to_file_path(self.relpath)
        # RFC2518, section 8.6.2 says this should recursively delete.
        shutil.rmtree(p)

    async def render(self, self_url, accepted_content_types, accepted_content_languages):
        content_types = webdav.pick_content_types(accepted_content_types, ["text/html"])
        assert content_types == ["text/html"]
        return await render_jinja_page("root.html", accepted_content_languages, self_url=self_url)

    def get_is_executable(self):
        return False

    def get_quota_used_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError

    def get_quota_available_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError

    def get_creationdate(self):
        # TODO(jelmer): Find creation date using store function
        raise KeyError


class RootPage(webdav.Resource):
    """A non-DAV resource."""

    resource_types: list[str] = []

    def __init__(self, backend) -> None:
        self.backend = backend

    def render(self, self_url, accepted_content_types, accepted_content_languages):
        content_types = webdav.pick_content_types(accepted_content_types, ["text/html"])
        assert content_types == ["text/html"]
        return render_jinja_page(
            "root.html",
            accepted_content_languages,
            principals=self.backend.find_principals(),
            self_url=self_url,
        )

    async def get_body(self):
        raise KeyError

    async def get_content_length(self):
        raise KeyError

    def get_content_type(self):
        return "text/html"

    def get_supported_locks(self):
        return []

    def get_active_locks(self):
        return []

    async def get_etag(self):
        h = hashlib.md5()
        for c in await self.get_body():
            h.update(c)
        return h.hexdigest()

    def get_last_modified(self):
        raise KeyError

    def get_content_language(self):
        return ["en-UK"]

    def get_member(self, name):
        return self.backend.get_resource("/" + name)

    def delete_member(self, name, etag=None):
        # This doesn't have any non-collection members.
        self.get_member("/" + name).destroy()

    def get_is_executable(self):
        return False

    def get_quota_used_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError

    def get_quota_available_bytes(self):
        # TODO(jelmer): Ask the store?
        raise KeyError


class Principal(webdav.Principal):
    def get_principal_url(self):
        return "."

    def get_principal_address(self):
        raise KeyError

    def get_calendar_home_set(self):
        return CALENDAR_HOME_SET

    def get_addressbook_home_set(self):
        return ADDRESSBOOK_HOME_SET

    def get_calendar_user_address_set(self):
        # TODO(jelmer): Make this configurable
        ret = []
        try:
            (fullname, email) = parseaddr(os.environ["EMAIL"])
        except KeyError:
            pass
        else:
            ret.append("mailto:" + email)
        return ret

    def set_infit_settings(self, settings):
        relpath = posixpath.join(self.relpath, ".infit")
        p = self.backend._map_to_file_path(relpath)
        with open(p, "w") as f:
            f.write(settings)

    def get_infit_settings(self):
        relpath = posixpath.join(self.relpath, ".infit")
        p = self.backend._map_to_file_path(relpath)
        if not os.path.exists(p):
            raise KeyError
        with open(p) as f:
            return f.read()

    def get_group_membership(self):
        """Get group membership URLs."""
        return []

    def get_calendar_user_type(self):
        # TODO(jelmer)
        return scheduling.CALENDAR_USER_TYPE_INDIVIDUAL

    def get_calendar_proxy_read_for(self):
        # TODO(jelmer)
        return []

    def get_calendar_proxy_write_for(self):
        # TODO(jelmer)
        return []

    def get_owner(self):
        return None

    def get_schedule_outbox_url(self):
        raise KeyError

    def get_schedule_inbox_url(self):
        # TODO(jelmer): make this configurable
        return "inbox"

    def get_creationdate(self):
        raise KeyError


class PrincipalBare(CollectionSetResource, Principal):
    """Principal user resource."""

    resource_types = [webdav.PRINCIPAL_RESOURCE_TYPE]

    @classmethod
    def create(cls, backend, relpath):
        p = super().create(backend, relpath)
        to_create = set()
        to_create.update(p.get_addressbook_home_set())
        to_create.update(p.get_calendar_home_set())
        for n in to_create:
            try:
                backend.create_collection(posixpath.join(relpath, n))
            except FileExistsError:
                pass
        return p

    async def render(self, self_url, accepted_content_types, accepted_content_languages):
        content_types = webdav.pick_content_types(accepted_content_types, ["text/html"])
        assert content_types == ["text/html"]
        return await render_jinja_page(
            "principal.html",
            accepted_content_languages,
            principal=self,
            self_url=self_url,
        )

    def subcollections(self):
        # TODO(jelmer): Return members
        return []


class PrincipalCollection(Collection, Principal):
    """Principal user resource."""

    resource_types = webdav.Collection.resource_types + [webdav.PRINCIPAL_RESOURCE_TYPE]

    @classmethod
    def create(cls, backend, relpath):
        p = super().create(backend, relpath)
        p.store.set_type(STORE_TYPE_PRINCIPAL)
        to_create = set()
        to_create.update(p.get_addressbook_home_set())
        to_create.update(p.get_calendar_home_set())
        for n in to_create:
            try:
                backend.create_collection(posixpath.join(relpath, n))
            except FileExistsError:
                pass
        return p


@functools.lru_cache(maxsize=STORE_CACHE_SIZE)
def open_store_from_path(path: str, **kwargs):
    store = DatabaseStore.open_from_path(path, **kwargs)
    store.load_extra_file_handler(ICalendarFile)
    store.load_extra_file_handler(VCardFile)
    return store


class FiresetBackend(webdav.Backend):
    def __init__(
        self, path, *, paranoid: bool = False, index_threshold: Optional[int] = None
    ) -> None:
        self.path = path
        self._user_principals: set[str] = set()
        self.paranoid = paranoid
        self.index_threshold = index_threshold
        self.store = DatabaseStore.open_from_path(None)

    def _map_to_file_path(self, relpath):
        return os.path.join(self.path, relpath.lstrip("/"))

    def _mark_as_principal(self, path):
        self._user_principals.add(posixpath.normpath(path))

    def create_collection(self, relpath):
        return Collection(self, relpath, self.store)

    def create_principal(self, relpath, create_defaults=False):
        principal = PrincipalBare.create(self, relpath)
        self._mark_as_principal(relpath)
        if create_defaults:
            create_principal_defaults(self, principal)

    def find_principals(self):
        """List all of the principals on this server."""
        return self._user_principals

    def get_resource(self, relpath: str) -> webdav.Resource:
        relpath = posixpath.normpath(relpath)
        if not relpath.startswith("/"):
            raise ValueError(f"relpath %r should start with /. Got '{relpath}'")

        if relpath == "/":
            return RootPage(self)

        p = self._map_to_file_path(relpath)
        if p is None:
            return None

        if os.path.isdir(p):
            try:
                store = open_store_from_path(
                    p,
                    double_check_indexes=self.paranoid,
                    index_threshold=self.index_threshold,
                )
            except NotStoreError:
                if relpath in self._user_principals:
                    return PrincipalBare(self, relpath)
                return CollectionSetResource(self, relpath)
            else:
                return {
                    STORE_TYPE_CALENDAR: CalendarCollection,
                    STORE_TYPE_ADDRESSBOOK: AddressbookCollection,
                    STORE_TYPE_PRINCIPAL: PrincipalCollection,
                    STORE_TYPE_SCHEDULE_INBOX: ScheduleInbox,
                    STORE_TYPE_SCHEDULE_OUTBOX: ScheduleOutbox,
                    STORE_TYPE_SUBSCRIPTION: SubscriptionCollection,
                    STORE_TYPE_OTHER: Collection,
                }[store.get_type()](self, relpath, store)

        else:
            (basepath, name) = os.path.split(relpath)
            assert name != "", f"path is {relpath!r}"
            store = self.get_resource(basepath)
            if store is None:
                return None

            if webdav.COLLECTION_RESOURCE_TYPE not in store.resource_types:
                return None

            try:
                return store.get_member(name)

            except KeyError:
                return None


class FiresetApp(webdav.WebDAVApp):
    """A wsgi App that provides a Fireset web server."""

    def __init__(self, backend, current_user_principal, strict=True) -> None:
        super().__init__(backend, strict=strict)

        def get_current_user_principal(env):
            try:
                return current_user_principal % env
            except KeyError:
                return None

        self.register_properties(
            [
                webdav.ResourceTypeProperty(),
                webdav.CurrentUserPrincipalProperty(get_current_user_principal),
                webdav.PrincipalURLProperty(),
                webdav.DisplayNameProperty(),
                webdav.GetETagProperty(),
                webdav.GetContentTypeProperty(),
                webdav.GetContentLengthProperty(),
                webdav.GetContentLanguageProperty(),
                caldav.SourceProperty(),
                caldav.CalendarHomeSetProperty(),
                carddav.AddressbookHomeSetProperty(),
                caldav.CalendarDescriptionProperty(),
                caldav.CalendarColorProperty(),
                caldav.CalendarOrderProperty(),
                caldav.CreatedByProperty(),
                caldav.UpdatedByProperty(),
                caldav.SupportedCalendarComponentSetProperty(),
                carddav.AddressbookDescriptionProperty(),
                carddav.PrincipalAddressProperty(),
                webdav.AppleGetCTagProperty(),
                webdav.DAVGetCTagProperty(),
                carddav.SupportedAddressDataProperty(),
                webdav.SupportedReportSetProperty(self.reporters),
                sync.SyncTokenProperty(),
                caldav.SupportedCalendarDataProperty(),
                caldav.CalendarTimezoneProperty(),
                caldav.MinDateTimeProperty(),
                caldav.MaxDateTimeProperty(),
                caldav.MaxResourceSizeProperty(),
                carddav.MaxResourceSizeProperty(),
                carddav.MaxImageSizeProperty(),
                access.CurrentUserPrivilegeSetProperty(),
                access.OwnerProperty(),
                webdav.CreationDateProperty(),
                webdav.SupportedLockProperty(),
                webdav.LockDiscoveryProperty(),
                infit.AddressbookColorProperty(),
                infit.SettingsProperty(),
                infit.HeaderValueProperty(),
                webdav.CommentProperty(),
                scheduling.CalendarUserAddressSetProperty(),
                scheduling.ScheduleInboxURLProperty(),
                scheduling.ScheduleOutboxURLProperty(),
                scheduling.CalendarUserTypeProperty(),
                scheduling.ScheduleTagProperty(),
                webdav.GetLastModifiedProperty(),
                timezones.TimezoneServiceSetProperty([]),
                webdav.AddMemberProperty(),
                caldav.ScheduleCalendarTransparencyProperty(),
                scheduling.ScheduleDefaultCalendarURLProperty(),
                caldav.MaxInstancesProperty(),
                caldav.MaxAttendeesPerInstanceProperty(),
                access.GroupMembershipProperty(),
                apache.ExecutableProperty(),
                caldav.CalendarProxyReadForProperty(),
                caldav.CalendarProxyWriteForProperty(),
                caldav.MaxAttachmentSizeProperty(),
                caldav.MaxAttachmentsPerResourceProperty(),
                caldav.ManagedAttachmentsServerURLProperty(),
                quota.QuotaAvailableBytesProperty(),
                quota.QuotaUsedBytesProperty(),
                webdav.RefreshRateProperty(),
                xmpp.XmppUriProperty(),
                xmpp.XmppServerProperty(),
                xmpp.XmppHeartbeatProperty(),
            ]
        )
        self.register_reporters(
            [
                caldav.CalendarMultiGetReporter(),
                caldav.CalendarQueryReporter(),
                carddav.AddressbookMultiGetReporter(),
                carddav.AddressbookQueryReporter(),
                webdav.ExpandPropertyReporter(),
                sync.SyncCollectionReporter(),
                caldav.FreeBusyQueryReporter(),
            ]
        )
        self.register_methods(
            [
                caldav.MkcalendarMethod(),
            ]
        )


def create_principal_defaults(backend, principal):
    """Create default calendar and addressbook for a principal.

    Args:
      backend: Backend in which the principal exists.
      principal: Principal object
    """
    calendar_path = posixpath.join(
        principal.relpath, principal.get_calendar_home_set()[0], "calendar"
    )
    _ = backend.create_collection(calendar_path)
    addressbook_path = posixpath.join(
        principal.relpath,
        principal.get_addressbook_home_set()[0],
        "addressbook",
    )
    _ = backend.create_collection(addressbook_path)
    calendar_path = posixpath.join(principal.relpath, principal.get_schedule_inbox_url())
    _ = backend.create_collection(calendar_path)


class RedirectDavHandler:
    def __init__(self, dav_root: str) -> None:
        self._dav_root = dav_root

    async def __call__(self, request):
        from aiohttp import web

        return web.HTTPFound(self._dav_root)


async def main_web_build_app():
    if not settings.current_user_principal.startswith("/"):
        current_user_principal = "/" + settings.current_user_principal

    backend = FiresetBackend(
        os.path.abspath(settings.directory),
        paranoid=settings.paranoid,
        index_threshold=settings.index_threshold,
    )
    backend._mark_as_principal(current_user_principal)

    if settings.autocreate or settings.defaults:
        if not os.path.isdir(settings.directory):
            os.makedirs(settings.directory)
        backend.create_principal(current_user_principal, create_defaults=settings.defaults)

    if not os.path.isdir(settings.directory):
        logger.warning(
            "%r does not exist. Run fireset with --autocreate?",
            settings.directory,
        )
    if not backend.get_resource(current_user_principal):
        logger.warning(
            "default user principal %s does not exist. " "Run fireset with --autocreate?",
            current_user_principal,
        )

    main_app = FiresetApp(
        backend,
        current_user_principal=current_user_principal,
        strict=settings.strict,
    )

    async def fireset_handler(request):
        return await main_app.aiohttp_handler(request, "/")

    from aiohttp import web

    app = web.Application()

    app.middlewares.append(
        basic_auth_middleware(
            ("/",),
            {settings.fireset_user: settings.fireset_password},
        )
    )

    for path in WELLKNOWN_DAV_PATHS:
        app.router.add_route("*", path, RedirectDavHandler("/").__call__)

    app.router.add_route("*", "/{path_info:.*}", fireset_handler)

    return app


def main_web_run():
    app = main_web_build_app()
    web.run_app(
        app=app,
        port=3665,
        access_log=logger,
        access_log_format='%{X-Real-Ip}i %t "%r" %s %b "%{Referer}i" "%{User-Agent}i"',
    )
