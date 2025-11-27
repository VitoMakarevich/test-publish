"""
Test Publish Package

A minimal Python package for testing PyPI publishing.
"""

__version__ = "1.1.0"

__all__ = ["__version__", "hello"]


def hello(name: str = "World") -> str:
    """
    Return a greeting message.

    Args:
        name: The name to greet (default: "World")

    Returns:
        A greeting string
    """
    return f"Hello, {name}!"

