import unittest

# TODO(author): replace with real checks.
# Test focus: Use a unittest.TestCase with `tempfile.TemporaryDirectory()` so each test gets a fresh db path (never touch the real data dir). Assert: (1) `set_quantity`/`get_quantity` round-trip an int correctly and the value PERSISTS across a new StockIndex instance pointing at the same path (proving on-disk persistence, not in-memory); (2) `get_quantity` returns the supplied default for an unknown SKU and does NOT raise; (3) `adjust` applies signed deltas (sale -N, restock +N) and a negative result raises ValueError leaving the stored value unchanged; (4) reading the raw db directly with `dbm.open(path,'r')` yields a *bytes* value (e.g. `db[b'WIDGET-1'] == b'42'`), proving values are stored as bytes not pickled ints; (5) `backend()` / `dbm.whichdb(path)` returns the expected backend string for an existing file (e.g. 'dbm.dumb') and `dbm.whichdb` of a nonexistent path is None; (6) `skus()` returns decoded str SKUs and `total_on_hand()` sums them. Keep assertions backend-tolerant where a platform may differ, but pin the 'values are bytes' check since that is the whole point of the lesson.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
