"""Check for task02-property-setter.

Grading policy: validity, not wording.
"""

import unittest
from decimal import Decimal

import domain


class TestPriceSetter(unittest.TestCase):
    def test_set_valid_price(self):
        p = domain.Product("A", "W", 100)
        p.price_cents = 250
        self.assertEqual(p.price_cents, 250)

    def test_negative_rejected_on_assignment(self):
        p = domain.Product("A", "W", 100)
        with self.assertRaises(ValueError):
            p.price_cents = -1

    def test_negative_rejected_in_constructor(self):
        # __init__ assigns through the same setter
        with self.assertRaises(ValueError):
            domain.Product("A", "W", -5)


if __name__ == "__main__":
    unittest.main()
