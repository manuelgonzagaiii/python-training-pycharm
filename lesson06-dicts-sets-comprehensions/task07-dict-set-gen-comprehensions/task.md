# Dict, set & generator comprehensions; the walrus

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 6.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a dict and a set with comprehensions in one expression each
- Stream over a generator expression to compute an aggregate without a temp list
- Use := to compute-and-reuse a value inside a comprehension filter
- Choose a generator over a list when only an aggregate is needed

## Python features introduced
`dict comprehension`, `set comprehension`, `generator expression`, `lazy evaluation`, `sum() over a generator`, `walrus operator := inside a comprehension`, `walrus in an if-guard`, `any()/all() over generators`, `memory: generator vs list`

## MiniERP increment
Adds price_index(catalog) (dict comprehension sku->price), all_tags(tags_index) (set comprehension union), and inventory_value(catalog) (generator expression summed; uses := to capture line totals) — completing the phase's core reporting set.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
def price_index(catalog: list[Product]) -> dict[str, int]:
    """sku -> price_cents, via dict comprehension."""
    ...

def all_tags(tags_index: dict[str, set[str]]) -> set[str]:
    """Every tag used anywhere, via set comprehension."""
    ...

def inventory_value(catalog: list[Product]) -> int:
    """Total value (sum of price*qty) via a generator expression; use := for the line total."""
    ...
- **Test focus:** price_index maps each sku to its price; all_tags is the deduped union of every tag set; inventory_value equals sum of price_cents*qty over all products and is computed via a generator (not an intermediate list).

</div>
