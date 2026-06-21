# Stage 2: validation with a setter

A property is not only for reading. Give it a **setter** and assignment runs your code too —
the place to enforce a rule. MiniERP must never store a negative price, regardless of which
interface tries to set it. This stage turns `price_cents` itself into a validated property so
the rule lives in one place and cannot be bypassed.

## Getter plus setter

A full read/write property is a getter and a setter over a **private backing attribute** (by
convention, the same name with a leading underscore):

```
    @property
    def price_cents(self):
        return self._price_cents

    @price_cents.setter
    def price_cents(self, value):
        if value < 0:
            raise ValueError("price must not be negative")
        self._price_cents = value
```

Now `product.price_cents` reads `_price_cents` through the getter, and `product.price_cents =
250` runs the setter, which validates before storing. The real value lives in `_price_cents`;
`price_cents` is the guarded gate in front of it. The leading underscore is a convention
meaning "internal — do not touch from outside"; Python does not enforce it, but it signals the
backing store is private.

The quiet payoff: `__init__` already does `self.price_cents = price_cents`. That assignment now
goes through the **same setter**, so a Product can never be *born* with a negative price either
— construction and later edits are validated by one piece of code. This is the core reason
properties beat plain public attributes: you can add a rule later without changing how callers
write the assignment.

## Your task

In `domain.py`, finish the `price_cents` setter so it rejects a negative `value` (raise
`ValueError`) and otherwise stores it in `self._price_cents`. The getter is provided.

## Worked example

```
>>> import domain
>>> p = domain.Product("A-001", "Widget", 100)
>>> p.price_cents = 250          # goes through the setter
>>> p.price_cents
250
>>> p.price_cents = -1
Traceback (most recent call last):
ValueError: price must not be negative
>>> domain.Product("B", "Bad", -5)   # __init__ uses the same setter
Traceback (most recent call last):
ValueError: price must not be negative
```

## What the check verifies, and what it leaves to you

- Enforced: assigning a negative price (directly or via the constructor) raises `ValueError`;
  a valid price round-trips through read and write.
- Your free choice: the exception message is yours, and you may validate however you like (an
  `if`, a guard clause). What the check insists on is that a negative price is rejected and a
  valid one is stored — the invariant, not the wording.

<div class="hint" title="If you are stuck">

In the setter: `if value < 0: raise ValueError(...)`, then `self._price_cents = value`. Store
into `_price_cents` (the backing attribute), not `price_cents` — assigning to `price_cents`
would call the setter again and loop forever.

</div>

Reference: Python documentation, "@property" — setter usage, at docs.python.org.
