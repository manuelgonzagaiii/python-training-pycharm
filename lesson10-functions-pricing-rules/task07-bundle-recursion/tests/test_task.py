"""Check for task07-bundle-recursion.

Grading policy: validity, not wording.
"""

import unittest

import rules


CATALOG = {
    "KIT": [("A", 2), ("B", 1)],
    "B": [("C", 3)],
}


class TestExpandBundle(unittest.TestCase):
    def test_leaf_returns_itself(self):
        self.assertEqual(rules.expand_bundle(CATALOG, "A", 5), [("A", 5)])

    def test_nested_bundle_flattens(self):
        result = dict(rules.expand_bundle(CATALOG, "KIT", 1))
        self.assertEqual(result, {"A": 2, "C": 3})

    def test_quantities_scale(self):
        result = dict(rules.expand_bundle(CATALOG, "KIT", 2))
        self.assertEqual(result, {"A": 4, "C": 6})

    def test_self_referencing_bundle_is_caught(self):
        # a bundle that contains itself would recurse forever; expansion must stop
        with self.assertRaises(RecursionError):
            rules.expand_bundle({"X": [("X", 1)]}, "X", 1)


if __name__ == "__main__":
    unittest.main()
