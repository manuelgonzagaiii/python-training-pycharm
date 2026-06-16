# Stage 8: a validating catalog with UserDict

So far the catalog has been a dict that any code can write to, with no guarantee that what
goes in is sensible — nothing stops a negative price or an empty SKU from being stored. The
fix is to make the catalog a **type of its own** that checks every insertion, so the rule
lives in one place and cannot be forgotten at a call site.

You might reach for `class Catalog(dict)` and override `__setitem__`. It almost works, but
there is a well-known trap: built-in `dict` does not route its other methods through your
`__setitem__`. `dict.update(...)`, `dict.setdefault(...)`, and the `dict(**kwargs)`
constructor all insert keys *without* calling the `__setitem__` you wrote — so your
validation has holes you cannot see. This is exactly why subclassing `dict` directly is
discouraged for this purpose.

`collections.UserDict` exists to close those holes. It is a dict-like class that keeps its
real data in a plain dict attribute called `.data` and implements every mutating method in
terms of `__setitem__`. Override that one method and **all** insertion paths — `update`,
`setdefault`, the constructor — funnel through your check:

```
>>> from collections import UserDict
>>> class Catalog(UserDict):
...     def __setitem__(self, sku, product):
...         if not sku:
...             raise ValueError("sku must be non-empty")
...         super().__setitem__(sku, product)   # hand the validated pair to UserDict
```

The `super().__setitem__(sku, product)` call is the crucial last step: after your checks
pass, you delegate the actual storing to the parent class, which puts it in `.data`. Skip
it and nothing is ever stored; replace it with `self.data[sku] = product` and it works too,
but going through `super()` is the cleaner expression of "do the normal thing now that I
have validated".

Because a `UserDict` behaves like a dict in every other respect — `len`, `in`, iteration,
`[]` reads — the rest of MiniERP treats a `Catalog` as just another mapping.

## Your task

In `catalog.py`, the `Catalog(UserDict)` class is written except for its final line. The
validation checks (non-empty SKU; non-negative price and quantity) are provided. Add the
call that stores the validated product by delegating to the parent `UserDict`.

## Worked example

```
>>> import catalog
>>> c = catalog.Catalog()
>>> c["A-001"] = catalog.make_product("A-001", "Widget", 999, 5)   # valid -> stored
>>> c["A-001"].name
'Widget'
>>> c["A-001"] = catalog.make_product("A-001", "Bad", -1, 5)       # invalid price
Traceback (most recent call last):
ValueError: price and qty must be non-negative
>>> len(c)                 # behaves like a dict
1
```

## What the check verifies, and what it leaves to you

- Enforced: a valid product is stored and readable back; an empty SKU, a negative price, or
  a negative quantity each raises `ValueError`; the catalog otherwise behaves like a dict
  (`len`, `in`, iteration).
- Your free choice: how you delegate the store — `super().__setitem__(sku, product)` or
  `self.data[sku] = product` both pass. The exception *messages* are yours; only that a
  `ValueError` is raised for invalid input is enforced.

<div class="hint" title="If you are stuck">

After the checks, store via the parent: `super().__setitem__(sku, product)`.

</div>

Reference: Python documentation, "collections.UserDict" at docs.python.org.
