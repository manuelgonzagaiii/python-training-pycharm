# The @audit Decorator (MILESTONE)

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 20.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a decorator factory @audit(action=...) that takes configuration and returns a real decorator
- Use inspect.signature(func).bind(*args, **kwargs) to capture named arguments for the audit entry
- Emit a structured AuditEntry (actor, action, target, timestamp) into the audit log on every successful call

## Python features introduced
`parametrized decorator (decorator factory: three nested defs)`, `closure over factory arguments`, `functools.wraps inside a factory`, `binding inspect.signature to name arguments`, `returning the wrapped result while emitting a side-effecting record`

## MiniERP increment
Delivers the phase milestone: a reusable @audit('product.create') / @audit('sale.record') decorator in core/audit.py that records every domain mutation into the audit log. Applied to the Products and Sales service functions so the audit module finally captures real events.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import functools, inspect
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any

@dataclass(slots=True, frozen=True)
class AuditEntry:
    action: str
    args: dict[str, Any]
    at: datetime = field(default_factory=lambda: datetime.now(UTC))

AUDIT_LOG: list[AuditEntry] = []

def audit(action: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        sig = inspect.signature(func)
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # TODO: bound = sig.bind(*args, **kwargs); bound.apply_defaults()
            #       result = func(...); append AuditEntry(action, bound.arguments-derived dict)
            #       return result
            ...
        return wrapper
    return decorator
- **Test focus:** @audit('x') records exactly one AuditEntry per call with the correct action and bound argument names; the wrapped function's return value is unchanged; metadata preserved via wraps.

</div>
