"""MiniERP entry point.

Running this file starts MiniERP and prints a short banner. Importing it does
nothing visible, so other code can reuse these helpers without side effects.
"""
import sys


def welcome() -> str:
    """Return the line shown when MiniERP starts."""
    return "Welcome to MiniERP"


def python_line() -> str:
    """Return a line that reports the Python version running this program."""
    version = sys.version_info
    return f"Running on Python {version.major}.{version.minor}.{version.micro}"


def describe(value) -> str:
    """Return a short string naming a value's type, for example '42 is a int'."""
    return f"{value!r} is a {type(value).__name__}"


def same_object(a, b) -> bool:
    """Return True only if a and b are the SAME object (identity, not equality)."""
    return a is b


if __name__ == "__main__":
    print(welcome())
    print(python_line())
