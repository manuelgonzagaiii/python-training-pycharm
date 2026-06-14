"""Read the bytecode with dis

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from __future__ import annotations
import dis, types


def opnames(code: types.CodeType) -> list[str]:
    """Return the ordered list of opcode names in `code` via dis.get_instructions."""
    raise NotImplementedError


def explain(code: types.CodeType) -> str:
    """Return a human-readable disassembly string for `code` (dis.Bytecode)."""
    raise NotImplementedError

"""

# Your code here.
