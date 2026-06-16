"""Check for stage 3: the catalog as a mutable list.

Grading policy: validity, not wording. We check that add_product mutates in
place and that seed_catalog returns a list of valid records.
"""

import unittest

import catalog


class TestCatalogList(unittest.TestCase):
    def test_add_product_mutates_in_place(self):
        cat = []
        p = catalog.make_product("A-1", "Widget", 999, 5)
        before_id = id(cat)
        result = catalog.add_product(cat, p)
        self.assertIsNone(result, "add_product mutates in place; it should return None")
        self.assertEqual(id(cat), before_id, "it must be the same list object, not a copy")
        self.assertEqual(len(cat), 1)
        self.assertEqual(cat[0], p)

    def test_add_product_grows_existing_catalog(self):
        cat = catalog.seed_catalog()
        n = len(cat)
        catalog.add_product(cat, catalog.make_product("Z-9", "New", 100, 1))
        self.assertEqual(len(cat), n + 1)

    def test_seed_catalog_is_nonempty_list_of_records(self):
        cat = catalog.seed_catalog()
        self.assertIsInstance(cat, list)
        self.assertGreater(len(cat), 0)
        for p in cat:
            self.assertIsInstance(p, tuple)
            self.assertEqual(len(p), 4)


if __name__ == "__main__":
    unittest.main()
