"""Check for task01-dict-by-sku.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestIndex(unittest.TestCase):
    def test_maps_sku_to_record(self):
        cat = catalog.seed_catalog()
        idx = catalog.index_by_sku(cat)
        for p in cat:
            self.assertEqual(idx[p[0]], p)

    def test_preserves_insertion_order(self):
        cat = catalog.seed_catalog()
        self.assertEqual(list(catalog.index_by_sku(cat)), [p[0] for p in cat])

    def test_membership(self):
        idx = catalog.index_by_sku(catalog.seed_catalog())
        self.assertIn("A-001", idx)
        self.assertNotIn("ZZZ", idx)


if __name__ == "__main__":
    unittest.main()
