# Augmented assignment and chained comparisons

> **Phase:** Numbers, Text & Bytes  •  **Stage:** 3.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use augmented assignment for running totals and counters
- Write range checks as chained comparisons instead of two and-ed comparisons
- Understand chained comparison short-circuit semantics (a < b < c evaluates b once)

## Python features introduced
`augmented assignment: += -= *= /= //= %= **=`, `augmented bitwise: &= |= ^= <<= >>=`, `chained comparisons (0 <= x <= 100)`, `comparison operators < <= > >= == !=`, `is vs == distinction`, `in-place accumulation patterns`

## MiniERP increment
Add MiniERP validation/accumulation helpers to `task.py`: `running_total(prices)` accumulates a subtotal with += , and `in_stock_range(qty, low, high)` validates an order quantity with a chained comparison `low <= qty <= high`. These feed inventory and cart logic later.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def running_total(prices: list[int]) -> int:
    total = 0
    # TODO: accumulate with += in a loop
    raise NotImplementedError

def in_stock_range(qty: int, low: int, high: int) -> bool:
    """True iff low <= qty <= high (inclusive), using a chained comparison."""
    # TODO: single chained comparison
    raise NotImplementedError
- **Test focus:** Tests verify += accumulation over varied/empty lists and that in_stock_range uses inclusive bounds; boundary values (qty==low, qty==high, below/above) are checked.

</div>
