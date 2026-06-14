# List comprehensions: the first reports

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 6.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Transform and filter the catalog in one expression
- Use an if-clause to filter and a ternary to relabel within a comprehension
- Flatten nested data with multiple for-clauses

## Python features introduced
`list comprehension`, `filtering with if clause`, `mapping expression`, `multiple for clauses`, `nested comprehension`, `conditional expression inside comprehension (A if C else B)`, `comprehension vs map/filter`

## MiniERP increment
Adds low_stock(catalog, threshold) and names_of(catalog) as comprehension-based reports — the reporting module's first concrete outputs, replacing imperative loops.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def low_stock(catalog: list[Product], threshold: int) -> list[Product]:
    """Return products whose qty is below threshold (list comprehension + if)."""
    ...

def names_of(catalog: list[Product]) -> list[str]:
    """Return just the product names."""
    ...
- **Test focus:** low_stock returns exactly the records with qty < threshold (boundary-correct, strictly less-than); names_of returns names in catalog order; both built as comprehensions.

</div>
