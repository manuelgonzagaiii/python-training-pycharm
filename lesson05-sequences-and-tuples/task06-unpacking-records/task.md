# Unpacking records, starred targets & swaps

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 5.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Destructure a product tuple into sku, name, price, qty in one line
- Use a starred target to split head/tail or init/last of the catalog
- Discard unwanted fields with _ and unpack inside for-loops
- Swap two values without a temp variable

## Python features introduced
`iterable unpacking`, `multiple assignment`, `starred target *rest`, `ignore with _`, `nested unpacking`, `swap via a, b = b, a`, `unpacking in for-loops`, `head/*tail and *init/last idioms`

## MiniERP increment
Adds describe(product) (unpacks a record into a readable label using the Money/text utilities from earlier phases) and split_featured(catalog) returning (first, *rest) — featured product plus the remainder for a 'rest of catalog' view.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from money import format_money  # reused from an earlier phase

def describe(product: Product) -> str:
    """Unpack the record and return e.g. 'SKU123 — Widget (USD 9.99), qty 5'."""
    sku, name, price_cents, qty = product
    ...

def split_featured(catalog: list[Product]) -> tuple[Product, list[Product]]:
    """Return (first_product, rest_of_catalog) using a starred target."""
    ...
- **Test focus:** describe unpacks all four fields into the expected formatted string (money via the reused util); split_featured returns the head record and a list of the remaining records, with rest being a list.

</div>
