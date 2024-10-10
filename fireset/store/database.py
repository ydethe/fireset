import typing as T

from . import Store


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
        pass

    def _get_raw(self, name: str, etag: T.Optional[str] = None) -> T.Iterable[bytes]:
        """Get the raw contents of an object.

        Args:
          name: Filename
          etag: Optional etag to return
        Returns: raw contents
        """
        pass

    def get_ctag(self) -> str:
        """Return the ctag for this store."""
        raise NotImplementedError(self.get_ctag)

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
        pass

    def delete_one(
        self,
        name: str,
        message: T.Optional[str] = None,
        author: T.Optional[str] = None,
        etag: T.Optional[str] = None,
    ) -> None:
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

    def set_type(self, store_type: str) -> None:
        """Set store type.

        Args:
          store_type: New store type (one of VALID_STORE_TYPES)
        """
        pass

    def set_description(self, description: str) -> None:
        """Set the extended description of this store.

        Args:
          description: String with description
        """
        pass

    def get_description(self) -> str:
        """Get the extended description of this store."""
        pass

    def get_displayname(self) -> str:
        """Get the display name of this store."""
        pass

    def set_displayname(self, displayname: str) -> None:
        """Set the display name of this store."""
        pass

    def get_color(self) -> str:
        """Get the color code for this store."""
        pass

    def set_color(self, color: str) -> None:
        """Set the color code for this store."""
        pass

    def iter_changes(self, old_ctag: str, new_ctag: str) -> T.Iterator[tuple[str, str, str, str]]:
        """Get changes between two versions of this store.

        Args:
          old_ctag: Old ctag (None for empty Store)
          new_ctag: New ctag
        Returns: Iterator over (name, content_type, old_etag, new_etag)
        """
        pass

    def get_comment(self) -> str:
        """Retrieve store comment.

        Returns: Comment
        """
        pass

    def set_comment(self, comment: str) -> None:
        """Set comment.

        Args:
          comment: New comment to set
        """
        pass

    def destroy(self) -> None:
        """Destroy this store."""
        pass

    def subdirectories(self) -> T.Iterator[str]:
        """Returns subdirectories to probe for other stores.

        Returns: List of names
        """
        pass

    def get_source_url(self) -> str:
        """Return source URL, if this is a subscription."""
        pass

    def set_source_url(self, url: str) -> None:
        """Set the source URL."""
        pass

    @classmethod
    def open_from_path(cls, path, **kwargs):
        """Open a GitStore from a path.

        Args:
          path: Path
        Returns: A `GitStore`
        """
        pass
