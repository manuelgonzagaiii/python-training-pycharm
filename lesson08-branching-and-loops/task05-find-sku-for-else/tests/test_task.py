"""Check for task05-find-sku-for-else.

Grading policy: validity, not wording.
"""

import unittest

import inventory

CATALOG = [
    ("A-001", "Widget", 999, 5),
    ("A-002", "Gadget", 1499, 0),
    ("B-010", "Gizmo", 250, 12),
]


class TestFindInCatalog(unittest.TestCase):
    def test_finds_existing(self):
        self.assertEqual(inventory.find_in_catalog(CATALOG, "B-010")[1], "Gizmo")

    def test_missing_raises_keyerror(self):
        with self.assertRaises(KeyError):
            inventory.find_in_catalog(CATALOG, "ZZZ")

    def test_empty_catalog_raises(self):
        with self.assertRaises(KeyError):
            inventory.find_in_catalog([], "A-001")


if __name__ == "__main__":
    unittest.main()
