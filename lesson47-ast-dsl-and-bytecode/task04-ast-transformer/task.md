# Rewrite rules with a NodeTransformer

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Transform an AST by returning new nodes from visit_X methods
- Rewrite friendly field aliases (e.g. 'total') to canonical names ('order.total')
- Keep source locations valid with copy_location/fix_missing_locations
- Round-trip the modified tree back to source with ast.unparse

## Python features introduced
`ast.NodeTransformer`, `visit_X returning a replacement node`, `ast.copy_location`, `ast.fix_missing_locations`, `constant folding / alias rewriting`, `ast.unparse to view the result`

## MiniERP increment
erp/rules/rewrite.py normalizes rules before compilation: admin-friendly aliases are rewritten to canonical context keys, and obviously-constant subexpressions are folded — so rules are stored in a canonical, faster form.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import ast

ALIASES = {"total": "order_total", "qty": "quantity", "tier": "customer_tier"}


class AliasRewriter(ast.NodeTransformer):
    def visit_Name(self, node: ast.Name) -> ast.AST:
        """Replace aliased names per ALIASES, preserving location."""
        raise NotImplementedError


def rewrite(tree: ast.Expression) -> ast.Expression:
    """Apply AliasRewriter and fix locations; return the new tree."""
    raise NotImplementedError

- **Test focus:** Tests AliasRewriter replaces aliased identifiers and leaves others untouched; tests rewrite returns a valid tree whose ast.unparse shows canonical names; asserts locations are fixed so the result compiles.

</div>
