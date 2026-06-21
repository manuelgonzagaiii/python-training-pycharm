"""Check for task06-format-protocol.

Grading policy: validity, not wording.
"""

import unittest
from decimal import Decimal

import domain


class TestMoneyFormat(unittest.TestCase):
    def test_default_spec(self):
        self.assertEqual(format(domain.Money(1500)), "$15.00")
        self.assertEqual(f"{domain.Money(1500)}", "$15.00")

    def test_full_spec(self):
        # validity, not wording: the "full" form must carry the dollars and the
        # currency code, but the exact layout is the learner's choice
        full = format(domain.Money(1500), "full")
        self.assertIn("15.00", full)
        self.assertIn("USD", full)
        self.assertNotIn("$", full)

    def test_cents_spec(self):
        self.assertEqual(format(domain.Money(1500), "cents"), "1500")

    def test_unknown_spec_raises(self):
        with self.assertRaises(ValueError):
            format(domain.Money(1500), "bogus")


if __name__ == "__main__":
    unittest.main()
