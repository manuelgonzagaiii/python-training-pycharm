"""Check for task07-dict-set-gen-comprehensions.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestComprehensions(unittest.TestCase):
    def test_price_index(self):
        cat = catalog.seed_catalog()
        self.assertEqual(catalog.price_index(cat), {p[0]: p[2] for p in cat})

    def test_all_tags_union(self):
        tags = {"A": {"new", "sale"}, "B": {"sale", "clearance"}}
        self.assertEqual(catalog.all_tags(tags), {"new", "sale", "clearance"})

    def test_inventory_value(self):
        cat = catalog.seed_catalog()
        self.assertEqual(catalog.inventory_value(cat), sum(p[2] * p[3] for p in cat))

    def test_inventory_value_skips_empty_lines(self):
        # an out-of-stock line contributes nothing to the total
        cat = [catalog.make_product("A", "x", 100, 0),   # qty 0 -> line value 0
               catalog.make_product("B", "y", 250, 4)]   # 1000
        self.assertEqual(catalog.inventory_value(cat), 1000)


if __name__ == "__main__":
    unittest.main()
