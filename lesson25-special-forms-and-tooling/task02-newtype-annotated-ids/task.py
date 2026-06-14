"""NewType & Annotated for IDs and Money

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from typing import NewType, Annotated
from decimal import Decimal

ProductId = NewType('ProductId', str)
CustomerId = NewType('CustomerId', str)

class Currency:
    def __init__(self, code: str) -> None: self.code = code
Money = Annotated[Decimal, Currency('USD')]

def charge(customer: CustomerId, amount: Money) -> None:
    # TODO: record the charge; passing a ProductId here must be a type error
    ...
"""

# Your code here.
