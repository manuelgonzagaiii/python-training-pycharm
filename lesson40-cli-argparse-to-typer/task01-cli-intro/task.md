# Why a CLI? Front-ends over one core

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 40.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that a UI is a thin adapter over the shared service layer built in earlier phases
- See the four-front-end architecture (CLI, Web, TUI, GUI) and why business logic must never live in a UI
- Recall how the existing core service API is called (create_product, record_sale, build_report, etc.)
- Preview the journey: raw sys.argv -> argparse -> Typer

## Python features introduced
`__main__ module`, `sys.argv`, `console_scripts entry point concept`, `separation of concerns`

## MiniERP increment
Add a `minierp/cli/` package and a `__main__.py` entry point that prints usage and routes to a (still empty) command dispatcher, importing the existing core service module to prove the wiring. No business logic is added — only the adapter seam.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Create minierp/cli/__init__.py and minierp/cli/__main__.py; show how `python -m minierp.cli` reaches a dispatch() stub that already imports services from the core.
- **Test focus:** Theory page — no automated checks; includes a runnable snippet showing sys.argv and a call into the core service.

</div>
