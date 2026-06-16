# Stage 6: modeling money with Decimal

This is the stage the whole phase has been building toward. Stage 2 proved that `float`
cannot hold money. Now you build the type that can. From here on, **every monetary value
in MiniERP is a `decimal.Decimal`**, created and rounded through the two functions you
write here.

## Decimal: a number that thinks in decimal

`decimal.Decimal` stores numbers as decimal digits, not binary fractions. So the
fractions that break `float` are exact:

```
>>> from decimal import Decimal
>>> Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
True
```

No tolerance, no `isclose` — just `==`, because there is no representation error to
hide.

## Always build from a string (never a float)

This is the single rule that makes Decimal safe, and the one beginners get wrong:

```
>>> Decimal("0.1")     # exact: the digits you typed
Decimal('0.1')
>>> Decimal(0.1)       # the float 0.1 -- already wrong -- copied into Decimal
Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

`Decimal(0.1)` faithfully copies the float's error. The fix is to construct from a
**string** (or an `int`, which is also exact): `Decimal("0.1")`. Because passing a float
is such a reliable mistake, the `money()` helper you write **refuses float input
outright** with a `TypeError`. A wrong type should fail loudly at the door, not quietly
corrupt a total.

## Rounding: pick a mode on purpose

Money has exactly two decimal places, so amounts must be **quantized** to cents.
`quantize` reshapes a Decimal to a target number of places, and you must tell it **how**
to round the last digit:

- `ROUND_HALF_UP` — the everyday "round half up" you learned in school: `2.005` becomes
  `2.01`. This is what most invoicing and tax rules expect.
- `ROUND_HALF_EVEN` (also called banker's rounding) — rounds a halfway value to the
  nearest *even* digit, which avoids a slight upward bias over millions of rows. It is
  Python's *default* for Decimal.

There is no universally "correct" mode; there is only the mode your jurisdiction or
accountant requires. The professional move is to choose one **explicitly and document
it**, so the behavior is never an accident. MiniERP uses `ROUND_HALF_UP`, named in the
code. We define a `CENTS` constant (`Decimal("0.01")`) as the quantization target:

```
>>> from decimal import Decimal, ROUND_HALF_UP
>>> Decimal("2.005").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
Decimal('2.01')
>>> Decimal("3").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
Decimal('3.00')          # two places, always
```

(Decimal also has a **context** — `decimal.getcontext()` — that controls overall
precision and the default rounding for a block of code, and `decimal.localcontext()` for
a temporary one. We pass `rounding=` directly to `quantize` here so the rounding choice
is visible right at the call site; the context is there when you need to set precision
globally.)

## Your task

Fill in the two blanks in `money.py`:

1. `money(value)` — return an exact `Decimal`. The float guard is written for you; you
   supply the construction. Build the Decimal from `str(value)` so a string or int both
   produce the exact value.
2. `round_money(amount)` — quantize `amount` to `CENTS` using `ROUND_HALF_UP`.

## Worked example

```
>>> import money
>>> money.money("0.1") + money.money("0.2") == money.money("0.3")
True
>>> money.money(0.1)
TypeError: money() refuses float; pass a string like '19.99'
>>> money.round_money(money.money("2.005"))
Decimal('2.01')
```

## What the check verifies, and what it leaves to you

- Enforced (the rules): `money("0.1") + money("0.2")` must equal `money("0.3")` exactly;
  a `float` argument must raise; `round_money` must round half up and produce two decimal
  places (`round_money(Decimal("3"))` is `Decimal("3.00")`).
- Your free choice: the exact wording of the error message, and any equivalent way to
  build the Decimal from the string. The *behavior* is fixed; the phrasing is yours.

<div class="hint" title="If you are stuck">

`money` returns `Decimal(str(value))` — wrapping in `str` is what makes a string or int
exact and keeps a float from sneaking in. `round_money` returns
`amount.quantize(CENTS, rounding=ROUND_HALF_UP)`.

</div>

Reference: Python documentation, "decimal — Decimal fixed point and floating point
arithmetic" at docs.python.org.
