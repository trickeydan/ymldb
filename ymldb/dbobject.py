"""
Object Classes.

In YMLDb, an object is a file containing some data that conforms to a specific schema.

An object has some data and a location within the DB.
"""

import attr
from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from .location import Location  # pragma: nocover


@attr.s(auto_attribs=True)
class DBObject:
    """
    The object class.

    In YMLDb, an object is a file containing some data that conforms to a specific schema.

    An object has some data and a location within the DB.
    """

    raw_data: Dict[str, Any]
    location: 'Location'
    # schema: 'Schema'
