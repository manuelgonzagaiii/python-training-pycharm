# Author pyproject.toml: PEP 621 Project Metadata

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 49.3 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a complete [build-system] table choosing a backend and declaring build requirements
- Fill the PEP 621 [project] table: name, description, readme, requires-python, license, authors, classifiers, keywords
- Declare runtime dependencies and optional-dependencies extras (e.g. [web], [tui], [dev]) so front-ends install only what they need
- Parse and validate your own pyproject.toml with stdlib tomllib

## Python features introduced
`pyproject.toml`, `tomllib (stdlib TOML reader)`, `PEP 621 [project] table`, `[build-system] requires/build-backend`, `dependencies & optional-dependencies extras`, `project.urls / authors / classifiers`, `requires-python`

## MiniERP increment
Add a real pyproject.toml at the project root for the `minierp` distribution: core has zero/minimal runtime deps, while extras gate the OSS front-end stacks (FastAPI/uvicorn/Jinja2 under [web], Textual/Rich under [tui], pytest/hypothesis/ruff/mypy under [dev]) introduced in earlier phases. This is the manifest the rest of the phase builds on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a function load_pyproject(path)->dict using tomllib plus a partially filled pyproject.toml; learner completes the [project] table and extras.
- **Test focus:** tomllib parses the file; required PEP 621 keys present with correct types; requires-python targets 3.14; optional-dependencies define the expected extras; build-system table names a backend and requires.

</div>
