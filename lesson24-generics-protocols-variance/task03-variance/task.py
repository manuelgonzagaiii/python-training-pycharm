"""Variance: Covariance & Contravariance

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from collections.abc import Sequence

class Item: ...
class Product(Item): ...

# Covariant producer: returns T, never accepts it -> can be 'narrowed' safely
class Reader[T_co]:        # PEP 695 infers covariance from usage
    def get_all(self) -> Sequence[T_co]:
        ...  # TODO

# Why this is invariant and breaks:
# def widen(items: list[Item]) -> None: ...
# widen(list_of_products)   # TODO: explain the error in the task text
"""

# Your code here.
