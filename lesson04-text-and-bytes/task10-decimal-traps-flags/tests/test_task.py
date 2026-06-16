"""Check for stage 10: Decimal signals, traps, and flags.

Grading policy: validity, not wording. We check that bad money strings become a
ValueError, valid ones quantize to cents, and that require_exact refuses to round
silently.
"""

import unittest
from decimal import Decimal

import money


class TestDecimalTraps(unittest.TestCase):
    def test_parse_money_valid_quantizes(self):
        self.assertEqual(money.parse_money("19.5"), Decimal("19.50"))

    def test_parse_money_matches_money_helper(self):
        self.assertEqual(money.parse_money("19.50"), money.money("19.50"))

    def test_parse_money_rejects_garbage(self):
        with self.assertRaises(ValueError):
            money.parse_money("twelve")
        with self.assertRaises(ValueError):
            money.parse_money("")

    def test_require_exact_passes_cent_amount(self):
        self.assertEqual(money.require_exact(Decimal("19.50")), Decimal("19.50"))

    def test_require_exact_rejects_subcent(self):
        with self.assertRaises(ValueError):
            money.require_exact(Decimal("19.505"))


if __name__ == "__main__":
    unittest.main()
