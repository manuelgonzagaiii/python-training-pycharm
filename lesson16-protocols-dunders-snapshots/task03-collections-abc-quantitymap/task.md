# Reusing collections.abc (Mapping mixin)

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 16.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Subclass collections.abc.MutableMapping and get keys/items/values/get/__contains__ for free by implementing the few required abstractmethods
- Understand which methods are abstract vs mixin-provided in collections.abc
- See how the standard ABCs formalize the protocols you implement by hand
- Choose Mapping vs Sequence for a domain collection

## Python features introduced
`collections.abc.Mapping`, `collections.abc.MutableMapping`, `implementing __getitem__/__len__/__iter__ to get mixin methods free`, `abstractmethods inherited from collections.abc`, `collections.abc.Sequence overview`

## MiniERP increment
Adds InventoryLevels, a MutableMapping from SKU code to on-hand Quantity, used by the Inventory module. By inheriting collections.abc.MutableMapping it behaves like a dict everywhere with minimal code.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from collections.abc import MutableMapping


class InventoryLevels(MutableMapping[str, int]):
    def __init__(self) -> None:
        self._data: dict[str, int] = {}

    def __getitem__(self, key: str) -> int: ...
    def __setitem__(self, key: str, value: int) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    # keys(), items(), get(), 'in' come for free from MutableMapping

- **Test focus:** InventoryLevels supports [], len(), iteration, in, and the inherited mixin methods (get/keys/items/update) without implementing them directly; negative stock raises ValueError on __setitem__.

</div>
