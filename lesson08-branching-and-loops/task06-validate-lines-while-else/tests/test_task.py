"""Check for task06-validate-lines-while-else.

Grading policy: validity, not wording.
"""

import unittest

import pricing

class TestAllLinesValid(unittest.TestCase):
    def test_all_valid(self):
        self.assertTrue(pricing.all_lines_valid([("A", 100, 1), ("B", 0, 5)]))

    def test_empty_is_valid(self):
        self.assertTrue(pricing.all_lines_valid([]))

    def test_non_positive_qty_invalid(self):
        self.assertFalse(pricing.all_lines_valid([("A", 100, 1), ("B", 100, 0)]))

    def test_negative_price_invalid(self):
        self.assertFalse(pricing.all_lines_valid([("A", -1, 3)]))


if __name__ == "__main__":
    unittest.main()
