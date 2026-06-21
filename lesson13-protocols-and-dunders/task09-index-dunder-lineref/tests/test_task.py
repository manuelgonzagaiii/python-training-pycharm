"""Check for task09-index-dunder-lineref.

Grading policy: validity, not wording.
"""

import unittest

import domain


import operator


class TestLineRef(unittest.TestCase):
    def test_operator_index(self):
        self.assertEqual(operator.index(domain.LineRef(5)), 5)

    def test_as_list_index(self):
        self.assertEqual([10, 20, 30, 40][domain.LineRef(2)], 30)

    def test_in_range(self):
        self.assertEqual(list(range(domain.LineRef(1), domain.LineRef(4))), [1, 2, 3])

    def test_rejects_zero(self):
        with self.assertRaises(ValueError):
            domain.LineRef(0)


if __name__ == "__main__":
    unittest.main()
