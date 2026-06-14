# Audit hooks & tracing with sys

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.2 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Install an audit hook that observes security-relevant runtime events
- Understand the (event, args) audit protocol and that hooks cannot be removed
- Write a minimal settrace tracer (line/call events) for a profiling-style tool
- See how coverage and debuggers are built atop settrace

## Python features introduced
`sys.addaudithook`, `audit events (open, exec, etc.)`, `sys.settrace / trace functions`, `frame/event/arg trace protocol`, `sys.gettrace`, `PEP 578 runtime audit hooks`, `coverage/profilers built on settrace (note)`

## MiniERP increment
Adds a security audit hook that records file-open and code-exec audit events into the ERP audit log (so any plugin or rule touching the filesystem is logged), plus an opt-in line tracer used to profile which service methods a CLI session exercises.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
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

- **Test focus:** Tests install_audit_hook captures an 'open' audit event when a file is opened; tests CallCounter records call counts for functions invoked inside the with-block and detaches the tracer (sys.gettrace() is None) on exit.

</div>
