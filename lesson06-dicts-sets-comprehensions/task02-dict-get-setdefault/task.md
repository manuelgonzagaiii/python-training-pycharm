# Stage 2: safe lookups with get and setdefault

Reading a missing key with square brackets raises `KeyError` and stops the program:

```
>>> stock = {"A-001": 5}
>>> stock["NOPE"]
Traceback (most recent call last):
KeyError: 'NOPE'
```

In a real ERP, "no product with that SKU" is a normal answer, not a crash. A user mistypes
a code; a report asks for an item that was deleted. The dict gives you two tools so the
ordinary "not there" case never throws.

## get: a default instead of an exception

`d.get(key)` returns the value if the key is present and `None` if it is not. Pass a
second argument to choose a different default:

```
>>> stock.get("A-001")
5
>>> stock.get("NOPE")        # returns None, no traceback
>>> stock.get("NOPE", 0)     # your own default
0
```

This is the idiomatic way to express "look it up, and tell me plainly if it is absent".

## setdefault: get-or-create in one step

When you are *building* a dict whose values are themselves containers — say, a list of
products per category — you keep hitting the same pattern: "if this key is missing, start
it with an empty list, then append". `setdefault(key, default)` does exactly that in one
call. It returns the existing value if the key is present, or inserts `default` and
returns it if not:

```
>>> groups = {}
>>> groups.setdefault("A", []).append("A-001")   # "A" was missing -> []
>>> groups.setdefault("A", []).append("A-002")   # "A" exists -> same list
>>> groups
{'A': ['A-001', 'A-002']}
```

Because it returns the list, you can `.append(...)` straight onto it. (In the next lesson
you will meet `collections.defaultdict`, which automates this further; `setdefault` is the
plain-dict way to understand what it does.)

## Your task

In `catalog.py`, finish two functions:

1. `find(index, sku)` — return the record for `sku`, or `None` if absent. Use `get`.
2. `group_by_category(catalog)` — bucket products by their category code (the SKU up to
   the first `-`). The category is already computed into `category`; you write the
   `setdefault(...).append(...)` line.

## Worked example

```
>>> import catalog
>>> idx = catalog.index_by_sku(catalog.seed_catalog())
>>> catalog.find(idx, "A-001")
('A-001', 'Widget', 999, 5)
>>> catalog.find(idx, "ZZZ") is None
True
>>> g = catalog.group_by_category(catalog.seed_catalog())
>>> sorted(g)
['A', 'B']
>>> [p[0] for p in g["A"]]
['A-001', 'A-002']
```

## What the check verifies, and what it leaves to you

- Enforced: `find` returns the record for a known SKU and `None` (never a `KeyError`) for
  an unknown one; `group_by_category` puts each product in a list under its category code.
- Your free choice: nothing about wording is fixed. Any implementation that returns the
  right values passes — for example, `find` could use `get` or an explicit membership
  test, as long as a missing SKU yields `None`.

<div class="hint" title="If you are stuck">

`find` is `return index.get(sku)`. The grouping line is
`groups.setdefault(category, []).append(product)`.

</div>

Reference: Python documentation, "Mapping Types — dict" (`get`, `setdefault`) at
docs.python.org.
