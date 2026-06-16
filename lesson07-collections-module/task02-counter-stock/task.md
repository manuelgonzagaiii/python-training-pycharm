# Stage 2: counting stock with Counter

Inventory is, at heart, counting: how many of each SKU are on hand, how many were received,
how many sold. You could keep those tallies in a plain dict, but you would write the same
guard everywhere — "if the SKU is not in the dict yet, start it at zero, then add". The
standard library has a dict subclass built for this: `collections.Counter`.

A `Counter` is a dict whose values are counts. Its one superpower for our purposes is that
**a missing key reads as 0 instead of raising**, so you can add to any key without
checking whether it exists first:

```
>>> from collections import Counter
>>> stock = Counter()
>>> stock["A-001"] += 5          # "A-001" was missing -> treated as 0, becomes 5
>>> stock["A-001"]
5
>>> stock["never-seen"]          # reading an unknown key -> 0, no KeyError
0
```

That single behaviour removes the `setdefault`/`get(..., 0)` boilerplate from every tally
loop.

## Counter arithmetic

Counters add and subtract as whole objects, which models receipts and sales cleanly:

```
>>> on_hand = Counter({"A-001": 5, "A-002": 2})
>>> movements = Counter({"A-001": -2, "A-002": 3})   # sold 2 of A-001, received 3 of A-002
>>> on_hand + movements
Counter({'A-002': 5, 'A-001': 3})
```

There is a sharp edge worth knowing now, because it is a classic source of surprise: the
`+` and `-` operators **keep only positive results** — any SKU that nets to zero or below
silently disappears from the result. For a "what is in stock right now" view that is often
what you want. But when you must preserve a zero balance or record an oversell as a
negative, use `Counter.update()` / `Counter.subtract()` (which keep every key) instead of
`+` / `-`. You will build a ledger with exactly that property in stage 9.

## Your task

In `catalog.py`, finish two functions:

1. `stock_counter(catalog)` — total each SKU's quantity into a `Counter`. You write the
   line that adds `product.qty` under `product.sku` (lean on the missing-key-is-0
   behaviour — no `if` needed).
2. `apply_movements(stock, deltas)` — return the result of applying the `deltas` Counter
   to the `stock` Counter with Counter arithmetic.

## Worked example

```
>>> import catalog
>>> sc = catalog.stock_counter(catalog.seed_catalog())
>>> sc["A-001"], sc["A-002"]
(5, 0)
>>> sc["not-a-real-sku"]          # missing key -> 0
0
>>> from collections import Counter
>>> catalog.apply_movements(Counter({"A-001": 5}), Counter({"A-001": -2}))["A-001"]
3
```

## What the check verifies, and what it leaves to you

- Enforced: `stock_counter` maps each SKU to its quantity and yields 0 for any SKU it has
  never seen; `apply_movements` adjusts stock up and down by the deltas.
- Your free choice: how you accumulate. The check exercises only outcomes both forms
  agree on, so adding with `+` or with `Counter.update` both pass — it does not pin you to
  one Counter operation.

<div class="hint" title="If you are stuck">

The tally line is `counter[product.sku] += product.qty`. Applying movements is
`return stock + deltas`.

</div>

Reference: Python documentation, "collections.Counter" at docs.python.org.
