"""Test that DBObject works as expected."""

from ymldb.dbobject import DBObject
from ymldb.location import Location


def test_dbobject_instantiation() -> None:
    """Test that we can create a DB Object."""
    dbo = DBObject(raw_data={}, location=Location(container=[], name=""))

    assert dbo.raw_data == {}
    assert dbo.location.name == ""
    assert dbo.location.container == []
