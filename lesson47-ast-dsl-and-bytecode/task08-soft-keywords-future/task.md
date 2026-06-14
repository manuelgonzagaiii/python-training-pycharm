# Soft keywords & from __future__

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.8 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain how soft keywords stay usable as ordinary identifiers (match/case/type)
- Enumerate soft keywords via keyword.softkwlist and contrast with hard keywords
- Understand what `from __future__ import annotations` changes at compile time
- Recognize __future__ as the mechanism that gated past syntax changes

## Python features introduced
`soft keywords (match, case, type, _ in match)`, `match/case as soft-keyword example (still valid as identifiers)`, `from __future__ import annotations`, `__future__ module / _Feature flags`, `keyword.kwlist vs keyword.softkwlist`, `PEP 563 deferred annotation evaluation`

## MiniERP increment
Adds a tiny rule-kind classifier in the engine that uses match/case to route a parsed rule by node shape, and confirms a column literally named 'match' or 'type' in imported data still works as an identifier — proving the DSL coexists with soft keywords.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import keyword, ast


def is_soft_keyword(name: str) -> bool:
    """True if `name` is a soft keyword (usable as an identifier)."""
    raise NotImplementedError


def classify(node: ast.AST) -> str:
    """Use match/case on node type: 'compare', 'boolean', 'arithmetic', 'other'."""
    match node:
        case _:
            raise NotImplementedError

- **Test focus:** Tests is_soft_keyword is True for 'match'/'case'/'type' and False for 'if'/'for'/'xyz' using keyword.softkwlist; tests classify routes ast.Compare/BoolOp/BinOp/other to the right labels via match/case; asserts a variable named match/type still binds normally.

</div>
