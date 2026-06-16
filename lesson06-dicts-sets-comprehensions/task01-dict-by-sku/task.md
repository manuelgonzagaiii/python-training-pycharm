# Stage 1: indexing the catalog by SKU

So far the catalog is a list, and finding a product by its SKU means scanning every
record until one matches. That is fine for three products and painful for thirty
thousand: the work grows with the size of the catalog. A **dict** (dictionary) fixes
this. It maps a *key* straight to a *value*, and the lookup takes roughly the same time
whether the dict holds three entries or three million — it does not walk the whole
collection to find one key.

That speed is the whole reason MiniERP keeps a SKU index. The list stays the catalog of
record (it has an order, it can hold duplicates while you are editing); the dict is a
fast lookup table built *from* the list whenever you need by-SKU access.

## What a dict is

A dict is a set of `key: value` pairs. You read and write a value by its key with square
brackets:

```
>>> stock = {"A-001": 5, "A-002": 0}
>>> stock["A-001"]
5
>>> stock["B-010"] = 12      # add or replace a pair
```

Two properties matter here. Keys are **unique** — assigning the same key again overwrites
the old value, it does not add a second entry. And since Python 3.7 a dict **keeps
insertion order**, so iterating the index yields SKUs in the order you added them. (Older
material that says "dicts are unordered" predates 3.7; that is legacy advice.)

A key must be **hashable** — an immutable value such as a string or a tuple. A SKU is a
string, so it is a natural key.

## Your task

In `catalog.py`, finish `index_by_sku(catalog)`. It walks the catalog and, for each
product, stores the record in `index` under its SKU (`product[0]`). The empty dict and
the `return` are written for you; you write the one line that records each pair.

## Worked example

```
>>> import catalog
>>> idx = catalog.index_by_sku(catalog.seed_catalog())
>>> idx["A-001"]
('A-001', 'Widget', 999, 5)
>>> "B-010" in idx          # membership test, no exception
True
>>> list(idx)               # keys, in insertion order
['A-001', 'A-002', 'B-010']
```

## What the check verifies, and what it leaves to you

- Enforced: every SKU maps to its own record; the index keeps catalog order; membership
  (`in`) reports present and absent keys correctly.
- Your free choice: how you write the loop body. Indexing (`index[product[0]] = product`)
  is shown, but any line that stores each record under its SKU passes.

<div class="hint" title="If you are stuck">

Inside the loop you have `product`, and `product[0]` is its SKU. Assign the whole record
into `index` under that key: `index[product[0]] = product`.

</div>

Reference: Python documentation, "Mapping Types — dict" at docs.python.org.
