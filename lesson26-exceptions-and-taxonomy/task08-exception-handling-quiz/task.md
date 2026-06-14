# Knowledge Check: Chaining, Groups & Clause Order

> **Phase:** Errors, Exceptions & Logging  •  **Stage:** 26.8 of 8  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Predict which handler fires given an ordered set of except clauses
- Recall whether finally runs when the try block returns or re-raises
- Distinguish when __cause__ vs __context__ is populated
- Know that a plain except ExceptionGroup behaves differently from except* and that BaseException must not be caught casually

## Python features introduced
`__cause__ vs __context__ semantics`, `except clause ordering rules`, `else vs finally execution order`, `ExceptionGroup vs single-exception catching`, `bare except / BaseException pitfalls`

## MiniERP increment
No code change: consolidates the lesson's mental model so learners can confidently choose handlers and chaining style when wiring exceptions through the remaining MiniERP services.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice task — answers are selected in the Task Description panel.
# No source file to edit.
- **Test focus:** None (choice task: correct option(s) configured in task metadata).

</div>
