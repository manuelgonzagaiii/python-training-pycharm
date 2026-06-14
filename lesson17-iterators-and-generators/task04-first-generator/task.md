# Replace the boilerplate with yield

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Rewrite the hand-rolled iterator as a one-line generator function
- Understand that calling a generator function returns a generator object (does not run the body yet)
- See execution suspend at yield and resume on the next next()
- Appreciate how much boilerplate yield removes versus __iter__/__next__

## Python features introduced
`generator functions`, `yield statement`, `lazy evaluation`, `generators implement the iterator protocol automatically`, `function state suspended/resumed at yield`, `generators are single-pass`

## MiniERP increment
Replace SalesLineCursor's class-based logic with a generator function iter_lines(ledger) in the reporting module, and have SalesLedger.__iter__ delegate to it — the report stream is now expressed as a generator, dramatically simpler than the manual protocol.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def iter_lines(lines):
    """Yield each sale line lazily. Same behavior as SalesLineCursor, far less code."""
    # TODO: loop over `lines` and yield each one
    ...

# Then SalesLedger.__iter__ becomes:  return iter_lines(self._lines)

- **Test focus:** iter_lines is a generator function (returns a generator); yields lines lazily in order; calling it does not execute the body until next() is called; integrates so SalesLedger stays multi-pass.

</div>
