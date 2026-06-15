"""Check for stage 3: peek under the hood with dis.

Grading policy: we grade the maths, not the implementation. Any
correct way to compute quantity times price passes, including price times quantity.
We deliberately do NOT check the bytecode itself: disassembly output changes between
Python versions and there is more than one valid way to write a multiplication, so
grading on it would reject correct answers.
"""

import unittest

from bytecode_demo import line_total


class TestLineTotal(unittest.TestCase):
    def test_basic_products(self):
        self.assertEqual(line_total(3, 5), 15)
        self.assertEqual(line_total(4, 3), 12)
        self.assertEqual(line_total(1, 99), 99)

    def test_zero_quantity(self):
        self.assertEqual(line_total(0, 9), 0, "Zero items should total zero.")

    def test_non_integer_price(self):
        self.assertEqual(line_total(2, 2.5), 5.0, "A quantity of 2 at 2.5 each is 5.0.")

    def test_any_correct_order_is_accepted(self):
        # quantity * price and price * quantity are both valid; both must pass.
        self.assertEqual(line_total(6, 7), line_total(7, 6))


if __name__ == "__main__":
    unittest.main()
