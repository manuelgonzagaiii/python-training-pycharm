# Stage 2: ordering with total_ordering

Equality lets objects be compared for sameness; **ordering** lets them be sorted and ranked.
MiniERP wants to sort invoices by amount and rank products by price, which means `Money` and
`Product` need to answer `<`, `<=`, `>`, `>=`. Writing all four by hand is repetitive and
error-prone, so Python gives you a shortcut: define one, and let `functools.total_ordering`
generate the rest.

## One comparison plus a decorator

The four ordering operators map to dunders `__lt__`, `__le__`, `__gt__`, `__ge__`. Define
`__eq__` (you already did) and just **`__lt__`**, then decorate the class with
`@total_ordering`, and it fills in the other three from those two:

```
from functools import total_ordering

@total_ordering
class Money:
    ...
    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("cannot compare Money of different currencies")
        return self.cents < other.cents
```

Now `Money(100) < Money(250)`, `>=`, `min()`, `max()`, and `sorted()` all work, even though
you wrote a single comparison. The same `NotImplemented` guard from the last stage applies, so
comparing a `Money` with an unrelated type defers rather than crashing. And note the
**currency guard**: comparing dollars to euros is meaningless, so it raises rather than
returning a wrong answer — failing loudly on nonsense is part of correct design.

`@total_ordering` is the right tool when one comparison naturally implies the rest, which is
almost always. The only reason to hand-write all four is a rare type whose operators are not
mutually consistent — not the case here.

`Product` gets a natural order too, by price. For sorting, defining `__lt__` alone is enough
(`sorted` only needs `<`), so `Product` is given `__lt__` comparing `price_cents` — no
decorator required unless you want the full set.

## Your task

In `domain.py`, finish `Money.__lt__` so it orders by the cent amount (after the type and
currency guards, which are provided). `Money` is already decorated with `@total_ordering`, and
`Product.__lt__` is written for you.

## Worked example

```
>>> import domain
>>> domain.Money(100) < domain.Money(250)
True
>>> domain.Money(250) >= domain.Money(250)     # earned from __lt__ + __eq__
True
>>> sorted([domain.Money(300), domain.Money(100), domain.Money(200)])[0].cents
100
>>> domain.Money(100, "USD") < domain.Money(100, "EUR")
Traceback (most recent call last):
ValueError: cannot compare Money of different currencies
```

## What the check verifies, and what it leaves to you

- Enforced: all four comparisons behave correctly (so `sorted`, `min`, `max` work); comparing
  different currencies raises `ValueError`; products sort by price.
- Your free choice: how you write the comparison, as long as it orders by the cent amount —
  the check grades the `<`, `<=`, `>`, `>=` behavior, not the exact expression. The
  `@total_ordering` decorator is supplied for you because it is the recommended, less
  error-prone route; this stage teaches that pattern (one `__lt__` generating the rest) rather
  than asking you to hand-write all four operators.

<div class="hint" title="If you are stuck">

`Money.__lt__` ends with `return self.cents < other.cents`. The decorator turns that one
comparison (plus `__eq__`) into the full `<`, `<=`, `>`, `>=` set.

</div>

Reference: Python documentation, "functools.total_ordering" and "Data model — object.__lt__"
at docs.python.org.
