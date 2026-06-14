# Making minierp installable

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.8 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write a minimal pyproject.toml declaring name, version, and a console-script entry point
- Read TOML configuration with the stdlib tomllib module
- Explain what an editable install does and why it suits development
- Connect a project.scripts entry to a callable in the package

## Python features introduced
`pyproject.toml`, `[build-system] / [project] tables`, `tomllib for reading TOML`, `editable install (pip install -e .) concept`, `project.scripts entry point`, `console entry point wiring`, `package discovery`

## MiniERP increment
Ship pyproject.toml so MiniERP is a real installable distribution with a `minierp` console command wired to a main() entry point; add a config_version() helper that reads the version straight out of pyproject.toml via tomllib. This completes the phase's headline milestone: an installable minierp package.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** pyproject.toml with [project] (name, version, scripts) + a minierp.__main__/main(); learner completes the TOML and a load_pyproject() that tomllib.load()s it to read [project].version.
- **Test focus:** tomllib parses pyproject.toml; [project].name == 'minierp' and version matches __version__; the declared console-script target resolves to a real callable.

</div>
