import unittest

# TODO(author): replace with real checks.
# Test focus: Verify the trap/flag machinery end to end. (1) parse_money: valid strings quantize to 2dp ('19.5' -> Decimal('19.50')); invalid strings ('twelve', '') raise ValueError (not a bare InvalidOperation leaking out). (2) split_payment: an exact case ('100.00', 4) returns four equal Decimal('25.00') shares; an inexact case ('100.00', 3) returns ['33.34','33.33','33.33']; assert across several totals/parts (incl. '9.99'/2, '0.10'/3) that sum(shares) == total EXACTLY and len(shares) == parts and every share is cent-quantized. (3) had_rounding: True for ('100.00', 3) and False for ('100.00', 4). (4) Isolation check: call getcontext().clear_flags(), invoke had_rounding/split_payment, and assert getcontext().flags[Inexact] is still False afterward — proving localcontext() did not leak signal flags into the global context. Optionally assert that an exact split_payment did not need the remainder fallback by checking the shares are all identical.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
