# Running totals & windows: accumulate, pairwise

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 18.4 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Compute a running revenue total with accumulate()
- Pass a custom binary function (and operator.add) to accumulate
- Use pairwise() to compute period-over-period deltas
- Use the initial= seed and reason about output length

## Python features introduced
`itertools.accumulate`, `accumulate with a binary func`, `itertools.pairwise`, `operator.add / operator.mul as accumulate funcs`, `initial= argument to accumulate`, `sliding-window deltas`

## MiniERP increment
Add cumulative_revenue(daily_totals) and period_deltas(daily_totals) to the analytics module: accumulate() yields the running revenue curve and pairwise() yields day-over-day change — feeding the dashboard's trend line without storing the whole series.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from itertools import accumulate, pairwise
from operator import add

def cumulative_revenue(daily_totals):
    """Lazy running total of a sequence of daily revenue figures."""
    # TODO: use accumulate (try operator.add) to yield the running sum
    ...

def period_deltas(daily_totals):
    """Yield (prev, curr, curr-prev) for each adjacent pair using pairwise."""
    # TODO: use pairwise to walk adjacent days
    ...

- **Test focus:** cumulative_revenue yields the correct running sums (and matches when using operator.add); period_deltas yields correct adjacent pairs and deltas with the right output length; both stay lazy.

</div>
