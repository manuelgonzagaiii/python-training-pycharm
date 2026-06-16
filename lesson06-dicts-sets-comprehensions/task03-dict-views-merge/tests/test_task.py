"""Check for task03-dict-views-merge.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestMerge(unittest.TestCase):
    def test_overrides_win_on_conflict(self):
        base = {"A-1": ("A-1", "Old", 100, 1)}
        over = {"A-1": ("A-1", "New", 200, 2)}
        self.assertEqual(catalog.apply_overrides(base, over)["A-1"], ("A-1", "New", 200, 2))

    def test_nonoverlapping_keys_survive(self):
        merged = catalog.apply_overrides({"A": ("A", "x", 1, 1)}, {"B": ("B", "y", 1, 1)})
        self.assertIn("A", merged)
        self.assertIn("B", merged)

    def test_base_not_mutated(self):
        base = {"A": ("A", "x", 1, 1)}
        catalog.apply_overrides(base, {"A": ("A", "z", 1, 1)})
        self.assertEqual(base["A"], ("A", "x", 1, 1))


if __name__ == "__main__":
    unittest.main()
