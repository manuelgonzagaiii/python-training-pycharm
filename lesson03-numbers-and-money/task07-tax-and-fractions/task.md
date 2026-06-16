# Stage 7: tax, discounts, and exact ratios with Fraction

You can now store money exactly. The last piece is applying **rates** to it — a tax of
8.25%, a discount of 10% — without bringing back the float errors you avoided in stages 2
and 6. This stage adds `apply_rate` and `tax_for` to `money.py`, and MiniERP can finally
compute an invoice total correctly.

## Fraction: a ratio with no rounding at all

`8.25%` written as a float is `0.0825`, which — like all the decimals from stage 2 — is
not stored exactly. `fractions.Fraction` sidesteps that entirely by keeping a numerator
and a denominator, so the ratio is **perfectly exact**:

```
>>> from fractions import Fraction
>>> Fraction(825, 100)        # 8.25% -> automatically reduced
Fraction(33, 4)
>>> Fraction(33, 4) == Fraction(825, 100)
True
>>> Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)   # exact: no 0.999...
Fraction(1, 1)
```

A `Fraction` reduces itself (`825/100` becomes `33/4`) and exposes `.numerator` and
`.denominator`. It is the right tool when a ratio must be *exact* — a tax rate, a split,
an aspect ratio — and a decimal would only approximate it.

## Decimal and Fraction do not mix directly

Here is the trap, and the reason this stage exists: Python will **not** let you multiply
a `Decimal` by a `Fraction` —

```
>>> Decimal("100.00") * Fraction(33, 4)
TypeError: unsupported operand type(s) for *: 'decimal.Decimal' and 'Fraction'
```

— because silently mixing two different exact systems would hide which one's rules
apply. You convert deliberately. To turn a percent `Fraction` into an exact `Decimal`
rate, divide its numerator by its denominator as Decimals, then divide by 100:

```
>>> rate = Decimal(Fraction(33, 4).numerator) / Decimal(Fraction(33, 4).denominator) / 100
>>> rate
Decimal('0.0825')
```

Now `amount * rate` is Decimal-times-Decimal, which is exact.

## Round once, at the very end

A rate applied to money almost never lands on a whole cent: `19.99 * 0.0825` is
`1.649175`. **Round once, after the multiply** — never round the rate first, and never
round a running result between steps, or the tiny truncations compound into a
"penny off" total across a long invoice. Both `apply_rate` and `tax_for` end with a
single `round_money`.

## Your task

Fill in the two blanks in `money.py`:

1. `apply_rate(amount, rate)` — return `amount * rate`, rounded to cents with
   `round_money`. (The rate here is already a `Decimal`, e.g. `Decimal("0.0825")`.)
2. `tax_for(amount, percent)` — `percent` is a `Fraction` of 100 (8.25% is
   `Fraction(33, 4)`). Convert it to an exact Decimal rate (numerator over denominator),
   and the rest of the line divides by 100 and rounds for you.

## Worked example

```
>>> import money
>>> from decimal import Decimal
>>> from fractions import Fraction
>>> money.apply_rate(money.money("19.99"), Decimal("0.0825"))
Decimal('1.65')
>>> money.tax_for(money.money("100.00"), Fraction(825, 100))
Decimal('8.25')
```

## What the check verifies, and what it leaves to you

- Enforced (the rules): `tax_for(money("100.00"), Fraction(825, 100))` is exactly
  `money("8.25")`; rates are rounded only once at the end (no double-rounding drift); a
  discount-then-tax pipeline reaches the expected cent.
- Your free choice: any equivalent way to compute the rate, as long as the arithmetic
  stays exact and rounds once. A different-but-correct conversion passes.

<div class="hint" title="If you are stuck">

`apply_rate` is `round_money(amount * rate)`. For `tax_for`, the missing piece is
`Decimal(percent.numerator) / Decimal(percent.denominator)` — that turns the Fraction
into an exact Decimal; the `/ 100` and the final `round_money` are already in place.

</div>

Reference: Python documentation, "fractions — Rational numbers" and "decimal — Decimal
fixed point and floating point arithmetic" at docs.python.org.
