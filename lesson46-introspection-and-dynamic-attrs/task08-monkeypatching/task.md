# Monkeypatching for hotfixes and tests

> **Phase:** Metaprogramming, Internals & Rare Corners  •  **Stage:** 46.8 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Swap a function or method at runtime and restore it deterministically
- Build a scoped patch context manager so changes never leak between tests
- Apply a controlled hotfix to a misbehaving ERP routine without editing its source
- Understand the risks of monkeypatching and when mock.patch is the better tool

## Python features introduced
`runtime attribute replacement (setattr on modules/classes)`, `saving and restoring originals`, `contextlib.contextmanager for scoped patches`, `function/method substitution`, `monkeypatch ethics & blast radius`, `unittest.mock.patch comparison (OSS preview)`

## MiniERP increment
Adds erp/patching.py with a patched(target, attr, new) context manager used to apply an emergency hotfix to a faulty tax-rounding function at runtime and to inject deterministic clocks/IDs in tests — restoring the original on exit.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from __future__ import annotations
import contextlib


@contextlib.contextmanager
def patched(target, attr: str, new):
    """Temporarily set target.attr = new, restoring the original on exit.

    Handle the case where the attribute did not previously exist.
    """
    raise NotImplementedError

- **Test focus:** Tests patched swaps a module-level function and a class method, that calls inside the block see the new behavior, and the original is restored after the block even on exception; tests the not-previously-set attribute case is removed on exit.

</div>
