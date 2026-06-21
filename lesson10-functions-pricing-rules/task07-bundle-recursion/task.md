# Stage 7: recursion and the recursion limit

Some MiniERP products are **bundles**: a "starter kit" is really 2 widgets and 1 manual, and
the manual might itself be a bundle. To price a bundle you must flatten it into its leaf
products. A structure that can contain itself is naturally handled by a function that calls
itself — **recursion**.

## Base case and recursive case

Every recursion needs two parts, and getting them right is the whole skill:

- The **base case** — a shape simple enough to answer directly, with no further recursion. For
  bundles, a plain product (a leaf) just returns itself.
- The **recursive case** — break the problem into smaller pieces and call the function on each,
  combining the results. A bundle expands each component, scaling quantities as it descends.

```
def expand_bundle(catalog, sku, qty):
    components = catalog.get(sku)
    if not components:
        return [(sku, qty)]          # base case: a leaf
    leaves = []
    for comp_sku, comp_qty in components:
        leaves += expand_bundle(catalog, comp_sku, comp_qty * qty)   # recursive case
    return leaves
```

The base case is what makes recursion **stop**. Without one, the function calls itself
forever.

## The recursion limit

Python guards against runaway recursion with a limit on how deep the call stack can go
(`sys.getrecursionlimit()`, 1000 by default). Exceed it and you get a `RecursionError` instead
of a crash. A bundle that accidentally references itself ("kit contains kit") would recurse
forever, so `expand_bundle` carries a depth counter and raises early with a clear message —
defensive recursion. Recursion is the natural fit for tree-shaped data like this; for a flat
list, a plain loop is simpler and avoids the stack limit entirely.

## Your task

In `rules.py`, finish `expand_bundle(catalog, sku, qty)`:

1. the **base case** — when a SKU has no components, return it as a single `(sku, qty)` line,
   and
2. the **recursive case** — expand each component, scaling its quantity by the bundle's `qty`.

## Worked example

```
>>> import rules
>>> catalog = {"KIT": [("A", 2), ("B", 1)], "B": [("C", 3)]}
>>> rules.expand_bundle(catalog, "A", 5)        # a leaf
[('A', 5)]
>>> dict(rules.expand_bundle(catalog, "KIT", 1))  # KIT -> 2 A, 1 B -> 1 B is 3 C
{'A': 2, 'C': 3}
>>> dict(rules.expand_bundle(catalog, "KIT", 2))  # quantities scale
{'A': 4, 'C': 6}
```

## What the check verifies, and what it leaves to you

- Enforced: a leaf SKU returns itself as one line; a nested bundle flattens to its leaves; the
  quantities multiply correctly down the tree.
- Your free choice: how you accumulate the leaves (a list with `+=`, `extend`, or a
  comprehension) and whether you keep the depth guard — the check grades the flattened result.

<div class="hint" title="If you are stuck">

The base case is `return [(sku, qty)]`. The recursive call is
`expand_bundle(catalog, component_sku, component_qty * qty, _depth + 1)` — note the quantity
is multiplied so a kit-of-kits scales correctly.

</div>

Reference: Python documentation, the `sys.getrecursionlimit` / `sys.setrecursionlimit`
functions and "RecursionError" at docs.python.org.
