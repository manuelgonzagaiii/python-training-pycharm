"""Execute rules via compile() + eval over a sandbox namespace

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
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

"""

# Your code here.
