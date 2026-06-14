# Lambdas, Sort Keys, and Higher-Order Builtins

> **Phase:** Control Flow & Functions  •  **Stage:** 10.4 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Write small anonymous functions with lambda for keys and predicates
- Sort and select cart lines by computed keys
- Use map/filter/any/all/enumerate/zip to express bulk operations declaratively

## Python features introduced
`lambda expressions`, `sorted() with key=`, `min()/max() with key=`, `map()`, `filter()`, `any()/all()`, `enumerate()`, `zip()`, `operator vs lambda key choice`

## MiniERP increment
Add reporting helpers to rules.py: rank_lines(lines) sorts cart lines by line total via sorted(key=lambda ...), cheapest_line/dearest_line use min/max with keys, line_numbers uses enumerate, and any_over_limit uses any() — the analytics primitives the Reporting module will surface.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def rank_lines(lines: list[tuple[str, float, int]]) -> list[tuple[str, float, int]]:
    """Sort lines by line total (price*qty) descending using sorted(key=lambda ...)."""
    ...


def any_over_limit(lines: list[tuple[str, float, int]], limit: float) -> bool:
    """True if any line total exceeds limit (use any() with a generator/lambda)."""
    ...
- **Test focus:** rank_lines orders by descending line total; min/max pick the right extremes; any_over_limit is True only when some line exceeds the limit; enumerate numbering is 1-based as specified.

</div>
