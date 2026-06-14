# Counter: stock levels and best-sellers

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.2 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Tally quantities and event counts with Counter instead of manual dict bumping
- Rank items with most_common(n)
- Combine stock movements with Counter + and - arithmetic
- Rely on a missing key returning 0, not KeyError

## Python features introduced
`collections.Counter`, `Counter from iterable`, `most_common`, `Counter arithmetic + and -`, `Counter update/subtract`, `missing key returns 0`, `elements()`, `total()`, `Counter as a multiset`

## MiniERP increment
Adds stock_counter(catalog) (sku -> on-hand qty) and apply_movements(stock, deltas) using Counter arithmetic to add receipts and subtract sales — the running inventory ledger plus a top_sellers(n) report.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from collections import Counter

def stock_counter(catalog: list[ProductRecord]) -> Counter[str]:
    """Return a Counter mapping sku -> qty on hand."""
    ...

def apply_movements(stock: Counter[str], deltas: Counter[str]) -> Counter[str]:
    """Return updated stock after adding deltas (Counter arithmetic)."""
    ...
- **Test focus:** stock_counter reflects each product's qty and returns 0 for unknown skus; apply_movements adds/subtracts correctly via Counter arithmetic; most_common ordering is verifiable through a top-sellers helper.

</div>
