# Conditional skips, expected failures & test discovery

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 43.3 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Skip tests that cannot run in the current environment (missing optional dependency, wrong OS) without failing the suite
- Mark a known-broken behavior with expectedFailure so it is tracked but not red
- Understand how unittest discovers test modules and how to control the pattern
- See the relationship between TestLoader, TestSuite and TestCase

## Python features introduced
`@unittest.skip / @unittest.skipIf / @unittest.skipUnless`, `@unittest.expectedFailure`, `TestCase.skipTest at runtime`, `test discovery: python -m unittest discover -s tests -p 'test_*.py'`, `TestLoader / TestSuite basics`, `sys.platform and importlib.util.find_spec for skip conditions`, `__main__ guard running unittest.main()`

## MiniERP increment
Add tests/test_textui.py for the curses Text-UI helpers, skipped with skipUnless when curses/_curses is unavailable (e.g. on the grading machine) using importlib.util.find_spec, and mark one not-yet-implemented reporting feature with expectedFailure. Add a tests/__main__-style runner so the whole suite can be discovered and run as `python -m unittest discover`.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import importlib.util
import unittest

HAS_CURSES = importlib.util.find_spec('_curses') is not None

@unittest.skipUnless(HAS_CURSES, 'curses not available on this platform')
class TextUiTests(unittest.TestCase):
    def test_render_menu(self):
        ...  # TODO

- **Test focus:** Checks confirm the skip condition is computed (not hard-coded True/False), that an expectedFailure marker exists, and that `python -m unittest discover` collects every test module the lesson has produced so far.

</div>
