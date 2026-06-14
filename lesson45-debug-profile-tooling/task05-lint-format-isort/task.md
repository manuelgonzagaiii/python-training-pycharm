# Style as a gate: ruff (lint), ruff-format/black & isort

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 45.5 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Configure ruff in pyproject and run it as a linter over the erp package
- Auto-format the codebase with ruff format (or black) and reconcile the two
- Sort imports deterministically with ruff's I rules or isort's black profile
- Use per-file-ignores and noqa responsibly rather than disabling rules globally

## Python features introduced
`ruff check (lint) and ruff rule selection/ignore in pyproject ([tool.ruff], [tool.ruff.lint])`, `ruff format (and black as the equivalent formatter)`, `import sorting via ruff's isort rules (I) or standalone isort ([tool.isort] / profile='black')`, `per-file-ignores and noqa codes`, `ruff check --fix and ruff format`, `line-length and target-version config`

## MiniERP increment
Add a [tool.ruff] configuration to pyproject (line length, target 3.14, selected rule sets incl. I for imports), then run ruff check --fix and ruff format across the MiniERP codebase, fixing the real lint findings (unused imports, shadowing, undefined names) so the whole project lints clean — giving MiniERP an enforced, consistent style.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # pyproject.toml
[tool.ruff]
line-length = 100
target-version = 'py314'
[tool.ruff.lint]
select = ['E', 'F', 'I', 'UP', 'B']
[tool.ruff.lint.per-file-ignores]
'tests/*' = ['S101']

# Run:  ruff check --fix .   &&   ruff format .

- **Test focus:** Checks confirm pyproject contains a ruff config selecting at least F/E/I rules, and that running `ruff check` on the erp package reports zero remaining errors and `ruff format --check` reports no changes needed.

</div>
