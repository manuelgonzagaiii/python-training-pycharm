# Build Backends Compared: setuptools vs hatchling

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 49.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that the build-backend string names an importable object implementing the PEP 517 hooks
- Configure setuptools to discover the src/minierp package (package-dir + find)
- Configure the same project under hatchling and compare the minimal config each requires
- Reason about why editable installs (PEP 660) exist and how the backend enables them

## Python features introduced
`[build-system] build-backend`, `setuptools.build_meta`, `hatchling.build`, `tool.setuptools.packages.find / package-dir`, `tool.hatch.build targets`, `backend-specific config tables`, `editable install hooks (PEP 660)`

## MiniERP increment
Make MiniERP buildable under both setuptools and hatchling: provide the [tool.setuptools] / [tool.hatch] tables so the chosen backend correctly finds and includes the src/minierp package and its package data. Settle on one backend for the project while documenting the alternative.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a helper select_backend(pyproject)->str and the two backend config fragments; learner completes whichever table the project standardizes on so the package is discoverable.
- **Test focus:** The pyproject names a valid build-backend; the backend's package-discovery config resolves to src/minierp; package-data/include globs cover non-Python assets (templates, sql); editable-install intent is configured.

</div>
