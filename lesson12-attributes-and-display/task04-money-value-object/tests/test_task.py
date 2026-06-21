"""Check for task04-money-value-object.

Grading policy: validity, not wording.
"""

import unittest
from decimal import Decimal

import domain


class TestMoney(unittest.TestCase):
    def test_stores_cents(self):
        m = domain.Money(1500)
        self.assertEqual(m.cents, 1500)
        self.assertEqual(m.currency, "USD")

    def test_from_dollars_string(self):
        self.assertEqual(domain.Money.from_dollars("15.99").cents, 1599)
        self.assertEqual(domain.Money.from_dollars(Decimal("15.00")).cents, 1500)
        # exactness: int(float("0.29") * 100) truncates to 28, so a float-based
        # conversion is caught here; the exact path yields 29
        self.assertEqual(domain.Money.from_dollars("0.29").cents, 29)
        self.assertEqual(domain.Money.from_dollars("19.99").cents, 1999)

    def test_dollars_property_exact(self):
        self.assertEqual(domain.Money(1599).dollars, Decimal("15.99"))
        self.assertIsInstance(domain.Money(100).dollars, Decimal)


if __name__ == "__main__":
    unittest.main()
