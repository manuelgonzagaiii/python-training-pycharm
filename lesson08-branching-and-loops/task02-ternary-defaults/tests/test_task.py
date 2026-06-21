"""Check for task02-ternary-defaults.

Grading policy: validity, not wording.
"""

import unittest

import pricing

class TestTernaries(unittest.TestCase):
    def test_display_default_currency_is_dollars(self):
        self.assertEqual(pricing.display_price(1500), "$15.00")
        self.assertEqual(pricing.display_price(5), "$0.05")

    def test_display_other_currency(self):
        s = pricing.display_price(1500, "EUR")
        self.assertIn("15.00", s)
        self.assertIn("EUR", s)
        self.assertNotIn("$", s)

    def test_clamp_floor(self):
        self.assertEqual(pricing.clamp_floor(-50), 0)
        self.assertEqual(pricing.clamp_floor(0), 0)
        self.assertEqual(pricing.clamp_floor(250), 250)


if __name__ == "__main__":
    unittest.main()
