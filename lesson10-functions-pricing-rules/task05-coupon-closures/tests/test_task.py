"""Check for task05-coupon-closures.

Grading policy: validity, not wording.
"""

import unittest

import rules


class TestClosures(unittest.TestCase):
    def test_make_coupon_discounts(self):
        ten_off = rules.make_coupon(10)
        self.assertEqual(ten_off(1000), 900)

    def test_zero_coupon_is_identity(self):
        self.assertEqual(rules.make_coupon(0)(1000), 1000)

    def test_table_each_coupon_keeps_own_percent(self):
        table = rules.build_coupon_table([5, 10, 20])
        self.assertEqual(table[5](1000), 950)
        self.assertEqual(table[10](1000), 900)
        self.assertEqual(table[20](1000), 800)


if __name__ == "__main__":
    unittest.main()
