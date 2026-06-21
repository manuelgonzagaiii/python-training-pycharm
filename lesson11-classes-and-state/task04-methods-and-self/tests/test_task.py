"""Check for task04-methods-and-self.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestPriceDisplay(unittest.TestCase):
    def test_dollars_and_cents(self):
        self.assertEqual(domain.Product("A", "W", 1500).price_display(), "$15.00")
        self.assertEqual(domain.Product("A", "W", 999).price_display(), "$9.99")
        self.assertEqual(domain.Product("A", "W", 5).price_display(), "$0.05")


if __name__ == "__main__":
    unittest.main()
