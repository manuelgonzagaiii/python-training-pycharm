# Checkpoint: introspection model

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.9 of 9  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Confirm understanding of when signature.bind raises vs succeeds
- Distinguish NotImplemented (singleton return) from NotImplementedError (exception)
- Recall that a MappingProxyType is a live view, not a copy
- Recall safe dynamic-dispatch guarding rules

## Python features introduced
`inspect.signature vs getfullargspec`, `getattr/hasattr/callable semantics`, `MappingProxyType immutability`, `NotImplemented vs NotImplementedError`, `Ellipsis identity`, `monkeypatch restore semantics`

## MiniERP increment
Knowledge check consolidating the registry/introspection layer; no code change. Ensures learners hold the mental model before the AST DSL builds on it.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice checkpoint — no code.
# Questions cover: MappingProxyType (live view vs copy), NotImplemented vs
# NotImplementedError, what Signature.bind raises, Ellipsis identity, and
# why dynamic dispatch must reject private/dunder names.

- **Test focus:** No unit test (choice task). Author supplies choice_options with the correct answers in task-info.yaml.

</div>
