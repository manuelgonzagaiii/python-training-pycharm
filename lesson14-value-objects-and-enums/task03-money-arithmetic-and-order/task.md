# Comparable, Addable Money (order & operators)

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 14.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Enable comparison operators with @dataclass(order=True) and understand the generated __lt__/__le__/...
- Implement arithmetic dunders (__add__, __sub__, __mul__) that keep Money immutable by returning new instances
- Return NotImplemented for unsupported operand types instead of raising
- Refuse to add Money of different currencies

## Python features introduced
`dataclass(order=True)`, `__add__ / __sub__ / __mul__`, `operator overloading on value objects`, `returning NotImplemented`, `guarding cross-currency operations`, `total ordering via order=True`

## MiniERP increment
Money gains arithmetic and ordering so invoice line totals, subtotals, and tax can be summed and compared. Enables sum() over line items and min/max price queries.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from dataclasses import dataclass
from decimal import Decimal
from money import Money  # extend the previous task's Money

# TODO: add order=True to the dataclass decorator,
# then implement __add__, __sub__, __mul__ (by int/Decimal).
# Cross-currency __add__/__sub__ must raise ValueError;
# unsupported types must return NotImplemented.

- **Test focus:** Money sorts correctly, Money + Money of same currency works, cross-currency raises, Money * int scales, adding a non-Money returns NotImplemented (so 1 + money path is correct).

</div>
