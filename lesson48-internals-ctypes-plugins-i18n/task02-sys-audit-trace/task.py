"""Audit hooks & tracing with sys

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import sys

_EVENTS: list[tuple[str, tuple]] = []


def install_audit_hook(interesting: set[str]) -> None:
    """addaudithook that appends (event, args) to _EVENTS for events in `interesting`."""
    raise NotImplementedError


class CallCounter:
    """settrace-based tracer counting 'call' events per function name."""
    def __init__(self) -> None:
        self.counts: dict[str, int] = {}
    def __enter__(self):
        raise NotImplementedError
    def __exit__(self, *exc):
        sys.settrace(None)

"""

# Your code here.
