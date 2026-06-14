# Memoizing expensive reports: lru_cache & cache

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.3 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Memoize a pure, expensive aggregation with lru_cache
- Inspect hits/misses via cache_info() and reset with cache_clear()
- Use functools.cache as the unbounded shorthand
- Understand arguments must be hashable and the function must be pure

## Python features introduced
`functools.lru_cache`, `lru_cache(maxsize=...)`, `functools.cache (unbounded)`, `cache_info()/cache_clear()`, `hashable-arguments requirement`, `caching pure aggregation functions`, `typed= parameter`

## MiniERP increment
Cache MiniERP's costly monthly_summary(year, month) aggregation in the analytics module with lru_cache(maxsize=128), exposing cache_info()/cache_clear() so the dashboard avoids recomputing repeated report queries, and note why mutable ledgers must invalidate the cache.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from functools import lru_cache

@lru_cache(maxsize=128)
def monthly_summary(year, month):
    """Expensive pure aggregation — memoized on (year, month)."""
    # TODO: compute and return the summary; arguments must be hashable
    ...

# monthly_summary.cache_info() / monthly_summary.cache_clear() are now available

- **Test focus:** Repeated calls with the same args hit the cache (cache_info hits increment, body runs once); cache_clear resets stats; distinct args miss then cache; verifies pure/hashable usage.

</div>
