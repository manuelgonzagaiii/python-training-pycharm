"""Leak-free descriptor storage with WeakKeyDictionary and proxy callbacks

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: In core/descriptors.py: `_storage: weakref.WeakKeyDictionary[object, dict[str, object]] = weakref.WeakKeyDictionary()` plus a `class TrackedField:` implementing `__set_name__`, `__get__`, `__set__`. Provide `class InstanceRegistry:` with `track(self, obj) -> None` that stores `weakref.ref(obj, self._on_collect)` and an `_on_collect(self, ref)` callback updating `self.live_count` and appending to an audit list. Provide `def safe_view(entity): return weakref.proxy(entity)`. Give learners a partially-filled descriptor (the __get__/__set__ bodies and the callback body are TODO) and a slotted `@dataclass(slots=True)` Product/Customer that declares one or two TrackedField attributes.
"""

# Your code here.
