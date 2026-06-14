"""A plugin system via entry points

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
from importlib.metadata import entry_points
from typing import Protocol, runtime_checkable

GROUP = "minierp.plugins"


@runtime_checkable
class ErpPlugin(Protocol):
    name: str
    def register(self, registry: dict) -> None: ...


def discover() -> dict[str, ErpPlugin]:
    """Find entry points in GROUP, load each, skip ones that fail to load or
    do not satisfy ErpPlugin. Return name -> plugin instance."""
    raise NotImplementedError

"""

# Your code here.
