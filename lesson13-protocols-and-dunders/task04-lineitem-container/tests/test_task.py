"""Check for task04-lineitem-container.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestLineItemInvoice(unittest.TestCase):
    def setUp(self):
        domain.Product._instances.clear()
        self.p = domain.Product("A-1", "Widget", 1000)

    def test_line_total_is_money(self):
        li = domain.LineItem(self.p, 3)
        self.assertIsInstance(li.line_total, domain.Money)
        self.assertEqual(li.line_total.cents, 3000)

    def test_len_bool_iter(self):
        inv = domain.Invoice([domain.LineItem(self.p, 1), domain.LineItem(self.p, 2)])
        self.assertEqual(len(inv), 2)
        self.assertTrue(inv)
        self.assertFalse(domain.Invoice())
        self.assertEqual(len(list(inv)), 2)

    def test_getitem_and_contains(self):
        inv = domain.Invoice([domain.LineItem(self.p, 1)])
        self.assertEqual(inv[0].quantity, 1)
        self.assertIn(self.p, inv)
        self.assertNotIn(domain.Product("Z-9", "Other", 1), inv)

    def test_contains_matches_by_value_not_identity(self):
        inv = domain.Invoice([domain.LineItem(self.p, 1)])
        domain.Product._instances.clear()   # a fresh same-SKU product is now a DIFFERENT object
        twin = domain.Product(self.p.sku, "Renamed", 999)
        self.assertIsNot(twin, self.p)
        self.assertIn(twin, inv)            # membership is by SKU equality, not identity


if __name__ == "__main__":
    unittest.main()
