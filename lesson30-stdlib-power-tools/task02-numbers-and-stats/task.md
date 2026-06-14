# Math and statistics for reporting

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.2 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use math.fsum/isclose to avoid floating-point accumulation and comparison bugs in totals
- Compute summary statistics (mean, median, stdev, quantiles) with the statistics module
- Pick the right rounding helper (ceil/floor) for pricing and quantities
- Understand when floats are acceptable vs when to escalate to Decimal

## Python features introduced
`math (isclose, fsum, ceil, floor, gcd, prod)`, `statistics (mean, median, mode, pstdev, stdev, quantiles)`, `decimal awareness vs float pitfalls`, `math.isclose for money comparisons`, `fractions module mention`

## MiniERP increment
Add a reporting helpers module: sales statistics over a list of invoice totals (mean/median order value, stdev, quantiles) and a safe summation using math.fsum, plus isclose-based money equality. Feeds MiniERP's analytics module with trustworthy aggregates.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/analytics.py with order_value_stats(totals) and total_revenue(invoices); learner implements them with statistics + math.fsum/isclose.
- **Test focus:** order_value_stats returns correct mean/median/stdev/quantiles; total_revenue uses fsum and matches an isclose-compared expected; empty-input handled.

</div>
