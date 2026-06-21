"""Check for task06-running-total-nonlocal-global.

Grading policy: validity, not wording.
"""

import unittest

import rules


class TestScope(unittest.TestCase):
    def test_running_total_accumulates(self):
        add = rules.make_running_total()
        self.assertEqual(add(10), 10)
        self.assertEqual(add(5), 15)
        self.assertEqual(add(0), 15)

    def test_independent_counters(self):
        a = rules.make_running_total()
        b = rules.make_running_total()
        a(100)
        self.assertEqual(b(3), 3)   # b is not affected by a

    def test_record_pricing_call_increments(self):
        first = rules.record_pricing_call()
        second = rules.record_pricing_call()
        self.assertEqual(second, first + 1)


if __name__ == "__main__":
    unittest.main()
