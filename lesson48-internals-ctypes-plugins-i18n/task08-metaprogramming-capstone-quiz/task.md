# Checkpoint: internals & extensibility

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 48.8 of 10  •  **Type:** `choice`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Confirm when gc (not refcounting) is required to reclaim memory
- Recall that a WeakValueDictionary entry disappears when the value is unreferenced
- Recall that memoryview slicing is zero-copy
- Recall how entry points decouple plugins from core and how gettext falls back

## Python features introduced
`sys.intern identity effects`, `gc cycle collection vs refcounting`, `weakref WeakValueDictionary semantics`, `memoryview zero-copy`, `entry-point plugin discovery`, `gettext fallback / locale categories`

## MiniERP increment
Final knowledge check for the phase — consolidates internals, ctypes, plugins and i18n. No code change; verifies the learner can reason about the extensibility and runtime layer they built.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Multiple-choice checkpoint — no code.
# Questions cover: why cycles need gc.collect, WeakValueDictionary eviction,
# memoryview zero-copy, entry-point plugin discovery decoupling, and gettext
# NullTranslations fallback behavior.

- **Test focus:** No unit test (choice task). Author supplies choice_options with correct answers in task-info.yaml.

</div>
