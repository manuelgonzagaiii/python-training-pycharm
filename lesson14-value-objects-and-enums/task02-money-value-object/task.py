"""Money as a Frozen Dataclass

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Money:
    amount: Decimal
    currency: str = "USD"

    def __post_init__(self) -> None:
        # TODO: coerce amount to Decimal, reject negative amounts and
        # empty/lowercase currency codes. Frozen => use object.__setattr__.
        ...

"""

# Your code here.
