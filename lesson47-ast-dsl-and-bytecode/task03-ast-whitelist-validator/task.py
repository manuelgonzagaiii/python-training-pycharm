"""Lock the DSL down with a NodeVisitor whitelist

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
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

"""

# Your code here.
