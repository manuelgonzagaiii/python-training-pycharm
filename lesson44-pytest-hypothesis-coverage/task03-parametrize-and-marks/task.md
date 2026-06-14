# Parametrization, marks & custom markers

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 44.3 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Replace subTest tables with @pytest.mark.parametrize and readable ids
- Mark individual parametrized cases as xfail/skip with pytest.param
- Define and register custom markers (e.g. slow, integration) and select them with -m
- Combine stacked parametrize to build an input matrix

## Python features introduced
`@pytest.mark.parametrize (single and stacked / matrix)`, `parametrize ids and pytest.param with marks (xfail/skip per-case)`, `@pytest.mark.skip / skipif / xfail`, `custom markers registered in pyproject ([tool.pytest.ini_options] markers)`, `running marker selections with pytest -m`, `@pytest.mark.parametrize at class and module level`

## MiniERP increment
Convert the invoicing total table and the inventory edge cases to @pytest.mark.parametrize with descriptive ids, mark a couple of known-hard rounding cases xfail, and register custom 'slow' and 'integration' markers in pyproject — tagging the export round-trip and full service tests so CI can run fast vs full subsets.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import pytest

@pytest.mark.parametrize('qty,price,tax,expected', [
    pytest.param(1, '10.00', '0.10', '11.00', id='single-taxed'),
    pytest.param(3, '5.00', '0.00', '15.00', id='multi-untaxed'),
    pytest.param(7, '0.10', '0.07', '0.75', marks=pytest.mark.xfail(reason='rounding'), id='penny-rounding'),
])
def test_line_total(qty, price, tax, expected):
    ...

- **Test focus:** Checks confirm parametrize replaces at least one subTest table, that ids and a per-case xfail/skip are used, and that custom markers are registered in pyproject and applied to real tests selectable via -m.

</div>
