"""MiniERP domain layer: real classes for the catalog.

Earlier phases carried a product as a bare tuple or a dict and passed it to free
functions. This phase makes it an object: a class that bundles the data (sku, name,
price) with the behavior that belongs to it (labels, display, validation,
construction). Prices stay integer cents, never float -- the representation the
catalog and pricing engine already use.
"""


class Product:
    """A product in the catalog: a SKU, a display name, and a price in cents.

    Bundling data with behavior is the whole point of a class. Where a tuple needed
    a free function like label(product), a Product carries label() on itself, so the
    data and the code that understands it travel together.
    """

    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        """Initialize a new product. `self` is the fresh instance; each assignment
        stores one argument as an attribute that lives on that specific object.
        """
        self.sku = sku
        self.name = name
        self.price_cents = price_cents

    def label(self) -> str:
        """A short human label, e.g. 'A-001 - Widget'."""
        return f"{self.sku} - {self.name}"
