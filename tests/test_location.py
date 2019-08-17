"""Test that location works as expected."""

from ymldb.location import Location


def test_location_instantiation() -> None:
    """Test that we can create location objects."""
    location = Location(container=[], name="beans")

    assert location.container == []
    assert location.name == "beans"


def test_location_to_str() -> None:
    """Test that we can get a string representation."""
    location = Location(container=[], name="beans")
    assert str(location) == ".beans"

    location = Location(container=["a"], name="beans")
    assert str(location) == ".a.beans"

    location = Location(container=["a", "b"], name="beans")
    assert str(location) == ".a.b.beans"

    location = Location(container=["a", "b"], name="")
    assert str(location) == ".a.b."
