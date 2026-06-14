# The assertion vocabulary, setUp/tearDown & subTest

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 43.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Remove duplicated setup with setUp/tearDown and class-level fixtures
- Guarantee cleanup deterministically with addCleanup
- Choose the most precise assertion instead of bare assertTrue
- Drive many input/expected pairs through one test with subTest so a single failure does not hide the rest
- Assert on emitted log records with assertLogs

## Python features introduced
`unittest setUp / tearDown / setUpClass / tearDownClass / addCleanup`, `assertion family: assertIn, assertIsNone, assertIsInstance, assertAlmostEqual, assertCountEqual, assertDictEqual, assertRaisesRegex`, `TestCase.subTest for table-driven cases`, `self.assertLogs for asserting on logging`, `Decimal for money assertions`

## MiniERP increment
Add tests/test_invoicing.py covering invoice totals, line items, tax and discounts. A setUp builds a fresh customer + product catalog for each test; a subTest loop validates a table of (quantity, unit_price, tax_rate) -> expected_total cases using Decimal and assertAlmostEqual, and assertLogs verifies the audit-log entry written when an invoice is finalized.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import unittest
from decimal import Decimal
from erp.sales import Invoice

class InvoiceTotalTests(unittest.TestCase):
    def setUp(self):
        self.invoice = Invoice(customer_id=1)
    def test_totals_table(self):
        cases = [(1, '10.00', '0.10'), (3, '5.00', '0.00')]
        for qty, price, tax in cases:
            with self.subTest(qty=qty, price=price, tax=tax):
                ...  # TODO compute and assert expected total

- **Test focus:** Checks verify setUp creates per-test state (no leakage between tests), that subTest is used for the table, and that at least one assertLogs/assertAlmostEqual/assertRaisesRegex is exercised against the real invoicing code.

</div>
