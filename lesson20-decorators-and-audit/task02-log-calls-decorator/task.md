# A First Wrapper: log_calls

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 20.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a minimal decorator that forwards arbitrary positional and keyword arguments
- Return the wrapped function's value unchanged so behavior is preserved
- Append a human-readable call record to a list the decorator closes over

## Python features introduced
`defining a decorator with an inner def`, `*args / **kwargs forwarding`, `calling the wrapped function and returning its result`, `closure over the decorated function`

## MiniERP increment
Adds a log_calls decorator in core/instrument.py and applies it to a service function so each invocation is captured. This is the seed of the audit trail, built by hand before functools is introduced.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from collections.abc import Callable
from typing import Any

calls: list[str] = []

def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # TODO: record f"{func.__name__}({args}, {kwargs})" into `calls`,
        #       then call func(*args, **kwargs) and return its result
        ...
    return wrapper
- **Test focus:** Decorated function returns the same value as the undecorated one; the call is recorded; *args and **kwargs both forward correctly.

</div>
