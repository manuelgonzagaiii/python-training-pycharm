"""Immutable updates with dataclasses.replace()

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: Carry forward the frozen `Money` dataclass and the `InventoryLine` value object from the previous p06 stages (both `frozen=True`, with `__post_init__` validation that uses `object.__setattr__` to normalise/quantise). In this stage, add the immutable-update helpers. Skeleton:

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
"""

# Your code here.
