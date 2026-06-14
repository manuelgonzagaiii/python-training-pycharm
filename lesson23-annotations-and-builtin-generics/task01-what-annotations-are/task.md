# What Annotations Really Are

> **Phase:** Modern Type System  •  **Stage:** 23.1 of 6  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that annotations are metadata stored in __annotations__ and are NOT checked or enforced by the interpreter at runtime
- Distinguish a variable annotation (name: T) from an assignment (name: T = value) and a function parameter/return annotation
- Know that static type checkers (mypy, pyright), not CPython, are what give annotations meaning
- See where the MiniERP domain layer currently lacks types and why that hurts the four upcoming interfaces

## Python features introduced
`variable annotations`, `function annotations`, `__annotations__`, `annotations are not enforced at runtime`, `PEP 3107`, `PEP 526`, `the typing module overview`

## MiniERP increment
Conceptual orientation: tour the existing untyped MiniERP domain modules (product.py, customer.py and the service layer) and identify every public signature that will be annotated over this phase. No code change yet; sets the target for the milestone.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # theory page only — shows live examples against existing MiniERP classes
class Product:  # already built in an earlier phase (Rich OOP)
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

# At runtime Python ignores annotations; they live in __annotations__.
x: int = 5
print(__annotations__)        # {'x': <class 'int'>}
print(Product.__init__.__annotations__)  # {} — nothing yet to annotate
# A checker (mypy/pyright) is what turns annotations into errors.
- **Test focus:** No checking (theory). Reader-facing examples demonstrate __annotations__ contents and that an int variable can still be assigned a str at runtime without error, motivating static checkers.

</div>
