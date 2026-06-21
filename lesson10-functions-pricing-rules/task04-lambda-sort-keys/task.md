# Stage 4: lambdas, sort keys, and higher-order builtins

The reporting layer needs to rank cart lines, find the cheapest and dearest, number them, and
flag big ones. All of these are one-liners once you can pass a small function as an argument —
which is what this stage is about.

## Functions are values; lambda makes small ones inline

A function is an ordinary value in Python: you can store it, pass it, return it. A **lambda**
is a compact way to write a small anonymous one inline:

```
lambda line: line[1] * line[2]
```

is a function of one argument `line` that returns `line[1] * line[2]` (price times qty — the
line total). It is exactly equivalent to a `def` with a single `return`, just without a name.
Keep lambdas to one simple expression; if it grows, use a named `def`.

## Higher-order builtins that take a key

A **higher-order function** is one that takes another function as an argument. Several
builtins take a `key=` function that maps each item to the value to compare by:

```
sorted(lines, key=lambda line: line[1] * line[2], reverse=True)   # by line total, high to low
min(lines, key=lambda line: line[1] * line[2])                    # smallest total
max(lines, key=lambda line: line[1] * line[2])                    # largest total
```

Two more builtins round out the toolkit:

- `enumerate(lines, start=1)` pairs each item with a counter — `(1, line)`, `(2, line)`, … —
  perfect for numbering rows.
- `any(...)` / `all(...)` collapse a sequence of booleans to one. Fed a **generator
  expression**, `any(total > limit for ...)` stops at the first true and never builds a list.

`sorted` returns a **new** list and leaves the original alone — important when the cart must
not be reordered as a side effect.

## Your task

In `rules.py`, finish two pieces. The `cheapest_line`, `dearest_line`, and `line_numbers`
helpers are written for you as worked examples to copy the pattern from. You fill in:

1. the `key=` **lambda** in `rank_lines` (the line total), and
2. the **generator condition** inside `any_over_limit` (a line total over the limit).

## Worked example

```
>>> import rules
>>> lines = [("A", 100, 2), ("B", 100, 5), ("C", 300, 1)]   # totals 200, 500, 300
>>> [row[0] for row in rules.rank_lines(lines)]
['B', 'C', 'A']
>>> rules.cheapest_line(lines)[0], rules.dearest_line(lines)[0]
('A', 'B')
>>> rules.any_over_limit(lines, 400), rules.any_over_limit(lines, 1000)
(True, False)
```

## What the check verifies, and what it leaves to you

- Enforced: `rank_lines` orders by line total, highest first; `cheapest`/`dearest` pick the
  right extremes; `line_numbers` is 1-based; `any_over_limit` is true exactly when some line
  exceeds the limit.
- Your free choice: the key can be a `lambda` or a named function or `operator`-based key —
  anything that computes the line total works. The check grades the ordering and results.

<div class="hint" title="If you are stuck">

The sort key is `lambda line: line[1] * line[2]`. The `any` condition is the same expression
compared to the limit: `line[1] * line[2] > limit`.

</div>

Reference: Python documentation, "Lambda Expressions" and the `sorted`, `min`, `max`,
`enumerate`, `any` builtins at docs.python.org.
