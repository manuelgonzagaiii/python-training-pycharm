# Frames & geometry: grid, pack, place

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 42.2 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Lay out a toolbar (pack), a form (grid with weights), and an overlay badge (place)
- Use sticky and row/column weights so the layout resizes correctly
- Compose nested ttk.Frames into a coherent window structure
- Know when each geometry manager is the right tool

## Python features introduced
`ttk.Frame`, `grid(row,column,sticky,columnspan)`, `grid_rowconfigure/columnconfigure(weight=)`, `pack(side, fill, expand)`, `place(relx, rely)`, `padding & sticky`, `nested frames`

## MiniERP increment
Build the main window shell: a top toolbar, a left product-list pane, and a right detail form, arranged with the three geometry managers and resizing cleanly. Still static, but it's the real GUI frame.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide build_layout(root) creating the frames with the toolbar packed; learner completes the grid form (labels/entries with weights) and a place()'d status badge.
- **Test focus:** Headless-construct the frames (Tk withdrawn) and assert the widget tree: toolbar uses pack, form children use grid at expected cells, column weights set, badge uses place. Skip cleanly if no display is available.

</div>
