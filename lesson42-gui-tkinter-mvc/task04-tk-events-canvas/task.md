# Event binding & a Canvas chart

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 42.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Bind mouse, keyboard, and virtual events to handlers and read the event object
- Draw on a Canvas: render a small bar chart of stock levels with rectangles and labels
- Use item tags and coords to update canvas items when data changes
- Schedule periodic refreshes with after()

## Python features introduced
`widget.bind('<Button-1>'/'<Double-1>'/'<KeyRelease>'/'<Return>')`, `event object attributes`, `bind_all & virtual events (<<TreeviewSelect>>)`, `tkinter.Canvas`, `create_rectangle/create_text/create_line`, `coords & item tags`, `after() scheduling`

## MiniERP increment
Add an inventory bar chart on a Canvas that reflects per-product stock from the core analytics service, double-click a bar to jump to that product, and auto-refresh via after(). The GUI gains interactive visualization.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide draw_chart(canvas, data) plotting axes; learner adds the bars/labels from injected stock data, the <Double-1> hit-test handler, and the after() refresh scheduling.
- **Test focus:** Test the pure geometry helper (values -> bar rectangles/scaling) and the hit-test (canvas x -> product index) headlessly; assert after()-driven refresh calls the service. Canvas pixels themselves are not asserted.

</div>
