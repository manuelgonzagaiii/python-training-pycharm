"""Soft keywords & from __future__

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import keyword, ast


def is_soft_keyword(name: str) -> bool:
    """True if `name` is a soft keyword (usable as an identifier)."""
    raise NotImplementedError


def classify(node: ast.AST) -> str:
    """Use match/case on node type: 'compare', 'boolean', 'arithmetic', 'other'."""
    match node:
        case _:
            raise NotImplementedError

"""

# Your code here.
