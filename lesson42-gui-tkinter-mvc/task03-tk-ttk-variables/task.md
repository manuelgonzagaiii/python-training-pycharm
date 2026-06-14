# ttk widgets, StringVar & two-way binding

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 42.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Bind ttk.Entry/Combobox to control variables for two-way data flow
- React to edits with trace_add so the controller validates/updates live
- Populate a ttk.Treeview with products from the core service as the list view
- Apply a ttk theme and validation to entry fields

## Python features introduced
`ttk.Entry/Label/Button/Combobox/Treeview`, `tkinter.StringVar/IntVar/BooleanVar`, `textvariable=`, `trace_add('write', cb)`, `var.get/set`, `validatecommand`, `ttk.Style/theme_use`

## MiniERP increment
Wire the form: a Treeview lists products from the core service; selecting a row fills StringVar-bound entries; edits flow through the controller into the service. The GUI is now a live, editable view of the domain.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a ProductForm with StringVars and a Treeview half-populated; learner adds textvariable bindings, the Treeview selection handler, and a trace_add validator.
- **Test focus:** Headless-test that selecting a Treeview row sets the StringVars from the injected service data, that a save invokes update_product with the var values, and that the validator rejects a non-numeric price.

</div>
