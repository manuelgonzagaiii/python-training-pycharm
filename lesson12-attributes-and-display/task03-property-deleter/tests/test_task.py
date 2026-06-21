"""Check for task03-property-deleter.

Grading policy: validity, not wording.
"""

import unittest
from decimal import Decimal

import domain


class TestDiscountDeleter(unittest.TestCase):
    def test_default_is_none(self):
        p = domain.Product("A", "W", 100)
        self.assertIsNone(p.discount_cents)

    def test_set_and_read(self):
        p = domain.Product("A", "W", 100)
        p.discount_cents = 50
        self.assertEqual(p.discount_cents, 50)

    def test_deleter_resets_to_none(self):
        p = domain.Product("A", "W", 100)
        p.discount_cents = 50
        del p.discount_cents
        self.assertIsNone(p.discount_cents)


if __name__ == "__main__":
    unittest.main()
