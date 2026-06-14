# How a terminal UI actually works

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 41.1 of 5  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand the curses model: a screen buffer you draw to and then refresh
- Know why curses.wrapper is essential (restores the terminal on crash)
- See the universal TUI loop: draw -> wait for key -> update state -> redraw
- Frame the TUI as another thin front-end over the core service

## Python features introduced
`curses module overview`, `terminal raw vs cooked mode`, `screen buffer & refresh model`, `the getch input loop concept`, `curses.wrapper safety`

## MiniERP increment
Add a `minierp/tui/` package and a curses bootstrap that opens a blank managed screen via curses.wrapper, prints a title bar from app metadata, and waits for 'q' to quit — establishing the TUI seam onto the core.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide run() that calls curses.wrapper(_main) where _main(stdscr) draws a header and loops on stdscr.getch(); learner reads it and notes the structure.
- **Test focus:** Theory page — no checks; runnable only in a real terminal, with a clear explanation of the draw/refresh/getch cycle.

</div>
