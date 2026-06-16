"""Check for task06-chainmap-layered-stock.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestChainMapLayeredStock(unittest.TestCase):
    def test_override_wins_else_default(self):
        default = {"A": 10, "B": 5}
        warehouse = {"A": 3}
        eff = catalog.effective_stock(default, warehouse)
        self.assertEqual(eff["A"], 3)   # override layer wins
        self.assertEqual(eff["B"], 5)   # falls through to default

    def test_earlier_override_searched_first(self):
        eff = catalog.effective_stock({"A": 1}, {"A": 2}, {"A": 3})
        self.assertEqual(eff["A"], 2)   # first override argument is searched first

    def test_default_untouched(self):
        default = {"A": 10}
        catalog.effective_stock(default, {"A": 3})
        self.assertEqual(default["A"], 10)  # layering does not mutate the default


if __name__ == "__main__":
    unittest.main()
