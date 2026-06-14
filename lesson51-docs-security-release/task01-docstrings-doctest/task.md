# Document the API: PEP 257 Docstrings & doctest

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 51.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write conformant PEP 257 docstrings (summary line, blank line, body) across MiniERP's public API
- Embed runnable examples and verify them with the stdlib doctest module
- Choose a docstring style (Google/NumPy/reST) consistently to feed a doc generator
- Use help()/__doc__ to confirm the documentation is discoverable at runtime

## Python features introduced
`docstrings (PEP 257)`, `module/class/function docstrings`, `__doc__`, `doctest module`, `doctest directives (ELLIPSIS, +SKIP)`, `help() introspection`, `Google/NumPy/reStructuredText docstring styles`

## MiniERP increment
Document MiniERP's public domain/service API with consistent, example-rich docstrings, and make those examples executable so `doctest` proves the documentation stays true to the code — turning the README-level knowledge into in-code, testable reference docs.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a function run_doctests(module)->results and a sample documented service; learner writes docstrings (with doctest examples) on the public API so the doctest run passes.
- **Test focus:** Targeted public functions have non-empty PEP 257-shaped docstrings; doctest runs the embedded examples with zero failures; docstring presence is asserted for the documented module's public names.

</div>
