# tkinter & MVC: one core, four UIs

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 42.1 of 6  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand the Tk root + mainloop event model and the widget parent hierarchy
- See the MVC split where the Model is the existing core service and the View is tkinter
- Recognise this is the same adapter seam used by the CLI, Web, and TUI
- Know why ttk (themed widgets) is preferred over classic tk widgets

## Python features introduced
`tkinter.Tk root window`, `mainloop event loop`, `widget hierarchy & master/parent`, `MVC/presenter pattern`, `ttk vs classic tk`

## MiniERP increment
Add a `minierp/gui/` package with an app skeleton: a Tk root, a root frame, a window title from app metadata, and a Controller object that holds a reference to the core service — the GUI seam, no widgets yet.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide gui/app.py with class MiniErpGui holding a controller and a root window, plus a Controller wrapping the core service; main() builds and (in real use) runs mainloop.
- **Test focus:** Theory page — no automated checks; explains mainloop, the widget tree, and the Model/View/Controller responsibilities.

</div>
