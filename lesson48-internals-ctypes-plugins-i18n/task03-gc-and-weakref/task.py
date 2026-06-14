"""Cycles, gc and weakref caches

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import weakref


class IdentityMap:
    """Cache entities by id, holding them weakly so they can be collected."""
    def __init__(self) -> None:
        self._cache: weakref.WeakValueDictionary = weakref.WeakValueDictionary()
    def get(self, key):
        raise NotImplementedError
    def put(self, key, entity) -> None:
        raise NotImplementedError


def on_finalize(entity, callback) -> weakref.finalize:
    """Register weakref.finalize(entity, callback) and return the finalizer."""
    raise NotImplementedError

"""

# Your code here.
