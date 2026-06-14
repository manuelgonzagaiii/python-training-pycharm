# OrderStatus with StrEnum

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 14.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Model a closed set of states with enum.StrEnum so members are real strings (JSON/CSV friendly)
- Generate lowercase member values automatically with auto() in StrEnum
- Guarantee no duplicate values with @unique
- Look up a member by value and iterate all members

## Python features introduced
`enum.StrEnum`, `enum.auto()`, `enum.unique decorator`, `StrEnum members usable as strings`, `iterating members`, `__members__`, `value lookup Enum(value)`

## MiniERP increment
Adds OrderStatus (DRAFT, CONFIRMED, FULFILLED, CANCELLED, REFUNDED) for invoices/sales orders. Because StrEnum members are strings, they serialize directly for the future Web/CLI layers.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from enum import StrEnum, auto, unique


@unique
class OrderStatus(StrEnum):
    DRAFT = auto()
    CONFIRMED = auto()
    FULFILLED = auto()
    CANCELLED = auto()
    REFUNDED = auto()

    # TODO: add a classmethod terminal() returning the set of
    # statuses from which no further transition is allowed.

- **Test focus:** OrderStatus.DRAFT == 'draft' (StrEnum string behavior), auto() yields lowercase names, OrderStatus('confirmed') looks up the member, terminal() returns the right set, @unique enforced.

</div>
