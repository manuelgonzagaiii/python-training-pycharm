"""Check for task09-dict-missing-stock-ledger.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestStockLedgerMissing(unittest.TestCase):
    def test_missing_key_reads_zero(self):
        ledger = catalog.StockLedger()
        self.assertEqual(ledger["new-sku"], 0)

    def test_missing_key_is_inserted(self):
        ledger = catalog.StockLedger()
        _ = ledger["new-sku"]
        self.assertIn("new-sku", ledger)  # reading a missing key inserted it

    def test_increment_first_time_sku(self):
        ledger = catalog.StockLedger()
        ledger["A-001"] += 5
        ledger["A-001"] += 3
        self.assertEqual(ledger["A-001"], 8)

    def test_existing_value_preserved(self):
        ledger = catalog.StockLedger()
        ledger["A-001"] = 10
        self.assertEqual(ledger["A-001"], 10)


if __name__ == "__main__":
    unittest.main()
