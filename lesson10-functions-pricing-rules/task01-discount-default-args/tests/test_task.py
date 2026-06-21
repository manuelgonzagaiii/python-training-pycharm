"""Check for task01-discount-default-args.

Grading policy: validity, not wording.
"""

import unittest

import rules


class TestDefaults(unittest.TestCase):
    def test_default_is_no_discount(self):
        self.assertEqual(rules.apply_percent(1000), 1000)

    def test_percent_applied_and_rounded(self):
        self.assertEqual(rules.apply_percent(1000, 10), 900)
        self.assertEqual(rules.apply_percent(999, 5), 949)   # 49.95 -> 50 off

    def test_accumulate_fresh_list_each_call(self):
        self.assertEqual(rules.accumulate_discounts(10), [10])
        self.assertEqual(rules.accumulate_discounts(20), [20])  # NOT [10, 20]

    def test_accumulate_uses_given_list(self):
        self.assertEqual(rules.accumulate_discounts(20, [10]), [10, 20])


if __name__ == "__main__":
    unittest.main()
