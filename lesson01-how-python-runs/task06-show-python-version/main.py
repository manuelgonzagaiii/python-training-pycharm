"""MiniERP entry point.

Running this file starts MiniERP and prints a short banner: a welcome line and the
version of Python that is actually running the program. Importing it does nothing
visible.
"""
import sys


def welcome() -> str:
    """Return the line shown when MiniERP starts."""
    return "Welcome to MiniERP"


def python_line() -> str:
    """Return a line that reports the Python version running this program."""
    version = sys.version_info
    return f"Running on Python {version.major}.{version.minor}.{version.micro}"


if __name__ == "__main__":
    print(welcome())
    print(python_line())
