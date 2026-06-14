# Measuring what you test: coverage.py & a fail-under gate

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 44.5 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Measure line and branch coverage of the erp package
- Read term-missing output to find untested branches and add a test that closes a real gap
- Configure coverage in pyproject with a fail_under threshold so coverage becomes a gate
- Use # pragma: no cover deliberately and justify each exclusion

## Python features introduced
`coverage.py via coverage run -m pytest and coverage report/coverage html`, `pytest-cov: pytest --cov=erp --cov-report=term-missing`, `branch coverage (--cov-branch)`, `[tool.coverage.run]/[tool.coverage.report] in pyproject (source, omit, fail_under)`, `# pragma: no cover`, `excluding TYPE_CHECKING/__repr__ blocks`, `reading the missing-lines report to add a targeted test`

## MiniERP increment
Configure coverage for MiniERP in pyproject (source=erp, --cov-branch, fail_under), then use the term-missing report to find an untested branch in the reporting/aggregation code and add the test that covers it — raising the project over its coverage threshold and producing an HTML report artifact.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # pyproject.toml
[tool.coverage.run]
source = ['erp']
branch = true
[tool.coverage.report]
fail_under = 85
show_missing = true

# Run:  pytest --cov=erp --cov-branch --cov-report=term-missing
# Then add the test that covers the reported missing branch.

- **Test focus:** Checks confirm coverage is configured in pyproject with branch + fail_under, and that the newly added test covers the specific previously-missing branch in the reporting code (i.e. coverage of that module increases) while the suite stays green.

</div>
