"""Check for stage 4: aliasing vs copying.

Grading policy: validity, not wording. We check that the snapshot is an
independent list with equal contents.
"""

import unittest

import catalog


class TestSnapshot(unittest.TestCase):
    def test_snapshot_is_a_distinct_object(self):
        cat = catalog.seed_catalog()
        snap = catalog.snapshot_catalog(cat)
        self.assertIsNot(snap, cat, "snapshot must be a new list, not the same object")
        self.assertEqual(snap, cat, "but with equal contents")

    def test_mutating_snapshot_leaves_source_unchanged(self):
        cat = catalog.seed_catalog()
        n = len(cat)
        snap = catalog.snapshot_catalog(cat)
        snap.append(catalog.make_product("Z-9", "New", 100, 1))
        self.assertEqual(len(cat), n, "appending to the snapshot must not grow the source")


if __name__ == "__main__":
    unittest.main()
