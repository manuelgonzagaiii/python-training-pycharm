# Stage 2: stacking discounts with *args and **kwargs

A promotional price can have any number of discounts stacked on it — a seasonal sale, a
loyalty cut, a clearance markdown — and you do not know how many in advance. Python lets a
function accept a variable number of arguments with two collecting parameters.

## *args collects extra positional arguments

A parameter written `*name` gathers all the leftover **positional** arguments into a
**tuple**:

```
def stack_discounts(price_cents, *percents):
    # call stack_discounts(1000, 10, 5) -> percents == (10, 5)
    for percent in percents:
        ...
```

So `stack_discounts(1000)` gives `percents == ()` and `stack_discounts(1000, 10, 5, 2)`
gives `percents == (10, 5, 2)`. You iterate it like any tuple.

## **kwargs collects extra keyword arguments

A parameter written `**name` gathers all the leftover **keyword** arguments into a **dict**:

```
def stack_discounts(price_cents, *percents, **options):
    # call ...(1000, 10, clamp_floor=True) -> options == {"clamp_floor": True}
    if options.get("clamp_floor"):
        ...
```

`options.get("clamp_floor")` reads a named option if it was passed and returns `None`
(falsey) otherwise — so the option is genuinely optional. The conventional names are `*args`
and `**kwargs`, but the names are yours; the `*` and `**` are what matter.

## Your task

In `rules.py`, finish `stack_discounts(price_cents, *percents, **options)`:

1. inside the loop, apply the current `percent` to the running `result`, and
2. read the `clamp_floor` option out of `**options`.

## Worked example

```
>>> import rules
>>> rules.stack_discounts(1000, 10, 10)        # 1000 -> 900 -> 810
810
>>> rules.stack_discounts(1000)                # no discounts
1000
>>> rules.stack_discounts(100, 200, clamp_floor=True)   # over-discounted, floored at 0
0
```

## What the check verifies, and what it leaves to you

- Enforced: each percent is applied in turn; passing no percents leaves the price unchanged;
  `clamp_floor=True` prevents a negative result while omitting it allows one.
- Your free choice: how you apply each percent (reusing `apply_percent` is intended, but an
  inline equivalent passes), and you may support more options as long as `clamp_floor`
  behaves.

<div class="hint" title="If you are stuck">

In the loop: `result = apply_percent(result, percent)`. The option read is
`options.get("clamp_floor")` — `.get` returns `None` when the key is absent, which is falsey.

</div>

Reference: Python documentation, "More on Defining Functions — Arbitrary Argument Lists" and
"Keyword Arguments" at docs.python.org.
