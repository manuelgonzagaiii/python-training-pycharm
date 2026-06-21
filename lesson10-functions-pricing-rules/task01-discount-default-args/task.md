# Stage 1: default arguments and the mutable-default gotcha

This lesson completes MiniERP's business-rules layer by going deep on functions: how
arguments work, how closures capture state, and how recursion expands bundles. Everything
lives in a new module, `rules.py`, built up across the eight stages. Money stays integer
cents; discounts are whole-percent integers, applied with rounding.

A **default argument** lets a parameter be optional by giving it a fallback value used when
the caller omits it:

```
def apply_percent(price_cents, percent=0):
    ...
```

Now `apply_percent(1500)` means "no discount" and `apply_percent(1500, 10)` takes 10% off.
Defaults make the common case short and the call site readable.

## The mutable-default gotcha

There is one trap that bites nearly every Python programmer once. A default value is
evaluated **exactly once — when the `def` runs**, not on each call. So a *mutable* default
like a list is created a single time and **shared by every call**:

```
def broken(x, acc=[]):       # the [] is made ONCE, at definition
    acc.append(x)
    return acc

broken(1)   # [1]
broken(2)   # [1, 2]  <- the SAME list, still holding 1
```

That shared-list bug would silently corrupt MiniERP totals. The fix is the **None-sentinel
idiom**: default to `None`, then create a fresh object inside the function when you see it:

```
def accumulate_discounts(amount, applied=None):
    if applied is None:
        applied = []      # a new list per call
    applied.append(amount)
    return applied
```

Now every call that omits `applied` gets its own list. The rule to remember: **never use a
mutable object as a default argument** — use `None` and build it inside.

## Your task

In `rules.py`, finish two functions:

1. `apply_percent(price_cents, percent=0)` — the `percent=0` default is written; you fill in
   the **None-sentinel test** in `accumulate_discounts`.
2. `accumulate_discounts(amount, applied=None)` — supply the `if` condition that detects "no
   list was passed" so a fresh one is created.

## Worked example

```
>>> import rules
>>> rules.apply_percent(1000)          # default: no discount
1000
>>> rules.apply_percent(1000, 10)      # 10% off
900
>>> rules.accumulate_discounts(10)     # fresh list
[10]
>>> rules.accumulate_discounts(20)     # NOT [10, 20] -- a new list, no sharing
[20]
```

## What the check verifies, and what it leaves to you

- Enforced: `apply_percent` with no percent leaves the price unchanged and otherwise discounts
  it; `accumulate_discounts` returns a **fresh** list on each defaulted call (the second call
  must not still contain the first call's value) and appends to a list you pass in.
- Your free choice: the sentinel can be written `applied is None` or `applied == None`
  (identity is the idiomatic form), as long as a fresh list is created when none is supplied.

<div class="hint" title="If you are stuck">

The condition is `if applied is None:`. Using `applied = []` as the default instead would
re-introduce the shared-list bug the stage is about.

</div>

Reference: Python documentation, "More on Defining Functions — Default Argument Values" at
docs.python.org.
