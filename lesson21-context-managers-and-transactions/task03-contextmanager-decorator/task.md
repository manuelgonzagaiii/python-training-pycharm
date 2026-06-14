# Generator-based Managers with @contextmanager

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 21.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Rewrite a small resource manager using @contextmanager and a single yield
- Place teardown in a finally so it runs on both success and error
- Understand that the exception is re-raised at the yield, so wrapping it lets you react

## Python features introduced
`contextlib.contextmanager`, `single yield splitting setup/teardown`, `try/finally around yield for guaranteed cleanup`, `yielding the as-value`, `how the generator maps to __enter__/__exit__`, `exceptions thrown back in at the yield point`

## MiniERP increment
Adds a concise @contextmanager-based switch_actor(name) to core/audit.py that sets the current audit actor for the duration of a block and restores it afterward — letting CLI/Web set 'who' is performing audited operations without a class.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from contextlib import contextmanager
from collections.abc import Iterator

current_actor: str = "system"

@contextmanager
def switch_actor(name: str) -> Iterator[str]:
    global current_actor
    previous = current_actor
    current_actor = name
    try:
        yield name
    finally:
        # TODO: restore current_actor = previous
        ...
- **Test focus:** Actor is the new value inside the block and restored after; restoration also happens when the block raises.

</div>
