"""Product Base Class & super()

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from money import Money
from sku import SKU


class Product:
    def __init__(self, sku: SKU, name: str, unit_price: Money) -> None:
        self.sku = sku
        self.name = name
        self.unit_price = unit_price

    def price(self) -> Money:
        # base price; subclasses may extend via super().price()
        return self.unit_price

    def line_total(self, qty: int) -> Money:
        # TODO: return price() * qty using Money arithmetic
        ...

"""

# Your code here.
