"""MiniERP inventory helpers: stock reservation and catalog search.

Pure functions over plain data. The catalog is passed in as a list of product
records shaped (sku, name, price_cents, qty) -- the same shape the catalog module
produces -- so nothing here imports another module. Quantities are integers.
"""


def reserve_units(available: int, requested: int) -> int:
    """Reserve stock in fixed batches until the request is met or stock runs out.

    Draws the stock down one batch (10 units) at a time with a while loop and
    returns how many units were actually reserved -- which can be less than
    requested when stock is short (partial fulfillment). The loop condition is
    what guarantees it ends: every pass reduces `available` or closes the gap, so
    one of the two tests eventually fails.
    """
    batch = 10
    reserved = 0
    while reserved < requested and available > 0:
        take = min(batch, requested - reserved, available)
        reserved += take
        available -= take
    return reserved


def find_in_catalog(catalog: list[tuple], sku: str) -> tuple:
    """Linear-scan the catalog for a product by SKU.

    Skips non-matching records with continue and breaks on the first match. The
    for/else attaches an else to the loop: it runs only when the loop was never
    broken out of, i.e. nothing matched -- the clean place to raise.
    """
    found = None
    for product in catalog:
        if product[0] != sku:
            continue
        found = product
        break
    else:
        raise KeyError(f"unknown sku: {sku}")
    return found
