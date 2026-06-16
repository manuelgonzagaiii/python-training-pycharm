"""Check for stage 2: a product as a tuple record.

Grading policy: validity, not wording. We check the shape, field order, and
immutability of the record.
"""

import unittest

import catalog


class TestProductRecord(unittest.TestCase):
    def test_is_a_four_tuple(self):
        p = catalog.make_product("A-1", "Widget", 999, 5)
        self.assertIsInstance(p, tuple)
        self.assertEqual(len(p), 4)

    def test_field_order(self):
        p = catalog.make_product("A-1", "Widget", 999, 5)
        self.assertEqual(p, ("A-1", "Widget", 999, 5))
        self.assertEqual(p[0], "A-1")
        self.assertEqual(p[2], 999)

    def test_record_is_immutable(self):
        p = catalog.make_product("A-1", "Widget", 999, 5)
        with self.assertRaises(TypeError):
            p[0] = "B-2"


if __name__ == "__main__":
    unittest.main()
