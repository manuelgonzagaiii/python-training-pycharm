"""Exception Chaining: raise from, __cause__ and __context__

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from decimal import Decimal, InvalidOperation
from errors import NotFoundError, ValidationError

def lookup_product(repo: dict[str, object], sku: str):
    try:
        return repo[sku]
    except KeyError as err:
        # TODO: raise NotFoundError('product', sku) from err
        raise NotImplementedError

def parse_price(raw: str) -> Decimal:
    try:
        return Decimal(raw)
    except InvalidOperation as err:
        # TODO: raise ValidationError(..., field='price') from err
        raise NotImplementedError
"""

# Your code here.
