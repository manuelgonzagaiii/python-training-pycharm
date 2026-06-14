"""Parse and walk a syntax tree

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
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

"""

# Your code here.
