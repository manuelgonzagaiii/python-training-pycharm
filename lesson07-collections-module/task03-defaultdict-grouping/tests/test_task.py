"""Check for task03-defaultdict-grouping.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestDefaultdictGrouping(unittest.TestCase):
    def test_group_by_category(self):
        cat = catalog.seed_catalog()
        groups = catalog.group_by_category_dd(cat)
        self.assertEqual(set(groups), {"A", "B"})
        self.assertEqual(len(groups["A"]), 2)
        self.assertEqual(len(groups["B"]), 1)

    def test_group_returns_plain_dict(self):
        groups = catalog.group_by_category_dd(catalog.seed_catalog())
        self.assertEqual(type(groups), dict)  # converted, not a leaked defaultdict

    def test_tag_to_skus_inverts(self):
        tags = {"A-001": {"new", "sale"}, "A-002": {"sale"}}
        inv = catalog.tag_to_skus(tags)
        self.assertEqual(inv["sale"], {"A-001", "A-002"})
        self.assertEqual(inv["new"], {"A-001"})


if __name__ == "__main__":
    unittest.main()
