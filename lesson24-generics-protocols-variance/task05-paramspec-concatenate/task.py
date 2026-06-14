"""ParamSpec & Concatenate for Decorators

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from collections.abc import Callable
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
"""

# Your code here.
