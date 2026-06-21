# Stage 3: shared versus per-object state

Some facts belong to *each* product — its SKU, its name, its price. Others belong to *every*
product at once — the currency MiniERP prices things in, a default tax rate. Python keeps
these two kinds of data in different places, and knowing which is which is one of the core
skills of designing a class.

## Instance attributes versus class attributes

You already met **instance attributes**: assigned with `self.x = ...` inside `__init__`, one
independent copy per object. A **class attribute** is defined directly in the class body, not
on `self`, and there is exactly **one** copy shared by the class and every instance:

```
class Product:
    CURRENCY = "USD"               # class attribute -- one copy, shared

    def __init__(self, sku, name, price_cents):
        self.sku = sku             # instance attribute -- one per object
        ...
```

Both are reachable through an instance, so `product.CURRENCY` works, but the lookup is the
point: Python checks the instance first, then falls back to the class. Since no instance sets
`CURRENCY`, every product reads the single class-level value. Change `Product.CURRENCY` and
every product sees the new value at once — that is what "shared" means.

Class attributes are the right home for **constants and defaults** that are the same for the
whole type: the currency code, a default tax rate, a version number. By convention,
constants are written in `UPPER_SNAKE_CASE`.

## The mutable-class-attribute trap

One caution for later: a class attribute that is a **mutable** object (a list or dict) is
shared too, so appending to it from one instance changes it for all of them. That is almost
never what you want for per-object data — per-object data goes on `self`. For an immutable
constant like a string or an int, sharing is exactly right, which is why `CURRENCY = "USD"`
is safe.

## Your task

In `domain.py`, add the shared class attribute `CURRENCY` set to the string `"USD"`. The
companion constant `DEFAULT_TAX_RATE_BPS` (a default tax rate in basis points) is written for
you alongside it.

## Worked example

```
>>> import domain
>>> domain.Product.CURRENCY            # read straight off the class
'USD'
>>> a = domain.Product("A", "Widget", 100)
>>> b = domain.Product("B", "Gizmo", 200)
>>> a.CURRENCY, b.CURRENCY             # both instances see the one shared value
('USD', 'USD')
>>> domain.Product.DEFAULT_TAX_RATE_BPS
0
```

## What the check verifies, and what it leaves to you

- Enforced: `Product.CURRENCY` is `"USD"` and is visible from instances; the
  `DEFAULT_TAX_RATE_BPS` constant exists.
- Your free choice: nothing about how you lay out the class body is fixed. `CURRENCY` must be
  the string `"USD"` because every later display reads it, but that is a real
  best-practice value, not a stylistic one.

<div class="hint" title="If you are stuck">

In the class body (not inside a method, and not on `self`), write `CURRENCY = "USD"`.

</div>

Reference: Python documentation, "Classes — Class and Instance Variables" at docs.python.org.
