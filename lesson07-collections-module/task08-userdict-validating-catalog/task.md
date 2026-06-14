# UserDict & UserList: a validating catalog wrapper

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.8 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Subclass UserDict to add validation that a plain dict subclass would miss
- Override __setitem__ to reject bad SKUs/prices on insert
- Understand the .data backing store and why UserDict is the safe base class
- See UserList as the list equivalent

## Python features introduced
`collections.UserDict`, `collections.UserList`, `subclassing built-in containers`, `overriding __setitem__/__getitem__`, `the .data attribute`, `why UserDict over subclassing dict directly`, `validation on insert`

## MiniERP increment
Adds Catalog(UserDict) — a SKU-keyed catalog that validates records on insertion (non-empty sku, non-negative price/qty) — the encapsulated, self-protecting catalog object the service layer and all four front-ends will share going forward.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from collections import UserDict

class Catalog(UserDict):
    """A SKU-keyed catalog that validates products on insertion."""
    def __setitem__(self, sku: str, product: ProductRecord) -> None:
        # validate sku non-empty and price/qty non-negative, then store
        ...
- **Test focus:** Catalog stores valid products and rejects invalid ones (empty sku or negative price/qty) by raising on __setitem__; valid inserts are retrievable via [] and `in`; the .data backing dict stays consistent.

</div>
