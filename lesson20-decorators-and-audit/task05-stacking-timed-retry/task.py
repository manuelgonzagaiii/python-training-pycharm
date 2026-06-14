"""Stacking Decorators: @timed and @retry

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import functools, time
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
"""

# Your code here.
