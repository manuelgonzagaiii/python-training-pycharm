"""Check for task03-arithmetic-operators.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestArithmetic(unittest.TestCase):
    def test_add_and_sub(self):
        self.assertEqual((domain.Money(1500) + domain.Money(250)).cents, 1750)
        self.assertEqual((domain.Money(1500) - domain.Money(250)).cents, 1250)

    def test_mul(self):
        self.assertEqual((domain.Money(250) * 3).cents, 750)

    def test_sum_uses_radd(self):
        total = sum([domain.Money(100), domain.Money(250), domain.Money(50)])
        self.assertEqual(total.cents, 400)

    def test_returns_new_instance(self):
        a = domain.Money(100)
        b = a + domain.Money(50)
        self.assertEqual(a.cents, 100)
        self.assertIsNot(a, b)

    def test_cross_currency_add_raises(self):
        with self.assertRaises(ValueError):
            domain.Money(100, "USD") + domain.Money(100, "EUR")


if __name__ == "__main__":
    unittest.main()
