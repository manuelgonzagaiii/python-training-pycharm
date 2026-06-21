# Stage 3: overloading arithmetic on Money

A line total is a unit price times a quantity; an invoice subtotal is a sum of line totals.
Those read most naturally as `price * qty` and `sum(line_totals)`. To make `Money` compose
with the normal `+`, `-`, and `*` operators, you implement the **arithmetic dunders**. Done
right, `Money` behaves like a number while staying exact integer cents.

## Operators are methods

`a + b` calls `a.__add__(b)`; `a * n` calls `a.__mul__(n)`. Each returns a **new** object —
operators never mutate their operands, which is exactly what you want for a value object:

```
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("cannot add Money of different currencies")
        return Money(self.cents + other.cents, self.currency)

    def __mul__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        return Money(self.cents * n, self.currency)
```

The familiar guards return: `NotImplemented` for an operand type you do not handle, and a
currency check so adding USD to EUR raises instead of producing nonsense. `__sub__` mirrors
`__add__`. Multiplication is `Money * int` (a price times a quantity), so it guards for an int.

## `__radd__` and why `sum()` needs it

`sum([m1, m2, m3])` starts from the integer `0` and computes `0 + m1 + ...`. But `int.__add__`
has no idea how to add a `Money`, so it returns `NotImplemented` — and Python then tries the
**reflected** operation `m1.__radd__(0)`. Implement `__radd__` to handle that starting `0` and
`sum()` over `Money` just works:

```
    def __radd__(self, other):
        if other == 0:          # the start value of sum()
            return self
        return NotImplemented
```

The pattern — left operand can't, so Python asks the right operand via the `__r*__` method — is
how Python makes mixed-type arithmetic extensible without every type knowing about every
other.

## Your task

In `domain.py`, finish two pieces of `Money` arithmetic:

1. `__add__` — return a new `Money` of the summed cents in the same currency (after the guards,
   which are provided).
2. `__radd__` — when the other operand is the `0` that `sum()` starts from, return `self`.

`__sub__` and `__mul__` are written for you.

## Worked example

```
>>> import domain
>>> (domain.Money(1500) + domain.Money(250)).cents
1750
>>> (domain.Money(250) * 3).cents
750
>>> sum([domain.Money(100), domain.Money(250), domain.Money(50)]).cents
400
>>> a = domain.Money(100); b = a + domain.Money(50)
>>> a.cents            # the original is untouched -- operators return new objects
100
```

## What the check verifies, and what it leaves to you

- Enforced: `+`, `-`, `*` produce correct new `Money`; the operands are not mutated; `sum()`
  over `Money` totals correctly via `__radd__`; mixing currencies in `+` raises.
- Your free choice: implementation details are yours, as long as the results are right and new
  instances are returned. Returning `NotImplemented` (not raising) for unsupported operands is
  insisted on, because that is what lets Python's reflected-operator machinery work.

<div class="hint" title="If you are stuck">

`__add__`: `return Money(self.cents + other.cents, self.currency)`. `__radd__`: `if other ==
0: return self`. The `0` is the value `sum()` starts from.

</div>

Reference: Python documentation, "Data model — emulating numeric types (__add__, __radd__,
__mul__)" at docs.python.org.
