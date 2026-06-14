# console_scripts Entry Points: Make `minierp` a Command

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 49.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Declare [project.scripts] so installing the wheel creates a `minierp` executable on PATH
- Understand the module:callable target convention and how the installer generates the wrapper
- Discover entry points at runtime with importlib.metadata.entry_points(), incl. custom groups for a front-end/plugin registry
- Route a single `minierp` command to the CLI/web/gui/tui front-ends built earlier

## Python features introduced
`[project.scripts] console_scripts`, `entry-point object reference (module:function)`, `importlib.metadata.entry_points()`, `entry-point groups & plugin discovery`, `sys.argv / argparse hand-off`, `generated wrapper scripts`

## MiniERP increment
Define MiniERP's console entry points: a primary `minierp` command (dispatching to the CLI) plus group-based entry points that let the four front-ends register themselves, so `importlib.metadata.entry_points(group='minierp.frontends')` enumerates cli/web/gui/tui. Wire a main() that argparse-dispatches subcommands to the existing front-ends.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide main(argv=None) and discover_frontends()->dict using importlib.metadata; learner declares [project.scripts]/[project.entry-points] and completes the dispatcher.
- **Test focus:** entry-point metadata declares console_scripts `minierp`; discover_frontends() returns the four expected front-ends from the metadata group; main(['--help']) and main(['version']) behave; bad subcommand exits non-zero.

</div>
