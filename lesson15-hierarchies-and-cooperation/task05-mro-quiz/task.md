# Knowledge Check: super() & MRO

> **Phase:** OOP Advanced & Modeling  •  **Stage:** 15.5 of 6  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Confirm that super() dispatches along the MRO rather than to the static parent
- Predict the print order of cooperative __init__ in a diamond
- Identify why forgetting super().__init__() breaks a mixin chain

## Python features introduced
`MRO reasoning`, `super() semantics`, `diamond resolution`, `cooperative multiple inheritance pitfalls`

## MiniERP increment
Reinforces the inheritance design decisions behind the entity hierarchy; no production code, but locks in the mental model used by every subsequent entity.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice knowledge check. Choose the correct answer in task.md.
#
# Q: Given class D(B, C), B(A), C(A) where each __init__ calls
#    super().__init__(), how many times does A.__init__ run when
#    you construct D()?
#   a) 0   b) 1   c) 2   d) depends on order

- **Test focus:** Single correct option recorded (answer: exactly once — cooperative super() with a proper diamond runs A.__init__ one time).

</div>
