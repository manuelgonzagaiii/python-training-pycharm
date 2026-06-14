"""Composing the full lazy report pipeline

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: def build_report(ledger, *, sku=None, page_no=None, page_size=50):
    """Compose the lazy stages into one report stream."""
    stream = iter(ledger)
    if sku is not None:
        stream = (ln for ln in stream if ln.product_sku == sku)
    # TODO: feed `stream` through revenue_by_sku, then page() if page_no is set
    ...

"""

# Your code here.
