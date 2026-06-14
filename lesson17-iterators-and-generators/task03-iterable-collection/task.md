# Make the report a reusable iterable

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand why a reusable collection must hand out a NEW iterator per __iter__ call
- Contrast a one-shot iterator with a multi-pass iterable
- Implement __len__ and __contains__ so the container feels native
- See that for x in coll twice works only when __iter__ is fresh each time

## Python features introduced
`separating iterable from iterator`, `__iter__ returning a fresh iterator each call`, `re-iteration semantics`, `container.__iter__ delegating to a helper iterator`, `__len__ for sized containers`, `__contains__ via membership`

## MiniERP increment
Wrap the sales data in a SalesLedger iterable whose __iter__ returns a fresh SalesLineCursor each time, so reports can be run repeatedly over the same ledger — turning the cursor from previous task into a proper reusable collection in the reporting module.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from .cursor import SalesLineCursor  # from the previous task

class SalesLedger:
    """A reusable, multi-pass iterable over sale lines."""
    def __init__(self, lines):
        self._lines = list(lines)

    def __iter__(self):
        # TODO: return a FRESH iterator each call so the ledger is multi-pass
        ...

    def __len__(self):
        ...

    def __contains__(self, line):
        ...

- **Test focus:** Iterating the ledger twice yields the same lines both times (multi-pass); each __iter__ returns a distinct object; len() and the `in` operator behave correctly.

</div>
