# Stage 6: unpacking records, starred targets, and swaps

A record is a tuple of four fields, and reaching them by index — `product[0]`, `product[2]`
— is both ugly and easy to get wrong. **Unpacking** pulls the fields into named variables in
one line, and it scales from a single record to splitting a whole list. This stage finishes
`catalog.py` for the lesson with two functions built on it.

## Unpacking a record

Put a tuple of names on the left of `=` and Python distributes the fields:

```
>>> sku, name, price_cents, qty = ("A-1", "Widget", 999, 5)
>>> name, qty
('Widget', 5)
```

The number of names must match the number of fields. This reads far better than
`product[0]`, `product[1]`, ... and it makes the field meanings obvious. It also works
directly in a `for` loop, so you can unpack each record as you iterate:

```
>>> for sku, name, price_cents, qty in catalog:
...     ...
```

If you do not need a field, the convention is to unpack it into `_`: `sku, _, price, _ =
record`. And unpacking gives you the cleanest **swap** in any language — no temporary
variable: `a, b = b, a`.

## Starred targets: head and tail

A `*name` target soaks up "all the rest" as a **list**, so you can split a sequence into
parts in one line:

```
>>> first, *rest = [10, 20, 30, 40]
>>> first, rest
(10, [20, 30, 40])
>>> *init, last = [10, 20, 30, 40]
>>> init, last
([10, 20, 30], 40)
```

MiniERP uses this to peel a "featured" product off the front of the catalog and keep the
remainder for a "rest of catalog" view.

## Your task

In `catalog.py`, fill in:

1. `describe(product)` — unpack the record into `sku, name, price_cents, qty` (the formatted
   return line is written for you).
2. `split_featured(catalog)` — unpack the list into `first` and a starred `*rest`.

## Worked example

```
>>> import catalog
>>> catalog.describe(catalog.make_product("A-001", "Widget", 999, 5))
'A-001 Widget $9.99 qty 5'
>>> featured, rest = catalog.split_featured(catalog.seed_catalog())
>>> featured
('A-001', 'Widget', 999, 5)
>>> rest                       # a list of the remaining records
[('A-002', 'Gadget', 1499, 0), ('B-010', 'Gizmo', 250, 12)]
```

## What the check verifies, and what it leaves to you

- Enforced: `describe` includes all four fields with the price shown in dollars (e.g. `999`
  -> `9.99`); `split_featured` returns the first record and the rest **as a list**.
- Your free choice: the exact label layout in `describe` is fixed here only because the line
  is provided; your job is the unpacking that feeds it.

<div class="hint" title="If you are stuck">

`describe` starts with `sku, name, price_cents, qty = product`. `split_featured` is
`first, *rest = catalog`.

</div>

Reference: Python documentation, "Assignment statements — unpacking and starred targets" at
docs.python.org.
