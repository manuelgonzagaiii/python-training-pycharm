# Running mypy & pyright

> **Phase:** Modern Type System  •  **Stage:** 23.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Install and invoke mypy and pyright on the MiniERP package and read their diagnostics
- Understand from __future__ import annotations: all annotations become strings, enabling forward references and avoiding import-time cost
- Know the difference between runtime-evaluated and deferred (stringized) annotations and when each matters
- Set up a baseline strict configuration the rest of the phase will be checked against

## Python features introduced
`mypy`, `pyright`, `from __future__ import annotations`, `PEP 563 deferred evaluation of annotations`, `configuring strictness`, `reading checker error messages`

## MiniERP increment
Adds from __future__ import annotations to the domain modules and a mypy/pyright config (strict-ish) to the project. Running the checkers on the now-annotated Product/Customer/services produces a clean baseline — the milestone's checking harness is born.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations  # all annotations stored as strings

# A forward reference now works without quotes:
def link(a: Product, b: Product) -> Pair:  # Pair defined later in the module
    ...

class Pair:
    def __init__(self, left: Product, right: Product) -> None: ...

# Project config to create:
#   mypy:    [tool.mypy] strict = true   (pyproject.toml)
#   pyright: { "typeCheckingMode": "strict" } (pyrightconfig.json)
- **Test focus:** An 'edu' check verifies that the module imports cleanly with the future import present, that forward-referenced names resolve via get_type_hints, and (where the runner allows) that mypy/pyright exit zero on the annotated modules.

</div>
