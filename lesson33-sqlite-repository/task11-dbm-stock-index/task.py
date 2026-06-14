"""Raw key/value persistence: a dbm stock index

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: Provide `erp/inventory/stock_index.py` with a `StockIndex` class wrapping a dbm file. In __init__, store the path (under a data dir, default e.g. `data/stock.dbm`) using pathlib; for portability and deterministic auto-checking, open with `dbm.dumb.open(...)` inside each method via `with`, OR open a `dbm.open(path, 'c')` handle - learners should code against the dbm mapping API either way. Implement `_encode_qty(n)`/`_decode_qty(b)` (e.g. `str(n).encode()` <-> `int(b.decode())`, or document int.to_bytes), `set_quantity`, `get_quantity` (catch KeyError, return default), `adjust` (read-modify-write a signed delta, never let on-hand go below 0 - raise ValueError), `skus` (decode every key), `total_on_hand`, and `backend()` returning `dbm.whichdb(str(self.path))`. Include a `__main__` demo that seeds a few SKUs, records a sale and a restock, and prints the backend name. Pre-seed the task with the data dir and a couple of starter SKUs so the increment is visibly wired into Inventory.
"""

# Your code here.
