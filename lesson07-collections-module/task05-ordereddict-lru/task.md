# Stage 5: a least-recently-used cache with OrderedDict

Some MiniERP lookups are worth caching — a product detail that is expensive to assemble,
say. A cache cannot grow forever, so when it is full you must evict something, and the
standard policy is **least-recently-used (LRU)**: throw out whatever has gone untouched the
longest, on the bet that recently-used things will be wanted again.

LRU needs to track *order of use*, and `collections.OrderedDict` is built to manage exactly
that. A plain dict remembers **insertion** order; an `OrderedDict` adds methods to
**reorder** entries after the fact, which is what "mark this as just used" requires:

- `od.move_to_end(key)` — move an existing key to the most-recently-used end.
- `od.popitem(last=False)` — remove and return the item at the *other* end, the oldest one.
  (`popitem()` with the default `last=True` pops the newest; `last=False` pops the oldest,
  which is the eviction you want.)

The recipe for "touch a key" is: insert or refresh the value, move that key to the recent
end, and if the cache has grown past its capacity, pop the oldest:

```
>>> from collections import OrderedDict
>>> cache = OrderedDict()
>>> def touch(c, k, v, cap):
...     c[k] = v
...     c.move_to_end(k)
...     if len(c) > cap:
...         c.popitem(last=False)
>>> for k in "ABC":          # capacity 2
...     touch(cache, k, k, 2)
>>> list(cache)              # A was least-recently-used, so it was evicted
['B', 'C']
```

(For a ready-made cache you would normally reach for `functools.lru_cache`, covered later;
building it by hand here is what makes the eviction policy concrete.)

## Your task

In `catalog.py`, finish `touch(cache, sku, product, capacity)`. The insert
(`cache[sku] = product`) and the over-capacity `if` are written; you write:

1. the call that marks `sku` as most-recently-used, and
2. the call that evicts the least-recently-used entry when over capacity.

## Worked example

```
>>> import catalog
>>> from collections import OrderedDict
>>> cache = OrderedDict()
>>> p = catalog.make_product
>>> catalog.touch(cache, "A", p("A", "n", 0, 0), 2)
>>> catalog.touch(cache, "B", p("B", "n", 0, 0), 2)
>>> catalog.touch(cache, "A", p("A", "n", 0, 0), 2)   # A is used again -> now newest
>>> catalog.touch(cache, "C", p("C", "n", 0, 0), 2)   # evicts B (now the oldest), not A
>>> list(cache)
['A', 'C']
```

## What the check verifies, and what it leaves to you

- Enforced: once over capacity, the least-recently-used key is evicted; re-touching a key
  protects it from being the next eviction.
- Your free choice: `capacity` is the caller's. The eviction *policy* (LRU) is what is
  fixed — any spelling that moves the touched key to the recent end and pops the oldest
  passes.

<div class="hint" title="If you are stuck">

Mark as recent with `cache.move_to_end(sku)`. Evict the oldest with
`cache.popitem(last=False)` — `last=False` is what makes it the *oldest*, not the newest.

</div>

Reference: Python documentation, "collections.OrderedDict" (`move_to_end`, `popitem`) at
docs.python.org.
