"""Check for task02-product-class.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestProduct(unittest.TestCase):
    def test_attributes_set(self):
        p = domain.Product("A-001", "Widget", 999)
        self.assertEqual(p.sku, "A-001")
        self.assertEqual(p.name, "Widget")
        self.assertEqual(p.price_cents, 999)

    def test_label(self):
        p = domain.Product("A-001", "Widget", 999)
        self.assertIn("A-001", p.label())
        self.assertIn("Widget", p.label())


if __name__ == "__main__":
    unittest.main()
