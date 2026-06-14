import unittest

# TODO(author): replace with real checks.
# Test focus: Verify order_dunning_worklist produces the exact clerk priority order and that dunning_cmp obeys the 3-way contract. Concrete checks: (1) dunning_cmp returns a value <0 / ==0 / >0 (assert the sign, not an exact magnitude) for representative pairs covering each rule; (2) self-comparison dunning_cmp(x, x, today=...) == 0; (3) two invoices differing only in days_past_due order most-overdue first; (4) equal age, different Decimal balances -> larger balance first (use Decimal literals to confirm no float drift); (5) equal age and balance, one priority=True -> it comes first; (6) full equality except invoice number -> ascending number; (7) a 6-8 invoice fixture exercising all four tie-breaks at once yields one deterministic expected list of invoice numbers; (8) order_dunning_worklist must not mutate the input list (pass a list, assert it is unchanged) and must return a new list; (9) sanity check that the result equals sorted(...) using functools.cmp_to_key with the same comparator (confirms the bridge was used correctly). Antisymmetry spot-check: sign(dunning_cmp(a, b)) == -sign(dunning_cmp(b, a)).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
