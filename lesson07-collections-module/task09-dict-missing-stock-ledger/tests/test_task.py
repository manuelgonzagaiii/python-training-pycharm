import unittest

# TODO(author): replace with real checks.
# Test focus: Verify __missing__ semantics and the ERP behaviour, not just the happy path. Tests: (1) a fresh StockLedger()[ 'SKU-NEW' ] returns 0 AND inserts the key (assert 'SKU-NEW' in ledger afterward, len grows) — proving auto-populate. (2) ledger['X'] += 3 then += 2 yields 5 starting from empty (no pre-seed). (3) .get('UNSEEN') returns None and .get('UNSEEN', -1) returns -1 WITHOUT inserting the key (len unchanged) — proving .get bypasses __missing__. (4) 'UNSEEN' in ledger is False and does NOT insert — proving __contains__/in bypasses __missing__. (5) apply_movements([('A',10),('B',5),('A',-3),('C',0)]) == {'A':7,'B':5,'C':0}; an empty iterable yields an empty ledger. (6) confirm StockLedger is a dict subclass (isinstance(ledger, dict)) and behaves identically to defaultdict(int) on the same movement stream (compare against collections.defaultdict(int) as an oracle). (7) reading a present key never calls __missing__ (set ledger['P']=9; assert ledger['P']==9 and len unchanged).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
