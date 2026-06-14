# Stacking Decorators: @timed and @retry

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 20.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Predict the order in which stacked decorators wrap a function
- Build @timed that measures perf_counter around the call and records the duration
- Build @retry(times=n) that re-invokes the function on exception up to n times, re-raising the last error

## Python features introduced
`stacking multiple decorators`, `application order (bottom-up) vs execution order (top-down)`, `time.perf_counter for timing`, `retry loop with exception capture`, `parametrized @retry(times=...)`, `interaction of @wraps across a stack`

## MiniERP increment
Adds @timed and @retry to core/instrument.py and stacks @audit + @timed + @retry on a flaky operation (e.g. an export that may transiently fail), giving the service layer resilience and performance metrics alongside auditing.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import functools, time
from collections.abc import Callable
from typing import Any

def timed(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        # TODO: call, record elapsed, return result
        ...
    return wrapper

def retry(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    # TODO: factory -> decorator -> wrapper that retries up to `times`
    ...
- **Test focus:** Stacking order observable in recorded events; @retry(3) succeeds on the 3rd attempt and re-raises after exhausting attempts; @timed records a non-negative duration.

</div>
