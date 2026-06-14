"""Rewrite rules with a NodeTransformer

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import ast

ALIASES = {"total": "order_total", "qty": "quantity", "tier": "customer_tier"}


class AliasRewriter(ast.NodeTransformer):
    def visit_Name(self, node: ast.Name) -> ast.AST:
        """Replace aliased names per ALIASES, preserving location."""
        raise NotImplementedError


def rewrite(tree: ast.Expression) -> ast.Expression:
    """Apply AliasRewriter and fix locations; return the new tree."""
    raise NotImplementedError

"""

# Your code here.
