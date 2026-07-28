"""Package bootstrap tests."""

import goalauthbench


def test_package_is_importable() -> None:
    """The installed package exposes the expected module."""
    assert goalauthbench.__name__ == "goalauthbench"
