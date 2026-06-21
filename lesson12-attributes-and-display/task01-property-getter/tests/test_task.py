"""Check for task01-property-getter.

Grading policy: validity, not wording.
"""

import unittest
from decimal import Decimal

import domain


class TestPriceDollars(unittest.TestCase):
    def test_computed_from_cents(self):
        p = domain.Product("A-001", "Widget", 1599)
        self.assertEqual(p.price_dollars, Decimal("15.99"))

    def test_reads_like_an_attribute(self):
        # a property is accessed without parentheses
        p = domain.Product("A", "W", 500)
        self.assertEqual(p.price_dollars, Decimal("5.00"))

    def test_exact_not_float(self):
        p = domain.Product("A", "W", 10)
        self.assertIsInstance(p.price_dollars, Decimal)


if __name__ == "__main__":
    unittest.main()
