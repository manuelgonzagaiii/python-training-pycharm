"""Physical, Digital & Bundle Products

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from product import Product
from money import Money


class PhysicalProduct(Product):
    def __init__(self, *args, shipping: Money, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.shipping = shipping

    def price(self) -> Money:
        # TODO: base price plus shipping
        ...


class BundleProduct(Product):
    # TODO: hold a list of (Product, qty); price() = discounted sum of components
    ...

"""

# Your code here.
