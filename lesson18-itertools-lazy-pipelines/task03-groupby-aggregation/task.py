"""Grouping with groupby (and why sorting matters)

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from itertools import groupby
from operator import attrgetter

def revenue_by_sku(ledger):
    """Yield (sku, total_units, subtotal) per product, lazily."""
    by_sku = sorted(ledger, key=attrgetter("product_sku"))  # groupby needs sorted input!
    for sku, group in groupby(by_sku, key=attrgetter("product_sku")):
        # TODO: consume `group` to sum units and subtotal, then yield the tuple
        ...

"""

# Your code here.
