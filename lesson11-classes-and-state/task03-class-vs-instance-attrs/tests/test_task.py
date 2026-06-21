"""Check for task03-class-vs-instance-attrs.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestClassAttrs(unittest.TestCase):
    def test_currency_is_class_level(self):
        self.assertEqual(domain.Product.CURRENCY, "USD")
        p = domain.Product("A", "W", 1)
        self.assertEqual(p.CURRENCY, "USD")  # instances see the class attribute

    def test_currency_shared_across_instances(self):
        a = domain.Product("A", "W", 1)
        b = domain.Product("B", "X", 2)
        self.assertEqual(a.CURRENCY, b.CURRENCY)

    def test_tax_rate_constant_exists(self):
        self.assertEqual(domain.Product.DEFAULT_TAX_RATE_BPS, 0)


if __name__ == "__main__":
    unittest.main()
