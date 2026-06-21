# Stage 1: computed attributes with @property

A Product stores its price as integer cents. But almost everything that *displays* a price
wants dollars — `15.99`, not `1599`. You could store both and keep them in sync by hand, but
that is a bug waiting to happen: change one and forget the other. A **computed property**
removes the duplication. It looks like a plain attribute to callers, but it is really a method
that runs each time you read it, so the value is always derived fresh from the source of
truth.

## What @property does

Decorate a method with `@property` and it becomes readable as an attribute — no parentheses:

```
    @property
    def price_dollars(self):
        return Decimal(self.price_cents) / 100
```

Now `product.price_dollars` (not `product.price_dollars()`) returns the price in dollars,
computed from `price_cents` every time. There is nothing to keep in sync: `price_cents` is the
one stored value, and `price_dollars` is always exactly `price_cents / 100`.

Two design points worth holding onto:

- **It is read-only here.** With only a getter, `product.price_dollars = 20` raises
  `AttributeError`. That is correct — the dollars are *derived*, so the price is set through
  `price_cents`, not the computed view. (The next stage adds a setter to make a *different*
  attribute writable-with-validation.)
- **Decimal, not float.** Dividing by 100 with `Decimal` keeps the result exact —
  `Decimal('15.99')`. A float `1599 / 100` would give `15.99` that is secretly
  `15.9900000000000002`. Money never touches float in this course, and a computed money view
  is no exception.

## Your task

In `domain.py`, finish the `price_dollars` property so it returns `price_cents` as an exact
`Decimal` number of dollars.

## Worked example

```
>>> import domain
>>> from decimal import Decimal
>>> p = domain.Product("A-001", "Widget", 1599)
>>> p.price_dollars                 # read like an attribute -- no ()
Decimal('15.99')
>>> p.price_dollars == Decimal("15.99")
True
```

## What the check verifies, and what it leaves to you

- Enforced: `price_dollars` returns the price in dollars as an exact `Decimal` (1599 cents
  becomes `Decimal('15.99')`), computed from `price_cents`.
- Your free choice: how you compute it, as long as the result is an exact `Decimal`. The check
  rejects a float result, because a float price would reintroduce the rounding errors the cents
  representation exists to avoid.

<div class="hint" title="If you are stuck">

`Decimal(self.price_cents) / 100` divides the integer cents by 100 and stays exact. Build the
`Decimal` from the int (`Decimal(self.price_cents)`), not from a float.

</div>

Reference: Python documentation, "@property" (Built-in Functions) at docs.python.org.
