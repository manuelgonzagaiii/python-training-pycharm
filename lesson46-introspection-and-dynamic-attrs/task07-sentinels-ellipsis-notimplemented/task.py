"""Sentinels: Ellipsis, NotImplemented, NotImplementedError

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations


class _Missing:
    """Unique sentinel distinct from None. Use `is MISSING` to test."""
    __slots__ = ()
    def __repr__(self) -> str: return "MISSING"


MISSING = _Missing()


def apply_patch(record: dict, **changes) -> dict:
    """Return updated copy: keys whose value is MISSING are left unchanged;
    an explicit None overwrites with None."""
    raise NotImplementedError


class Money:
    def __init__(self, cents: int): self.cents = cents
    def __eq__(self, other) -> bool:
        """Compare by cents with another Money; return NotImplemented otherwise."""
        raise NotImplementedError
    def __hash__(self) -> int: return hash(self.cents)

"""

# Your code here.
