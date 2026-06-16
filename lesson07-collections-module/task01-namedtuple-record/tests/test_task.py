"""Check for task01-namedtuple-record.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestNamedTupleRecord(unittest.TestCase):
    def test_make_product_named_fields(self):
        p = catalog.make_product("A-001", "Widget", 999, 5)
        self.assertEqual(p.sku, "A-001")
        self.assertEqual(p.name, "Widget")
        self.assertEqual(p.price_cents, 999)
        self.assertEqual(p.qty, 5)

    def test_record_is_still_a_tuple(self):
        p = catalog.make_product("A-001", "Widget", 999, 5)
        self.assertIsInstance(p, tuple)
        self.assertEqual(p[0], "A-001")
        self.assertEqual(tuple(p), ("A-001", "Widget", 999, 5))

    def test_reprice_changes_only_price(self):
        p = catalog.make_product("A-001", "Widget", 999, 5)
        q = catalog.reprice(p, 1299)
        self.assertEqual(q.price_cents, 1299)
        self.assertEqual(q.sku, p.sku)
        self.assertEqual(q.qty, p.qty)
        self.assertEqual(p.price_cents, 999)  # original record unchanged


if __name__ == "__main__":
    unittest.main()
