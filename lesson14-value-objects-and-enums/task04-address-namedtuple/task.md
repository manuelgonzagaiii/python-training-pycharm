# Address as a typing.NamedTuple

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 14.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define a lightweight immutable record with typing.NamedTuple and typed fields
- Add methods and defaults to a NamedTuple subclass
- Use ._replace to derive a modified copy and ._asdict for serialization
- Contrast NamedTuple (tuple-based, indexable, lightweight) with a frozen dataclass

## Python features introduced
`typing.NamedTuple`, `class-based NamedTuple with defaults`, `NamedTuple methods (._replace, ._asdict, ._fields)`, `field annotations on NamedTuple`, `tuple unpacking`, `immutability of tuples`

## MiniERP increment
Adds Address (street, city, region, postal_code, country) used by Customer billing/shipping. Demonstrates a tuple-backed value object alongside the dataclass-backed Money.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import NamedTuple


class Address(NamedTuple):
    street: str
    city: str
    postal_code: str
    country: str = "US"
    region: str = ""

    def one_line(self) -> str:
        # TODO: return a single-line formatted address
        ...

- **Test focus:** Address is indexable and unpackable, defaults apply, ._replace yields a changed copy without mutating the original, one_line formats correctly, ._asdict round-trips fields.

</div>
