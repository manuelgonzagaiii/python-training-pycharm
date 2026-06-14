# namedtuple: self-documenting product records

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.1 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Upgrade the positional tuple record to a named record without losing tuple behavior
- Access fields by name and create modified copies with _replace
- Convert to a dict with _asdict for serialization
- Confirm namedtuples still unpack and index like plain tuples

## Python features introduced
`collections.namedtuple`, `typing.NamedTuple`, `field access by name`, `_replace`, `_asdict`, `_fields`, `defaults`, `tuple compatibility / unpacking still works`, `indexing still works`

## MiniERP increment
Refactors the Product record into a typing.NamedTuple ('ProductRecord' with sku/name/price_cents/qty) and adds reprice(product, new_price) using _replace — every prior function keeps working because a namedtuple IS a tuple, while code becomes readable by field name.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from typing import NamedTuple

class ProductRecord(NamedTuple):
    sku: str
    name: str
    price_cents: int
    qty: int

def reprice(product: ProductRecord, new_price: int) -> ProductRecord:
    """Return a copy with price_cents replaced (use _replace)."""
    ...
- **Test focus:** ProductRecord allows name access and still unpacks/indexes as a 4-tuple; reprice returns a new record with only price_cents changed and qty/name/sku intact; _asdict round-trips the fields.

</div>
