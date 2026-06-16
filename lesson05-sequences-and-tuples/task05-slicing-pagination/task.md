# Stage 5: deep slicing — pagination and recent products

A catalog of thousands of products is never shown all at once. The CLI shows a page; the web
UI shows "page 2 of 40"; the dashboard shows the five most recently added items. All of that
is **slicing**, which you met on strings in Lesson 4 and which works identically on lists.
This stage builds the catalog's first read API.

## Pagination is arithmetic plus a slice

A "page" is a fixed-size window into the list. Page `number` (counting from 1) of `size`
items starts at index `(number - 1) * size` and runs for `size` items:

```
>>> items = list(range(10))      # [0, 1, ..., 9]
>>> size, number = 3, 2
>>> start = (number - 1) * size  # 3
>>> items[start:start + size]    # page 2
[3, 4, 5]
```

The crucial safety property, the same one slicing gave you on strings: **a slice never
raises `IndexError`**. Ask for page 99 of a 5-item list and you get an empty list, not a
crash — so the read API is robust against any page number a UI might send.

## "Most recent N" with negative indices and a reversed step

Products are appended to the end, so the newest are at the tail. `catalog[-n:]` takes the
last `n`. To show newest-first, reverse with a step of `-1`:

```
>>> items[-3:]        # the last three
[7, 8, 9]
>>> items[-3:][::-1]  # last three, newest first
[9, 8, 7]
```

If `n` is larger than the catalog, `catalog[-n:]` simply gives you everything (clamping
again), so `recent` is safe for any `n`.

## Your task

In `catalog.py`, fill in:

1. `page(catalog, number, size)` — the slice for page `number` (the `start` is computed for
   you).
2. `recent(catalog, n)` — the last `n` records, newest first.

## Worked example

```
>>> import catalog
>>> cat = catalog.seed_catalog()
>>> catalog.page(cat, 1, 2) == cat[0:2]
True
>>> catalog.page(cat, 99, 2)        # past the end
[]
>>> catalog.recent(cat, 2)          # newest first
[('B-010', 'Gizmo', 250, 12), ('A-002', 'Gadget', 1499, 0)]
```

## What the check verifies, and what it leaves to you

- Enforced: `page` returns the correct window for in-range and past-the-end pages (empty,
  no error); `recent` returns the last `n` newest-first and handles `n` larger than the
  catalog.
- Your free choice: how you express the slices, as long as the results match (e.g. `recent`
  via `catalog[-n:][::-1]` or `list(reversed(catalog[-n:]))`).

<div class="hint" title="If you are stuck">

`page` is `catalog[start:start + size]`. `recent` is `catalog[-n:][::-1]`.

</div>

Reference: Python documentation, "Sequence Types — Common Sequence Operations (slicing)" at
docs.python.org.
