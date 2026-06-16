"""Check for stage 7: rates, tax, and exact ratios with Fraction.

Grading policy: validity, not wording. We check exact tax amounts, a single
final rounding (no double-rounding drift), and a combined discount + tax
pipeline, so any correct implementation passes.
"""

import unittest
from decimal import Decimal
from fractions import Fraction

import money


class TestRates(unittest.TestCase):
    def test_apply_rate_rounds_to_cents(self):
        # 8.25% of 19.99 = 1.649175 -> 1.65
        self.assertEqual(
            money.apply_rate(money.money("19.99"), Decimal("0.0825")),
            money.money("1.65"),
        )

    def test_tax_for_exact_percentage(self):
        self.assertEqual(
            money.tax_for(money.money("100.00"), Fraction(825, 100)),
            money.money("8.25"),
        )

    def test_tax_for_whole_percent(self):
        self.assertEqual(
            money.tax_for(money.money("10.00"), Fraction(7)),
            money.money("0.70"),
        )

    def test_tax_for_rounds_once_at_the_end(self):
        # 8.255% of 200.00 is 16.51 exactly. Rounding the percent to cents first
        # (double-rounding) would give 16.52 -- the drift this stage warns against.
        self.assertEqual(
            money.tax_for(money.money("200.00"), Fraction(1651, 200)),
            money.money("16.51"),
        )

    def test_discount_then_tax_pipeline(self):
        price = money.money("50.00")
        net = price - money.apply_rate(price, Decimal("0.10"))        # 10% off -> 45.00
        taxed = net + money.tax_for(net, Fraction(825, 100))          # +8.25% -> 48.71
        self.assertEqual(taxed, money.money("48.71"))


if __name__ == "__main__":
    unittest.main()
