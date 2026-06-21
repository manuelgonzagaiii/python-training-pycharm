# Stage 6: LEGB scope, nonlocal, and global

When you use a name, Python decides which variable it means by searching scopes in a fixed
order — **LEGB**:

- **L**ocal: names assigned in the current function.
- **E**nclosing: names in any function wrapped around this one.
- **G**lobal: names at the top level of the module.
- **B**uilt-in: names like `len`, `print`, `min`.

Python walks L -> E -> G -> B and uses the first match. That covers **reading** a name. The
catch is **reassigning** one.

## The reassignment rule

By default, assigning to a name inside a function makes it **local** — even if a same-named
variable exists in an enclosing or global scope. So this does not do what it looks like:

```
def make_running_total():
    total = 0
    def add(n):
        total += n      # ERROR: `total +=` makes `total` local, then reads it before it exists
        return total
    return add
```

To say "reassign the variable from the enclosing scope, do not make a new local," you declare
it:

- **`nonlocal total`** — reassign a variable from the nearest **enclosing function**.
- **`global _counter`** — reassign a variable at **module level**.

```
def add(n):
    nonlocal total
    total += n          # now updates the enclosing `total`
    return total
```

This is how a closure can carry **mutable** state (a running total) across calls, and how a
module-level counter (a pricing-call tally the audit log will later read) gets bumped from
inside a function.

## Your task

In `rules.py`, finish two functions:

1. `make_running_total()` — add the `nonlocal` declaration in `add` so it updates the
   enclosing `total` instead of creating a local.
2. `record_pricing_call()` — add the `global` declaration so it bumps the module-level
   counter `_pricing_calls`.

## Worked example

```
>>> import rules
>>> add = rules.make_running_total()
>>> add(10), add(5), add(0)
(10, 15, 15)
>>> other = rules.make_running_total()      # independent state
>>> other(3)
3
>>> a = rules.record_pricing_call(); b = rules.record_pricing_call()
>>> b == a + 1
True
```

## What the check verifies, and what it leaves to you

- Enforced: a running total accumulates across calls; two totals are independent of each other;
  `record_pricing_call` returns a value one greater each call.
- Your free choice: nothing about the structure is yours to change here — the point is the two
  scope declarations, and they must be `nonlocal` and `global` respectively.

<div class="hint" title="If you are stuck">

Inside `add`, the missing line is `nonlocal total`. Inside `record_pricing_call`, it is
`global _pricing_calls`. Both must come before the line that reassigns the name.

</div>

Reference: Python documentation, "The nonlocal statement", "The global statement", and
"Python Scopes and Namespaces" at docs.python.org.
