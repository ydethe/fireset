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

"""Stores and store sets.

ETags (https://en.wikipedia.org/wiki/HTTP_ETag) used in this file
are always strong, and should be returned without wrapping quotes.
"""

import logging
import mimetypes
from collections.abc import Iterable, Iterator
from typing import Optional

from .index import IndexDict, IndexKey, IndexValueIterator


logger = logging.getLogger("fireset_logger")


STORE_TYPE_ADDRESSBOOK = "addressbook"
STORE_TYPE_CALENDAR = "calendar"
STORE_TYPE_PRINCIPAL = "principal"
STORE_TYPE_SCHEDULE_INBOX = "schedule-inbox"
STORE_TYPE_SCHEDULE_OUTBOX = "schedule-outbox"
STORE_TYPE_SUBSCRIPTION = "subscription"
STORE_TYPE_OTHER = "other"
VALID_STORE_TYPES = (
    STORE_TYPE_ADDRESSBOOK,
    STORE_TYPE_CALENDAR,
    STORE_TYPE_PRINCIPAL,
    STORE_TYPE_SCHEDULE_INBOX,
    STORE_TYPE_SCHEDULE_OUTBOX,
    STORE_TYPE_SUBSCRIPTION,
    STORE_TYPE_OTHER,
)

MIMETYPES = mimetypes.MimeTypes()
MIMETYPES.add_type("text/calendar", ".ics")  # type: ignore
MIMETYPES.add_type("text/vcard", ".vcf")  # type: ignore

DEFAULT_MIME_TYPE = "application/octet-stream"


class InvalidCTag(Exception):
    """The request CTag can not be retrieved."""

    def __init__(self, ctag) -> None:
        self.ctag = ctag


class File:
    """A file type handler."""

    content: Iterable[bytes]
    content_type: str

    def __init__(self, content: Iterable[bytes], content_type: str) -> None:
        self.content = content
        self.content_type = content_type

    def validate(self) -> None:
        """Verify that file contents are valid.

        :raise InvalidFileContents: Raised if a file is not valid
        """

    def normalized(self) -> Iterable[bytes]:
        """Return a normalized version of the file."""
        return self.content

    def describe(self, name: str) -> str:
        """Describe the contents of this file.

        Used in e.g. commit messages.
        """
        return name

    def get_uid(self) -> str:
        """Return UID.

        :raise NotImplementedError: If UIDs aren't supported for this format
        :raise KeyError: If there is no UID set on this file
        :raise InvalidFileContents: If the file is misformatted
        Returns: UID
        """
        raise NotImplementedError(self.get_uid)

    def describe_delta(self, name: str, previous: Optional["File"]) -> Iterator[str]:
        """Describe the important difference between this and previous one.

        Args:
          name: File name
          previous: Previous file to compare to.

        Raises:
          InvalidFileContents: If the file is misformatted
        Returns: List of strings describing change
        """
        assert name is not None
        item_description = self.describe(name)
        assert item_description is not None
        if previous is None:
            yield "Added " + item_description
        else:
            yield "Modified " + item_description

    def _get_index(self, key: IndexKey) -> IndexValueIterator:
        """Obtain an index for this file.

        Args:
          key: Index key
        Returns:
          iterator over index values
        """
        raise NotImplementedError(self._get_index)

    def get_indexes(self, keys: Iterable[IndexKey]) -> IndexDict:
        """Obtain indexes for this file.

        Args:
          keys: Iterable of index keys
        Returns: Dictionary mapping key names to values
        """
        ret = {}
        for k in keys:
            ret[k] = list(self._get_index(k))
        return ret


class Filter:
    """A filter that can be used to query for certain resources.

    Filters are often resource-type specific.
    """

    content_type: str

    def check(self, name: str, resource: File) -> bool:
        """Check if this filter applies to a resource.

        Args:
          name: Name of the resource
          resource: File object
        Returns: boolean
        """
        raise NotImplementedError(self.check)

    def index_keys(self) -> list[IndexKey]:
        """Returns a list of indexes that could be used to apply this filter.

        Returns: AND-list of OR-options
        """
        raise NotImplementedError(self.index_keys)

    def check_from_indexes(self, name: str, indexes: IndexDict) -> bool:
        """Check from a set of indexes whether a resource matches.

        Args:
          name: Name of the resource
          indexes: Dictionary mapping index names to values
        Returns: boolean
        """
        raise NotImplementedError(self.check_from_indexes)


def open_by_content_type(content: Iterable[bytes], content_type: str, extra_file_handlers) -> File:
    """Open a file based on content type.

    Args:
      content: list of bytestrings with content
      content_type: MIME type
    Returns: File instance
    """
    return extra_file_handlers.get(content_type.split(";")[0], File)(content, content_type)


def open_by_extension(
    content: Iterable[bytes],
    name: str,
    extra_file_handlers: dict[str, type[File]],
) -> File:
    """Open a file based on the filename extension.

    Args:
      content: list of bytestrings with content
      name: Name of file to open
    Returns: File instance
    """
    (mime_type, _) = MIMETYPES.guess_type(name)
    if mime_type is None:
        mime_type = DEFAULT_MIME_TYPE
    return open_by_content_type(content, mime_type, extra_file_handlers=extra_file_handlers)


class DuplicateUidError(Exception):
    """UID already exists in store."""

    def __init__(self, uid: str, existing_name: str, new_name: str) -> None:
        self.uid = uid
        self.existing_name = existing_name
        self.new_name = new_name


class NoSuchItem(Exception):
    """No such item."""

    def __init__(self, name: str) -> None:
        self.name = name


class InvalidETag(Exception):
    """Unexpected value for etag."""

    def __init__(self, name: str, expected_etag: str, got_etag: str) -> None:
        self.name = name
        self.expected_etag = expected_etag
        self.got_etag = got_etag


class NotStoreError(Exception):
    """Not a store."""

    def __init__(self, path: str) -> None:
        self.path = path


class InvalidFileContents(Exception):
    """Invalid file contents."""

    def __init__(self, content_type: str, data, error) -> None:
        self.content_type = content_type
        self.data = data
        self.error = error


class OutOfSpaceError(Exception):
    """Out of disk space."""

    def __init__(self) -> None:
        pass


class LockedError(Exception):
    """File or store being accessed is locked."""

    def __init__(self, path: str) -> None:
        self.path = path
