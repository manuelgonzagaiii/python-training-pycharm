# curses: colors, attributes & an edit field

> **Phase:** User Interfaces: CLI, TUI & GUI  •  **Stage:** 41.3 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Initialise color pairs and apply attributes to convey state (selected, low-stock, error)
- Build a minimal inline edit field (capture keystrokes, handle backspace, Enter to commit)
- Use color to flag low-stock products returned by the core inventory service
- Degrade gracefully when has_colors() is False

## Python features introduced
`curses.start_color`, `init_pair & color_pair`, `A_BOLD/A_REVERSE/A_UNDERLINE attributes`, `has_colors`, `echo/noecho`, `reading a text field char-by-char`, `KEY_BACKSPACE handling`, `addstr with attr`

## MiniERP increment
Add a quick 'adjust quantity' action: select a product, type a new amount in an inline field, press Enter, and the TUI calls the core service to update stock — with low-stock rows shown in red. The TUI can now mutate state.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide an EditField class (buffer, cursor, feed(key)->done?) half-written and a color setup function; learner finishes feed() (backspace/enter) and the commit that calls adjust_stock.
- **Test focus:** Headless-test EditField.feed for digits/backspace/enter producing the right buffer and commit value; assert the low-stock predicate picks the right rows; assert commit calls the service with the parsed int.

</div>
