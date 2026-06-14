# Dynamic Manager Stacks with ExitStack

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 21.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Open a variable number of resources (one per import file) under a single ExitStack
- Register cleanup callbacks with stack.callback
- Understand reverse-order unwinding and how pop_all defers cleanup

## Python features introduced
`contextlib.ExitStack`, `stack.enter_context()`, `registering an unknown number of managers`, `stack.callback() for cleanup hooks`, `stack.pop_all() to transfer ownership`, `guaranteed unwinding in reverse order`

## MiniERP increment
Implements bulk_import(paths): opens every CSV source file via ExitStack.enter_context so a failure midway still closes all already-opened handles, feeding the Import/Export module a robust multi-file loader.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from contextlib import ExitStack
from pathlib import Path
from collections.abc import Iterable

def bulk_import(paths: Iterable[Path]) -> list[str]:
    rows: list[str] = []
    with ExitStack() as stack:
        handles = [stack.enter_context(open(p)) for p in paths]
        # TODO: read each handle, extend rows; register stack.callback(...) for cleanup
        ...
    return rows
- **Test focus:** All files are read and aggregated; if one path is bad, previously opened handles are still closed (no leaked files); cleanup callbacks fire in reverse order.

</div>
