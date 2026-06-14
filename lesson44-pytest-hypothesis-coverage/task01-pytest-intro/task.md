# From unittest to pytest: plain assert & rich introspection

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 44.1 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Run the existing unittest suite unchanged under pytest
- Rewrite tests as plain functions using assert, and read pytest's rich failure introspection
- Replace assertRaises/assertAlmostEqual with pytest.raises/pytest.approx
- Select and re-run tests with -k, -x and --lf
- Configure pytest once in pyproject.toml

## Python features introduced
`pytest as a test runner over existing unittest TestCases`, `plain assert statements with pytest assertion rewriting`, `pytest.raises context manager`, `pytest.approx for float/Decimal comparison`, `function-style tests (no class required)`, `running pytest -q, -k, -x, --lf`, `pyproject.toml [tool.pytest.ini_options] (testpaths, addopts)`

## MiniERP increment
Add a pyproject.toml [tool.pytest.ini_options] section (testpaths=['tests'], strict markers) and add tests/test_pricing_pytest.py rewriting the invoicing/pricing checks as plain pytest functions with assert, pytest.raises and pytest.approx — proving the existing domain code passes under the new runner.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import pytest
from erp.sales import Invoice, money

def test_discount_applied():
    inv = Invoice(customer_id=1)
    inv.add_line('SKU-1', qty=2, unit_price=money('10.00'))
    inv.apply_discount(0.10)
    assert inv.total() == pytest.approx(money('18.00'))

def test_negative_qty_rejected():
    with pytest.raises(ValueError):
        Invoice(customer_id=1).add_line('SKU-1', qty=-1, unit_price=money('1.00'))

- **Test focus:** Checks confirm pyproject configures pytest, that new tests use plain assert (not self.assert*), and that pytest.raises and pytest.approx are each used against real domain behavior, with the whole suite green under `pytest`.

</div>
