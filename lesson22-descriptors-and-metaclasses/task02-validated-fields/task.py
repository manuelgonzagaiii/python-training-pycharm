"""Descriptor-Validated Fields: SKU, Money, NonNegative, Email (MILESTONE)

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import re
from decimal import Decimal
from .fields import Field

class SKU(Field):
    PATTERN = re.compile(r"^[A-Z]{3}-\d{4}$")
    def validate(self, value: str) -> str:
        # TODO: raise ValueError if not PATTERN.fullmatch(value); return value
        ...

class Money(Field):
    def validate(self, value) -> Decimal:
        # TODO: coerce to Decimal, reject negatives / non-numeric
        ...

class NonNegative(Field):
    def validate(self, value: int) -> int: ...

class Email(Field):
    def validate(self, value: str) -> str: ...
"""

# Your code here.
