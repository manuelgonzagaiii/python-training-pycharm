import unittest

# TODO(author): replace with real checks.
# Test focus: Verify replace() semantics and immutability: (1) `m = Money("10.00"); m2 = m.with_amount("7.50")` returns a distinct object, `m2.amount == Decimal('7.50')`, `m2.currency == m.currency`, and `m is not m2` while `m.amount` is unchanged (original untouched). (2) `m.scaled(3).amount == Decimal('30.00')` and currency preserved. (3) replace() re-runs __post_init__: `m.with_amount("-1")` raises ValueError (negative rejected) and `m.with_amount("2.5")` is re-quantised to Decimal('2.50'). (4) Direct mutation `m.amount = Decimal('1')` raises dataclasses.FrozenInstanceError, proving why replace() is needed. (5) `line.adjusted(delta_qty=+5)` returns a new InventoryLine with quantity increased, original `line.quantity` unchanged, and `unit_price` identity preserved; `line.adjusted(new_unit_price=Money('9.99'))` swaps price and recomputes any derived total. (6) `dataclasses.replace(line, quantity=-1)` propagates the __post_init__ validation error, confirming the copy is validated, not blindly constructed.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
