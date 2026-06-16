"""Check for task04-tags-as-sets.

Grading policy: validity, not wording.
"""

import unittest

import catalog


TAGS = {"A": {"new", "sale"}, "B": {"sale"}, "C": {"clearance"}}


class TestTagSets(unittest.TestCase):
    def test_all_tags_superset(self):
        self.assertEqual(catalog.products_with_all_tags(TAGS, {"sale"}), {"A", "B"})
        self.assertEqual(catalog.products_with_all_tags(TAGS, {"new", "sale"}), {"A"})

    def test_any_tags_intersection(self):
        self.assertEqual(catalog.products_with_any_tags(TAGS, {"clearance", "new"}), {"A", "C"})

    def test_results_are_sets(self):
        self.assertIsInstance(catalog.products_with_all_tags(TAGS, {"sale"}), set)
        self.assertIsInstance(catalog.products_with_any_tags(TAGS, {"sale"}), set)


if __name__ == "__main__":
    unittest.main()
