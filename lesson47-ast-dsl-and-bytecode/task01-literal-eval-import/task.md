# Safe data parsing with ast.literal_eval

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.1 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Parse user/imported literal data safely without executing arbitrary code
- Articulate exactly why eval(input) is a security hole and literal_eval is not
- Handle malformed literals with precise exception types
- Use literal_eval to read simple config/import values

## Python features introduced
`ast.literal_eval`, `why eval() on input is dangerous`, `literal vs expression distinction`, `ValueError/SyntaxError handling`, `parsing nested literals (dict/list/tuple)`

## MiniERP increment
Hardens the ERP import/export path: literal-typed cells and a small inline-literal config format are parsed with ast.literal_eval instead of eval, closing a code-injection vector in data import.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import ast


def parse_literal(text: str) -> object:
    """Safely parse a Python literal (int/float/str/bool/None/list/dict/tuple).

    Raise ValueError for anything that is not a pure literal.
    """
    raise NotImplementedError

- **Test focus:** Tests parse_literal accepts ints, floats, strings, None/bool, nested list/dict/tuple; asserts it raises ValueError for names, calls, operators, and syntactically invalid input (e.g. '__import__("os")', '1+1', 'open').

</div>
