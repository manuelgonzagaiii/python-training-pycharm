# Fixtures, scopes, conftest & dependency injection

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 44.2 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Replace setUp/tearDown with composable fixtures and choose the right scope
- Share fixtures across modules with conftest.py
- Use tmp_path for filesystem tests, monkeypatch instead of mock.patch, capsys/caplog for output and logs
- Build a layered fixture stack (db -> repository -> service) injected into tests

## Python features introduced
`@pytest.fixture`, `fixture scopes: function/module/session`, `conftest.py for shared fixtures`, `yield fixtures for setup+teardown`, `built-in fixtures: tmp_path, monkeypatch, capsys, caplog`, `fixture composition (fixtures depending on fixtures)`, `autouse fixtures`, `request fixture and indirect params`

## MiniERP increment
Add tests/conftest.py providing the core test fixtures for MiniERP: a session-scoped seeded catalog, a function-scoped in-memory store, and a built service (customers/sales/payments) wired together. Rewrite the payments and notifier tests to consume these fixtures, using monkeypatch for the clock and tmp_path for an export round-trip — giving the whole suite a clean, reusable harness.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import pytest
from erp.app import build_services

@pytest.fixture(scope='session')
def catalog():
    return seed_catalog()  # TODO

@pytest.fixture
def services(catalog):
    return build_services(catalog=catalog, store=InMemoryStore())

# In a test:
def test_export_roundtrip(services, tmp_path, monkeypatch):
    ...

- **Test focus:** Checks confirm a conftest.py exists with at least one shared fixture, that fixtures of differing scope are used, and that tmp_path + monkeypatch (or capsys/caplog) are exercised in real service tests.

</div>
