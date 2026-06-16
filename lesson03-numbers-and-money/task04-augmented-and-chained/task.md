# Stage 4: augmented assignment and chained comparisons

Two small pieces of syntax you will use in almost every function from here on: the
shorthand for updating a variable, and Python's way of writing a range check the way
you would say it out loud. Both go into `money.py` as helpers MiniERP's cart and
inventory logic will lean on.

## Augmented assignment: update in place

`total += price` means `total = total + price`. Every arithmetic operator has an
augmented form:

```
+=  -=  *=  /=  //=  %=  **=          # arithmetic
&=  |=  ^=  <<=  >>=                  # bitwise (you meet these next stage)
```

It is not only shorter — it says "change this variable," which is exactly what an
accumulator does. The classic pattern is summing a list:

```
total = 0
for price in prices:
    total += price        # grow the subtotal one item at a time
```

For immutable numbers, `total += price` and `total = total + price` are identical. (The
distinction starts to matter for mutable objects like lists later; for ints it is pure
shorthand.)

## Chained comparisons: write the range as a range

Python lets you chain comparison operators, so a "between" check reads like maths:

```
low <= qty <= high
```

That is **one expression**, not two. It is equivalent to `low <= qty and qty <= high`,
with one important nicety: the middle value `qty` is evaluated **once**. If `qty` were an
expensive function call, the chained form would not call it twice. You can chain any of
`<  <=  >  >=  ==  !=`, though a simple inclusive range is by far the most common.

Compare the two ways to ask "is this order quantity allowed?":

```
if low <= qty and qty <= high:   # works, but repeats qty and reads heavier
if low <= qty <= high:           # clearer, evaluates qty once
```

The second is the Pythonic one, and the Zen tie-breaker (readability) chooses it.

## Your task

Fill in the two blanks in `money.py`:

1. `running_total(prices)` — accumulate the subtotal with `+=` inside the loop.
2. `in_stock_range(qty, low, high)` — return the inclusive range check as a single
   chained comparison.

## Worked example

```
>>> import money
>>> money.running_total([10, 20, 30])
60
>>> money.in_stock_range(5, 1, 10), money.in_stock_range(11, 1, 10)
(True, False)
>>> money.in_stock_range(1, 1, 10)     # bounds are inclusive
True
```

## What the check verifies, and what it leaves to you

- Enforced: `running_total` sums the list (and returns `0` for an empty list);
  `in_stock_range` is **inclusive** on both ends, so `qty == low` and `qty == high` are
  in range while one below or above is not.
- Your free choice: how you write the loop body, and whether `in_stock_range` uses a
  chained comparison or an `and` of two comparisons — both are valid, so both pass. The
  chained form is what the stage teaches and what we recommend.

<div class="hint" title="If you are stuck">

Inside the loop, `total += price` adds the current price to the running total. For the
range check, `low <= qty <= high` is the whole return expression.

</div>

Reference: Python documentation, "Expressions — Comparisons" (chained comparisons) and
"Simple statements — Augmented assignment statements" at docs.python.org.
