"""Check for task02-dict-get-setdefault.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestSafeAccess(unittest.TestCase):
    def test_find_known(self):
        idx = catalog.index_by_sku(catalog.seed_catalog())
        self.assertEqual(catalog.find(idx, "A-001"), idx["A-001"])

    def test_find_unknown_is_none(self):
        idx = catalog.index_by_sku(catalog.seed_catalog())
        self.assertIsNone(catalog.find(idx, "ZZZ"))

    def test_group_by_category(self):
        g = catalog.group_by_category(catalog.seed_catalog())
        self.assertIsInstance(g["A"], list)
        self.assertEqual({p[0] for p in g["A"]}, {"A-001", "A-002"})
        self.assertEqual({p[0] for p in g["B"]}, {"B-010"})


if __name__ == "__main__":
    unittest.main()
