# Positional-Only and Keyword-Only Parameters

> **Phase:** Control Flow & Functions  •  **Stage:** 10.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Force callers to pass certain args by keyword using the * separator
- Lock certain args as positional-only using the / separator
- Design signatures that read clearly and resist breaking changes

## Python features introduced
`keyword-only parameters (after *)`, `positional-only parameters (before /)`, `the / and * separators in signatures`, `designing call-site clarity`, `mixing positional-only, normal, and keyword-only`

## MiniERP increment
Add apply_tax(amount, /, *, rate, inclusive=False) to rules.py: amount is positional-only (an internal detail) while rate and inclusive are keyword-only (must be explicit at the call site), making MiniERP's tax calls self-documenting and refactor-safe.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def apply_tax(amount: float, /, *, rate: float, inclusive: bool = False) -> float:
    """amount is positional-only; rate and inclusive are keyword-only.
    inclusive=False -> add tax on top; True -> back tax out of amount."""
    ...
- **Test focus:** Exclusive tax adds rate*amount; inclusive tax extracts embedded tax; passing rate positionally raises TypeError; passing amount by keyword raises TypeError.

</div>
