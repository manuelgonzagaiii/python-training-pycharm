# Stage 7: dict and set comprehensions, generators, and the walrus

The comprehension shape from the last stage is not limited to lists. Change the brackets
and you build a dict or a set; drop the brackets and you get a lazy generator. This stage
collects all three, plus one small operator that lets an expression name an intermediate
value as it goes.

## Dict comprehension

Wrap `key: value` pairs in braces to build a dict in one expression:

```
>>> {product[0]: product[2] for product in catalog}   # sku -> price_cents
{'A-001': 999, 'A-002': 1499, 'B-010': 250}
```

The shape is `{ KEY: VALUE for ITEM in ITERABLE }`. This is the natural way to turn a list
of records into a lookup table.

## Set comprehension

Braces with a single value (no colon) build a set, so duplicates collapse automatically.
This one also uses **two** `for` clauses to flatten a collection of tag sets into the flat
set of every tag used:

```
>>> {tag for tags in tags_index.values() for tag in tags}
{'new', 'sale', 'clearance'}
```

Read nested `for` clauses left to right, outer to inner — the same order you would nest
the loops.

## Generator expressions and the walrus

The same shape with **round** brackets is a **generator expression**. It does not build a
list in memory; it yields one item at a time as something consumes it. Feeding a generator
straight into `sum(...)` totals a sequence without ever materialising it — ideal for an
inventory value over a huge catalog:

```
>>> sum(product[2] * product[3] for product in catalog)
```

The **walrus operator** `:=` assigns *inside* an expression, giving the value a name you
can reuse in the same line without a separate statement. MiniERP's inventory total counts
only the lines that actually carry stock — a line worth nothing is skipped — so it needs
each line total in two places: the `> 0` filter that drops empty lines, and the sum
itself. The walrus computes it once and names it:

```
sum(line for product in catalog if (line := product[2] * product[3]) > 0)
```

`line := product[2] * product[3]` computes the line value, binds it to `line`, and both
the `> 0` filter and the `sum` reuse that one value. Without the walrus you would write
`product[2] * product[3]` twice — once to test it, once to add it — recomputing it each
time. The parentheses around the walrus are required. Use `:=` sparingly: it earns its
place exactly here, where a value is filtered on and then reused; over-used, it hurts
readability.

## Your task

In `catalog.py`, finish three functions:

1. `price_index(catalog)` — a **dict** comprehension mapping SKU (`product[0]`) to price
   (`product[2]`).
2. `all_tags(tags_index)` — a **set** comprehension of every tag across all the tag sets.
3. `inventory_value(catalog)` — complete the **walrus** assignment that names each line
   total inside the generator.

## Worked example

```
>>> import catalog
>>> cat = catalog.seed_catalog()
>>> catalog.price_index(cat)
{'A-001': 999, 'A-002': 1499, 'B-010': 250}
>>> sorted(catalog.all_tags({"A": {"new", "sale"}, "B": {"sale", "clearance"}}))
['clearance', 'new', 'sale']
>>> catalog.inventory_value(cat)        # in-stock lines only: 999*5 + 250*12 (A-002 is out of stock)
7995
```

## What the check verifies, and what it leaves to you

- Enforced: `price_index` maps each SKU to its price; `all_tags` returns the union of all
  tags as a set; `inventory_value` totals `price_cents * qty` over the lines that carry
  stock (a zero-stock line adds nothing either way).
- Your free choice: the comprehension style is recommended but not mandatory — an
  equivalent loop, or `inventory_value` written without the walrus, passes as long as the
  returned value is correct.

<div class="hint" title="If you are stuck">

`price_index` is `{product[0]: product[2] for product in catalog}`. `all_tags` is
`{tag for tags in tags_index.values() for tag in tags}`. The walrus piece is
`line := product[2] * product[3]`.

</div>

Reference: Python documentation, "Comprehensions" and "Assignment expressions (PEP 572)"
at docs.python.org.
