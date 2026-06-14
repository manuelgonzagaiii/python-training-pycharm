# Freeze a Single-File Executable with PyInstaller

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 50.5 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a dependency-free single-file MiniERP executable with PyInstaller --onefile
- Detect frozen execution via sys.frozen and locate bundled resources through sys._MEIPASS
- Write a resource_path() helper that works both from source and inside the frozen bundle
- Bundle non-code assets (HTML templates, SQL) with --add-data and resolve hidden imports

## Python features introduced
`PyInstaller (OSS) onefile build`, `sys.frozen attribute`, `sys._MEIPASS bundle dir`, `resource path resolution at runtime`, `--add-data for templates/assets`, `hidden-imports`, `entry-point script for freezing`, `spec file basics`

## MiniERP increment
Ship MiniERP to users who have no Python at all: a frozen single-file `minierp` executable that bundles the code plus its templates/SQL assets. The app's resource loading is made freeze-safe (sys.frozen/_MEIPASS aware) so the web UI templates and DB schema load identically whether run from source or from the frozen binary.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide is_frozen()->bool and resource_path(rel)->Path handling both sys._MEIPASS and the source tree, plus a PyInstaller spec/command; learner completes the resolver and the data-bundling args.
- **Test focus:** is_frozen() reads sys.frozen safely (False from source); resource_path resolves an existing bundled asset under both branches (monkeypatched sys.frozen/_MEIPASS); --add-data covers templates and schema; no absolute paths leak.

</div>
