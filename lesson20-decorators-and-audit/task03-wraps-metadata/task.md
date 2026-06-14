# Preserving Identity with functools.wraps

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 20.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- See that an unwrapped decorator clobbers __name__ and __doc__
- Apply @functools.wraps(func) to copy metadata and set __wrapped__
- Recover the original via __wrapped__ for unwrapping

## Python features introduced
`functools.wraps`, `__name__ / __doc__ / __wrapped__ / __module__ preservation`, `functools.WRAPPER_ASSIGNMENTS`, `why naive wrappers break introspection and help()`

## MiniERP increment
Hardens log_calls so decorated service functions keep their real names in logs, tracebacks, and the audit records — essential before audit entries reference function identity.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import functools
from collections.abc import Callable
from typing import Any

def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)  # TODO: explain & rely on what this copies
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        ...
    return wrapper

# TODO: expose original via wrapper.__wrapped__
- **Test focus:** wrapper.__name__ and __doc__ equal the original's; wrapper.__wrapped__ is the original function; behavior still preserved.

</div>
