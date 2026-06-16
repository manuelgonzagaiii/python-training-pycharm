"""Check for task07-spread-unpacking-calls.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestSpreadUnpacking(unittest.TestCase):
    def test_merge_flattens_in_order(self):
        a = [catalog.make_product("A-001", "W", 1, 1)]
        b = [catalog.make_product("B-001", "G", 2, 2),
             catalog.make_product("B-002", "Z", 3, 3)]
        self.assertEqual(catalog.merge_catalogs(a, b), a + b)

    def test_merge_no_args(self):
        self.assertEqual(catalog.merge_catalogs(), [])

    def test_build_product_from_fields(self):
        fields = {"sku": "A-001", "name": "Widget", "price_cents": 999, "qty": 5}
        p = catalog.build_product(**fields)
        self.assertEqual(p, catalog.make_product("A-001", "Widget", 999, 5))
        self.assertEqual(p.sku, "A-001")


if __name__ == "__main__":
    unittest.main()
