# Callable Strategies & the Context-Manager Protocol

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 16.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Make an object callable with __call__ so a TaxRule instance can be used like a function
- Implement __enter__/__exit__ to build a transactional context manager by hand
- Control exception propagation from __exit__ via its return value
- Use parenthesized multiple context managers in a single with-statement

## Python features introduced
`__call__`, `__enter__ / __exit__`, `context manager protocol`, `with-statement`, `exception suppression in __exit__ (return True/False)`, `parenthesized context managers`

## MiniERP increment
Adds a callable TaxRule(amount) -> Money and a UnitOfWork context manager that buffers changes to a Repository and commits on clean exit / rolls back on exception. This transactional seam underpins Sales, Payments and the Audit log.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from money import Money


class TaxRule:
    def __init__(self, rate_percent: int) -> None:
        self.rate_percent = rate_percent

    def __call__(self, base: Money) -> Money:
        # TODO: return the tax owed on `base`
        ...


class UnitOfWork:
    def __enter__(self) -> "UnitOfWork": ...
    def __exit__(self, exc_type, exc, tb) -> bool:
        # commit on success, roll back on exception; do not suppress
        ...

- **Test focus:** TaxRule instances are callable and compute tax, UnitOfWork commits buffered changes on clean exit and discards them when an exception propagates, __exit__ returns False so exceptions are not swallowed, parenthesized with-block works.

</div>
