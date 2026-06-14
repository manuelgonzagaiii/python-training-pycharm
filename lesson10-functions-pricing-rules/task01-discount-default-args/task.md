# Default Arguments and the Mutable-Default Gotcha

> **Phase:** Control Flow & Functions  •  **Stage:** 10.1 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define functions with sensible default arguments
- Diagnose and fix the mutable-default-argument bug using the None sentinel
- Document behavior with a docstring and annotate parameters

## Python features introduced
`def and return`, `default parameter values`, `the shared mutable-default gotcha (def f(x, acc=[]))`, `None-sentinel idiom for defaults`, `docstrings`, `parameter annotations`

## MiniERP increment
Add apply_percent(price, percent=0.0) and accumulate_discounts(amount, applied=None) to rules.py: the accumulator deliberately uses the None-sentinel idiom so the discount-history list is not shared across calls — fixing a class of bug that would corrupt MiniERP totals.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def apply_percent(price: float, percent: float = 0.0) -> float:
    """Reduce price by percent (0..1). Default percent leaves price unchanged."""
    ...


def accumulate_discounts(amount: float, applied: list[float] | None = None) -> list[float]:
    """Append amount to a per-call history list. Use the None sentinel, NOT a mutable default."""
    if applied is None:
        applied = []
    ...
- **Test focus:** apply_percent with default returns price unchanged and applies percents correctly; repeated accumulate_discounts calls do NOT share state (proves the gotcha is avoided).

</div>
