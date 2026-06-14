# Why containers? Sequences as the catalog's spine

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 5.1 of 6  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that a sequence is an ordered, indexable collection and that list/tuple/range/str all share one protocol
- Know the headline difference: list is mutable, tuple and range are immutable
- See where each sequence type will live in MiniERP (list of products, tuple per product record, range for ID generation)
- Read 0-based and negative indexing fluently

## Python features introduced
`list`, `tuple`, `range`, `sequence protocol`, `len()`, `indexing`, `0-based indexing`, `negative indexing`, `mutability vs immutability overview`

## MiniERP increment
Introduces the design decision for this phase: the catalog will be an in-memory list of product records (tuples), and explains the roadmap (dicts, sets, Counter come in later lessons). No code change yet — sets the architecture the next tasks implement.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py — the single evolving module for Phase 3.
# A product record is an ordered sequence of fields. This page explains WHY
# we pick a tuple for the record and a list for the collection.
#
# (No code to write on this page — read, then continue to the next task.)
- **Test focus:** No checks (theory page). Learner reads the concept intro for the sequence-based catalog design.

</div>
