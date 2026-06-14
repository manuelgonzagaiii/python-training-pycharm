# Your first TestCase: locking in inventory behavior

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 43.1 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand what an automated test is and why a regression suite matters for a multi-interface app
- Write a unittest.TestCase subclass with test_* methods
- Use the core assertions assertEqual/assertTrue and the assertRaises context manager
- Run tests with `python -m unittest` and read pass/fail/error output
- Test the existing domain layer (not a toy function) so the suite has real value

## Python features introduced
`unittest`, `unittest.TestCase`, `TestCase.assertEqual`, `TestCase.assertTrue`, `TestCase.assertRaises (context-manager form)`, `python -m unittest`, `test method naming convention (test_*)`, `AAA arrange-act-assert structure`, `import of the existing erp package under test`

## MiniERP increment
Create the project's first real test module, tests/test_inventory.py, exercising the existing Product/Inventory domain objects: adding stock, removing stock, and that removing more than available raises the domain's InsufficientStock error. Establishes the tests/ package that the rest of the phase grows.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import unittest
from erp.inventory import Inventory, InsufficientStock

class InventoryTests(unittest.TestCase):
    def test_receive_increases_quantity(self):
        inv = Inventory()
        inv.receive('SKU-1', 10)
        self.assertEqual(inv.quantity('SKU-1'), 10)
    # TODO: test removing stock, and that over-issue raises InsufficientStock

- **Test focus:** Author's hidden checks confirm the learner's test module actually imports and exercises the real Inventory class, uses assertEqual/assertRaises correctly, and that running `python -m unittest` discovers and passes at least the three required behaviors.

</div>
