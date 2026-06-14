# Multi-statement rule actions with exec

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compile and exec a small multi-line rule body that sets output variables
- Understand exec returns None and results live in the namespace
- Reuse the validator concept for statement-level safety
- Know when a rule needs exec (actions) vs eval (predicates)

## Python features introduced
`exec(code, ns)`, `compile mode 'exec'`, `statements vs expressions`, `reading results back out of the namespace dict`, `ast.parse mode 'exec'`, `difference between eval and exec return values (None)`

## MiniERP increment
Adds 'action rules': a discount rule may set `discount_pct = 10` across a couple of lines. erp/rules/actions.py compiles in 'exec' mode and runs the body in a sandbox namespace, returning the produced output variables to the pricing service.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import ast


def run_action(src: str, context: dict[str, object], out: str) -> object:
    """Compile `src` in 'exec' mode, run it with `context` as the namespace,
    and return the value bound to name `out` afterward.

    Use empty builtins. Raise KeyError if `out` was not set.
    """
    raise NotImplementedError

- **Test focus:** Tests run_action executes a multi-statement body, reads back the named output variable, and raises KeyError when the output name is never assigned; verifies the context values are visible to the body and builtins are restricted.

</div>
