"""
Location Classes.

In YMLDb, a location describes the path at which we can find an object.
"""
import attr
from typing import Sequence


@attr.s(auto_attribs=True)
class Location:
    """
    The location class.

    In YMLDb, a location describes the path at which we can find an object.
    """

    container: Sequence[str]
    name: str

    def __str__(self) -> str:
        """Get a string representation."""
        if len(self.container) == 0:
            return f".{self.name}"
        else:
            return f".{'.'.join(self.container)}.{self.name}"
