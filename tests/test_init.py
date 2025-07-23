"""Test package initialization."""

import directives


def test_version():
    """Test that version is defined."""
    assert hasattr(directives, "__version__")
    assert isinstance(directives.__version__, str)