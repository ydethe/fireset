import typing as T
import logging
from uuid import UUID
import mimetypes
from collections.abc import Iterator
from typing import Optional

from .db_connection import get_db_vcard_by_etag, list_vcard_ids
from .index import Index, MemoryIndex, AutoIndexManager
from . import File, Filter, InvalidFileContents, open_by_extension, open_by_content_type

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


class DatabaseStore(object):
    """A object store."""

    extra_file_handlers: dict[str, type[File]]

    def __init__(
        self,
        index: Index,
        *,
        double_check_indexes: bool = False,
        index_threshold: Optional[int] = None,
    ) -> None:
        self.extra_file_handlers = {}
        self.index = index
        self.index_manager = AutoIndexManager(self.index, threshold=index_threshold)
        self.double_check_indexes = double_check_indexes

    def load_extra_file_handler(self, file_handler: type[File]) -> None:
        self.extra_file_handlers[file_handler.content_type] = file_handler

    def iter_with_filter(self, filter: Filter) -> Iterator[tuple[str, File, str]]:
        """Iterate over all items in the store that match a particular filter.

        Args:
          filter: Filter to apply
        Returns: iterator over (name, file, etag) tuples
        """
        if self.index_manager is not None:
            try:
                necessary_keys = filter.index_keys()
            except NotImplementedError:
                pass
            else:
                present_keys = self.index_manager.find_present_keys(necessary_keys)
                if present_keys is not None:
                    return self._iter_with_filter_indexes(filter, present_keys)
        return self._iter_with_filter_naive(filter)

    def _iter_with_filter_naive(self, filter: Filter) -> Iterator[tuple[str, File, str]]:
        for name, content_type, etag in self.iter_with_etag():
            if not filter.content_type == content_type:
                continue
            file = self.get_file(name, content_type, etag)
            try:
                if filter.check(name, file):
                    yield (name, file, etag)
            except InvalidFileContents:
                logger.warning("Unable to parse file %s, skipping.", name)

    def _iter_with_filter_indexes(self, filter: Filter, keys) -> Iterator[tuple[str, File, str]]:
        for name, content_type, etag in self.iter_with_etag():
            if not filter.content_type == content_type:
                continue
            try:
                file_values = self.index.get_values(name, etag, keys)
            except KeyError:
                # Index values not yet present for this file.
                file = self.get_file(name, content_type, etag)
                try:
                    file_values = file.get_indexes(self.index.available_keys())
                except InvalidFileContents:
                    logger.warning("Unable to parse file %s for indexing, skipping.", name)
                    file_values = {}
                self.index.add_values(name, etag, file_values)
                if filter.check_from_indexes(name, file_values):
                    yield (name, file, etag)
            else:
                if file_values is None:
                    continue
                file = self.get_file(name, content_type, etag)
                if self.double_check_indexes:
                    if file_values != file.get_indexes(keys):
                        raise AssertionError(f"{file_values!r} != {file.get_indexes(keys)!r}")
                    if filter.check_from_indexes(name, file_values) != filter.check(name, file):
                        raise AssertionError(
                            f"index based filter {filter} "
                            f"(values: {file_values}) not matching "
                            "real file filter"
                        )
                if filter.check_from_indexes(name, file_values):
                    file = self.get_file(name, content_type, etag)
                    yield (name, file, etag)

    def get_file(
        self,
        name: str,
        content_type: Optional[str] = None,
        etag: Optional[str] = None,
    ) -> File:
        """Get the contents of an object.

        Returns: A File object
        """
        if content_type is None:
            return open_by_extension(
                self._get_raw(name, etag),
                name,
                extra_file_handlers=self.extra_file_handlers,
            )
        else:
            return open_by_content_type(
                self._get_raw(name, etag),
                content_type,
                extra_file_handlers=self.extra_file_handlers,
            )

    def get_type(self) -> str:
        """Get type of this store.

        Returns: one of VALID_STORE_TYPES
        """
        ret = STORE_TYPE_OTHER
        for name, content_type, etag in self.iter_with_etag():
            if content_type == "text/calendar":
                ret = STORE_TYPE_CALENDAR
            elif content_type == "text/vcard":
                ret = STORE_TYPE_ADDRESSBOOK
        return ret

    def iter_with_etag(self, ctag: T.Optional[str] = None) -> T.Iterator[tuple[str, str, str]]:
        """Iterate over all items in the store with etag.

        content_type can be one of:
        - "text/calendar"
        - "text/vcard"

        Args:
            ctag: Possible ctag to iterate for
        Returns: iterator over (name, content_type, etag) tuples
        """
        for etag in list_vcard_ids():
            name = f"{etag}.vcf"
            yield (name, "text/vcard", etag)

    def _get_raw(self, name: str, etag: T.Optional[str] = None) -> T.Iterable[bytes]:
        """Get the raw contents of an object.

        Args:
            name: Filename
            etag: Optional etag to return
        Returns: raw contents
        """
        etag = UUID(name[:-4])
        vcard = get_db_vcard_by_etag(etag)
        data = vcard.toVcard()
        return [data]

    def get_ctag(self) -> str:
        """Return the ctag for this store."""
        return "ctag1"

    def import_one(
        self,
        name: str,
        content_type: str,
        data: T.Iterable[bytes],
        message: T.Optional[str] = None,
        author: T.Optional[str] = None,
        replace_etag: T.Optional[str] = None,
    ) -> tuple[str, str]:
        """Import a single object.

        Args:
            name: Name of the object
            content_type: Content type of the object
            data: serialized object as list of bytes
            message: Commit message
            author: Optional author
            replace_etag: Etag to replace
        Raise:
            NameExists: when the name already exists
            DuplicateUidError: when the uid already exists
        Returns: (name, etag)
        """
        logger.info(f"{name}: {data}")
        if content_type == "text/vcard":
            vcard = get_db_vcard_by_etag(name)
            logger.debug(f"{vcard.nom}")
        return name, "etag1"

    def delete_one(
        self,
        name: str,
        message: T.Optional[str] = None,
        author: T.Optional[str] = None,
        etag: T.Optional[str] = None,
    ):
        """Delete an item.

        Args:
            name: Filename to delete
            message: Commit message
            author: Optional author
            etag: Optional mandatory etag of object to remove
        Raises:
            NoSuchItem: when the item doesn't exist
            InvalidETag: If the specified ETag doesn't match the current
        """
        pass

    def set_type(self, store_type: str):
        """Set store type.

        Args:
            store_type: New store type (one of VALID_STORE_TYPES)
        """
        pass

    def set_description(self, description: str):
        """Set the extended description of this store.

        Args:
            description: String with description
        """
        pass

    def get_description(self) -> str:
        """Get the extended description of this store."""
        return "fireset description"

    def get_displayname(self) -> str:
        """Get the display name of this store."""
        return "fireset"

    def set_displayname(self, displayname: str):
        """Set the display name of this store."""
        pass

    def get_color(self) -> str:
        """Get the color code for this store."""
        return "blue"

    def set_color(self, color: str):
        """Set the color code for this store."""
        pass

    def iter_changes(self, old_ctag: str, new_ctag: str) -> T.Iterator[tuple[str, str, str, str]]:
        """Get changes between two versions of this store.

        Args:
            old_ctag: Old ctag (None for empty Store)
            new_ctag: New ctag
        Returns: Iterator over (name, content_type, old_etag, new_etag)
        """
        return []

    def get_comment(self) -> str:
        """Retrieve store comment.

        Returns: Comment
        """
        return "comment"

    def set_comment(self, comment: str):
        """Set comment.

        Args:
            comment: New comment to set
        """
        pass

    def destroy(self):
        """Destroy this store."""
        pass

    def subdirectories(self) -> T.Iterator[str]:
        """Returns subdirectories to probe for other stores.

        Returns: List of names
        """
        return []

    def get_source_url(self) -> str:
        """Return source URL, if this is a subscription."""
        return "source url"

    def set_source_url(self, url: str):
        """Set the source URL."""
        pass

    @classmethod
    def open_from_path(cls, path, **kwargs):
        """Open a DatabaseStore from a path.

        Args:
            path: Path
        Returns: A `DatabaseStore`
        """
        return DatabaseStore(MemoryIndex(), **kwargs)
