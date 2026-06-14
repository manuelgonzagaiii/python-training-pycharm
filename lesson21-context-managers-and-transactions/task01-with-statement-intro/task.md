# The with Statement & the Manager Protocol

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 21.1 of 6  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Read a with block as enter -> body -> exit, with exit always running
- Understand what __enter__ returns and what __exit__ receives
- Know that returning True from __exit__ swallows the exception

## Python features introduced
`with statement semantics`, `__enter__ / __exit__ protocol`, `the value bound by as`, `__exit__(exc_type, exc, tb) signature`, `returning True from __exit__ to suppress`, `guaranteed cleanup vs try/finally`

## MiniERP increment
Frames the upcoming Transaction manager by contrasting manual try/finally repository save/restore with the with-based approach the learner will build. No code change.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Theory page. Shows the protocol skeleton the next tasks implement:
#
#   class Manager:
#       def __enter__(self): return resource
#       def __exit__(self, exc_type, exc, tb) -> bool | None: ...
#
# and how `with Manager() as r:` maps onto it.
- **Test focus:** None (theory page).

</div>
