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


def add_product(catalog: list[Product], product: Product) -> None:
    """Append a product record to the catalog, in place (no new list is created)."""
    catalog.append(product)


def seed_catalog() -> list[Product]:
    """Return a starter catalog with a few products."""
    return [
        make_product("A-001", "Widget", 999, 5),
        make_product("A-002", "Gadget", 1499, 0),
        make_product("B-010", "Gizmo", 250, 12),
    ]
