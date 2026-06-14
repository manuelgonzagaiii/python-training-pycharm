"""Dynamic dispatch with getattr/hasattr/callable

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations


def public_callables(obj) -> dict[str, object]:
    """Map public (no leading underscore) callable attribute names -> the callable.

    Use dir()/getattr()/callable(). Skip names starting with '_'.
    """
    raise NotImplementedError


def dispatch(service, verb: str, /, **kwargs):
    """Resolve `verb` on `service` and call it with kwargs.

    Raise LookupError if verb is missing, private, or not callable.
    """
    raise NotImplementedError

"""

# Your code here.
