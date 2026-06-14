# Single-Source __version__ with importlib.metadata & SemVer

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 49.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Single-source the version: declare it once (in package metadata) and read it at runtime via importlib.metadata.version()
- Expose minierp.__version__ and a parsed version_info tuple without duplicating the number
- Apply semantic-versioning rules (when to bump MAJOR vs MINOR vs PATCH) and understand PEP 440 vs SemVer
- Handle the not-installed case (running from source) gracefully with PackageNotFoundError

## Python features introduced
`importlib.metadata.version()`, `__version__ convention`, `semantic versioning (MAJOR.MINOR.PATCH)`, `PEP 440 version specifiers`, `dynamic version in pyproject`, `PackageNotFoundError handling`, `tuple version_info`

## MiniERP increment
Give MiniERP an authoritative version. minierp.__version__ resolves from installed metadata (falling back cleanly when run from a source checkout), `minierp version` prints it, and the number is set to 1.0.0 to mark the impending release — single-sourced so it can never drift between code and package.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide get_version()->str and parse_version(s)->tuple[int,int,int]; learner wires importlib.metadata + dynamic version and the SemVer parser.
- **Test focus:** get_version() returns a PEP 440/SemVer string matching pyproject; parse_version splits MAJOR.MINOR.PATCH correctly and rejects malformed input; PackageNotFoundError path returns a sane fallback; __version__ is exported.

</div>
