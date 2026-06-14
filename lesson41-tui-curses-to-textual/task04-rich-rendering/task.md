# Rich: tables, panels & styled output

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 41.4 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Render core-service data as polished tables and panels with far less code than curses
- Use Rich markup/styles for emphasis and status coloring
- Reuse Rich output inside the CLI from Lesson 1 (e.g. the report --table format)
- Capture Rich output deterministically so it can be tested

## Python features introduced
`rich.console.Console`, `rich.table.Table`, `rich.panel.Panel`, `rich markup & styles`, `console.print`, `rich.box`, `Console capture for testing`, `rich.text.Text`

## MiniERP increment
Upgrade the CLI's `report --table` and product listings to render via Rich tables/panels, and add a `minierp dashboard` snapshot that prints KPI panels from the analytics service. One renderer now serves CLI and the upcoming Textual app.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide build_products_table(products)->Table partially filled; learner adds columns/rows and a KPIs panel, then routes the CLI table format through it.
- **Test focus:** Use Console(record=True)/capture to render a fixed product list and assert the export text contains expected headers, values, and that low-stock styling is applied (via segments/markup).

</div>
