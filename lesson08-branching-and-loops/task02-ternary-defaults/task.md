# Conditional Expressions for Compact Defaults

> **Phase:** Control Flow & Functions  •  **Stage:** 8.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use the ternary conditional expression where a value, not a branch, is needed
- Recognize when a ternary improves readability and when a full if-statement is clearer
- Distinguish expressions (produce a value) from statements (perform an action)

## Python features introduced
`conditional expression (a if cond else b)`, `nested ternary (readability tradeoffs)`, `ternary vs if-statement choice`, `expression vs statement distinction`

## MiniERP increment
Add display_price(price, currency='USD') to pricing.py that formats a price with a ternary picking the symbol ('$' if USD else the ISO code), and round_money(x) that uses a ternary to clamp tiny negative rounding artifacts to 0.0. These helpers are reused by every later total calculation.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def display_price(price: float, currency: str = "USD") -> str:
    """'$12.50' for USD, else '12.50 EUR'-style using a ternary."""
    ...


def round_money(x: float) -> float:
    """Round to 2 decimals; a tiny negative like -0.0001 becomes 0.0 via a ternary."""
    ...
- **Test focus:** display_price returns symbol form for USD and code form otherwise; round_money clamps near-zero negatives to 0.0 and rounds to 2 decimals.

</div>
