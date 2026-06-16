# Stage 6: layered lookups with ChainMap

Stock levels in MiniERP come in layers. There is a baseline — the default level for every
SKU — and on top of it, overrides: a warehouse adjustment, a held-for-an-order reservation,
a manual correction. A lookup should check the override layers first and fall back to the
default only when no override applies.

You could merge the layers into one dict with `|`, but merging **copies** everything and
freezes a snapshot — change an underlying layer afterwards and the merged copy is stale.
`collections.ChainMap` takes a different approach: it groups several dicts and **searches
them in order** without copying. A lookup walks the layers left to right and returns the
first one that has the key:

```
>>> from collections import ChainMap
>>> defaults = {"A": 10, "B": 5}
>>> warehouse = {"A": 3}
>>> stock = ChainMap(warehouse, defaults)   # warehouse searched first, then defaults
>>> stock["A"]      # found in warehouse -> the override wins
3
>>> stock["B"]      # not in warehouse -> falls through to defaults
5
```

Two things follow from "searches, does not copy". First, **order is the priority**: the
earliest map that contains the key wins, so put the highest-priority override first.
Second, the underlying dicts are referenced live — edit `defaults` later and the ChainMap
sees the change immediately, and writing through the ChainMap only ever touches its *first*
map, leaving the rest untouched. That makes it ideal for layered configuration and
scoped settings, not just stock.

In this function the signature is `effective_stock(default_levels, *overrides)`. The
`*overrides` collects any number of override dicts into a tuple. You want every override
searched **before** the default, so the ChainMap is built from the spread overrides first,
then the default last.

## Your task

In `catalog.py`, finish `effective_stock(default_levels, *overrides)`. Return a `ChainMap`
that searches the `overrides` first (in the order given) and `default_levels` last.

## Worked example

```
>>> import catalog
>>> eff = catalog.effective_stock({"A": 10, "B": 5}, {"A": 3})
>>> eff["A"], eff["B"]       # A overridden, B from the default
(3, 5)
>>> eff2 = catalog.effective_stock({"A": 1}, {"A": 2}, {"A": 3})
>>> eff2["A"]                # first override argument is searched first
2
```

## What the check verifies, and what it leaves to you

- Enforced: an override shadows the default for the same SKU; a SKU with no override falls
  through to the default; when several overrides are passed, the earlier argument is found
  first; the default dict is not mutated.
- Your free choice: how many override layers the caller passes is up to them. The fixed
  rule is the search order — overrides ahead of the default.

<div class="hint" title="If you are stuck">

Spread the collected overrides ahead of the default:
`ChainMap(*overrides, default_levels)`. The `*` unpacks the overrides tuple into separate
maps.

</div>

Reference: Python documentation, "collections.ChainMap" at docs.python.org.
