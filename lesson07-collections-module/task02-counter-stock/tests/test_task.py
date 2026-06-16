"""Check for task02-counter-stock.

Grading policy: validity, not wording.
"""

import unittest

import catalog


from collections import Counter


class TestCounterStock(unittest.TestCase):
    def test_stock_counter_sums_qty(self):
        cat = catalog.seed_catalog()
        sc = catalog.stock_counter(cat)
        for p in cat:
            self.assertEqual(sc[p.sku], p.qty)

    def test_missing_sku_reads_zero(self):
        sc = catalog.stock_counter(catalog.seed_catalog())
        self.assertEqual(sc["does-not-exist"], 0)

    def test_apply_movements_adjusts(self):
        stock = Counter({"A-001": 5, "A-002": 2})
        deltas = Counter({"A-001": -2, "A-002": 3})
        result = catalog.apply_movements(stock, deltas)
        self.assertEqual(result["A-001"], 3)
        self.assertEqual(result["A-002"], 5)


if __name__ == "__main__":
    unittest.main()
