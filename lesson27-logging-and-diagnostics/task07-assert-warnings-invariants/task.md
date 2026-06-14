# assert, __debug__ & the warnings Module

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 27.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use assert only for internal invariants that must hold if the code is correct — never for validating user input
- Understand that asserts vanish under python -O (__debug__ False) and why that dictates their use
- Emit forward-looking signals with warnings.warn and a chosen category instead of failing
- Route warnings into the logging system with logging.captureWarnings so they share the audit trail

## Python features introduced
`assert statement and its truthiness/message form`, `__debug__ flag and -O optimized mode (asserts stripped)`, `when to use assert (internal invariants) vs raise (input validation)`, `warnings.warn with category`, `DeprecationWarning / UserWarning`, `custom Warning subclass`, `warnings.simplefilter / filterwarnings`, `logging.captureWarnings(True)`

## MiniERP increment
Adds internal-invariant asserts to the service layer (e.g. asserting post-condition stock never goes negative after a validated sale) and introduces a `DeprecatedFieldWarning` raised via warnings.warn when callers pass a legacy product field; startup now calls logging.captureWarnings(True) so those warnings land in MiniERP's logs. This cleanly separates impossible-state assertions from user-facing ValidationErrors.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import warnings
from errors import ValidationError

class DeprecatedFieldWarning(UserWarning):
    """Raised when a caller uses a legacy field name."""

def apply_stock_delta(current: int, delta: int) -> int:
    if current + delta < 0:                 # user-facing condition -> raise
        raise ValidationError("insufficient stock", field="stock")
    result = current + delta
    assert result >= 0, "invariant: stock must never be negative"  # internal check
    # TODO: if a legacy field is in play elsewhere, warnings.warn(..., DeprecatedFieldWarning)
    return result
- **Test focus:** Negative-stock user input raises ValidationError (not AssertionError); the invariant assert holds on valid paths; warnings.warn emits DeprecatedFieldWarning catchable with warnings.catch_warnings; captureWarnings routing is exercised.

</div>
