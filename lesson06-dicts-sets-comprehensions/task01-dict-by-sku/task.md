# Index the catalog by SKU with a dict

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 6.1 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a dict keyed by SKU for direct product lookup
- Rely on guaranteed insertion-order iteration
- Test membership with `in` and handle a missing key
- Understand why a dict beats scanning a list for lookups

## Python features introduced
`dict`, `dict literal`, `key-based access []`, `dict insertion order (guaranteed since 3.7)`, `in operator for membership`, `KeyError`, `type hint dict[str, Product]`, `O(1) lookup vs list scan`

## MiniERP increment
Adds index_by_sku(catalog) -> dict[str, Product]: the catalog gains a fast lookup structure that every later module (sales, invoicing) will use to resolve a SKU to a product.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def index_by_sku(catalog: list[Product]) -> dict[str, Product]:
    """Return a dict mapping each product's sku to its record, preserving order."""
    ...
- **Test focus:** index_by_sku maps each sku to the correct record; iteration order matches the input list; lookup of a known sku succeeds and `in` works for present/absent skus.

</div>
