"""Check for task05-repr-and-str.

Grading policy: validity, not wording.
"""

import unittest
from decimal import Decimal

import domain


class TestReprStr(unittest.TestCase):
    def test_money_repr_roundtrips(self):
        m = domain.Money(1500, "USD")
        # a good repr is unambiguous: eval-ing it rebuilds an equal-valued Money
        rebuilt = eval(repr(m), {"Money": domain.Money})
        self.assertEqual((rebuilt.cents, rebuilt.currency), (1500, "USD"))

    def test_money_str_is_human(self):
        self.assertEqual(str(domain.Money(1500)), "$15.00")

    def test_product_repr_has_fields(self):
        r = repr(domain.Product("A-001", "Widget", 999))
        self.assertIn("A-001", r)
        self.assertIn("999", r)

    def test_product_str(self):
        self.assertIn("A-001", str(domain.Product("A-001", "Widget", 999)))


if __name__ == "__main__":
    unittest.main()
