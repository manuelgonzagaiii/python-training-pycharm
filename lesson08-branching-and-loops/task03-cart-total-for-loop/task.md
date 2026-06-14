# Totalling a Cart with for

> **Phase:** Control Flow & Functions  •  **Stage:** 8.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Iterate a sequence and accumulate a running total
- Unpack each line item directly in the for target
- Reuse earlier pricing helpers inside a loop

## Python features introduced
`for loop`, `iterating a list of dicts/tuples`, `accumulator pattern`, `range()`, `augmented assignment (+=)`, `tuple unpacking in the loop target`

## MiniERP increment
Add cart_subtotal(lines) to pricing.py where lines is a list of (sku, base_price, qty) tuples; loop over them, call unit_price_for, and accumulate the rounded subtotal. This is MiniERP's first end-to-end order calculation.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def cart_subtotal(lines: list[tuple[str, float, int]]) -> float:
    """Sum unit_price_for(base, qty) * qty over all lines; round the result."""
    total = 0.0
    for sku, base_price, qty in lines:
        ...
    ...
- **Test focus:** Empty cart returns 0.0; single and multi-line carts total correctly with tier multipliers applied; result is rounded to 2 decimals.

</div>
