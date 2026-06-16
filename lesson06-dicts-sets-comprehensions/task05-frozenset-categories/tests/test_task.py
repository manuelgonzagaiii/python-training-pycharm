"""Check for task05-frozenset-categories.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestFrozenset(unittest.TestCase):
    def test_set_of_frozensets(self):
        combos = catalog.catalog_tag_combinations({"A": {"new", "sale"}, "C": {"clearance"}})
        self.assertIsInstance(combos, set)
        for c in combos:
            self.assertIsInstance(c, frozenset)

    def test_identical_combinations_collapse(self):
        combos = catalog.catalog_tag_combinations({"A": {"new", "sale"}, "B": {"sale", "new"}})
        self.assertEqual(len(combos), 1)

    def test_usable_as_set_element(self):
        combos = catalog.catalog_tag_combinations({"A": {"x"}})
        self.assertIn(frozenset({"x"}), combos)


if __name__ == "__main__":
    unittest.main()
