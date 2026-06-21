"""Check for task08-bytes-protocol-money.

Grading policy: validity, not wording.
"""

import unittest

import domain


class TestMoneyBytes(unittest.TestCase):
    def test_roundtrip(self):
        m = domain.Money(1599, "USD")
        self.assertEqual(domain.Money.from_bytes(bytes(m)), m)

    def test_fixed_12_bytes(self):
        self.assertEqual(len(bytes(domain.Money(1500))), 12)

    def test_negative_and_other_currency_roundtrip(self):
        m = domain.Money(-2500, "EUR")
        self.assertEqual(domain.Money.from_bytes(bytes(m)), m)


if __name__ == "__main__":
    unittest.main()
