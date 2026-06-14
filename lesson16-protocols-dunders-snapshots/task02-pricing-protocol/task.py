"""PricingStrategy: Protocol vs ABC

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import Protocol, runtime_checkable
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

"""

# Your code here.
