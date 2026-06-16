# Stage 3: merging dicts with the | operator

MiniERP often needs to layer one set of values over another: a base price list with a
few promotional overrides, default settings with a customer's custom settings, a saved
catalog with edits made this session. The question is always the same — combine two dicts
so that the second one wins on any key they share.

Since Python 3.9 the merge operator `|` does this directly:

```
>>> base = {"A": 1, "B": 2}
>>> over = {"B": 20, "C": 30}
>>> base | over
{'A': 1, 'B': 20, 'C': 30}
```

Read it left to right: start from `base`, then apply `over`. Keys only in `base` survive,
keys only in `over` are added, and where they collide the **right-hand** value wins
(`B` becomes 20). This is the modern, readable replacement for the older
`{**base, **over}` spread and for `dict(base, **over)`; both still work, but `|` says
"merge" plainly.

One property to hold onto: `base | over` builds a **new** dict and leaves both operands
untouched. That matters when `base` is shared state you must not corrupt. (There is also
`|=`, which merges *in place* into the left dict — use that only when you intend to mutate
it.)

## Your task

In `catalog.py`, finish `apply_overrides(base, overrides)` so it returns a new dict where
entries in `overrides` replace matching entries in `base`. One expression with `|`.

## Worked example

```
>>> import catalog
>>> base = {"A-1": ("A-1", "Old", 100, 1)}
>>> over = {"A-1": ("A-1", "New", 200, 2), "B-1": ("B-1", "Extra", 50, 9)}
>>> merged = catalog.apply_overrides(base, over)
>>> merged["A-1"]
('A-1', 'New', 200, 2)
>>> "B-1" in merged
True
>>> base["A-1"]            # the original is left intact
('A-1', 'Old', 100, 1)
```

## What the check verifies, and what it leaves to you

- Enforced: on a shared key the override wins; keys unique to either side all survive; the
  original `base` is not mutated.
- Your free choice: which merge spelling you use. `base | overrides` is the modern form,
  but `{**base, **overrides}` produces the same result and also passes — the check grades
  the result, not the syntax.

<div class="hint" title="If you are stuck">

Return `base | overrides`. The order matters: the right operand wins on shared keys, so
`overrides` must be on the right.

</div>

Reference: Python documentation, "Mapping Types — dict" (the `|` and `|=` operators, PEP
584) at docs.python.org.
