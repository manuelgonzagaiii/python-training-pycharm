# Parse and walk a syntax tree

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.2 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Turn rule source text into an AST and read its structure with ast.dump
- Walk the tree and identify node categories that appear in rules
- Override visit_X methods on a NodeVisitor to react to specific nodes
- Build the mental map needed to validate and transform rules

## Python features introduced
`ast.parse (mode='eval')`, `ast.dump`, `ast node types (Expression, BinOp, Compare, BoolOp, Name, Constant, Attribute)`, `ast.walk`, `ast.iter_child_nodes`, `node fields (_fields)`, `ast.NodeVisitor (generic_visit, visit_X)`

## MiniERP increment
Adds erp/rules/parse.py: parse_rule(text) returns an ast.Expression for a rule, plus a NodeVisitor that collects the set of Name/Attribute identifiers a rule references — the basis for the safety whitelist and for telling admins which fields a rule depends on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import ast


def parse_rule(text: str) -> ast.Expression:
    """Parse a single rule expression in eval mode."""
    raise NotImplementedError


class NameCollector(ast.NodeVisitor):
    """Collect referenced identifier names (Name + dotted Attribute roots)."""
    def __init__(self) -> None:
        self.names: set[str] = set()
    def visit_Name(self, node: ast.Name) -> None:
        raise NotImplementedError


def referenced_names(text: str) -> set[str]:
    raise NotImplementedError

- **Test focus:** Tests parse_rule returns an ast.Expression for valid rules and raises SyntaxError otherwise; tests referenced_names collects all Name identifiers from comparisons/boolean expressions and walks into Attribute access; verifies generic_visit recursion reaches nested nodes.

</div>
