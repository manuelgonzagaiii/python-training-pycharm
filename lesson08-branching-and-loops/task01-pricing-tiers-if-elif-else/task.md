# Tiered Pricing with if/elif/else

> **Phase:** Control Flow & Functions  •  **Stage:** 8.1 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write multi-branch decisions with if/elif/else and understand that only the first matching branch runs
- Use chained comparisons to express quantity bands cleanly
- Reason about truthiness and short-circuiting in boolean conditions

## Python features introduced
`if statement`, `elif`, `else`, `comparison operators (<, <=, >, >=, ==, !=)`, `boolean operators and/or/not`, `chained comparisons (a <= x < b)`, `truthiness of values`, `return statement`

## MiniERP increment
Create pricing.py with quantity_tier(qty) returning a discount-tier label ('none'/'bulk'/'wholesale') from quantity bands, and unit_price_for(base_price, qty) that selects a per-unit price using if/elif/else over those bands. This is the first stone of the business-rules layer that later tasks extend.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def quantity_tier(qty: int) -> str:
    """Return 'none', 'bulk', or 'wholesale' based on qty bands."""
    # 1..9 -> 'none', 10..49 -> 'bulk', 50+ -> 'wholesale'
    ...


def unit_price_for(base_price: float, qty: int) -> float:
    """Per-unit price after the quantity-tier multiplier."""
    # none x1.0, bulk x0.95, wholesale x0.90
    ...
- **Test focus:** Boundary quantities (1, 9, 10, 49, 50, 100) map to correct tiers; unit_price_for applies the right multiplier at each boundary; invalid qty<=0 raises ValueError.

</div>
