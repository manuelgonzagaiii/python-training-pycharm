# Stage 10: Decimal signals, traps, and flags

Back in Lesson 3 you built `money.py` and the `money`/`round_money` helpers. This stage
extends that same module with the machinery that makes money handling *defensive*: parsing
untrusted input safely, and refusing to silently lose a fraction of a cent. To do that you
need to understand three words people use loosely and Python defines precisely.

## Signal, trap, flag

When a `Decimal` operation hits a special condition, it raises a **signal** — a named
condition like `Inexact` (the result had to be rounded), `InvalidOperation` (e.g. parsing
`"twelve"`), `DivisionByZero`, or `Rounded`. What *happens* to a signal depends on the
context:

- A **trap** turns a signal into a raised exception. By default the context traps
  `InvalidOperation` and `DivisionByZero` (the dangerous ones) but **not** `Inexact` —
  rounding is normal, so it does not raise.
- A **flag** is a sticky record that a signal occurred, set whether or not it is trapped.
  You can read `ctx.flags[Inexact]` after the fact to ask "did anything get rounded?"

The context that holds these is reachable with `decimal.getcontext()`, and
`decimal.localcontext()` gives you a **temporary** one for a `with` block so your changes
do not leak out.

## parse_money: lean on a default trap

`InvalidOperation` is already trapped, so `Decimal("twelve")` raises it. Rather than let
that Decimal-specific exception escape, `parse_money` catches it and re-raises a plain
`ValueError` — callers then handle one obvious error type:

```
>>> Decimal("twelve")
decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]
```

## require_exact: turn a trap ON for a region

Sometimes you want the *opposite* of normal rounding — you want an error if money would be
lost. Turn the `Inexact` trap on inside a `localcontext()` and quantizing an amount with
sub-cent precision raises instead of rounding it away:

```
>>> from decimal import localcontext, Inexact
>>> with localcontext() as ctx:
...     ctx.traps[Inexact] = True
...     Decimal("19.505").quantize(Decimal("0.01"))    # raises Inexact
```

The trap is switched off again the moment the `with` block ends — that is the point of a
*local* context.

## Your task

Fill in the two blanks in `money.py`:

1. `parse_money(text)` — name the signal to catch (`InvalidOperation`) so a bad string
   becomes a `ValueError`.
2. `require_exact(amount)` — turn the `Inexact` trap on for the local context
   (`ctx.traps[Inexact] = True`).

## Worked example

```
>>> import money
>>> money.parse_money("19.5")
Decimal('19.50')
>>> money.parse_money("twelve")
ValueError: not valid money: 'twelve'
>>> money.require_exact(Decimal("19.505"))
ValueError: amount has sub-cent precision: 19.505
```

## What the check verifies, and what it leaves to you

- Enforced: a valid string parses and quantizes to cents; garbage (`"twelve"`, `""`)
  raises `ValueError` rather than leaking a Decimal exception; `require_exact` accepts a
  clean cent amount and rejects sub-cent precision.
- Your free choice: the error message wording.

<div class="hint" title="If you are stuck">

`parse_money` catches `InvalidOperation`. `require_exact` sets `ctx.traps[Inexact] = True`.

</div>

Reference: Python documentation, "decimal — Decimal: Context objects, Signals, and the
trap/flag model" at docs.python.org.
