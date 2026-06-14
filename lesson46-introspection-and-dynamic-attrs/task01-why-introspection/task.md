# Why a program inspects itself

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.1 of 9  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain what introspection and metaprogramming mean and when they pay off
- Understand that ERP services, methods and modules are all inspectable objects
- Recognize the trade-offs (power, indirection, debuggability) of dynamic code
- Preview the phase: registry -> rules-DSL -> plugins -> internals -> i18n

## Python features introduced
`introspection concept`, `everything-is-an-object model`, `__dict__ and attribute model`, `metaprogramming vs ordinary code`, `type() / object identity recap`

## MiniERP increment
Frames the phase: the existing tested ERP service layer will be made self-describing so a single generic dispatcher can drive CLI/Web/TUI instead of four hand-written command tables. No code change yet — sets the architectural goal.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Theory task — no code to write.
# Read the description, then open the ERP service module from the previous
# phase and notice: every service is a class, every command is a method,
# every method has a signature. The next tasks make the program read that.

- **Test focus:** No automated test (theory page). Concept-only intro to introspection and the phase roadmap.

</div>
