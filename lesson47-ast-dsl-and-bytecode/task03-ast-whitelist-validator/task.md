# Lock the DSL down with a NodeVisitor whitelist

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.3 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Implement a deny-by-default validator that only permits a safe node set
- Explain why allowlisting node types beats blocklisting strings
- Forbid calls, attribute access to dunders, comprehensions and lambdas in rules
- Produce clear errors pointing at the offending construct

## Python features introduced
`ast.NodeVisitor`, `allowlist of permitted node types`, `rejecting Call/Import/Attribute-on-dunder/Lambda/Subscript-of-callables`, `raising a custom RuleError on disallowed nodes`, `visiting operator nodes (Add, Lt, Eq, And, Or, Not, In)`, `isinstance node checks`

## MiniERP increment
erp/rules/validate.py validates every admin rule before it is ever executed: only comparisons, boolean/arithmetic ops, names and constants are allowed. Function calls, imports, attribute traversal into dunders, and assignments are rejected — the safety gate for the whole rules engine.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import ast


class RuleError(ValueError):
    """Raised when a rule uses a construct outside the safe subset."""


ALLOWED = (
    ast.Expression, ast.BoolOp, ast.BinOp, ast.UnaryOp, ast.Compare,
    ast.Name, ast.Load, ast.Constant, ast.And, ast.Or, ast.Not,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod,
    ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.In, ast.NotIn,
)


class Validator(ast.NodeVisitor):
    def generic_visit(self, node: ast.AST) -> None:
        """Raise RuleError unless type(node) is in ALLOWED, then recurse."""
        raise NotImplementedError


def validate(tree: ast.Expression) -> ast.Expression:
    """Validate and return the tree, or raise RuleError."""
    raise NotImplementedError

- **Test focus:** Tests validate accepts safe rules (comparisons, and/or/not, arithmetic, names, constants, in) and raises RuleError for Call ('f()'), attribute access, subscripts, lambdas, comprehensions, assignments/walrus, and __dunder names.

</div>
