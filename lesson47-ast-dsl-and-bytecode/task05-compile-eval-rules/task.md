# Execute rules via compile() + eval over a sandbox namespace

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.5 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compile a validated/rewritten AST into a code object
- Execute the code object against a restricted globals so no builtins leak
- Feed ERP record fields in as the eval locals/context
- Assemble the full safe pipeline: parse -> validate -> rewrite -> compile -> eval

## Python features introduced
`compile(tree, filename, 'eval')`, `code objects (types.CodeType)`, `eval(code, globals, locals)`, `restricted namespace ({'__builtins__': {}})`, `passing a context mapping as locals`, `PEP 695 type alias (type Context = ...)`, `separating validate -> rewrite -> compile -> eval pipeline`

## MiniERP increment
Delivers the rules engine: erp/rules/engine.py compile_rule(text) -> CodeObject and evaluate(code, context) -> bool. Discount, validation and report-filter rules now run from admin-authored text, executed safely against per-record context. This completes the ast rules-DSL milestone.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import ast, types
from .parse import parse_rule
from .validate import validate
from .rewrite import rewrite

type Context = dict[str, object]


def compile_rule(text: str) -> types.CodeType:
    """parse -> validate -> rewrite -> compile (mode 'eval'). Return code object."""
    raise NotImplementedError


def evaluate(code: types.CodeType, context: Context) -> object:
    """eval `code` with empty builtins and `context` as the names available."""
    raise NotImplementedError

- **Test focus:** Tests compile_rule returns a CodeType for valid rules and rejects unsafe ones (RuleError); tests evaluate computes correct booleans for varied contexts (e.g. quantity>=100 and customer_tier=='gold'); asserts builtins are unreachable (eval of a name like 'open' raises NameError).

</div>
