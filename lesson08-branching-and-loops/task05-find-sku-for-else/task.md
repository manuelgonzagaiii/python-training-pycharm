# Stage 5: catalog search with for/else

Searching a list for the first match, then doing something different when **nothing**
matches, is so common that Python gives loops their own `else` clause for it. It is one of
the language's most misunderstood features, so it is worth getting the mental model exact.

A loop's `else` runs **only if the loop finished without a `break`.** Read it as a
"no-break else", or as "the loop ran to exhaustion". It does *not* mean "the other branch"
and it has nothing to do with whether the loop body ran.

```
for product in catalog:
    if product[0] == sku:
        found = product
        break          # match -> leave the loop, skip the else
else:
    raise KeyError(...)  # loop exhausted, never broke -> nothing matched
```

If a `break` fires, the `else` is skipped. If the loop walks every item and never breaks,
the `else` runs. That maps perfectly onto "found it" versus "searched everything and came
up empty". The alternative — a `found = False` flag checked after the loop — works too,
but the `for/else` says the intent in the loop's own structure.

Two more control keywords appear here: **`continue`** jumps straight to the next iteration
(used to skip records that do not match), and **`break`** exits the loop immediately.

## Your task

In `inventory.py`, finish `find_in_catalog(catalog, sku)`. The scan, the `continue` on a
mismatch, and the `break` on a hit are written. You supply the **`else` clause's body**:
when the loop never broke (no SKU matched), raise a `KeyError` naming the unknown SKU.

## Worked example

```
>>> import inventory
>>> catalog = [("A-001", "Widget", 999, 5), ("B-010", "Gizmo", 250, 12)]
>>> inventory.find_in_catalog(catalog, "B-010")
('B-010', 'Gizmo', 250, 12)
>>> inventory.find_in_catalog(catalog, "ZZZ")
Traceback (most recent call last):
KeyError: 'unknown sku: ZZZ'
```

## What the check verifies, and what it leaves to you

- Enforced: an existing SKU returns its record; an absent SKU (including in an empty
  catalog) raises `KeyError`.
- Your free choice: the exact `KeyError` message is yours. And a flag-based search instead
  of `for/else` passes too — the `for/else` is the idiom this stage teaches, not a
  requirement of the check.

<div class="hint" title="If you are stuck">

The `else` body is `raise KeyError(f"unknown sku: {sku}")`. It belongs to the `for`, not
to an `if`, and runs only when the loop completed without a `break`.

</div>

Reference: Python documentation, "break and continue Statements, and else Clauses on
Loops" at docs.python.org.
