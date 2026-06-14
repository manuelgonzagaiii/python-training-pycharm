# Reading installed metadata

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 29.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Read an installed distribution's version with importlib.metadata.version
- Fetch metadata fields (Summary, Author) from importlib.metadata.metadata
- Enumerate entry points as a plugin/registration mechanism
- Fall back gracefully with PackageNotFoundError when running from source

## Python features introduced
`importlib.metadata.version`, `importlib.metadata.metadata`, `importlib.metadata.entry_points`, `importlib.metadata.PackageNotFoundError`, `distribution vs import package`, `__version__ vs installed metadata`

## MiniERP increment
Add minierp.about(): report the package version preferring importlib.metadata.version('minierp') and falling back to __version__ when not installed, plus summary/author when available. Powers a trustworthy `minierp --version`/about command across all four front-ends.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/_about.py with about(); learner implements the metadata lookup with PackageNotFoundError fallback to __version__.
- **Test focus:** about() returns a version string in both installed and source-run cases; PackageNotFoundError path falls back to __version__; metadata fields surfaced when present.

</div>
