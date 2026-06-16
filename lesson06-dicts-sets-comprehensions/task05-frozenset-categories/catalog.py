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


def snapshot_catalog(catalog: list[Product]) -> list[Product]:
    """Return an independent shallow copy: mutating the result must not change the source."""
    return list(catalog)


def page(catalog: list[Product], number: int, size: int) -> list[Product]:
    """Return page `number` (1-based) of `size` items, using a slice."""
    start = (number - 1) * size
    return catalog[start:start + size]


def recent(catalog: list[Product], n: int) -> list[Product]:
    """The last n products, most recent first."""
    return catalog[-n:][::-1]


def describe(product: Product) -> str:
    """Unpack a record into a readable label, e.g. 'A-001 Widget $9.99 qty 5'."""
    sku, name, price_cents, qty = product
    return f"{sku} {name} ${price_cents // 100}.{price_cents % 100:02d} qty {qty}"


def split_featured(catalog: list[Product]) -> tuple[Product, list[Product]]:
    """Return (featured, rest): the first product, plus the remaining records as a list."""
    first, *rest = catalog
    return first, rest


def index_by_sku(catalog: list[Product]) -> dict[str, Product]:
    """Map each product's sku to its record, preserving catalog order."""
    index = {}
    for product in catalog:
        index[product[0]] = product
    return index


def find(index: dict[str, Product], sku: str) -> Product | None:
    """Return the product for sku, or None if absent (no KeyError)."""
    return index.get(sku)


def group_by_category(catalog: list[Product]) -> dict[str, list[Product]]:
    """Bucket products by category code (the sku up to the first '-')."""
    groups: dict[str, list[Product]] = {}
    for product in catalog:
        category = product[0].split("-")[0]
        groups.setdefault(category, []).append(product)
    return groups


def apply_overrides(base: dict[str, Product], overrides: dict[str, Product]) -> dict[str, Product]:
    """Return a new dict where overrides replace matching base entries (the | merge)."""
    return base | overrides


def products_with_all_tags(tags_index: dict[str, set[str]], required: set[str]) -> set[str]:
    """SKUs whose tag set contains all of `required` (a superset test)."""
    result = set()
    for sku, tags in tags_index.items():
        if tags >= required:
            result.add(sku)
    return result


def products_with_any_tags(tags_index: dict[str, set[str]], wanted: set[str]) -> set[str]:
    """SKUs sharing at least one tag with `wanted` (a non-empty intersection)."""
    result = set()
    for sku, tags in tags_index.items():
        if tags & wanted:
            result.add(sku)
    return result


def catalog_tag_combinations(tags_index: dict[str, set[str]]) -> set[frozenset[str]]:
    """The distinct tag combinations present, as a set of frozensets."""
    combinations = set()
    for tags in tags_index.values():
        combinations.add(frozenset(tags))
    return combinations
