"""MiniERP entry point.

Running this file starts MiniERP. Importing it from another file must do nothing
visible, so the rest of the program can reuse welcome() without side effects.
"""


def welcome() -> str:
    """Return the line shown when MiniERP starts."""
    return "Welcome to MiniERP"


if __name__ == "__main__":
    print(welcome())
