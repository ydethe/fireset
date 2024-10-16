import typing as T
import logging
from uuid import UUID

from . import Store
from .index import MemoryIndex
from .db_connection import get_db_vcard_by_etag, list_vcard_ids


logger = logging.getLogger("fireset_logger")


class DatabaseStore(Store):
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
