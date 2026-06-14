# Release MiniERP 1.0: The Checklist & the Tag

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 51.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Codify a release checklist: tests green, version bumped to 1.0.0, CHANGELOG updated, wheel+sdist build clean, docs build, docker image builds, entry points work
- Verify the installed version matches the intended release via importlib.metadata
- Understand the final publish step (twine to a package index) without requiring any paid service
- Automate the checklist as a runnable gate that returns pass/fail

## Python features introduced
`CHANGELOG / Keep a Changelog`, `semantic versioning bump to 1.0.0`, `git tag (annotated) conceptually`, `importlib.metadata version assertion`, `reproducible build verification`, `release checklist automation`, `twine/PyPI publish (concept, OSS)`, `programmatic checklist runner`

## MiniERP increment
Cut the release: a programmatic release_check() that runs the full gate (version==1.0.0, artifacts build, entry points resolve, docs/docker present, capstone passes) and a CHANGELOG marking MiniERP 1.0.0 — the final stage that declares MiniERP a packaged, documented, containerized, installable 1.0 product and closes the 18-phase course.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide release_check(ctx)->Report with individual check functions and a CHANGELOG skeleton; learner implements each gate (version, build, entry points, docs/docker presence) and the aggregate pass/fail.
- **Test focus:** release_check returns all-pass only when version is 1.0.0, required artifacts/files exist, entry points resolve via importlib.metadata, and prior gates pass; a deliberately failing input flips the report to fail with the offending item named.

</div>
