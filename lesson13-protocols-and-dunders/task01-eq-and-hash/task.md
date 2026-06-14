# Value Equality and Hashing

> **Phase:** OOP Foundations  •  **Stage:** 13.1 of 10  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement __eq__ comparing by value with an isinstance guard, returning NotImplemented for foreign types
- Implement a consistent __hash__ over the same fields so equal objects hash equal
- Understand the contract: defining __eq__ without __hash__ makes a class unhashable
- Use the objects safely in sets and as dict keys

## Python features introduced
`__eq__`, `__hash__`, `NotImplemented sentinel`, `isinstance guard in __eq__`, `hashing a tuple of fields`, `set/dict membership`, `identity vs equality`

## MiniERP increment
Make Money and Product compare by value and hash on their identifying fields (Money on cents+currency, Product on sku), so the catalog can deduplicate products in a set and use Money as dict keys in reports.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** class Money:
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        ...  # compare cents and currency

    def __hash__(self) -> int:
        ...  # hash((self.cents, self.currency))
- **Test focus:** Assert two Money with same cents+currency are equal and have equal hashes; assert unequal currencies compare unequal; assert a set dedupes equal Products; assert comparing to a non-Money returns NotImplemented (so == yields False, not an error).

</div>
