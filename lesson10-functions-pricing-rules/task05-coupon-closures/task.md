# Closures and the Late-Binding Gotcha

> **Phase:** Control Flow & Functions  •  **Stage:** 10.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create configured functions with a closure factory
- Explain and fix the late-binding bug where loop closures share the final value
- Treat functions as first-class values stored in lists/dicts

## Python features introduced
`closures (functions capturing enclosing variables)`, `function factories returning functions`, `free variables`, `the late-binding closure gotcha in loops`, `default-arg capture workaround`, `first-class functions`

## MiniERP increment
Add make_coupon(percent) to rules.py returning a closure that discounts a price, and build_coupon_table(percents) that creates one coupon per percent — correctly using the default-arg capture trick to dodge the late-binding gotcha, so MiniERP's coupon registry behaves as intended.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def make_coupon(percent: float):
    """Return a closure price->discounted_price capturing percent."""
    def coupon(price: float) -> float:
        ...
    return coupon


def build_coupon_table(percents: list[float]) -> list:
    """Return a list of coupon closures. Avoid the late-binding gotcha."""
    # WRONG: [lambda p: p*(1-pct) for pct in percents]  # all share final pct
    ...
- **Test focus:** make_coupon closures apply their captured percent; build_coupon_table coupons each apply distinct percents (proves late-binding gotcha avoided), not all the last one.

</div>
