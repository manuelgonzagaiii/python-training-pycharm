"""Check for task01-pricing-tiers-if-elif-else.

Grading policy: validity, not wording.
"""

import unittest

import pricing

class TestTiers(unittest.TestCase):
    def test_tier_bands(self):
        self.assertEqual(pricing.quantity_tier(1), "none")
        self.assertEqual(pricing.quantity_tier(9), "none")
        self.assertEqual(pricing.quantity_tier(10), "bulk")
        self.assertEqual(pricing.quantity_tier(49), "bulk")
        self.assertEqual(pricing.quantity_tier(50), "wholesale")
        self.assertEqual(pricing.quantity_tier(1000), "wholesale")

    def test_non_positive_rejected(self):
        for bad in (0, -1, -50):
            with self.assertRaises(ValueError):
                pricing.quantity_tier(bad)

    def test_unit_price_applies_tier_discount(self):
        self.assertEqual(pricing.unit_price_for(1000, 5), 1000)    # none: 0% off
        self.assertEqual(pricing.unit_price_for(1000, 10), 950)    # bulk: 5% off
        self.assertEqual(pricing.unit_price_for(1000, 50), 900)    # wholesale: 10% off

    def test_unit_price_rounds_to_cent(self):
        # 5% of 999 = 49.95 -> rounds to 50 cents off
        self.assertEqual(pricing.unit_price_for(999, 10), 949)


if __name__ == "__main__":
    unittest.main()
