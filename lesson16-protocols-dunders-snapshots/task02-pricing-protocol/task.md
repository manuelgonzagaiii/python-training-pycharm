# PricingStrategy: Protocol vs ABC

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 16.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Define a structural contract with typing.Protocol that any matching class satisfies without inheritance
- Mark a Protocol @runtime_checkable to allow isinstance checks
- Contrast Protocol (structural, no inheritance needed) with ABC (nominal, must subclass)
- Implement multiple interchangeable pricing strategies that satisfy the Protocol implicitly

## Python features introduced
`typing.Protocol`, `structural (duck) typing`, `@runtime_checkable`, `Protocol vs abc.ABC tradeoffs`, `callable protocol member`, `isinstance against runtime_checkable Protocol`

## MiniERP increment
Adds pricing.py with a PricingStrategy Protocol and several strategies (NoDiscount, PercentageDiscount, BulkDiscount). The Sales module will accept any object matching the Protocol, decoupling pricing rules from the invoice engine.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from typing import Protocol, runtime_checkable
from money import Money


@runtime_checkable
class PricingStrategy(Protocol):
    def quote(self, unit_price: Money, qty: int) -> Money: ...


class PercentageDiscount:
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def quote(self, unit_price: Money, qty: int) -> Money:
        # TODO: apply percentage discount to unit_price * qty
        ...

- **Test focus:** Strategies satisfy PricingStrategy without subclassing, isinstance(strategy, PricingStrategy) is True for runtime_checkable, each strategy quotes correctly, a non-conforming object fails the isinstance check.

</div>
