# Build a Wheel and an sdist with `build`

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 49.5 of 7  •  **Type:** `output`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Run `python -m build` to produce both a wheel and an sdist into dist/
- Inspect a wheel's *-dist-info (METADATA, RECORD, entry_points.txt) with stdlib zipfile and an sdist with tarfile
- Understand which files land in each artifact and why the sdist is the buildable source bundle
- Verify the build is clean and the version/metadata match pyproject

## Python features introduced
`python -m build`, `build (PyPA front-end)`, `wheel format internals`, `sdist contents`, `zipfile / tarfile (stdlib) to inspect artifacts`, `RECORD & dist-info metadata`, `reproducible builds`

## MiniERP increment
Produce the first distributable artifacts of MiniERP — dist/minierp-<ver>.whl and dist/minierp-<ver>.tar.gz — and a small audit script (run as the output program) that opens the wheel and prints its dist-info metadata, proving the package is correctly assembled.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide inspect_wheel(path) and inspect_sdist(path) helpers using zipfile/tarfile; task.py builds (or loads a prebuilt) artifact and prints a deterministic report compared to expected output.
- **Test focus:** output: stdout lists the wheel's dist-info files, the distribution name/version parsed from METADATA, and the presence of entry_points.txt — matched against the expected text.

</div>
