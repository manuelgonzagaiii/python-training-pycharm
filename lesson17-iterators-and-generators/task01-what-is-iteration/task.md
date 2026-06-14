# How for-loops actually work

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.1 of 8  •  **Type:** `theory`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Understand that a for-loop calls iter() once then next() repeatedly until StopIteration
- Distinguish an iterable (has __iter__) from an iterator (has __iter__ and __next__)
- See that lists, dicts, files and generators are all just iterables
- Motivate laziness: why streaming rows beats building a giant list in memory for ERP reports

## Python features introduced
`iterable vs iterator distinction`, `iter() built-in`, `next() built-in`, `StopIteration`, `for-loop desugaring`, `__iter__ and __next__ protocol overview`, `for-else (conceptual)`

## MiniERP increment
No code change yet: read-only concept page that frames the phase by showing how MiniERP's current eager report (which builds a full list of all sales lines before returning) wastes memory, and previews the lazy streaming pipeline the lesson will build on top of the existing domain model.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # Theory page only — no code to write.
# Illustration shown in the description (you will NOT edit this):
#
#   sales = [line_a, line_b, line_c]
#   it = iter(sales)        # for-loop step 1: get an iterator
#   next(it)                # -> line_a   (for-loop step 2..n)
#   next(it)                # -> line_b
#   next(it)                # -> line_c
#   next(it)                # raises StopIteration -> loop ends

- **Test focus:** None (theory task: no automated checking).

</div>
