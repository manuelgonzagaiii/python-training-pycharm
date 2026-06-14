# Ordered data with bisect, heapq, and array

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.7 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Keep a list sorted and do O(log n) lookups/inserts with bisect (and the key= argument)
- Use heapq as a priority queue and for top-N queries (nlargest/nsmallest)
- Store large numeric series compactly with array.array and pick the right typecode
- Choose the right structure for ordered lookups vs priority vs compact numerics

## Python features introduced
`bisect.bisect_left / bisect_right / insort`, `maintaining a sorted list`, `key-based bisect (Python 3.10+ key= argument)`, `heapq (heappush, heappop, nlargest, nsmallest, heapify)`, `priority queue pattern`, `array.array (typed compact arrays)`, `array typecodes and memory efficiency`

## MiniERP increment
Speed up MiniERP queries: a price-sorted product index using bisect for range/threshold lookups, a low-stock alert queue using heapq (smallest-quantity-first) with top-N restock reports via nlargest/nsmallest, and a compact array.array of daily sales counts for the analytics series. Inventory and analytics now use fit-for-purpose structures.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/indexes.py with PriceIndex (bisect over a price-keyed list), LowStockQueue (heapq), and daily_series(counts) -> array.array; learner implements insert/lookup/top-N.
- **Test focus:** bisect index returns products under/over a price threshold and stays sorted on insert; heapq queue pops lowest-stock first and nlargest restock list is correct; array holds the typed series.

</div>
