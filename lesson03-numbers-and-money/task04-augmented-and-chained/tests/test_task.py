"""Check for stage 4: running totals (+=) and chained comparisons.

Grading policy: validity, not wording. Any correct accumulation and any correct
inclusive range check pass, however you write the body.
"""

import unittest

import money


class TestAccumulationAndRange(unittest.TestCase):
    def test_running_total_adds_up(self):
        self.assertEqual(money.running_total([10, 20, 30]), 60)

    def test_running_total_empty_is_zero(self):
        self.assertEqual(money.running_total([]), 0)

    def test_running_total_single_item(self):
        self.assertEqual(money.running_total([99]), 99)

    def test_in_stock_range_inside(self):
        self.assertTrue(money.in_stock_range(5, 1, 10))

    def test_in_stock_range_is_inclusive(self):
        self.assertTrue(money.in_stock_range(1, 1, 10), "low bound should be allowed")
        self.assertTrue(money.in_stock_range(10, 1, 10), "high bound should be allowed")

    def test_in_stock_range_outside(self):
        self.assertFalse(money.in_stock_range(0, 1, 10))
        self.assertFalse(money.in_stock_range(11, 1, 10))


if __name__ == "__main__":
    unittest.main()
