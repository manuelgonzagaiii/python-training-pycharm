# Stage 3: grouping with defaultdict

In Lesson 6 you grouped products by category with `setdefault`:

```
groups.setdefault(category, []).append(product)
```

That works, but the `setdefault(category, [])` part is pure ceremony — it exists only to
make sure a list is there before you append. `collections.defaultdict` moves that ceremony
into the container itself, so the loop body shrinks to the thing you actually mean.

## How defaultdict works

You hand `defaultdict` a **factory** — a zero-argument callable that produces the default
value. When you read a key that is missing, the defaultdict calls the factory, stores the
result under that key, and returns it. So the key is always ready to be used:

```
>>> from collections import defaultdict
>>> groups = defaultdict(list)       # factory is `list` -> missing keys become []
>>> groups["A"].append("A-001")      # "A" missing -> list() -> [], then append
>>> groups["A"].append("A-002")
>>> dict(groups)
{'A': ['A-001', 'A-002']}
```

The factory is the function itself, not a call — pass `list`, not `list()`. `defaultdict(set)`
gives empty-set defaults, `defaultdict(int)` gives `0` (handy for counting, though `Counter`
is purpose-built for that).

One habit to build: a `defaultdict` *creates* a key the instant you read it, even a key you
only meant to check. If you do not want that, test with `in` first, or — when handing the
result to other code — convert it back to a plain dict with `dict(groups)` so callers get
ordinary "missing means missing" behaviour. Both functions here return `dict(...)` for that
reason; that line is written for you.

## Your task

In `catalog.py`, finish two groupings by choosing the right `defaultdict` factory:

1. `group_by_category_dd(catalog)` — bucket products into **lists** by category code. The
   factory should default missing keys to an empty list.
2. `tag_to_skus(tags_index)` — invert the tag index so each tag maps to the **set** of
   SKUs carrying it. The factory should default missing keys to an empty set.

## Worked example

```
>>> import catalog
>>> g = catalog.group_by_category_dd(catalog.seed_catalog())
>>> sorted(g), len(g["A"])
(['A', 'B'], 2)
>>> type(g).__name__              # converted back to a plain dict
'dict'
>>> inv = catalog.tag_to_skus({"A-001": {"new", "sale"}, "A-002": {"sale"}})
>>> sorted(inv["sale"])
['A-001', 'A-002']
```

## What the check verifies, and what it leaves to you

- Enforced: products land in the correct category buckets; the tag index is correctly
  inverted to tag -> set of SKUs; `group_by_category_dd` returns a plain `dict` (not a
  leaked defaultdict).
- Your free choice: the grouping mechanism. A `setdefault`-based version like last lesson's
  produces the same result and passes — `defaultdict` is what this stage teaches because it
  is cleaner, not because the check forbids the alternative.

<div class="hint" title="If you are stuck">

The list grouping uses `defaultdict(list)`; the inverted index uses `defaultdict(set)`.
Pass the type itself as the factory, with no parentheses.

</div>

Reference: Python documentation, "collections.defaultdict" at docs.python.org.
