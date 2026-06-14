# Dynamic imports with importlib

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.6 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Load a module at runtime from a string name with importlib.import_module
- Resolve a function from a dynamically imported module via getattr
- Check whether a module exists with importlib.util.find_spec before importing
- Handle ModuleNotFoundError to fail gracefully on missing plugins

## Python features introduced
`importlib.import_module`, `import by string name`, `getattr to fetch a callable from a module`, `importlib.util.find_spec`, `ModuleNotFoundError handling`, `plugin dispatch by name`

## MiniERP increment
Turn the plugin loader real: a run_plugin(name) that import_modules `minierp.plugins.<name>`, fetches its run() callable, and invokes it — with a clear error if the plugin is absent. MiniERP can now dispatch reporting/export commands by name, the seed of its command registry.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** plugin_runner.py with run_plugin(name); learner implements the import_module + getattr + error handling. A sample plugin exposes run() returning a report string.
- **Test focus:** run_plugin('demo') returns the plugin's output; run_plugin('nope') raises/returns the documented missing-plugin error; find_spec used to pre-check.

</div>
