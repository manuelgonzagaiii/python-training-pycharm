# @transaction via __enter__/__exit__ (MILESTONE)

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 21.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement Transaction.__enter__ that snapshots repository state (deepcopy) and returns the repo
- Implement __exit__ that discards the snapshot on success but restores it when exc_type is not None
- Return False so exceptions still propagate after rollback

## Python features introduced
`class-based context manager`, `__enter__ returning a working handle`, `__exit__ inspecting exc_type to commit vs rollback`, `deep snapshot with copy.deepcopy`, `returning False from __exit__ to propagate`, `reusing the same object as both decorator-free CM`

## MiniERP increment
Delivers the phase milestone: a Transaction context manager in core/transaction.py. `with Transaction(repo):` makes a sequence of create/update/sale calls all-or-nothing — partial multi-step operations no longer corrupt the in-memory store.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import copy
from types import TracebackType

class Transaction:
    def __init__(self, repo: "Repository") -> None:
        self.repo = repo
        self._snapshot: object | None = None
    def __enter__(self) -> "Repository":
        self._snapshot = copy.deepcopy(self.repo.state)
        return self.repo
    def __exit__(self, exc_type: type[BaseException] | None,
                 exc: BaseException | None, tb: TracebackType | None) -> bool:
        # TODO: if exc_type is not None: restore self.repo.state from snapshot
        #       always clear snapshot; return False to propagate
        ...
- **Test focus:** On a clean block, mutations persist; when the block raises, repository state is byte-for-byte restored to the pre-block snapshot and the exception still propagates.

</div>
