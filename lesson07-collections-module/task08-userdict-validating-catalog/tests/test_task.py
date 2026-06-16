"""Check for task08-userdict-validating-catalog.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestValidatingCatalog(unittest.TestCase):
    def test_valid_insert(self):
        c = catalog.Catalog()
        p = catalog.make_product("A-001", "Widget", 999, 5)
        c["A-001"] = p
        self.assertEqual(c["A-001"], p)
        self.assertEqual(len(c), 1)

    def test_rejects_empty_sku(self):
        c = catalog.Catalog()
        with self.assertRaises(ValueError):
            c[""] = catalog.make_product("X", "Y", 1, 1)

    def test_rejects_negative_price(self):
        c = catalog.Catalog()
        with self.assertRaises(ValueError):
            c["A-001"] = catalog.make_product("A-001", "Widget", -1, 5)

    def test_rejects_negative_qty(self):
        c = catalog.Catalog()
        with self.assertRaises(ValueError):
            c["A-001"] = catalog.make_product("A-001", "Widget", 999, -5)

    def test_behaves_like_dict(self):
        c = catalog.Catalog()
        c["A-001"] = catalog.make_product("A-001", "Widget", 999, 5)
        self.assertIn("A-001", c)
        self.assertEqual(list(c), ["A-001"])


if __name__ == "__main__":
    unittest.main()
