"""Check for task01-eq-and-hash.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestEqHash(unittest.TestCase):
    def setUp(self):
        domain.Product._instances.clear()

    def test_money_equality_by_value(self):
        self.assertEqual(domain.Money(1500, "USD"), domain.Money(1500, "USD"))
        self.assertNotEqual(domain.Money(1500, "USD"), domain.Money(1500, "EUR"))
        self.assertNotEqual(domain.Money(1500), domain.Money(1600))

    def test_money_hashable(self):
        s = {domain.Money(1500), domain.Money(1500), domain.Money(250)}
        self.assertEqual(len(s), 2)
        self.assertEqual({domain.Money(1500): "a"}[domain.Money(1500)], "a")

    def test_product_equality_by_sku(self):
        a = domain.Product("A-1", "Widget", 100)
        self.assertEqual(a, domain.Product("A-1", "Other", 999))
        self.assertNotEqual(a, domain.Product("B-2", "Widget", 100))

    def test_not_equal_to_other_type(self):
        self.assertNotEqual(domain.Money(100), 100)
        self.assertNotEqual(domain.Product("A-1", "W", 1), "A-1")


if __name__ == "__main__":
    unittest.main()
