# curses: windows, the input loop & navigation

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 41.2 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create sub-windows (header, list, status bar) and draw text safely within bounds
- Run a getch loop translating arrow keys into a moving selection
- Page a list of records fetched from the core service and highlight the current row
- Redraw efficiently with noutrefresh + doupdate

## Python features introduced
`curses.wrapper`, `stdscr/newwin windows`, `addstr/addnstr`, `window.refresh/noutrefresh/doupdate`, `getch & curses.KEY_UP/KEY_DOWN`, `curs_set`, `getmaxyx`, `keypad(True)`

## MiniERP increment
Build a scrollable product browser: the TUI fetches products from the core service, lists them in a window, and lets the user move the selection with arrow keys, with a status bar showing position. Read-only but live against the core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a ListView class holding items + selected index with move(delta) clamping; learner wires getch -> move and the draw() that renders rows and highlights the selection.
- **Test focus:** Unit-test the headless ListView/state machine: move() clamps at both ends, page math (visible window) is correct, and the rows come from the injected service. (curses drawing itself is not asserted.)

</div>
