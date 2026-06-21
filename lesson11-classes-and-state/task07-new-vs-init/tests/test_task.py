"""Check for task07-new-vs-init.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestInterning(unittest.TestCase):
    def setUp(self):
        domain.Product._instances.clear()

    def test_same_sku_returns_same_object(self):
        a = domain.Product("A-001", "Widget", 999)
        b = domain.Product("A-001", "Renamed", 100)
        self.assertIs(a, b)  # interned by SKU

    def test_different_sku_distinct_objects(self):
        a = domain.Product("A-001", "Widget", 999)
        c = domain.Product("B-010", "Gizmo", 250)
        self.assertIsNot(a, c)

    def test_init_still_runs(self):
        p = domain.Product("Z-9", "Thing", 42)
        self.assertEqual(p.price_cents, 42)


if __name__ == "__main__":
    unittest.main()
