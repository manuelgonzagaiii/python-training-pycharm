# Debugging with breakpoint() and pdb

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 45.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Set a breakpoint with the builtin and control it via PYTHONBREAKPOINT
- Navigate execution with the core pdb commands and inspect locals
- Drop into a post-mortem debugger after an exception, including pytest --pdb
- Know which debugging move fits which situation

## Python features introduced
`the builtin breakpoint()`, `PYTHONBREAKPOINT environment variable (including =0 to disable)`, `pdb commands: l(ist), n(ext), s(tep), c(ontinue), w(here), p/pp, until, return`, `post-mortem debugging: pdb.pm(), python -m pdb script.py, pytest --pdb`, `breakpoint conditions and the commands/display features`, `inspecting the call stack and frame locals`

## MiniERP increment
A concept page that walks through debugging a real MiniERP defect: a discount that produces the wrong invoice total. It shows placing breakpoint() in the pricing path, stepping through with pdb, inspecting frame locals to spot a Decimal/float mix-up, and using `pytest --pdb` for post-mortem on the failing test — documented as a reusable debugging playbook in the repo.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # A read-only theory page. Shows, e.g.:
#   def apply_discount(self, rate):
#       breakpoint()        # PYTHONBREAKPOINT=0 to disable in CI
#       ...
# and a transcript of  pytest --pdb  landing in the failing frame.
- **Test focus:** No automated check (theory page). The page must concretely demonstrate breakpoint(), PYTHONBREAKPOINT, the core pdb navigation commands, and a post-mortem/`pytest --pdb` workflow against a real MiniERP bug.

</div>
