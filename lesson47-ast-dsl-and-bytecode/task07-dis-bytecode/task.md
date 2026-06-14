# Read the bytecode with dis

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 47.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Disassemble a compiled rule to see the opcodes Python will run
- Read code-object attributes (co_consts/co_names) that bytecode references
- Iterate instructions programmatically with dis.Bytecode/get_instructions
- Use disassembly as a debugging/teaching aid for the rules engine

## Python features introduced
`dis.dis`, `dis.Bytecode`, `dis.Instruction (opname, argval, offset)`, `code object attributes (co_consts, co_names, co_varnames, co_code)`, `dis.get_instructions`, `stack-machine model intro`

## MiniERP increment
Adds an admin diagnostics command `rule explain <text>` that compiles a rule and prints its disassembly plus referenced names — helping operators understand and debug what a rule actually does.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import dis, types


def opnames(code: types.CodeType) -> list[str]:
    """Return the ordered list of opcode names in `code` via dis.get_instructions."""
    raise NotImplementedError


def explain(code: types.CodeType) -> str:
    """Return a human-readable disassembly string for `code` (dis.Bytecode)."""
    raise NotImplementedError

- **Test focus:** Tests opnames returns a non-empty ordered list including comparison/boolean opcodes for a compiled rule; tests explain produces a string containing recognizable opnames; verifies it works on a code object from compile_rule.

</div>
