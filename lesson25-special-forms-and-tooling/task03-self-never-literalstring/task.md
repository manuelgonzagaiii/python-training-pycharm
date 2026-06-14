# Self, Never & LiteralString

> **Phase:** Modern Type System  •  **Stage:** 25.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Annotate fluent/builder methods with Self so subclasses chain correctly without naming the class
- Use Never / NoReturn for functions that never return and assert_never for exhaustive match dead-ends
- Use LiteralString to require compile-time-constant strings (e.g. SQL fragments) and reject runtime-built ones
- Connect Never to exhaustiveness checking over a Literal/Enum

## Python features introduced
`typing.Self`, `typing.Never`, `typing.NoReturn`, `typing.LiteralString`, `fluent builder returning Self`, `assert_never for exhaustiveness`, `SQL-injection-safe LiteralString`

## MiniERP increment
Adds a typed InvoiceBuilder whose with_line/with_customer return Self (subclass-safe chaining), an assert_never guard in the status match (proving all cases handled), and a query helper that only accepts LiteralString fragments — preparing safe SQL for the later persistence module.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import Self, Never, LiteralString, assert_never

class InvoiceBuilder:
    def with_customer(self, c: CustomerId) -> Self:
        ...  # TODO: set and return self
    def with_line(self, p: ProductId, qty: int) -> Self:
        ...  # TODO: append and return self

def handle(status: Status) -> str:
    match status:
        case 'draft' | 'sent' | 'paid' | 'void':
            return status
        case _ as unreachable:
            assert_never(unreachable)  # Never

def sql(fragment: LiteralString) -> None: ...  # rejects f-strings built from user input
- **Test focus:** Tests chain builder calls (each returns the same/derived object) and verify the assembled invoice; assert_never path is shown to be unreachable for valid Status; a documented case shows a runtime-built str rejected where LiteralString is required.

</div>
