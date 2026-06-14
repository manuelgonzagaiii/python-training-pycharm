# LEGB Scope, nonlocal, and global

> **Phase:** Control Flow & Functions  •  **Stage:** 10.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Trace name resolution through Local, Enclosing, Global, Built-in scopes
- Use nonlocal to mutate an enclosing function's variable
- Use global deliberately (and understand why it is usually avoided)

## Python features introduced
`LEGB scope resolution`, `nonlocal keyword`, `global keyword`, `enclosing-scope mutation via closures`, `module-level state`, `why reassignment needs a scope declaration`

## MiniERP increment
Add make_running_total() to rules.py returning an add(n) closure that updates an enclosing accumulator via nonlocal, plus a module-level audit counter bumped through global in record_pricing_call() — instrumentation the Audit-log module will later consume.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** _PRICING_CALLS = 0


def record_pricing_call() -> int:
    """Increment the module-level counter using global; return new count."""
    global _PRICING_CALLS
    ...


def make_running_total():
    total = 0.0
    def add(n: float) -> float:
        nonlocal total
        ...
    return add
- **Test focus:** Successive add() calls accumulate via nonlocal; record_pricing_call increments the module global across calls; omitting nonlocal/global would rebind locally (covered by the contrast in tests).

</div>
