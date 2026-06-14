# ParamSpec & Concatenate for Decorators

> **Phase:** Modern Type System  •  **Stage:** 24.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Capture an arbitrary callable's full parameter list with ParamSpec (**P) so a decorator preserves its signature
- Write a typed decorator returning Callable[P, R] that keeps the wrapped function's checked signature
- Use Concatenate to type a decorator that injects a leading argument (e.g. a User/AuditContext)
- Express ParamSpec with the PEP 695 [**P] form and the classic ParamSpec('P') form

## Python features introduced
`ParamSpec`, `typing.Concatenate`, `PEP 695 def f[**P] paramspec syntax`, `Callable[P, R]`, `signature-preserving decorators`, `functools.wraps with types`, `injecting a leading argument with Concatenate`

## MiniERP increment
Builds the typed @audited decorator for the Audit-log module: it wraps service methods, records the call, and (via Concatenate) can supply the acting user as a leading parameter — all while mypy/pyright keep the original signatures intact for callers.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from collections.abc import Callable
from typing import Concatenate, ParamSpec, TypeVar
import functools

P = ParamSpec('P')
R = TypeVar('R')

def audited(fn: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        ...  # TODO: log then call fn(*args, **kwargs)
    return wrapper

# Concatenate form: inject a leading User into the call
# def with_user(fn: Callable[Concatenate[User, P], R]) -> Callable[P, R]: ...
- **Test focus:** Tests confirm an @audited function still returns the right value, that the audit record is written, and that *args/**kwargs forwarding preserves behavior; a signature check (inspect.signature / wraps) confirms the wrapper mirrors the original.

</div>
