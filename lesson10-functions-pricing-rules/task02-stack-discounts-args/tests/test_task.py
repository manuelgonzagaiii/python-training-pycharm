"""Check for task02-stack-discounts-args.

Grading policy: validity, not wording.
"""

import unittest

import rules


class TestStackDiscounts(unittest.TestCase):
    def test_sequential_percents(self):
        self.assertEqual(rules.stack_discounts(1000, 10, 10), 810)  # 1000->900->810

    def test_no_percents_unchanged(self):
        self.assertEqual(rules.stack_discounts(1000), 1000)

    def test_clamp_floor_option(self):
        self.assertEqual(rules.stack_discounts(100, 200, clamp_floor=True), 0)

    def test_without_clamp_can_go_negative(self):
        self.assertLess(rules.stack_discounts(100, 200), 0)


if __name__ == "__main__":
    unittest.main()
