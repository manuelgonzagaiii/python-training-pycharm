"""Defensive Input Validation at the Service Boundary

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from decimal import Decimal, InvalidOperation
from errors import ValidationError

def validate_product_payload(data: dict[str, object]) -> dict[str, object]:
    """Return a cleaned payload or raise ValidationError(field=...).
    Rules: sku non-empty (stripped); name non-empty; price Decimal >= 0;
    stock int >= 0.
    """
    # TODO: guard each field with an early raise; use match/case to pick the rule;
    #       use a walrus when checking (sku := str(data.get('sku','')).strip())
    raise NotImplementedError
"""

# Your code here.
