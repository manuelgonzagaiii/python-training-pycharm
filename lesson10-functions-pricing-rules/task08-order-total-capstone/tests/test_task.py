"""Check for task08-order-total-capstone.

Grading policy: validity, not wording.
"""

import unittest

import rules


class TestOrderTotal(unittest.TestCase):
    def test_plain_total(self):
        out = rules.order_total([("A", 1000, 1)])
        self.assertEqual(out["subtotal"], 1000)
        self.assertEqual(out["total"], 1000)

    def test_full_pipeline(self):
        lines = [("A", 1000, 2), ("B", 500, 4)]   # subtotal 4000
        out = rules.order_total(lines, tier_percent=10, coupons=(5,), tax_rate_bps=825)
        self.assertEqual(out["subtotal"], 4000)
        self.assertEqual(out["after_discounts"], 3420)  # 4000 -10% =3600, -5% =3420
        self.assertEqual(out["tax"], 282)               # 8.25% of 3420
        self.assertEqual(out["total"], 3702)

    def test_breakdown_keys(self):
        out = rules.order_total([("A", 1000, 1)], tax_rate_bps=1000)
        for key in ("subtotal", "after_discounts", "tax", "total"):
            self.assertIn(key, out)


if __name__ == "__main__":
    unittest.main()
