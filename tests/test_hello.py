"""
Tests for test_publish package.
"""

from test_publish import hello


def test_hello_default():
    """Test hello function with default argument."""
    assert hello() == "Hello, World!"


def test_hello_custom():
    """Test hello function with custom name."""
    assert hello("Python") == "Hello, Python!"


def test_hello_empty_string():
    """Test hello function with empty string."""
    assert hello("") == "Hello, !"

