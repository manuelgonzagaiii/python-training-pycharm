# Distributions, Wheels & Why pyproject Exists

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 49.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish an *import package* (what you `import`) from a *distribution package* (what you `pip install`)
- Explain what a wheel (.whl, a zip with a known layout) and an sdist (.tar.gz) are and when each is used
- Understand the PEP 517/518 contract: a front-end (pip/build) calls a build *backend* declared in pyproject.toml
- Know why pyproject.toml replaced setup.py/setup.cfg and where PEP 621 [project] metadata lives
- See where installed packages land (site-packages) and how that differs from your working source tree

## Python features introduced
`import system`, `sys.path`, `modules vs packages`, `__init__.py`, `regular vs namespace packages (PEP 420)`, `site-packages`, `PEP 517/518 build interface`, `PEP 621 project metadata`, `wheel vs sdist`, `source tree vs build artifact`

## MiniERP increment
No code change yet: produce ARCHITECTURE/packaging notes describing how the existing MiniERP source tree (core domain/service layer + the CLI/Web/Desktop/Text-UI front-ends built in earlier phases) will be reorganized into a single installable `minierp` distribution package, identifying the one import-package root and the modules that become entry points.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** A read-only page; task.py holds a runnable snippet that prints sys.path and lists already-installed distributions so the learner sees the concepts live.
- **Test focus:** Theory page — no automated checks; the runnable snippet simply illustrates site-packages vs source tree.

</div>
