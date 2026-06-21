"""Check for task05-invoice-total.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestInvoiceTotal(unittest.TestCase):
    def setUp(self):
        domain.Product._instances.clear()

    def test_total_sums_lines(self):
        p1 = domain.Product("A", "x", 1000)
        p2 = domain.Product("B", "y", 250)
        inv = domain.Invoice([domain.LineItem(p1, 2), domain.LineItem(p2, 4)])
        self.assertIsInstance(inv.total, domain.Money)
        self.assertEqual(inv.total.cents, 3000)

    def test_empty_total_is_money_zero(self):
        self.assertIsInstance(domain.Invoice().total, domain.Money)
        self.assertEqual(domain.Invoice().total.cents, 0)

    def test_str_renders_lines_and_total(self):
        p = domain.Product("A", "Widget", 500)
        s = str(domain.Invoice([domain.LineItem(p, 2)]))
        self.assertIn("Widget", s)
        self.assertIn("10.00", s)


if __name__ == "__main__":
    unittest.main()
