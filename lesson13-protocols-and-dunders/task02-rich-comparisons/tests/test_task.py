"""Check for task02-rich-comparisons.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestOrdering(unittest.TestCase):
    def setUp(self):
        domain.Product._instances.clear()

    def test_money_full_ordering(self):
        a, b = domain.Money(100), domain.Money(250)
        self.assertLess(a, b)
        self.assertLessEqual(a, domain.Money(100))
        self.assertGreater(b, a)
        self.assertGreaterEqual(b, domain.Money(250))

    def test_money_sorted_min_max(self):
        ms = [domain.Money(300), domain.Money(100), domain.Money(200)]
        self.assertEqual([m.cents for m in sorted(ms)], [100, 200, 300])
        self.assertEqual(min(ms).cents, 100)
        self.assertEqual(max(ms).cents, 300)

    def test_cross_currency_compare_raises(self):
        with self.assertRaises(ValueError):
            domain.Money(100, "USD") < domain.Money(100, "EUR")

    def test_product_sorts_by_price(self):
        ps = [domain.Product("A", "x", 300), domain.Product("B", "y", 100), domain.Product("C", "z", 200)]
        self.assertEqual([p.price_cents for p in sorted(ps)], [100, 200, 300])


if __name__ == "__main__":
    unittest.main()
