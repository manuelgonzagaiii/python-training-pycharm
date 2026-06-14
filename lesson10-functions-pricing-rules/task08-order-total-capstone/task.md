# Assemble the Order-Total Pipeline

> **Phase:** Control Flow & Functions  •  **Stage:** 10.8 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compose many small functions into one clear pipeline
- Expose a well-annotated, well-documented public entry point
- Connect the dispatcher to executable pricing handlers

## Python features introduced
`composing functions from this phase`, `function annotations for the public API`, `docstrings as the module contract`, `keyword-only options end-to-end`, `match/case routing to handlers`, `pure-function design (no side effects)`

## MiniERP increment
Add order_total(catalog, lines, *, tier_percent=0.0, coupons=(), tax_rate=0.0) to rules.py that expands bundles, computes the subtotal, stacks tier and coupon discounts, applies keyword-only tax, and returns an itemized breakdown dict. Wire dispatch()'s PRICE/DISCOUNT routes to call it, completing the phase milestone: a match/case dispatcher backed by a full pricing/discount rules layer.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def order_total(catalog: list[dict], lines: list[tuple[str, float, int]], *,
               tier_percent: float = 0.0, coupons: tuple = (), tax_rate: float = 0.0) -> dict:
    """Full pipeline: expand bundles -> subtotal -> tier+coupon discounts -> tax.
    Returns an itemized breakdown: {'subtotal':..., 'discount':..., 'tax':..., 'total':...}."""
    ...
- **Test focus:** Breakdown fields are internally consistent (subtotal - discount + tax == total); tier_percent, coupons, and tax_rate each move the total correctly; passing tax_rate positionally is rejected; dispatch() PRICE route returns this breakdown.

</div>
