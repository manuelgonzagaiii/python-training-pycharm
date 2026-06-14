# Static type checking with mypy and a pyright cross-check

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 45.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Run mypy in (near-)strict mode over MiniERP and fix the real type errors it finds
- Use targeted `# type: ignore[code]` and typing.cast instead of blanket suppression
- Guard expensive/cyclic imports with TYPE_CHECKING and add a py.typed marker
- Cross-check with pyright and understand why two checkers can disagree

## Python features introduced
`mypy on the erp package`, `[tool.mypy] in pyproject: strict, disallow_untyped_defs, warn_unused_ignores, ignore_missing_imports`, `reading and fixing mypy errors; typing.cast and # type: ignore[code]`, `typing.TYPE_CHECKING import guard`, `reveal_type for debugging inference`, `pyright/basedpyright as an independent cross-check (basic vs strict)`, `py.typed marker for the package`

## MiniERP increment
Add a [tool.mypy] strict-ish config and a py.typed marker, then run mypy over the erp package and fix the genuine type defects it surfaces (e.g. an Optional that was never None-checked in the payments path, a Decimal|float mismatch in pricing). Add the pyright config so MiniERP is validated by two independent type checkers in CI.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # pyproject.toml
[tool.mypy]
python_version = '3.14'
strict = true
warn_unused_ignores = true
# add erp/py.typed (empty file)
# Run:  mypy erp   and   pyright erp

- **Test focus:** Checks confirm a strict-ish mypy config and a py.typed marker exist, and that `mypy erp` reports zero errors after the learner's annotations/fixes (the suite verifies the previously-failing type defect is now correctly typed).

</div>
