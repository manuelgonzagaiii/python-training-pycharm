# PaymentMethod via the Functional Enum API

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 14.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create an enum dynamically with the functional API Enum('PaymentMethod', [...])
- Understand member .name vs .value and aliasing
- Choose between functional and class syntax appropriately
- Use an enum member as a match/case subject

## Python features introduced
`functional Enum API (Enum('Name', names))`, `enum.IntEnum`, `Enum aliases (_ignore_/value reuse)`, `Enum.__members__`, `name vs value attributes`, `Enum in match/case with __match_args__ awareness`

## MiniERP increment
Adds PaymentMethod (CASH, CARD, BANK_TRANSFER, STORE_CREDIT) for the Payments module, built with the functional API to show the alternative construction style. Used by payment recording later in the phase.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from enum import Enum

# Build PaymentMethod using the FUNCTIONAL API instead of class syntax.
# TODO: PaymentMethod = Enum('PaymentMethod', ...)


def settlement_days(method) -> int:
    # TODO: use match/case over PaymentMethod members to return
    # how many days until funds settle (CASH=0, CARD=2, BANK_TRANSFER=3, STORE_CREDIT=0)
    ...

- **Test focus:** PaymentMethod created via functional API has the expected members, .name/.value correct, settlement_days dispatches correctly via match/case for every member.

</div>
