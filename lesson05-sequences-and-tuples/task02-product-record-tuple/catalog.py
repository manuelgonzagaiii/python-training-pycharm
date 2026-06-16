"""MiniERP's in-memory catalog.

The catalog is a list of product records. Each record is a tuple of
(sku, name, price_cents, qty): a fixed shape, so a tuple; the collection grows,
so a list. Prices are integer cents, never float. This module is the catalog's
backbone, extended across the whole data-structures phase.
"""


type Product = tuple[str, str, int, int]  # (sku, name, price_cents, qty)


def make_product(sku: str, name: str, price_cents: int, qty: int) -> Product:
    """Return a product as an immutable tuple record, fields in their fixed order."""
    return (sku, name, price_cents, qty)
