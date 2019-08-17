"""Test that the version number is a string."""

from ymldb import __version__


def test_version_string() -> None:
    """Test that the version number of the module is a string."""
    assert isinstance(__version__, str)
