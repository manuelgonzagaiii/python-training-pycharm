"""Party Hierarchy: Customer & Supplier

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from address import Address
from money import Money
from mixins import Timestamped, Identified


class Party(Timestamped, Identified):
    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        super().__init__(**kwargs)


class Customer(Party):
    def __init__(self, name: str, credit_limit: Money, **kwargs) -> None:
        # TODO: store credit_limit, call super().__init__, manage addresses
        ...

"""

# Your code here.
