# __missing__: how defaultdict really works (auto-zeroing the stock ledger)

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.9 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain that Python's dict calls __missing__(self, key) ONLY when a normal d[key] lookup fails on a dict *subclass* — and that this is the exact hook collections.defaultdict uses under the hood.
- Override __missing__ so an absent SKU resolves to a freshly inserted 0 balance, letting `ledger[sku] += qty` work without any `if sku not in ...` guard.
- Distinguish the three access paths precisely: d[key] triggers __missing__; dict.get(key) and `key in d` do NOT (they never insert and never call your hook).
- Recognise that __missing__ is the idiomatic, allocation-light alternative to pre-seeding a plain dict or pre-checking membership, and reimplement defaultdict's behaviour by hand to demystify it.
- Understand that returning a value from __missing__ does not by itself store it — you must explicitly assign self[key] = value to make the key persist (the auto-populate pattern).

## Python features introduced
`dict.__missing__ dunder hook`, `subclassing the built-in dict`, `d[key] subscription vs dict.get() vs the in / __contains__ operator (which bypass __missing__)`, `auto-populating a key from inside __missing__ via self[key] = ...`, `KeyError and the default dict behaviour __missing__ overrides`, `relationship between __missing__ and collections.defaultdict / default_factory`, `self-referential mutating subscript (ledger[sku] += qty) enabled by __missing__`, `super().__init__ in a dict subclass`, `PEP 604 union return annotations (int | ...)`, `f-string '=' self-documenting debug form (optional, in docstring examples)`

## MiniERP increment
Adds an inventory stock-balance ledger to the Inventory module. A new dict-subclass `StockLedger` maps SKU -> on-hand quantity (int). Its `__missing__(self, sku)` auto-inserts a 0 balance for any SKU seen for the first time, so applying a stream of stock movements becomes `for sku, delta in movements: ledger[sku] += delta` with no membership guards. A module-level `apply_movements(movements)` builds a `StockLedger` from an iterable of (sku, delta) pairs (positive for receipts, negative for sales/shipments) and returns it, giving Reporting a clean running-balance view. This is the hand-rolled version of `defaultdict(int)`; later inventory tasks can swap in or compare against defaultdict knowing exactly what it does. Relies only on plain dict subclassing and integer arithmetic already covered in earlier phases.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class StockLedger(dict):
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

- **Test focus:** Verify __missing__ semantics and the ERP behaviour, not just the happy path. Tests: (1) a fresh StockLedger()[ 'SKU-NEW' ] returns 0 AND inserts the key (assert 'SKU-NEW' in ledger afterward, len grows) — proving auto-populate. (2) ledger['X'] += 3 then += 2 yields 5 starting from empty (no pre-seed). (3) .get('UNSEEN') returns None and .get('UNSEEN', -1) returns -1 WITHOUT inserting the key (len unchanged) — proving .get bypasses __missing__. (4) 'UNSEEN' in ledger is False and does NOT insert — proving __contains__/in bypasses __missing__. (5) apply_movements([('A',10),('B',5),('A',-3),('C',0)]) == {'A':7,'B':5,'C':0}; an empty iterable yields an empty ledger. (6) confirm StockLedger is a dict subclass (isinstance(ledger, dict)) and behaves identically to defaultdict(int) on the same movement stream (compare against collections.defaultdict(int) as an oracle). (7) reading a present key never calls __missing__ (set ledger['P']=9; assert ledger['P']==9 and len unchanged).

</div>
