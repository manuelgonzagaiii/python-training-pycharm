# Model a product as a tuple record

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 5.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create fixed-shape records as tuples (sku, name, price_cents, qty)
- Access fields by index and understand why a tuple communicates 'fixed shape'
- Define a PEP 695 type alias to name the record shape once
- Prove immutability by attempting (and catching) item assignment

## Python features introduced
`tuple`, `tuple literal`, `tuple packing`, `indexing`, `len()`, `tuple is immutable`, `type hints with tuple[...]`, `PEP 695 type alias for the record shape`

## MiniERP increment
Adds make_product() returning a 4-field tuple record and a Product type alias to catalog.py — the atomic unit every later task in the phase manipulates.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py
type Product = tuple[str, str, int, int]  # (sku, name, price_cents, qty)

def make_product(sku: str, name: str, price_cents: int, qty: int) -> Product:
    """Return a product as an immutable tuple record."""
    ...
- **Test focus:** make_product returns a 4-tuple in the right field order; the result is a tuple (immutable); indexing yields the expected sku/name/price/qty.

</div>
