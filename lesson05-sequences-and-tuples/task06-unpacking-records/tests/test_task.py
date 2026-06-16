"""Check for stage 6: unpacking records and starred targets.

Grading policy: validity, not wording. We check the unpacked, formatted label
and the head/tail split.
"""

import unittest

import catalog


class TestUnpacking(unittest.TestCase):
    def test_describe_includes_all_fields(self):
        s = catalog.describe(catalog.make_product("A-001", "Widget", 999, 5))
        self.assertIn("A-001", s)
        self.assertIn("Widget", s)
        self.assertIn("9.99", s)   # 999 cents formatted as dollars
        self.assertIn("5", s)      # qty

    def test_describe_formats_cents_exactly(self):
        self.assertIn("2.50", catalog.describe(catalog.make_product("X", "Y", 250, 1)))
        self.assertIn("14.99", catalog.describe(catalog.make_product("X", "Y", 1499, 1)))

    def test_split_featured_head_and_tail(self):
        cat = catalog.seed_catalog()
        featured, rest = catalog.split_featured(cat)
        self.assertEqual(featured, cat[0])
        self.assertEqual(rest, cat[1:])
        self.assertIsInstance(rest, list, "the starred target collects into a list")


if __name__ == "__main__":
    unittest.main()
