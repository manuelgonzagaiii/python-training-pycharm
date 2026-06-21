# Stage 4: class patterns and __match_args__

Token lists and dicts are loose. Once a request is understood, MiniERP turns it into a
**typed object** — `AddRequest`, `PriceRequest`, `DiscountRequest` — so the rest of the
system passes around real types instead of guessing at dict keys. `match` can then dispatch
on those types with **class patterns**.

## Dataclasses for the request types

A `@dataclass` writes the boilerplate (`__init__`, `__repr__`, `__eq__`) for a class that is
mostly fields:

```
from dataclasses import dataclass

@dataclass(slots=True)
class PriceRequest:
    sku: str
    qty: int
```

`slots=True` stores the fields in a fixed `__slots__` layout instead of a per-instance dict:
less memory and no accidental new attributes. (You will go deeper on dataclasses and slots
in the OOP phase; here they are just a quick way to define the request types.)

## Class patterns: type plus fields

```
match req:
    case AddRequest(sku, qty):          # positional subpatterns
        ...
    case PriceRequest(sku=s, qty=q):    # keyword subpatterns
        ...
```

A class pattern checks `isinstance(req, AddRequest)` **and** extracts fields in one step.
There are two ways to name the fields:

- **Positional** — `AddRequest(sku, qty)` — relies on the class's `__match_args__`, a tuple
  naming the fields in order. A `@dataclass` generates it automatically from the field order,
  so positional subpatterns just work.
- **Keyword** — `PriceRequest(sku=s, qty=q)` — names the fields explicitly and does not
  depend on order.

One sharp edge worth knowing: if you make a dataclass `kw_only=True`, its `__match_args__` is
**empty**, and a positional class pattern will not match it. That is exactly why these
request classes are not keyword-only — the positional `AddRequest(sku, qty)` pattern depends
on it.

## Your task

In `dispatch.py`, finish `describe(req)`. The dataclasses and the discount/fallback cases are
written. Fill in:

1. the **positional** class pattern for `AddRequest` (binding `sku` and `qty`), and
2. the **keyword** class pattern for `PriceRequest` (binding `s` and `q`).

## Worked example

```
>>> import dispatch
>>> dispatch.describe(dispatch.AddRequest("A-001", 3))
'add 3 x A-001'
>>> dispatch.describe(dispatch.PriceRequest("A-001", 2))
'price 2 x A-001'
>>> dispatch.describe(object())
'unknown request'
```

## What the check verifies, and what it leaves to you

- Enforced: each request type is recognized and its fields are surfaced in the summary; an
  unrecognized object yields `'unknown request'`.
- Your free choice: you may write `AddRequest` with keyword subpatterns
  (`AddRequest(sku=sku, qty=qty)`) instead of positional — both bind the fields correctly and
  pass. What the check pins down is that each field lands in its right role (the SKU read as the
  SKU, the quantity as the quantity); the summary text itself is the provided part of the stage.

<div class="hint" title="If you are stuck">

Positional: `case AddRequest(sku, qty):`. Keyword: `case PriceRequest(sku=s, qty=q):`.

</div>

Reference: Python documentation, "The match statement" (class patterns, `__match_args__`) and
"dataclasses" at docs.python.org.
