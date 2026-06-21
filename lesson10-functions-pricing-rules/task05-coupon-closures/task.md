# Stage 5: closures and the late-binding gotcha

MiniERP keeps a registry of coupons, each a small function that discounts a price by a fixed
amount. The clean way to build those is a **function factory** — a function that returns a
function — which brings us to closures.

## Closures: functions that remember

A function defined inside another function can use the outer function's variables, and it
keeps access to them **even after the outer function has returned**. That captured
environment is a **closure**:

```
def make_coupon(percent):
    def coupon(price_cents):
        return apply_percent(price_cents, percent)   # remembers `percent`
    return coupon

ten_off = make_coupon(10)
ten_off(1000)     # 900 -- `percent` is still 10, long after make_coupon returned
```

Each call to `make_coupon` produces a new `coupon` with its own captured `percent`. This is
how you manufacture configured behaviour without classes.

## The late-binding gotcha

Here is the trap. A closure captures the **variable**, not the value it had when the closure
was created. So closures built in a loop all share the loop variable and see its **final**
value:

```
table = {}
for percent in [5, 10, 20]:
    table[percent] = lambda p: apply_percent(p, percent)   # BUG
# every lambda now uses percent == 20, the last value
```

All three lambdas read the same `percent`, which ends at 20. The standard fix is to **bind
the current value as a default argument**, which is evaluated immediately, at each iteration:

```
table[percent] = lambda p, percent=percent: apply_percent(p, percent)   # snapshots now
```

The `percent=percent` default freezes this iteration's value into the lambda, so each coupon
keeps its own rate.

## Your task

In `rules.py`, finish two functions:

1. `make_coupon(percent)` — fill in the closure body that discounts a price by the captured
   `percent`.
2. `build_coupon_table(percents)` — fill in the **default-argument capture** that snapshots
   `percent` per iteration, dodging the late-binding gotcha.

## Worked example

```
>>> import rules
>>> rules.make_coupon(10)(1000)
900
>>> table = rules.build_coupon_table([5, 10, 20])
>>> table[5](1000), table[10](1000), table[20](1000)
(950, 900, 800)
```

## What the check verifies, and what it leaves to you

- Enforced: a coupon from `make_coupon(p)` discounts by `p`; in the table, **each** coupon
  applies its own percent (the late-binding bug would make them all use 20).
- Your free choice: the check grades only the outcome — that each coupon discounts by its own
  percent — so a different valid construction (such as `functools.partial(apply_percent,
  percent=p)`) would also satisfy it. The blanks in this stage are placed around the
  default-argument idiom, because dodging the late-binding gotcha is the specific skill it teaches.

<div class="hint" title="If you are stuck">

The closure body is `apply_percent(price_cents, percent)`. The capture is `percent=percent`
in the lambda's parameter list — that default is evaluated now, not when the lambda is later
called.

</div>

Reference: Python documentation, "Nested functions and closures" (Programming FAQ: "Why do
lambdas defined in a loop with different values all return the same result?") at
docs.python.org.
