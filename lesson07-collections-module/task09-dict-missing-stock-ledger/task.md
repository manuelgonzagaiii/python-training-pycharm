# Stage 9: __missing__ and a self-zeroing stock ledger

This stage closes the lesson by revealing the mechanism behind the containers you have been
using. Back in stage 2, `Counter` returned `0` for a key it had never seen, and `defaultdict`
manufactured a value on a missing key. Both rely on one hook the language offers to any
dict subclass: **`__missing__`**.

When you read `d[key]` and the key is absent, `dict` does not immediately raise. It first
looks for a method named `__missing__` on the class; if one exists, it calls
`d.__missing__(key)` and returns *that* result instead of raising `KeyError`. `defaultdict`
is simply a dict whose `__missing__` calls the factory and stores the result. Knowing this,
you can build your own missing-key policy in a few lines.

MiniERP wants a **stock ledger**: a SKU -> on-hand-quantity map where a SKU you have never
recorded reads as `0` *and is created at 0*, so the first movement against it just works:

```
ledger["new-sku"] += 5      # reads new-sku (missing -> 0, inserted), then stores 5
```

For that `+=` to work on a brand-new SKU, the read must do two things: return `0` **and**
insert the `0` so the write has something to update. So `__missing__` here both stores and
returns:

```
class StockLedger(dict):
    def __missing__(self, sku):
        self[sku] = 0       # insert the new key at zero...
        return 0            # ...and return that zero to the read
```

Note the difference from `Counter`: `Counter[missing]` returns `0` but does **not** insert
the key (the count stays absent). This ledger *does* insert, because we want every SKU we
have ever touched to remain on the books — even at a zero balance — which is the honest
behaviour for inventory. That is the gap stage 2 flagged about `Counter` arithmetic dropping
non-positive results; here you build the container that keeps them.

## Your task

In `catalog.py`, finish `StockLedger.__missing__(self, sku)`. On a missing SKU, insert a
`0` balance for it and return that `0`.

## Worked example

```
>>> import catalog
>>> ledger = catalog.StockLedger()
>>> ledger["A-001"]              # never seen -> reads 0...
0
>>> "A-001" in ledger            # ...and was inserted by the read
True
>>> ledger["B-010"] += 12        # works on a brand-new SKU
>>> ledger["B-010"] += 3
>>> ledger["B-010"]
15
```

## What the check verifies, and what it leaves to you

- Enforced: reading a missing SKU returns `0` and inserts the key at `0`; `+=` on a
  first-time SKU accumulates correctly; an existing balance is left unchanged by a read.
- Your free choice: the body's exact form is open, as long as a missing key both reads as
  `0` and is stored. (Returning `0` without inserting would pass the read test but break the
  `+=`-on-a-new-SKU behaviour, so the insert is genuinely required.)

<div class="hint" title="If you are stuck">

Two lines: `self[sku] = 0` then `return 0`. The assignment is what makes `ledger[sku] += n`
work the first time a SKU appears.

</div>

Reference: Python documentation, "object.__missing__" (Data model, mapping emulation) and
"collections.defaultdict" at docs.python.org.
