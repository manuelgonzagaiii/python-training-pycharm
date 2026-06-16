# Stage 2: why 0.1 + 0.2 != 0.3

This is a knowledge check, not a coding task — but it decides the most important design
choice in the whole phase. Read it, then pick the one correct answer.

## The result that breaks naive money code

```
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
```

A `float` is a binary fraction with a fixed number of bits. Most decimal fractions —
including `0.1`, `0.2`, and `0.3` — **have no exact binary representation**, the same
way `1/3` has no exact decimal representation (`0.3333...`). So the computer stores the
nearest binary value it can, and the tiny errors add up. This is true in every
mainstream language; it is the IEEE-754 standard doing exactly what it promises, not a
bug.

## Why this is fatal for money

Money is **exact**. An invoice is paid or it is not; a balance is zero to the cent or it
is not. If prices are floats, then `subtotal == amount_paid` can be `False` even when
the customer paid the right amount, purely because of representation error. Cents go
missing. Auditors do not accept "off by 0.00000000004."

People reach for two "fixes" that are still wrong for currency:

- `math.isclose(a, b)` asks "are these *close enough*?" That is the right question for a
  measurement and the wrong one for money, where a payment one cent short is short, full
  stop. Worse, its tolerance is *relative* to the size of the numbers, so on a large
  enough invoice it will accept a one-cent shortfall as "close" — and the floats it
  compares have already drifted besides.
- Rounding floats before comparing hides the symptom but keeps the disease: you are
  still doing arithmetic on inexact values, so errors still accumulate across many lines.

A couple of `float` facts worth knowing even though we avoid floats for money:
`(2.0).is_integer()` is `True`, and floats have special values `float('inf')` and
`float('nan')` — and `nan` is never equal to anything, even itself.

## The decision

MiniERP stores money as **`decimal.Decimal`, built from strings**, and compares it with
plain `==`. `Decimal('0.1') + Decimal('0.2') == Decimal('0.3')` is `True`, exactly, with
no tolerance needed. You will build that money helper in stage 6. This quiz is the gate:
get the reasoning right here, and the Decimal refactor later will feel obvious.

## Question

MiniERP must decide whether an invoice for `$19.99` has been **paid in full**. Which
approach is correct?

Pick the single best answer below, then press **Check**.
