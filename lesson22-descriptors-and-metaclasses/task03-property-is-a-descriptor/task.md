# How @property Works Underneath

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 22.3 of 7  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- See that @property is just a descriptor whose __get__ calls your getter
- Understand why a read-only property raises on assignment (no fset)
- Know when a custom descriptor beats property: reuse across many attributes/classes

## Python features introduced
`property as a built-in data descriptor`, `property.__get__/__set__/__delete__ calling fget/fset/fdel`, `@property / @x.setter desugared to property(fget).setter(fset)`, `comparison: property vs custom descriptor`, `functools.cached_property as a non-data descriptor`

## MiniERP increment
Refactors one computed attribute (Invoice.total) from a hand-written property to show equivalence, and documents in core/fields.py why the reusable descriptors from the previous task are preferable for repeated validation. No new behavior.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Theory page. Shows the equivalence:
#
#   class Invoice:
#       @property
#       def total(self): return sum(l.amount for l in self.lines)
#
# is roughly:
#   def _total(self): ...
#   total = property(_total)   # a data descriptor instance on the class
#
# plus a cached_property contrast (non-data: instance dict shadows it).
- **Test focus:** None (theory page).

</div>
