"""Check for task04-lambda-sort-keys.

Grading policy: validity, not wording.
"""

import unittest

import rules


LINES = [("A", 100, 2), ("B", 100, 5), ("C", 300, 1)]  # totals 200, 500, 300


class TestHigherOrder(unittest.TestCase):
    def test_rank_by_total_desc(self):
        self.assertEqual([row[0] for row in rules.rank_lines(LINES)], ["B", "C", "A"])

    def test_cheapest_and_dearest(self):
        self.assertEqual(rules.cheapest_line(LINES)[0], "A")
        self.assertEqual(rules.dearest_line(LINES)[0], "B")

    def test_line_numbers_one_based(self):
        numbered = rules.line_numbers(LINES)
        self.assertEqual(numbered[0][0], 1)
        self.assertEqual(numbered[-1][0], len(LINES))

    def test_any_over_limit(self):
        self.assertTrue(rules.any_over_limit(LINES, 400))
        self.assertFalse(rules.any_over_limit(LINES, 1000))


if __name__ == "__main__":
    unittest.main()
