# Decorator Pitfalls

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 20.7 of 7  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Distinguish a decorator from a decorator factory and know when parentheses are required
- Recognize symptoms of a missing functools.wraps
- Reason correctly about bottom-up application order in a stack

## Python features introduced
`wraps vs no-wraps consequences`, `decorator factory vs decorator confusion (forgetting the extra layer)`, `decoration time vs call time`, `stacking order reasoning`, `mutable-default-in-closure gotchas`

## MiniERP increment
Consolidates the audit/instrumentation work conceptually so the learner can debug their own decorators in the MiniERP service layer; no new runtime code.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice knowledge check. Example item:
#
# Given:
#   @audit            # note: no parentheses
#   def create(...): ...
# What happens?
#   a) Works, action defaults to None
#   b) TypeError: create() missing 'action'  (audit expects `action`, got the function)
#   c) Nothing until first call
#   d) Registers create in AUDIT_LOG immediately
# (correct: b)
- **Test focus:** Correct multiple-choice answers selected (choice task).

</div>
