# Strict Clean: mypy & pyright Green

> **Phase:** Modern Type System  •  **Stage:** 25.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Run mypy --strict and pyright strict across the whole domain/service package and drive errors to zero
- Add a py.typed marker so downstream interface code (CLI/Web/Desktop/TUI) sees MiniERP as a typed library (PEP 561)
- Interpret and fix common strict diagnostics (missing return types, untyped defs, Any leakage, implicit Optional)
- Lock in the phase milestone: a fully, cleanly typed shared core

## Python features introduced
`mypy --strict`, `pyright strict mode`, `py.typed marker (PEP 561)`, `fixing strict-mode diagnostics`, `disallow_untyped_defs / reportUnknown*`, `shipping a typed package`

## MiniERP increment
Final pass: every domain and service module passes mypy --strict and pyright strict with zero errors, and the package ships a py.typed file. This is the phase deliverable — a type-checked MiniERP core the four interface phases will build on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Goal: zero errors from both checkers across the package.
#   $ mypy --strict miniERP/
#   $ pyright miniERP/
# Add an empty marker file so the package advertises its types (PEP 561):
#   miniERP/py.typed   (empty file)
# TODO: resolve any remaining strict diagnostics (untyped defs, implicit Optional,
#       returning Any, missing ClassVar, etc.) until both runs are green.
- **Test focus:** An 'edu' check verifies the py.typed marker exists in the package and that the annotated modules import and pass get_type_hints without resolution errors; where the runner supports it, mypy --strict and pyright are invoked and required to exit zero on the package.

</div>
