# Immutable updates with dataclasses.replace()

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 16.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain why mutating a frozen dataclass raises FrozenInstanceError, and why an in-place setter is not an option for value objects
- Use dataclasses.replace(obj, **changes) to produce a NEW frozen instance with selected fields overridden, leaving the original untouched
- Connect replace() to the already-taught NamedTuple._replace as the dataclass equivalent for value objects
- Predict that replace() re-runs __init__ and therefore __post_init__ (validation/normalisation fires again on the copy)
- Know that init=False fields are NOT carried over by replace() unless recomputed in __post_init__, and how that interacts with derived fields
- Reach for object.__setattr__ only inside __post_init__, and prefer replace() everywhere else

## Python features introduced
`dataclasses.replace`, `frozen dataclasses (frozen=True)`, `dataclasses.fields`, `dataclasses.is_dataclass`, `field(init=False) interaction with replace()`, `__post_init__ re-run on replace`, `object.__setattr__ vs replace() for frozen instances`, `FrozenInstanceError`, `keyword-only changes via **kwargs`, `PEP 604 unions (X | Y) in annotations`, `decimal.Decimal for money`, `StrEnum (carried from earlier p06 task)`

## MiniERP increment
Adds immutable-update methods to the frozen value objects in the MiniERP domain core (built in earlier p06 tasks). On the frozen `Money` dataclass, add `with_amount(self, amount)` and `scaled(self, factor)` that return new `Money` instances via `dataclasses.replace`, so currency is preserved and the original is never mutated; replace()'s re-run of `__post_init__` re-validates that the new amount is a non-negative `Decimal` and re-quantises it to the currency's minor units. On the frozen `InventoryLine` value object (sku, quantity, unit_price: Money), add `adjusted(self, *, delta_qty=0, new_unit_price=None)` returning a replaced copy with a recomputed `line_total`. This gives the inventory service a clean, audit-friendly way to apply stock adjustments and price corrections by emitting new immutable line snapshots instead of editing state in place — exactly what the later Audit-log module needs.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Carry forward the frozen `Money` dataclass and the `InventoryLine` value object from the previous p06 stages (both `frozen=True`, with `__post_init__` validation that uses `object.__setattr__` to normalise/quantise). In this stage, add the immutable-update helpers. Skeleton:

from __future__ import annotations
from dataclasses import dataclass, field, replace
from decimal import Decimal

@dataclass(frozen=True, slots=True)
class Money:
    amount: Decimal
    currency: str = "USD"
    def __post_init__(self) -> None:
        # normalise to Decimal, reject negatives, quantise to 2 dp (already built earlier)
        ...
    def with_amount(self, amount: Decimal | int | str) -> "Money":
        # TODO: return a new Money via dataclasses.replace, currency preserved
        ...
    def scaled(self, factor: Decimal | int | str) -> "Money":
        # TODO: multiply amount by factor and return a replaced copy
        ...

@dataclass(frozen=True, slots=True)
class InventoryLine:
    sku: str
    quantity: int
    unit_price: Money
    def adjusted(self, *, delta_qty: int = 0, new_unit_price: Money | None = None) -> "InventoryLine":
        # TODO: use replace() to override quantity and/or unit_price, never mutate self
        ...

Learners fill in the TODOs using only dataclasses.replace (no manual constructor calls, no attribute assignment).
- **Test focus:** Verify replace() semantics and immutability: (1) `m = Money("10.00"); m2 = m.with_amount("7.50")` returns a distinct object, `m2.amount == Decimal('7.50')`, `m2.currency == m.currency`, and `m is not m2` while `m.amount` is unchanged (original untouched). (2) `m.scaled(3).amount == Decimal('30.00')` and currency preserved. (3) replace() re-runs __post_init__: `m.with_amount("-1")` raises ValueError (negative rejected) and `m.with_amount("2.5")` is re-quantised to Decimal('2.50'). (4) Direct mutation `m.amount = Decimal('1')` raises dataclasses.FrozenInstanceError, proving why replace() is needed. (5) `line.adjusted(delta_qty=+5)` returns a new InventoryLine with quantity increased, original `line.quantity` unchanged, and `unit_price` identity preserved; `line.adjusted(new_unit_price=Money('9.99'))` swaps price and recomputes any derived total. (6) `dataclasses.replace(line, quantity=-1)` propagates the __post_init__ validation error, confirming the copy is validated, not blindly constructed.

</div>
