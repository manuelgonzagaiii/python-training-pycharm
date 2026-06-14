# Cycles, gc and weakref caches

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.3 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create and detect a reference cycle and force its collection with gc.collect
- Register a gc callback to observe collection cycles
- Build a weakref-based identity map so cached records are GC'd when unused
- Use weakref.finalize for deterministic cleanup instead of fragile __del__

## Python features introduced
`gc.collect`, `gc.get_objects / gc.garbage`, `gc.callbacks`, `reference cycles`, `weakref.ref / weakref.proxy`, `weakref.WeakValueDictionary`, `weakref.finalize`, `__del__ vs finalize`

## MiniERP increment
Adds erp/cache.py: a WeakValueDictionary identity-map cache for loaded ERP entities (so cached records vanish when no longer referenced, avoiding leaks), with weakref.finalize closing per-entity resources and a gc callback feeding collection stats to diagnostics.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
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

- **Test focus:** Tests IdentityMap returns a live cached entity then drops it after the strong ref is deleted and gc.collect() runs; tests on_finalize's callback fires when the entity is collected; verifies a deliberately-built cycle is reclaimed by gc.collect().

</div>
