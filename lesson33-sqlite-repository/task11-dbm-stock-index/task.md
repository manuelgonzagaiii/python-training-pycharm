# Raw key/value persistence: a dbm stock index

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.11 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that a dbm database is a persistent, on-disk mapping whose keys AND values are raw bytes only (str is auto-encoded to bytes with the default codec) - unlike shelve, which pickles arbitrary Python objects on top of dbm
- Open and close a dbm store safely with `with dbm.open(path, flag) as db:` and know what the flags 'r'/'w'/'c'/'n' mean
- Serialize an int to bytes when writing and parse it back when reading, because dbm cannot store ints directly (TypeError otherwise)
- Use the mapping operations dbm exposes (db[key], key in db, db.keys(), len(db)) and handle a missing key (KeyError)
- Use `dbm.whichdb(path)` to detect which concrete backend created an existing database file (e.g. 'dbm.dumb'), and know it returns None for a path that is not a dbm file
- Articulate WHEN to reach for raw dbm over shelve: no pickle overhead, no arbitrary-object deserialization risk, and language-agnostic byte values - at the cost of doing your own (de)serialization

## Python features introduced
`dbm`, `dbm.open`, `dbm.whichdb`, `dbm.dumb`, `bytes/str distinction`, `str.encode / bytes.decode`, `int.to_bytes / int.from_bytes (or str-encoded ints)`, `context manager (with) on a dbm object`, `mapping protocol on dbm: __getitem__/__setitem__/__contains__/keys/__len__`, `dict.setdefault-style default handling`, `KeyError handling`, `os.path / pathlib for the db file path`, `flag argument to dbm.open ('c','r','w','n')`

## MiniERP increment
Adds a lightweight, persistent on-hand stock index to the Inventory module, backed by a raw dbm key/value store, kept separate from the richer pickled product catalog (shelve) built earlier in this phase. New module `erp/inventory/stock_index.py` exposes a small `StockIndex` class that maps a product SKU to its current on-hand quantity, persisted to a `.dbm` file under the ERP data directory. Methods: `set_quantity(sku, qty)`, `get_quantity(sku, default=0)`, `adjust(sku, delta)` (apply a signed inventory movement, e.g. -3 on a sale, +50 on a restock), `skus()` (decoded list of SKUs on file), `total_on_hand()`, and a `backend()` helper that returns `dbm.whichdb(path)` so the CLI/reporting layer can report which dbm flavor is in use. Keys are SKU strings encoded to bytes; values are quantities encoded as bytes; the class converts at the boundary so callers keep working with plain str SKUs and int quantities. This gives the Sales and Reporting modules a fast, low-overhead source of truth for stock levels without loading the whole pickled catalog.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide `erp/inventory/stock_index.py` with a `StockIndex` class wrapping a dbm file. In __init__, store the path (under a data dir, default e.g. `data/stock.dbm`) using pathlib; for portability and deterministic auto-checking, open with `dbm.dumb.open(...)` inside each method via `with`, OR open a `dbm.open(path, 'c')` handle - learners should code against the dbm mapping API either way. Implement `_encode_qty(n)`/`_decode_qty(b)` (e.g. `str(n).encode()` <-> `int(b.decode())`, or document int.to_bytes), `set_quantity`, `get_quantity` (catch KeyError, return default), `adjust` (read-modify-write a signed delta, never let on-hand go below 0 - raise ValueError), `skus` (decode every key), `total_on_hand`, and `backend()` returning `dbm.whichdb(str(self.path))`. Include a `__main__` demo that seeds a few SKUs, records a sale and a restock, and prints the backend name. Pre-seed the task with the data dir and a couple of starter SKUs so the increment is visibly wired into Inventory.
- **Test focus:** Use a unittest.TestCase with `tempfile.TemporaryDirectory()` so each test gets a fresh db path (never touch the real data dir). Assert: (1) `set_quantity`/`get_quantity` round-trip an int correctly and the value PERSISTS across a new StockIndex instance pointing at the same path (proving on-disk persistence, not in-memory); (2) `get_quantity` returns the supplied default for an unknown SKU and does NOT raise; (3) `adjust` applies signed deltas (sale -N, restock +N) and a negative result raises ValueError leaving the stored value unchanged; (4) reading the raw db directly with `dbm.open(path,'r')` yields a *bytes* value (e.g. `db[b'WIDGET-1'] == b'42'`), proving values are stored as bytes not pickled ints; (5) `backend()` / `dbm.whichdb(path)` returns the expected backend string for an existing file (e.g. 'dbm.dumb') and `dbm.whichdb` of a nonexistent path is None; (6) `skus()` returns decoded str SKUs and `total_on_hand()` sums them. Keep assertions backend-tolerant where a platform may differ, but pin the 'values are bytes' check since that is the whole point of the lesson.

</div>
