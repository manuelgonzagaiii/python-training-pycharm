# Collect products into a mutable list

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 5.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use a list as the growable collection of product records
- Distinguish in-place mutation (append/extend) from creating a new list
- Understand that the list holds references to immutable tuple records

## Python features introduced
`list`, `list literal`, `list.append`, `list.extend`, `list.insert`, `list mutability`, `in-place mutation vs rebinding`, `list as collection of tuples`

## MiniERP increment
Adds add_product(catalog, product) that appends a record to the catalog list in place, plus seed_catalog() returning a starter list of products. The catalog now exists as a living list.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def add_product(catalog: list[Product], product: Product) -> None:
    """Append a product record to the catalog in place."""
    ...

def seed_catalog() -> list[Product]:
    """Return a starter list with a few product records."""
    ...
- **Test focus:** add_product mutates the passed list in place (same object id, length grows by 1); seed_catalog returns a non-empty list of valid 4-tuples.

</div>
