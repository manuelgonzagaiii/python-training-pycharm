# Literal and Capture Patterns

> **Phase:** Control Flow & Functions  •  **Stage:** 9.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a basic match with literal cases and a catch-all wildcard
- Distinguish a literal pattern from a capture pattern that binds a variable
- Model a closed command vocabulary with StrEnum

## Python features introduced
`match statement`, `case with literal patterns`, `capture patterns (bind a name)`, `wildcard pattern _`, `StrEnum (from enum)`, `PEP 604 return union (str | None)`

## MiniERP increment
Create cli/dispatch.py with a Command(StrEnum) of verbs (ADD, PRICE, DISCOUNT, REPORT, HELP) and normalize_verb(token) that matches a raw string literal to the canonical Command via match/case, capturing unknown tokens into a default and returning Command.HELP for anything unrecognized.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from enum import StrEnum


class Command(StrEnum):
    ADD = "add"
    PRICE = "price"
    DISCOUNT = "discount"
    REPORT = "report"
    HELP = "help"


def normalize_verb(token: str) -> Command:
    """Map a raw token to a Command via match/case; unknown -> HELP."""
    match token.strip().lower():
        case "add":
            return Command.ADD
        case _:
            ...
- **Test focus:** Known verbs map to the right Command members including case/whitespace normalization; unknown tokens fall through the wildcard to Command.HELP.

</div>
