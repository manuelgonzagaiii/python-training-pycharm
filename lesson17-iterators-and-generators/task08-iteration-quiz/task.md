# Iterator & generator gotchas

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.8 of 8  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Predict whether iterating something twice re-yields or yields nothing
- Identify what calling a generator function returns before any next()
- Choose the correct desugaring of yield from
- Reason about eager vs lazy memory behavior

## Python features introduced
`StopIteration semantics`, `single-pass vs multi-pass`, `generator laziness`, `yield from semantics`, `list comp vs gen expr distinction`

## MiniERP increment
No code change: a knowledge check consolidating the iterator/generator model before the itertools and functools lessons build heavily on it.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice task — no code to write.
# Example question:
#   q = (x*x for x in range(3))
#   list(q); list(q)  ->  what is the SECOND list(q)?
#     A) [0, 1, 4]   B) []   C) raises StopIteration   D) [0, 1, 4, 0, 1, 4]

- **Test focus:** None (choice task: answer key embedded in task config, no unit tests).

</div>
