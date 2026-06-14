# Leak-free descriptor storage with WeakKeyDictionary and proxy callbacks

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.9 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain why storing per-instance descriptor state in a plain dict keyed by the instance leaks memory (the dict keeps every instance alive forever) and how WeakKeyDictionary fixes it by keying on identity without owning a strong reference
- Implement a reusable data descriptor whose per-instance storage lives in a module/class-level WeakKeyDictionary instead of the instance __dict__, so it works even on slotted/immutable domain objects
- Register a callback= with weakref.ref or weakref.proxy so a function fires the moment a tracked object is garbage-collected, and use that to drive cache eviction / audit accounting
- Recognise that accessing a weakref.proxy after its referent is collected raises ReferenceError, and guard dereferences accordingly
- Contrast WeakKeyDictionary (key not kept alive) with the already-seen WeakValueDictionary (value not kept alive) and pick the right one for a caching problem
- Understand that a class must expose __weakref__ (the default unless __slots__ omits it) for any of weakref to work

## Python features introduced
`weakref.WeakKeyDictionary`, `weakref.ref with callback= argument`, `weakref.proxy with callback= argument`, `weakref.ReferenceError on dead proxy access`, `data descriptor protocol (__set_name__, __get__, __set__, __delete__)`, `object identity as a dictionary key vs __hash__/__eq__ keying`, `__weakref__ slot and why __slots__ classes need it for weak references`, `garbage-collection timing / reference-count drop triggering callbacks`, `try/except around proxy dereference`, `PEP 604 unions (X | None) in annotations`, `dataclasses interplay: why slotted dataclasses break naive instance-dict storage`

## MiniERP increment
Adds a reusable, leak-free field-descriptor infrastructure to the MiniERP core domain. Introduces `core/descriptors.py` with a `TrackedField` data descriptor whose per-entity values are stored in a module-level `weakref.WeakKeyDictionary` keyed by the owning entity instance — so entities can be slotted/kw_only dataclasses (Product, Customer) without polluting __dict__, and when an entity is dropped its stored field state is reclaimed automatically (no leak in long-running server/Web sessions). The same module adds an `InstanceRegistry` that holds `weakref.ref(entity, callback=...)` for every live domain entity; the callback fires on collection to decrement a live-instance gauge and append a lightweight 'evicted' line to the in-memory audit log, giving Reporting an accurate live-object count without ever pinning objects in memory. A small `safe_view(entity)` helper hands callers a `weakref.proxy` to an entity (for read-only reporting passes) and demonstrates catching ReferenceError when the proxy outlives its target.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** In core/descriptors.py: `_storage: weakref.WeakKeyDictionary[object, dict[str, object]] = weakref.WeakKeyDictionary()` plus a `class TrackedField:` implementing `__set_name__`, `__get__`, `__set__`. Provide `class InstanceRegistry:` with `track(self, obj) -> None` that stores `weakref.ref(obj, self._on_collect)` and an `_on_collect(self, ref)` callback updating `self.live_count` and appending to an audit list. Provide `def safe_view(entity): return weakref.proxy(entity)`. Give learners a partially-filled descriptor (the __get__/__set__ bodies and the callback body are TODO) and a slotted `@dataclass(slots=True)` Product/Customer that declares one or two TrackedField attributes.
- **Test focus:** Verify the descriptor round-trips values per-instance (two entities don't share state) and that distinct-but-equal entities are kept distinct (identity keying, not __eq__ keying). Verify _storage shrinks after an entity is del'd and gc.collect() runs — i.e. no leak — by asserting len(_storage) drops to 0 and that the entity is gone from the WeakKeyDictionary. Verify the InstanceRegistry callback fires on collection: live_count returns to its baseline and an 'evicted' audit entry is appended after del + gc.collect(). Verify that dereferencing safe_view(entity) after the entity is collected raises weakref.ReferenceError. Use gc.collect() to force deterministic collection and assert WeakKeyDictionary keys reflect only still-live instances; confirm the descriptor also works on a slotted dataclass (which has no usable instance __dict__).

</div>
