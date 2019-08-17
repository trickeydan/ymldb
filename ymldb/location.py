"""
Location Classes.

In YMLDb, a location describes the path at which we can find an object.
"""

from typing import Sequence


class Location:
    """
    The location class.

    In YMLDb, a location describes the path at which we can find an object.
    """

    container: Sequence[str]
    name: str

    def __init__(
        self,
        *,
        container: Sequence[str] = [],
        name: str,
    ) -> None:
        self.container = container
        self.name = name

    def __str__(self) -> str:
        """Get a string representation."""
        if len(self.container) == 0:
            return f".{self.name}"
        else:
            return f".{'.'.join(self.container)}.{self.name}"
