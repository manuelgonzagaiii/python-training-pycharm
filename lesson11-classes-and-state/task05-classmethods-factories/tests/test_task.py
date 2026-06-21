"""Check for task05-classmethods-factories.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestFactories(unittest.TestCase):
    def test_from_row(self):
        p = domain.Product.from_row(("A-001", "Widget", 999))
        self.assertIsInstance(p, domain.Product)
        self.assertEqual((p.sku, p.name, p.price_cents), ("A-001", "Widget", 999))

    def test_from_dict(self):
        p = domain.Product.from_dict({"sku": "B-010", "name": "Gizmo", "price_cents": 250})
        self.assertEqual((p.sku, p.name, p.price_cents), ("B-010", "Gizmo", 250))


if __name__ == "__main__":
    unittest.main()
