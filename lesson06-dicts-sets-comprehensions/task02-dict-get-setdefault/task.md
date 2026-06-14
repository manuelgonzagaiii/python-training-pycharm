# Safe access: get, setdefault & grouping

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 6.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Read possibly-missing keys with .get(key, default) instead of try/except
- Build a one-to-many grouping with setdefault (key -> list of products)
- Update and remove entries with update/pop

## Python features introduced
`dict.get with default`, `dict.setdefault`, `dict.pop`, `dict.update`, `avoiding KeyError`, `accumulate-into-list pattern with setdefault`, `nested dict / list-of-values`

## MiniERP increment
Adds group_by_category(catalog) that buckets products by a category prefix of the SKU using setdefault, and find(index, sku) that returns None for unknown SKUs via .get — the catalog can now be browsed by category and queried safely.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def find(index: dict[str, Product], sku: str) -> Product | None:
    """Return the product for sku, or None if absent (no exception)."""
    ...

def group_by_category(catalog: list[Product]) -> dict[str, list[Product]]:
    """Bucket products by category code (first 3 chars of sku) using setdefault."""
    ...
- **Test focus:** find returns the record for a known sku and None (not KeyError) for an unknown one; group_by_category produces a dict whose values are lists, with each product placed under its category code.

</div>
