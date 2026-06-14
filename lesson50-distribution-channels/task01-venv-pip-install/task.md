# Install into a venv with pip; Understand Isolation

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 50.1 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create an isolated environment programmatically with the stdlib venv module and detect activation via sys.prefix != sys.base_prefix
- Install the MiniERP wheel (and an editable `pip install -e .`) and confirm the `minierp` command appears
- Select optional extras at install time (e.g. `minierp[web]`) so a user pulls only the front-ends they want
- Explain why virtual environments prevent dependency collisions

## Python features introduced
`venv module (EnvBuilder)`, `pip install (wheel & editable -e)`, `sys.prefix / sys.base_prefix`, `site-packages discovery`, `environment isolation`, `pip install '.[extra]' extras selection`, `subprocess to drive pip`

## MiniERP increment
Provide a reproducible install path for MiniERP: a helper/script that builds a fresh venv, installs the wheel with chosen extras, and smoke-tests that `minierp version` runs inside it — the canonical 'does it install cleanly?' check that gates the release.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide make_venv(path) and in_virtualenv()->bool plus a smoke_test() that shells out to the installed command; learner completes the venv/EnvBuilder and detection logic.
- **Test focus:** in_virtualenv() correctly compares sys.prefix/sys.base_prefix; make_venv creates a python executable; the install smoke test reports the expected version string; extras resolve to the right dependency set.

</div>
