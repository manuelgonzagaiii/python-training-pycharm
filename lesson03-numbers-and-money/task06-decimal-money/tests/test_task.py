"""Check for stage 6: exact money with Decimal.

Grading policy: validity, not wording. We check the money contract — built from
a string it is exact, float is rejected, and rounding is half-up to two places —
so any correct implementation passes.
"""

import unittest
from decimal import Decimal

import money


class TestMoney(unittest.TestCase):
    def test_money_returns_a_decimal(self):
        self.assertIsInstance(money.money("19.99"), Decimal)

    def test_money_is_exact(self):
        # The whole point: this is True, unlike 0.1 + 0.2 == 0.3 with floats.
        self.assertEqual(money.money("0.1") + money.money("0.2"), money.money("0.3"))

    def test_money_rejects_float(self):
        with self.assertRaises(TypeError):
            money.money(0.1)

    def test_money_accepts_int(self):
        self.assertEqual(money.money(5), Decimal("5"))

    def test_round_money_rounds_half_up(self):
        self.assertEqual(money.round_money(Decimal("2.005")), Decimal("2.01"))
        self.assertEqual(money.round_money(Decimal("2.004")), Decimal("2.00"))

    def test_round_money_gives_two_places(self):
        result = money.round_money(Decimal("3"))
        self.assertEqual(result, Decimal("3.00"))
        self.assertEqual(str(result), "3.00", "amount should display with two decimals")


if __name__ == "__main__":
    unittest.main()
