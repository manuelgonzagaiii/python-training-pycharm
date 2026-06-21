# Stage 8: assemble the order-total pipeline

This is the phase's capstone. Every function you wrote — discounts, stacking, tax — comes
together in one public entry point, `order_total`, that prices a whole order and returns an
itemized breakdown. It is a study in **composition**: small, well-tested functions wired into
a pipeline, each doing one thing.

## The pipeline

```
order_total(lines, *, tier_percent=0, coupons=(), tax_rate_bps=0)
```

The steps, in order:

1. **Subtotal** — sum `price_cents * qty` across the lines.
2. **Tier discount** — take the customer-tier percent off the subtotal with `apply_percent`.
3. **Coupons** — stack each coupon percent on top with `stack_discounts`, spreading the
   `coupons` tuple into its `*percents` with `*coupons`.
4. **Tax** — apply tax to the discounted amount with `apply_tax`, passing `rate_bps` by name
   because it is keyword-only.

The function returns a dict — `subtotal`, `after_discounts`, `tax`, `total` — so callers (the
dispatcher's PRICE route, a receipt, a report) can show the full breakdown, not just one
number.

Two design choices worth noticing. The discount and tax options are **keyword-only** (after
the `*`), so a call reads `order_total(lines, tax_rate_bps=825)` and never a bare mystery
number. And `order_total` is **pure** — it reads its inputs and returns a value with no
side effects — which is exactly what let every piece of it be unit-tested in isolation. (Bundle
lines from `expand_bundle` are flattened into `lines` before this is called, keeping the
pricing pipeline independent of the catalog.)

## Your task

In `rules.py`, finish `order_total`. The subtotal and the tier discount are written. Fill in:

1. the **coupon stacking** — stack the `coupons` onto the tiered amount, spreading them as
   `*args`, and
2. the **tax application** — tax the discounted amount, passing `rate_bps` as the keyword-only
   argument it is.

## Worked example

```
>>> import rules
>>> rules.order_total([("A", 1000, 1)])              # nothing applied
{'subtotal': 1000, 'after_discounts': 1000, 'tax': 0, 'total': 1000}
>>> rules.order_total([("A", 1000, 2), ("B", 500, 4)],
...                   tier_percent=10, coupons=(5,), tax_rate_bps=825)
{'subtotal': 4000, 'after_discounts': 3420, 'tax': 282, 'total': 3702}
```

## What the check verifies, and what it leaves to you

- Enforced: the subtotal, the discounted amount (tier then coupons), the tax, and the final
  total are all correct, and the breakdown dict carries those keys.
- Your free choice: you may add more keys to the breakdown (a per-line detail, the effective
  rate) as long as the four core figures are present and correct.

<div class="hint" title="If you are stuck">

Coupons: `stack_discounts(after_tier, *coupons)` — the `*` spreads the tuple into separate
percent arguments. Tax: `apply_tax(after_coupons, rate_bps=tax_rate_bps)` — `rate_bps` must be
named.

</div>

Reference: Python documentation, "Unpacking Argument Lists" (the `*coupons` call) and the
function-definition sections referenced through this lesson, at docs.python.org.
