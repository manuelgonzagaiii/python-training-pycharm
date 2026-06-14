# Class Patterns with __match_args__

> **Phase:** Control Flow & Functions  •  **Stage:** 9.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Match against object types and destructure their fields positionally and by keyword
- Define __match_args__ (directly or via dataclass) to enable positional class patterns
- Dispatch on typed request objects rather than raw dicts

## Python features introduced
`class patterns Type(...)`, `__match_args__ for positional subpatterns`, `keyword subpatterns in class patterns`, `dataclass with slots and kw_only`, `isinstance-style structural dispatch`

## MiniERP increment
Add request dataclasses (AddRequest, PriceRequest, DiscountRequest) with slots/kw_only to cli/dispatch.py and a describe(req) that uses class patterns — PriceRequest(sku=s, qty=q), AddRequest(sku, qty) — to render a human summary, formalizing the typed command objects the dispatcher will execute.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class PriceRequest:
    sku: str
    qty: int


def describe(req: object) -> str:
    """Render a summary using class patterns over request dataclasses."""
    match req:
        case PriceRequest(sku=s, qty=q):
            ...
        case _:
            return "unknown request"
- **Test focus:** Each request dataclass matches its class pattern and binds the right fields; an unrelated object falls to the wildcard summary.

</div>
