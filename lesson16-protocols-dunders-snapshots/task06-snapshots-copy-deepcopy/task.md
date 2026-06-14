# Snapshots: copy, deepcopy & custom hooks

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 16.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish shallow (copy.copy) from deep (copy.deepcopy) copies and the aliasing bugs shallow copies cause with nested lists
- Implement __copy__ and __deepcopy__ to control how an entity is cloned
- Use the memo dict in __deepcopy__ to handle shared/cyclic references
- Produce an immutable point-in-time snapshot of an Invoice

## Python features introduced
`copy.copy`, `copy.deepcopy`, `__copy__`, `__deepcopy__`, `shallow vs deep semantics`, `memo dict in __deepcopy__`, `aliasing bugs from shallow copies`

## MiniERP increment
Adds snapshot()/clone() to Invoice using copy.deepcopy with a custom __deepcopy__ that freezes line items, so the Reporting/Audit modules can store immutable historical snapshots without later edits leaking back in. Completes the phase's clean domain model.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import copy


class Invoice:
    def __init__(self, number: str) -> None:
        self.number = number
        self.lines: list = []

    def __deepcopy__(self, memo: dict) -> "Invoice":
        # TODO: build a clone; use copy.deepcopy(self.lines, memo)
        # and register self in memo to handle shared references
        ...

    def snapshot(self) -> "Invoice":
        return copy.deepcopy(self)

- **Test focus:** deepcopy of an Invoice produces independent line lists (mutating the copy doesn't touch the original), shallow copy shares the lines list (demonstrating the bug), __deepcopy__ uses memo, snapshot is independent of later edits.

</div>
