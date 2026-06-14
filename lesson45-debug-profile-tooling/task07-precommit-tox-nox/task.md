# The one-command quality gate: pre-commit, tox & nox

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 45.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Wire formatting, linting and type checks into git via pre-commit so bad code can't be committed
- Define multi-step environments with tox and the same with nox sessions
- Run the entire quality gate (format check, lint, types, tests, coverage) with one command
- Understand the right ordering and how local hooks mirror CI

## Python features introduced
`pre-commit (.pre-commit-config.yaml) with ruff/ruff-format/mypy hooks and built-in hygiene hooks`, `pre-commit run --all-files and the git hook install`, `tox.ini environments (lint, type, py314) and tox -q`, `nox (noxfile.py) sessions as a Python-native alternative`, `passing args through to underlying tools`, `ordering the gate: format -> lint -> type -> tests+coverage`

## MiniERP increment
Add .pre-commit-config.yaml (ruff, ruff-format, mypy, trailing-whitespace/end-of-file hooks), a tox.ini with lint/type/test environments, and an equivalent noxfile.py — so the full MiniERP quality gate (format -> lint -> type -> tests+coverage, every step from this phase) runs green with a single `nox` / `tox` invocation. This is the phase's capstone deliverable.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks: [{id: ruff, args: ['--fix']}, {id: ruff-format}]

# noxfile.py
import nox
@nox.session
def tests(session):
    session.install('-e', '.', 'pytest', 'pytest-cov', 'hypothesis')
    session.run('pytest', '--cov=erp', '--cov-branch')

- **Test focus:** Checks confirm a valid .pre-commit-config.yaml (with ruff + a formatter + a type hook), and a tox.ini and/or noxfile.py defining ordered lint/type/test sessions; the grader runs the test session and confirms the assembled gate passes on the now clean, typed, covered MiniERP codebase.

</div>
