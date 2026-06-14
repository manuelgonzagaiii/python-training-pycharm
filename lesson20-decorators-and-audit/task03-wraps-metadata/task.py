"""Preserving Identity with functools.wraps

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import functools
from collections.abc import Callable
from typing import Any

def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)  # TODO: explain & rely on what this copies
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        ...
    return wrapper

# TODO: expose original via wrapper.__wrapped__
"""

# Your code here.
