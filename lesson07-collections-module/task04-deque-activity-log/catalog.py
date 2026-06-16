"""MiniERP's in-memory catalog and inventory.

The catalog is a list of product records, now upgraded to a typing.NamedTuple so
fields read by name while staying a tuple. This phase also adds the specialized
collections containers the inventory engine needs. Prices are integer cents.
"""
from collections import Counter, defaultdict, deque
from typing import NamedTuple


class ProductRecord(NamedTuple):
    """A product record with named fields. A NamedTuple IS a tuple, so all the
    earlier sequence code keeps working unchanged, while fields are now readable
    by name (product.sku) instead of by position (product[0]).
    """
    sku: str
    name: str
    price_cents: int
    qty: int


type Product = ProductRecord  # the record type -- now a named tuple


def make_product(sku: str, name: str, price_cents: int, qty: int) -> Product:
    """Return a product record (now a named tuple) with fields in their fixed order."""
    return ProductRecord(sku, name, price_cents, qty)


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


def low_stock(catalog: list[Product], threshold: int) -> list[Product]:
    """Products whose qty is strictly below threshold, via a list comprehension."""
    return [product for product in catalog if product[3] < threshold]


def names_of(catalog: list[Product]) -> list[str]:
    """The product names in catalog order, via a list comprehension."""
    return [product[1] for product in catalog]


def price_index(catalog: list[Product]) -> dict[str, int]:
    """sku -> price_cents, via a dict comprehension."""
    return {product[0]: product[2] for product in catalog}


def all_tags(tags_index: dict[str, set[str]]) -> set[str]:
    """Every tag used anywhere, via a set comprehension over all tag sets."""
    return {tag for tags in tags_index.values() for tag in tags}


def inventory_value(catalog: list[Product]) -> int:
    """Total value in cents, counting only the lines that carry stock, via a generator expression."""
    return sum(line for product in catalog if (line := product[2] * product[3]) > 0)


def reprice(product: Product, new_price: int) -> Product:
    """Return a copy of the record with only price_cents changed, via _replace."""
    return product._replace(price_cents=new_price)


def stock_counter(catalog: list[Product]) -> Counter[str]:
    """A Counter mapping sku -> quantity on hand (a missing sku reads as 0)."""
    counter = Counter()
    for product in catalog:
        counter[product.sku] += product.qty
    return counter


def apply_movements(stock: Counter[str], deltas: Counter[str]) -> Counter[str]:
    """Apply receipts (+) and sales (-) to stock via Counter arithmetic."""
    return stock + deltas


def group_by_category_dd(catalog: list[Product]) -> dict[str, list[Product]]:
    """Group products by category code using defaultdict(list); return a plain dict."""
    groups = defaultdict(list)
    for product in catalog:
        groups[product.sku.split("-")[0]].append(product)
    return dict(groups)


def tag_to_skus(tags_index: dict[str, set[str]]) -> dict[str, set[str]]:
    """Invert the tag index: each tag -> the set of skus carrying it (defaultdict(set))."""
    inverted = defaultdict(set)
    for sku, tags in tags_index.items():
        for tag in tags:
            inverted[tag].add(sku)
    return dict(inverted)


def new_activity_log(capacity: int) -> deque[str]:
    """A bounded log that keeps only the last `capacity` events (a ring buffer)."""
    return deque(maxlen=capacity)


def record_event(log: deque[str], message: str) -> None:
    """Append an event; when full, the oldest is dropped automatically."""
    log.append(message)


def recent_events(log: deque[str]) -> list[str]:
    """The logged events, newest first."""
    return list(log)[::-1]
