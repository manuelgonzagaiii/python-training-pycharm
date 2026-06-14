# Deep slicing: pagination and recent products

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 5.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Page through the catalog with start:stop slices computed from page/size
- Grab the most recent N products with negative-index slicing
- Reverse a sequence with a negative step
- Rely on slices never raising IndexError

## Python features introduced
`slicing start:stop:step`, `negative indices in slices`, `negative step / reversal [::-1]`, `slice object semantics`, `out-of-range slices are safe`, `copy via [:]`

## MiniERP increment
Adds page(catalog, number, size) and recent(catalog, n) for paginated/most-recent catalog views — the first read-API the CLI and web front-ends will call.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def page(catalog: list[Product], number: int, size: int) -> list[Product]:
    """Return page `number` (1-based) of `size` items using slicing."""
    ...

def recent(catalog: list[Product], n: int) -> list[Product]:
    """Return the last n products, newest first."""
    ...
- **Test focus:** page returns the correct slice for in-range and past-the-end pages (empty, no error); recent returns the last n in reversed order and handles n larger than the catalog.

</div>
