"""Who called this? inspect.stack

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import inspect
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CallSite:
    function: str
    filename: str
    lineno: int


def caller_site(depth: int = 1) -> CallSite:
    """Return the CallSite `depth` frames above the immediate caller.

    Use inspect.stack(); be careful to drop frame references afterward.
    """
    raise NotImplementedError

"""

# Your code here.
