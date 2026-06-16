"""Check for stage 5: slicing for pagination and recent products.

Grading policy: validity, not wording. We check the returned slices, including
the edge cases (page past the end; n larger than the catalog).
"""

import unittest

import catalog


def _cat(n):
    return [catalog.make_product(f"P{i}", "X", 100, 1) for i in range(n)]


class TestSlicing(unittest.TestCase):
    def test_page_in_range(self):
        cat = _cat(10)
        self.assertEqual(catalog.page(cat, 1, 3), cat[0:3])
        self.assertEqual(catalog.page(cat, 2, 3), cat[3:6])

    def test_page_past_the_end_is_empty(self):
        cat = _cat(5)
        self.assertEqual(catalog.page(cat, 99, 3), [])  # clamps, no IndexError

    def test_recent_is_newest_first(self):
        cat = _cat(5)
        self.assertEqual(catalog.recent(cat, 2), [cat[4], cat[3]])

    def test_recent_n_larger_than_catalog(self):
        cat = _cat(3)
        self.assertEqual(catalog.recent(cat, 10), [cat[2], cat[1], cat[0]])


if __name__ == "__main__":
    unittest.main()
