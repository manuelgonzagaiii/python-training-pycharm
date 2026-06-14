# Textual: a reactive TUI app

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 41.5 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a Textual App that composes widgets and reacts to events instead of a manual getch loop
- Load products into a DataTable from the core service and filter via an Input widget
- Bind keys to actions (add, refresh, quit) and push a modal screen to create a record
- Test a Textual app headlessly with the Pilot harness

## Python features introduced
`textual.app.App`, `compose() & widgets (Header/Footer/DataTable/Input)`, `reactive attributes`, `message/event handlers (on_*)`, `actions & key bindings (BINDINGS)`, `Screen navigation`, `run_async/pilot testing`

## MiniERP increment
Ship `minierp tui` as a Textual app: a DataTable of products/customers with live filtering, key bindings, and a modal 'new product' form that calls the core service — a modern TUI front-end fully replacing the raw-curses prototype while reusing the Rich renderers.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a MiniErpApp(App) skeleton with BINDINGS and a compose() yielding Header/DataTable/Footer; learner fills the on_mount data load, the filter handler, and the add-product action.
- **Test focus:** Use Textual's async Pilot to mount the app, simulate keypresses/filter input, and assert the DataTable row set matches the (injected) service data and that the add action invokes create_product.

</div>
