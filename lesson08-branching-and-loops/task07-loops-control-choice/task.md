# break, continue, pass, and the else clauses

> **Phase:** Control Flow & Functions  •  **Stage:** 8.7 of 7  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Predict exactly when a loop's else clause executes
- Distinguish break (exit), continue (skip), and pass (no-op)
- Avoid the common misconception that else runs 'at the end always'

## Python features introduced
`break vs continue vs pass semantics`, `for-else / while-else trigger conditions`, `loop control flow reasoning`

## MiniERP increment
No code change: a knowledge check consolidating the loop-control semantics used by find_in_catalog and all_lines_valid before the dispatcher work begins, ensuring learners can reason about the control flow they just wrote.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice knowledge check; no code to edit.
# Q: In `for x in xs: ... else: ...`, when does the else block run?
#   A) Always after the loop body
#   B) Only if the loop completes without hitting break  <-- correct
#   C) Only if xs is empty
#   D) Never, else is illegal after for
- **Test focus:** Single correct option: the else clause runs only when the loop finishes without executing break.

</div>
