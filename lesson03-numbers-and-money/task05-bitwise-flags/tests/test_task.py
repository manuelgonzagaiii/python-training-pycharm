"""Check for stage 5: product attribute bit flags.

Grading policy: validity, not wording. We check the flag contract — setting a
flag makes has_flag true, clearing makes it false, and neither disturbs the
other flags — so any correct bitwise implementation passes.
"""

import unittest

import money


class TestFlags(unittest.TestCase):
    def test_flags_are_distinct_single_bits(self):
        flags = {money.TAXABLE, money.DISCOUNTABLE, money.RETURNABLE}
        self.assertEqual(len(flags), 3, "the three flags must be distinct")
        for flag in flags:
            self.assertEqual(flag & (flag - 1), 0, "each flag should be a single bit")

    def test_set_then_has(self):
        flags = money.set_flag(0, money.TAXABLE)
        self.assertTrue(money.has_flag(flags, money.TAXABLE))
        self.assertFalse(money.has_flag(flags, money.RETURNABLE))

    def test_set_is_idempotent(self):
        once = money.set_flag(0, money.DISCOUNTABLE)
        twice = money.set_flag(once, money.DISCOUNTABLE)
        self.assertEqual(twice, once)

    def test_clear_removes_only_that_flag(self):
        flags = money.set_flag(money.set_flag(0, money.TAXABLE), money.RETURNABLE)
        flags = money.clear_flag(flags, money.TAXABLE)
        self.assertFalse(money.has_flag(flags, money.TAXABLE))
        self.assertTrue(money.has_flag(flags, money.RETURNABLE), "other flags untouched")

    def test_clear_absent_flag_is_harmless(self):
        flags = money.set_flag(0, money.TAXABLE)
        self.assertEqual(money.clear_flag(flags, money.RETURNABLE), flags)


if __name__ == "__main__":
    unittest.main()
