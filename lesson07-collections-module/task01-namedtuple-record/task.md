# Stage 1: upgrading the record to a NamedTuple

The catalog record has been a plain tuple of four fields, reached by position:
`product[0]` for the SKU, `product[2]` for the price. That works, but the numbers carry
no meaning — a reader has to remember that index 2 is the price and not the quantity, and
a typo like `product[3]` where you meant `product[2]` is a silent bug, not an error.

A **named tuple** keeps everything good about the tuple and removes that weakness. It is
still a tuple — same immutability, same unpacking, same indexing, works anywhere a tuple
works — but each field also has a name. This is the first refactor of the catalog, and a
realistic one: you start with the simplest thing that works (a bare tuple), then upgrade
the type once the shape has settled, **without** rewriting all the code that used it.

## typing.NamedTuple

There are two ways to make one. The older `collections.namedtuple("Product", "sku name
...")` builds the class from a string of field names. The modern, preferred form is a
class with `typing.NamedTuple` as its base, because the fields get real type annotations
and it reads like an ordinary class:

```
from typing import NamedTuple

class ProductRecord(NamedTuple):
    sku: str
    name: str
    price_cents: int
    qty: int
```

Now both styles of access work on the same object:

```
>>> p = ProductRecord("A-001", "Widget", 999, 5)
>>> p.price_cents          # by name -- clear
999
>>> p[2]                   # by position -- still a tuple
999
>>> isinstance(p, tuple)
True
>>> sku, name, price, qty = p   # unpacks like any tuple
```

Because a `ProductRecord` *is* a tuple, every function written in the earlier lessons —
`describe`, `split_featured`, `index_by_sku`, the comprehensions — keeps working
unchanged. That is the payoff of the upgrade: you change the constructor in one place and
carry the rest forward. The module keeps `type Product = ProductRecord` so the name
`Product` still refers to "the record type", as it always has.

## Editing without copying: _replace

A tuple is immutable, so you cannot assign `product.price_cents = 1299`. To "change" a
field you make a **copy** with that one field replaced. Named tuples provide `_replace`
for exactly this:

```
>>> p._replace(price_cents=1299)
ProductRecord(sku='A-001', name='Widget', price_cents=1299, qty=5)
>>> p.price_cents          # the original is untouched
999
```

The leading underscore looks private but is not — it is named that way only so it cannot
collide with a field called `replace`. This copy-with-changes style is how you "edit"
immutable records throughout MiniERP: repricing returns a new record rather than mutating
a shared one, so nothing else holding the old record is surprised.

## Your task

In `catalog.py`, finish two pieces:

1. `make_product(...)` — return a `ProductRecord` built from the four arguments.
2. `reprice(product, new_price)` — return a copy of the record with only `price_cents`
   changed, using `_replace`.

## Worked example

```
>>> import catalog
>>> p = catalog.make_product("A-001", "Widget", 999, 5)
>>> p.sku, p.qty
('A-001', 5)
>>> q = catalog.reprice(p, 1299)
>>> q.price_cents, p.price_cents     # copy changed, original intact
(1299, 999)
```

## What the check verifies, and what it leaves to you

- Enforced: `make_product` returns a record whose fields are reachable both by name
  (`p.sku`) and by position (`p[0]`), and which is still a `tuple`; `reprice` changes only
  the price and leaves the original record unchanged.
- Your free choice: nothing about the field *order* is yours to change (the record's shape
  is fixed and shared across the whole course), but how you spell the constructor call is —
  positional or keyword arguments both pass.

<div class="hint" title="If you are stuck">

`make_product` returns `ProductRecord(sku, name, price_cents, qty)`. `reprice` returns
`product._replace(price_cents=new_price)`.

</div>

Reference: Python documentation, "typing.NamedTuple" and "collections.namedtuple"
(`_replace`) at docs.python.org.
