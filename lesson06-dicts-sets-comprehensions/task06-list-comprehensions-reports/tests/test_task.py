"""Check for task06-list-comprehensions-reports.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestComprehensionReports(unittest.TestCase):
    def test_low_stock_is_strictly_less_than(self):
        cat = [catalog.make_product("A", "x", 100, 2),
               catalog.make_product("B", "y", 100, 5),
               catalog.make_product("C", "z", 100, 0)]
        low = catalog.low_stock(cat, 5)
        self.assertEqual({p[0] for p in low}, {"A", "C"})  # qty 5 is NOT low

    def test_low_stock_returns_list(self):
        self.assertIsInstance(catalog.low_stock(catalog.seed_catalog(), 1), list)

    def test_names_of_in_order(self):
        cat = catalog.seed_catalog()
        self.assertEqual(catalog.names_of(cat), [p[1] for p in cat])


if __name__ == "__main__":
    unittest.main()
