# Stage 6: batch validation with while/else

A `while` loop can take the same `else` clause a `for` loop can, with the identical rule:
the `else` runs **only if the loop ended without a `break`.** That is the perfect fit for
"is *every* line valid?" — walk the lines, break the moment you hit a bad one, and let the
`else` declare success only when the loop got all the way through unbroken.

```
i = 0
while i < len(lines):
    ...
    if bad_line:
        break          # found a problem -> skip the else
    i += 1
else:
    return True        # never broke -> every line was fine
return False
```

This is an **index-driven** while loop: `i` is a manual counter, and `i += 1` is what
advances it. Forgetting that increment is the classic infinite-loop bug, so it is written
for you here — the point of the stage is the `break` and the `while/else`, not the
counter.

You will also see **`pass`** in this function. `pass` is a statement that does nothing — a
placeholder where Python's syntax requires a statement but you have no work to do. Here it
marks the "this line is valid, carry on" branch explicitly, a spot where real systems
might later log or tally the good line.

## Your task

In `pricing.py`, finish `all_lines_valid(lines)`. The loop, the `while/else` returning
`True`, and the final `return False` are written. You supply the **condition that detects
an invalid line** — the test inside the `if` that triggers the `break`. A line is invalid
when its quantity is not positive or its base price is negative.

## Worked example

```
>>> import pricing
>>> pricing.all_lines_valid([("A", 100, 1), ("B", 0, 5)])   # B has qty 0
True
>>> pricing.all_lines_valid([("A", 100, 1), ("B", 100, 0)]) # B has qty 0 -> invalid
False
>>> pricing.all_lines_valid([("A", -1, 3)])                 # negative price
False
>>> pricing.all_lines_valid([])                             # nothing to reject
True
```

## What the check verifies, and what it leaves to you

- Enforced: a cart with all valid lines (and an empty cart) returns `True`; a single line
  with `qty <= 0` or a negative base price makes it `False`.
- Your free choice: how you express "invalid". `qty <= 0 or base_price_cents < 0` and the
  equivalent `not (qty > 0 and base_price_cents >= 0)` both pass, as do a `for/else` or an
  `all(...)`-based rewrite — the check grades the True/False result.

<div class="hint" title="If you are stuck">

The break condition is `qty <= 0 or base_price_cents < 0`. The `else` belongs to the
`while`: it runs (returning `True`) only when no line tripped the `break`.

</div>

Reference: Python documentation, "break and continue Statements, and else Clauses on
Loops" and "The pass statement" at docs.python.org.
