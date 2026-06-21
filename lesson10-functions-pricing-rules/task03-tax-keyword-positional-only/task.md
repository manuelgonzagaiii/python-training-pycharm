# Stage 3: positional-only and keyword-only parameters

By default a Python parameter can be filled either positionally or by name. Sometimes you
want to *forbid* one of those, to make calls clearer and the function safer to refactor. Two
separators in the signature control this.

## The `*` separator: keyword-only

Everything **after** a bare `*` in the parameter list must be passed **by name**:

```
def apply_tax(amount, *, rate_bps, inclusive=False):
    ...

apply_tax(1000, rate_bps=825)     # ok
apply_tax(1000, 825)              # TypeError: rate_bps is keyword-only
```

Forcing `rate_bps=825` at the call site means nobody can write a bare `apply_tax(1000, 825)`
and leave the reader guessing what `825` is. The call documents itself.

## The `/` separator: positional-only

Everything **before** a `/` must be passed **positionally** — callers may not use its name:

```
def apply_tax(amount, /, *, rate_bps):
    ...

apply_tax(amount=1000, rate_bps=825)   # TypeError: amount is positional-only
```

Why forbid the name? Because `amount` is an internal detail. Making it positional-only means
you can later rename the parameter without breaking any caller — nobody was allowed to depend
on the name. Together, `/` and `*` split a signature into three zones:
`f(positional_only, /, normal, *, keyword_only)`.

This stage uses basis points for the rate: 1 bp = 0.01%, so 8.25% tax is `rate_bps=825`.
Integer basis points keep the tax math exact (no float), consistent with the rest of the
engine.

## Your task

In `rules.py`, finish the **signature** of `apply_tax(amount_cents, /, *, rate_bps,
inclusive=False)`. The body is written. You add the two separators:

1. the `/` that makes `amount_cents` positional-only, and
2. the `*` that makes `rate_bps` and `inclusive` keyword-only.

## Worked example

```
>>> import rules
>>> rules.apply_tax(10000, rate_bps=825)              # 8.25% of $100.00
825
>>> rules.apply_tax(10825, rate_bps=825, inclusive=True)   # tax already included
825
>>> rules.apply_tax(10000, 825)                       # rate must be named
Traceback (most recent call last):
TypeError: ...
```

## What the check verifies, and what it leaves to you

- Enforced: tax is computed correctly (and extracted when `inclusive=True`); passing
  `amount_cents` by keyword raises `TypeError` (it is positional-only); passing the rate
  positionally raises `TypeError` (it is keyword-only).
- Your free choice: nothing about the body is yours to change here — the separators are the
  whole point, and they are exactly `/` and `*` in those positions.

<div class="hint" title="If you are stuck">

The signature is `def apply_tax(amount_cents: int, /, *, rate_bps: int, inclusive: bool =
False)`. The `/` comes right after the positional-only parameters; the `*` comes right before
the keyword-only ones.

</div>

Reference: Python documentation, "Special parameters — Positional-or-Keyword,
Positional-Only, Keyword-Only" at docs.python.org.
