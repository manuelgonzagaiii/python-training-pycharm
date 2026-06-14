# Menus & dialogs: messagebox, filedialog, Menu

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 42.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a menubar with File/Edit/Help cascades and keyboard accelerators
- Confirm destructive actions with messagebox and report errors from the service
- Use filedialog to pick CSV paths and call the existing import/export service
- Wrap risky controller calls so service errors surface as dialogs, not crashes

## Python features introduced
`tkinter.Menu (menubar, cascades, accelerators)`, `root.config(menu=)`, `tkinter.messagebox (askyesno/showerror/showinfo)`, `tkinter.filedialog (askopenfilename/asksaveasfilename)`, `command callbacks`, `simpledialog`, `keyboard accelerators`

## MiniERP increment
Add a menubar: File -> Import/Export CSV (via filedialog into the existing import/export service), delete-with-confirm via messagebox, and a Help -> About box. The desktop GUI is now feature-complete over the core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide build_menu(root, controller) with a File cascade stub; learner adds Import/Export commands calling filedialog + the service, and the confirm-delete using messagebox.askyesno.
- **Test focus:** Inject fakes for filedialog/messagebox and assert Import calls import_csv with the chosen path, Export calls export_csv, and a 'No' on the confirm dialog skips delete while 'Yes' calls delete_product.

</div>
