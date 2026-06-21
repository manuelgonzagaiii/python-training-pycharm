"""Check for task04-stock-check-while.

Grading policy: validity, not wording.
"""

import unittest

import inventory

class TestReserveUnits(unittest.TestCase):
    def test_full_reservation(self):
        self.assertEqual(inventory.reserve_units(100, 35), 35)

    def test_partial_when_short(self):
        self.assertEqual(inventory.reserve_units(25, 100), 25)

    def test_nothing_to_reserve(self):
        self.assertEqual(inventory.reserve_units(0, 10), 0)
        self.assertEqual(inventory.reserve_units(100, 0), 0)

    def test_never_over_reserves(self):
        self.assertLessEqual(inventory.reserve_units(100, 7), 100)
        self.assertEqual(inventory.reserve_units(100, 7), 7)


if __name__ == "__main__":
    unittest.main()
