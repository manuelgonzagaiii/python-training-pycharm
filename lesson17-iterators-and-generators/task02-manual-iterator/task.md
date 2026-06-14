# A hand-written iterator over sales lines

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement the full iterator protocol by hand without any generator sugar
- Return self from __iter__ and advance/raise StopIteration in __next__
- Experience that a hand-rolled iterator is single-pass (exhausts once)
- Drive it with both an explicit while/next loop and a normal for-loop

## Python features introduced
`custom __iter__`, `custom __next__`, `raising StopIteration`, `iterator is self-returning from __iter__`, `iter()/next() built-ins`, `single-pass exhaustion semantics`, `__slots__ on the iterator class`

## MiniERP increment
Add a SalesLineCursor iterator class to the reporting module that walks the existing list of sale lines one at a time, exposing the domain as a reusable iterator instead of a raw list — the first lazy building block for streaming reports.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from dataclasses import dataclass

# `SaleLine` already exists in the domain model from earlier phases:
#   SaleLine(product_sku: str, qty: int, unit_price: float)

class SalesLineCursor:
    """A single-pass iterator over a sequence of SaleLine objects."""
    __slots__ = ("_lines", "_pos")

    def __init__(self, lines):
        self._lines = list(lines)
        self._pos = 0

    def __iter__(self):
        # TODO: an iterator's __iter__ should return itself
        ...

    def __next__(self):
        # TODO: return the next SaleLine, or raise StopIteration when exhausted
        ...

- **Test focus:** Verify __iter__ returns self; next() yields lines in order then raises StopIteration; a for-loop consumes all lines; the cursor is single-pass (a second loop yields nothing).

</div>
