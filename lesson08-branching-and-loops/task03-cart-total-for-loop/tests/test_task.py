"""Check for task03-cart-total-for-loop.

Grading policy: validity, not wording.
"""

import unittest

import pricing

class TestCartSubtotal(unittest.TestCase):
    def test_subtotal_prices_each_line_by_tier(self):
        lines = [("A", 1000, 5), ("B", 1000, 10)]   # 5*1000 + 10*950
        self.assertEqual(pricing.cart_subtotal(lines), 5000 + 9500)

    def test_empty_cart_is_zero(self):
        self.assertEqual(pricing.cart_subtotal([]), 0)

    def test_single_line(self):
        self.assertEqual(pricing.cart_subtotal([("A", 250, 3)]), 750)


if __name__ == "__main__":
    unittest.main()
