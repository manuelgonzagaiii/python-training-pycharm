# Stage 4: a Money value object

Prices, discounts, taxes, line totals, invoice grand totals — money is everywhere in MiniERP,
and so far it has been passed around as bare integer cents. A bare int works but says nothing:
is `1599` cents, dollars, a quantity? And it carries no currency. This stage introduces a
**value object** — a small class whose whole job is to represent one kind of value correctly —
to give money a real type.

## What a value object is

A value object is defined by its **value**, not its identity: two `Money` objects with the same
cents and currency *are* the same money, the way two `Decimal("15.00")` are equal. Such objects
are small, focused, and ideally immutable. `Money` here holds two facts and the behavior that
belongs to them:

```
class Money:
    def __init__(self, cents, currency="USD"):
        self.cents = cents          # integer minor units -- exact, never float
        self.currency = currency
```

Storing **integer cents** is the key decision, and it is the same one the catalog and pricing
engine already made. Integers are exact; binary floats are not (`0.1 + 0.2` is famously not
`0.3`), and rounding errors in money are unacceptable. So `Money` never stores a float.

> A note on what comes later: this is the plain-class version of `Money`. A later lesson
> re-expresses the very same idea — integer cents plus a currency — as a frozen dataclass once
> you have learned dataclasses, and that version supersedes this one. The representation never
> changes; only the machinery around it gets tighter. Building it by hand first is what makes
> the dataclass version feel like a shortcut rather than magic.

## A convenience constructor and a computed view

People think in dollars, so a factory that takes dollars is handy — but to stay exact it accepts
a **string or `Decimal`**, never a float, and converts to cents:

```
    @classmethod
    def from_dollars(cls, dollars, currency="USD"):
        return cls(int(Decimal(str(dollars)) * 100), currency)
```

And the reverse, a computed property that reports the amount in dollars:

```
    @property
    def dollars(self):
        return Decimal(self.cents) / 100
```

Together these are the boundary: dollars (human, Decimal) in and out, integer cents stored
inside. This is the same "Decimal at the edges, integer cents in the core" rule the money work
in earlier phases established.

## Your task

In `domain.py`, finish the two conversions on `Money`:

1. `from_dollars(...)` — convert the `dollars` argument to exact integer cents.
2. the `dollars` property — return the stored cents as an exact `Decimal` number of dollars.

## Worked example

```
>>> import domain
>>> from decimal import Decimal
>>> m = domain.Money(1599)
>>> m.cents, m.currency
(1599, 'USD')
>>> domain.Money.from_dollars("15.99").cents
1599
>>> m.dollars
Decimal('15.99')
```

## What the check verifies, and what it leaves to you

- Enforced: `Money` stores integer cents and a currency; `from_dollars("15.99")` yields `1599`
  cents; `dollars` returns an exact `Decimal`.
- Your free choice: the currency default and how you convert are yours, as long as the cents
  come out exact. The check rejects a conversion that loses cents to binary-float rounding —
  for example `int(float(dollars) * 100)`, which truncates `"0.29"` to 28 instead of 29.
  Building from `Decimal`, or from exact integer math, keeps it right, which is why this course
  never reaches for `float` in money.

<div class="hint" title="If you are stuck">

`from_dollars`: `int(Decimal(str(dollars)) * 100)` — `str(dollars)` lets it accept a string or
a `Decimal` while refusing to trust a float. `dollars` property: `Decimal(self.cents) / 100`.

</div>

Reference: Python documentation, "decimal — Decimal fixed point arithmetic" and "@classmethod"
at docs.python.org.
