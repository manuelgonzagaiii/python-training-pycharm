# What a Decorator Really Is

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 20.1 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that a decorator is just a callable that takes a function and returns a (usually wrapping) function
- See that @deco above def f is exactly f = deco(f)
- Recall closures from earlier phases as the mechanism that lets a wrapper capture the original function

## Python features introduced
`first-class functions`, `functions as arguments`, `functions returning functions`, `closures`, `the @ syntax as syntactic sugar`, `decorator = func -> func`

## MiniERP increment
No code change yet: orients the learner around the existing service-layer functions (create_product, record_sale) that later tasks will wrap with audit/transaction behavior. Establishes the 'cross-cutting concerns' vocabulary used throughout the phase.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Theory page only. Shows the existing service functions as the wrap targets:
#
#   def create_product(repo, *, sku, name, price): ...
#   def record_sale(repo, *, customer_id, lines): ...
#
# and demonstrates that `@deco` is sugar for `f = deco(f)`.
# No code to write.
- **Test focus:** None (theory page, no checking).

</div>
