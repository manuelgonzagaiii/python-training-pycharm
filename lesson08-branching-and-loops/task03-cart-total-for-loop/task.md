# Stage 3: totalling a cart with a for loop

A `for` loop walks each item of a sequence in turn. The everyday job it does in business
code is the **accumulator pattern**: start a running total at zero, then add something for
each item.

```
subtotal = 0
for line in lines:
    subtotal += something(line)
```

Three pieces make this work, and each is worth naming:

- The **accumulator** (`subtotal`) is created *before* the loop. If you put it inside, it
  would reset to 0 on every pass and you would end up with only the last item's
  contribution.
- `+=` is **augmented assignment**: `subtotal += x` means `subtotal = subtotal + x`. It
  reads as "add x into the total".
- Each cart line is a tuple `(sku, base_price_cents, qty)`, and the loop target can
  **unpack** it directly: `for sku, base_price_cents, qty in lines:` gives three named
  variables per pass instead of `line[0]`, `line[1]`, `line[2]`.

This is MiniERP's first end-to-end order calculation: price each line at its quantity tier
(reusing `unit_price_for` from stage 1) and sum the lot.

## Your task

In `pricing.py`, finish `cart_subtotal(lines)`. The accumulator and the loop are written;
you supply the value added on each pass — this line's total, which is the quantity times
the tier-adjusted unit price.

## Worked example

```
>>> import pricing
>>> lines = [("A-001", 1000, 5), ("B-010", 1000, 10)]
>>> pricing.cart_subtotal(lines)        # 5 * 1000  +  10 * 950
14500
>>> pricing.cart_subtotal([])           # nothing to add
0
```

## What the check verifies, and what it leaves to you

- Enforced: the subtotal prices each line by its quantity tier and sums them; an empty
  cart totals to 0.
- Your free choice: how you compute each line's contribution, as long as it uses the tier
  pricing. You could call `unit_price_for` (the intended reuse) or inline the same
  calculation — the check grades the total.

<div class="hint" title="If you are stuck">

Each pass adds `qty * unit_price_for(base_price_cents, qty)` to the subtotal.

</div>

Reference: Python documentation, "for statements" and "The for statement" (language
reference) at docs.python.org.
