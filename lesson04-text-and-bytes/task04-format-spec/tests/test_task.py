"""Check for stage 4: the format-spec mini-language.

Grading policy: validity, not wording. We check the produced strings.
"""

import unittest
from decimal import Decimal

import text


class TestFormatSpec(unittest.TestCase):
    def test_fmt_money_thousands_and_cents(self):
        self.assertEqual(text.fmt_money(Decimal("1234.5")), "$1,234.50")

    def test_fmt_money_zero(self):
        self.assertEqual(text.fmt_money(Decimal("0")), "$0.00")

    def test_fmt_money_millions(self):
        self.assertEqual(text.fmt_money(Decimal("1000000")), "$1,000,000.00")

    def test_fmt_col_left_is_default(self):
        self.assertEqual(text.fmt_col("Hi", 5), "Hi   ")

    def test_fmt_col_right(self):
        self.assertEqual(text.fmt_col("Hi", 5, ">"), "   Hi")

    def test_fmt_col_center(self):
        self.assertEqual(text.fmt_col("Hi", 6, "^"), "  Hi  ")


if __name__ == "__main__":
    unittest.main()
