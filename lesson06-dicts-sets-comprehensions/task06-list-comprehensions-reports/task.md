# Stage 6: list comprehensions for reports

A report is almost always "take the catalog, keep the rows that match, pull out the
column I care about". Written the long way that is three lines of boilerplate every time:

```
result = []
for product in catalog:
    if product[3] < threshold:
        result.append(product)
return result
```

A **list comprehension** says the same thing in one expression that reads close to plain
English — "this product, for each product in the catalog, if its quantity is low":

```
[product for product in catalog if product[3] < threshold]
```

The shape is `[ EXPRESSION for ITEM in ITERABLE if CONDITION ]`. The `if` is optional —
drop it to keep everything. The `EXPRESSION` is what each kept item becomes, so it does
double duty as a filter (the `if`) and a transform (the expression). To collect names
instead of whole records, make the expression `product[1]`.

Why prefer it: it is shorter, there is no `append` call to omit, and it signals intent — a
reader sees "this builds a list by filtering/mapping" at a glance. It also tends to be a
little faster, because the list is built by the interpreter rather than by repeated
Python-level `.append` calls. The one caution is readability: if a comprehension grows a
second `if`, nested loops, and a complicated expression all at once, a plain loop is
clearer. Keep them to one obvious transform.

## Your task

In `catalog.py`, write two comprehensions:

1. `low_stock(catalog, threshold)` — the products whose quantity (`product[3]`) is
   **strictly** below `threshold`.
2. `names_of(catalog)` — each product's name (`product[1]`), in catalog order.

## Worked example

```
>>> import catalog
>>> cat = [catalog.make_product("A", "Widget", 100, 2),
...        catalog.make_product("B", "Gadget", 100, 5),
...        catalog.make_product("C", "Gizmo", 100, 0)]
>>> [p[0] for p in catalog.low_stock(cat, 5)]   # qty 5 is NOT below 5
['A', 'C']
>>> catalog.names_of(cat)
['Widget', 'Gadget', 'Gizmo']
```

## What the check verifies, and what it leaves to you

- Enforced: `low_stock` uses a strict `<` (a quantity exactly equal to the threshold is
  not low) and returns a **list**; `names_of` returns the names in order.
- Your free choice: you do not have to use a comprehension — an explicit loop that builds
  the same list passes too. The comprehension is the recommended form, and what this stage
  is teaching, but the check grades the resulting list.

<div class="hint" title="If you are stuck">

`low_stock` is `[product for product in catalog if product[3] < threshold]`. `names_of`
is `[product[1] for product in catalog]`.

</div>

Reference: Python documentation, "List Comprehensions" (the tutorial, Data Structures
section) at docs.python.org.
