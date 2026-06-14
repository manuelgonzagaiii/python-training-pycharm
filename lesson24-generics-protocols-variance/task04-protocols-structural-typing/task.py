"""Protocols & Structural Typing

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import Protocol, runtime_checkable
from decimal import Decimal

@runtime_checkable
class SupportsTotal(Protocol):
    def total(self) -> Decimal: ...

def grand_total(items: list[SupportsTotal]) -> Decimal:
    # TODO: sum item.total() across items
    ...

# Invoice and Payment already have .total(); they satisfy this with NO inheritance.
"""

# Your code here.
