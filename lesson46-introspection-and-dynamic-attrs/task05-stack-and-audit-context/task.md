# Who called this? inspect.stack

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.5 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Walk the call stack to capture the caller's function and line for audit context
- Read frame info safely and understand why lingering frame refs cause cycles
- Enrich the existing audit log with the originating call site without changing call sites
- Recognize when stack inspection is appropriate vs an anti-pattern

## Python features introduced
`inspect.stack`, `inspect.currentframe`, `FrameInfo (filename, lineno, function)`, `inspect.getframeinfo`, `frame.f_locals / f_back`, `frame reference hygiene (del frame)`

## MiniERP increment
Augments the ERP audit log so each entry records the calling function and source location captured via inspect.stack — useful for tracing which front-end / rule triggered a mutation, with no change to the services being audited.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
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

- **Test focus:** Tests caller_site(1) reports the function that called the helper (not the helper itself) with correct function name and a plausible lineno; tests that increasing depth walks further up; ensures no frame objects leak (via gc check).

</div>
