"""__missing__: how defaultdict really works (auto-zeroing the stock ledger)

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: class StockLedger(dict):
    """A SKU -> on-hand-quantity map whose missing keys default to 0.

    Subscripting an unknown SKU must INSERT a 0 balance and return it, so
    that ``ledger[sku] += delta`` works for first-time SKUs. This is the
    same mechanism ``collections.defaultdict(int)`` uses internally.
    """

    def __missing__(self, sku: str) -> int:
        # TODO: insert a 0 balance for `sku`, then return it.
        # Note: dict.get(sku) and `sku in ledger` must NOT trigger this.
        ...


def apply_movements(movements) -> StockLedger:
    """Fold an iterable of (sku, delta) movements into a StockLedger.

    delta > 0 -> receipt/return; delta < 0 -> sale/shipment.
    Unknown SKUs start at 0 thanks to StockLedger.__missing__.
    """
    ledger = StockLedger()
    # TODO: for sku, delta in movements: ledger[sku] += delta
    ...
    return ledger

"""

# Your code here.
