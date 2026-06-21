# Stage 1: tiered pricing with if/elif/else

This lesson starts MiniERP's business-rules layer: the pure functions that decide what a
customer pays. Everything here lives in `pricing.py`, and every later stage extends the
same module.

First, a decision that holds for the whole pricing engine: **money is integer cents,
never a floating-point number.** A price of fifteen dollars is the integer `1500`, not
`15.0`. Binary floats cannot represent most decimal cents exactly (you met `0.1 + 0.2 !=
0.3` back in the numbers lesson), so using them for money quietly accumulates rounding
errors. Integer cents are exact. This matches how the catalog already stores
`price_cents`, and it is the representation the rest of the course builds on. Discounts
are whole-percent integers (5 means 5% off), applied with rounding so totals stay exact
to the cent.

## if / elif / else: one decision, several outcomes

An `if/elif/else` chain tests conditions from top to bottom and runs **the first branch
that matches** — then skips the rest entirely. That "first match wins, others skipped"
rule is the whole point, and it lets each later test assume the ones above it already
failed:

```
>>> def tier(qty):
...     if qty < 10:
...         return "none"
...     elif qty < 50:    # only reached when qty >= 10 already
...         return "bulk"
...     else:
...         return "wholesale"
```

Because control never reaches `elif qty < 50` unless `qty < 10` was false, you do **not**
write `elif 10 <= qty < 50`. Writing the redundant lower bound is not wrong, but it is
noise. (When you do need both bounds at once — outside such a chain — Python lets you
*chain* comparisons: `10 <= qty < 50` is read as `10 <= qty and qty < 50`.)

## Your task

In `pricing.py`, finish two functions:

1. `quantity_tier(qty)` — return the tier label for a quantity: `'none'` for 1-9,
   `'bulk'` for 10-49, `'wholesale'` for 50 and up. The `qty <= 0` guard and the branch
   bodies are written; you fill in the two band conditions.
2. `unit_price_for(base_price_cents, qty)` — fill in the call that looks up this
   quantity's tier so the function can take that tier's discount off the price.

## Worked example

```
>>> import pricing
>>> pricing.quantity_tier(5), pricing.quantity_tier(20), pricing.quantity_tier(100)
('none', 'bulk', 'wholesale')
>>> pricing.unit_price_for(1000, 5)     # 'none' tier: 0% off
1000
>>> pricing.unit_price_for(1000, 10)    # 'bulk' tier: 5% off
950
>>> pricing.unit_price_for(1000, 50)    # 'wholesale' tier: 10% off
900
```

## What the check verifies, and what it leaves to you

- Enforced: the tier boundaries map correctly (1, 9 -> none; 10, 49 -> bulk; 50+ ->
  wholesale); a non-positive quantity raises `ValueError`; `unit_price_for` applies the
  right per-tier discount and rounds to the nearest cent.
- Your free choice: how you phrase the conditions. `qty < 10` and a chained
  `1 <= qty <= 9` are both accepted, as long as the boundaries land in the right tier.

<div class="hint" title="If you are stuck">

The first band condition is `qty < 10`; the second is `qty < 50`. In `unit_price_for`,
the missing piece is `quantity_tier(qty)` — reuse the function you just wrote rather than
repeating the bands.

</div>

Reference: Python documentation, "if statements" and "Comparisons" at docs.python.org.
