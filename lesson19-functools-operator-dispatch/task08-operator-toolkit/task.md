# The operator module as first-class functions

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.8 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use attrgetter/itemgetter as sort and groupby keys
- Use methodcaller to call a method across a stream
- Feed operator.add into reduce/accumulate instead of lambdas
- Sort by multiple fields with a single multi-arg getter

## Python features introduced
`operator.itemgetter`, `operator.attrgetter`, `operator.methodcaller`, `operator.add/mul/lt etc.`, `operator funcs as sort/reduce/map keys`, `multi-field itemgetter/attrgetter`, `replacing lambdas with operator`

## MiniERP increment
Refactor the analytics module's sorting/grouping/folding to use the operator module throughout: attrgetter for report keys, multi-field attrgetter for tie-broken top-seller ordering, methodcaller to normalize rows, and operator.add in the reducers — making the aggregation layer lambda-free and faster.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from operator import attrgetter, itemgetter, methodcaller, add
from functools import reduce

def top_sellers(rows, n):
    """Sort ProductSales rows by revenue desc, then sku asc; return top n."""
    # TODO: sorted(..., key=attrgetter('revenue','sku')) then reverse appropriately
    ...

def total(amounts):
    # TODO: reduce(add, amounts, 0.0)
    ...

- **Test focus:** attrgetter/itemgetter keys sort correctly including multi-field tie-breaks; methodcaller applies the method across the stream; reduce(add, ...) matches sum; results equal the earlier lambda-based versions.

</div>
