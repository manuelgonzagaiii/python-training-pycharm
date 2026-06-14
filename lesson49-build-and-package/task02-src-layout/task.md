# Adopt a src/ Layout for the minierp Package

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 49.2 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Restructure the project into a src/minierp/ import-package root with subpackages for domain, services, and each interface
- Understand why a src/ layout prevents accidental imports from the working directory and forces you to test the installed package
- Curate the public API of the top-level package with explicit __all__ exports
- Use correct relative vs absolute imports across the reorganized tree

## Python features introduced
`src layout vs flat layout`, `package __init__.py exports`, `__all__`, `relative imports`, `import package discovery`, `pathlib.Path`, `module __name__/__package__`

## MiniERP increment
Move the feature-complete MiniERP code under src/minierp/ (subpackages: minierp.domain, minierp.services, minierp.cli, minierp.web, minierp.gui, minierp.tui, minierp.storage) with a clean top-level __init__.py that re-exports the core public API. Behaviour is unchanged; only the package layout is consolidated for distribution.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide the target src/minierp/__init__.py skeleton and a function build_package_tree()/get_public_api() the test can introspect; learner fills exports and fixes imports.
- **Test focus:** Importing minierp succeeds; minierp.__all__ lists the expected public names; key subpackages (domain, services, cli, web) import without error; no module imports from a top-level flat path.

</div>
