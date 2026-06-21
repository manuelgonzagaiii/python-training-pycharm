"""Check for task03-tax-keyword-positional-only.

Grading policy: validity, not wording.
"""

import unittest

import rules


class TestApplyTax(unittest.TestCase):
    def test_basic_tax(self):
        self.assertEqual(rules.apply_tax(10000, rate_bps=825), 825)

    def test_amount_is_positional_only(self):
        with self.assertRaises(TypeError):
            rules.apply_tax(amount_cents=10000, rate_bps=825)

    def test_rate_is_keyword_only(self):
        with self.assertRaises(TypeError):
            rules.apply_tax(10000, 825)

    def test_inclusive_extracts_tax(self):
        self.assertEqual(rules.apply_tax(10825, rate_bps=825, inclusive=True), 825)


if __name__ == "__main__":
    unittest.main()
