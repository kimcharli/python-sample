"""Test package initialization."""

import python_sample


def test_version():
    """Test that version is defined."""
    assert hasattr(python_sample, "__version__")
    assert isinstance(python_sample.__version__, str)
