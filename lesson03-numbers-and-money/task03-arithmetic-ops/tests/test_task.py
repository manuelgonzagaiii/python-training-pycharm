"""Check for stage 3: quantity math with divmod, // and %.

Grading policy: we verify the arithmetic is correct, not how you wrote it. Any
implementation that returns the right packing and split values passes; the
function bodies are your free choice.
"""

import unittest

import money


class TestQuantityMath(unittest.TestCase):
    def test_units_to_cases_basic(self):
        self.assertEqual(money.units_to_cases(27, 12), (2, 3))

    def test_units_to_cases_exact_fit(self):
        self.assertEqual(money.units_to_cases(24, 12), (2, 0))

    def test_units_to_cases_under_one_case(self):
        self.assertEqual(money.units_to_cases(5, 12), (0, 5))

    def test_units_to_cases_always_reconstructs_total(self):
        for units, per_case in [(100, 7), (0, 3), (13, 1), (12, 12)]:
            full, loose = money.units_to_cases(units, per_case)
            self.assertEqual(full * per_case + loose, units)
            self.assertTrue(0 <= loose < per_case, "loose units must be a valid remainder")

    def test_split_evenly_always_reconstructs_total(self):
        for total, parts in [(100, 3), (10, 2), (7, 7), (0, 4), (5, 1)]:
            base, remainder = money.split_evenly(total, parts)
            self.assertEqual(base * parts + remainder, total, "shares must add back to total")
            self.assertTrue(0 <= remainder < parts, "remainder must be smaller than parts")

    def test_split_evenly_single_part_gets_everything(self):
        self.assertEqual(money.split_evenly(50, 1), (50, 0))


if __name__ == "__main__":
    unittest.main()
