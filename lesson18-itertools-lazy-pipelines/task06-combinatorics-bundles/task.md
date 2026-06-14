# product, permutations, combinations for bundles

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 18.6 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a size x color variant matrix with product()
- Enumerate product bundles with combinations() (order-independent)
- Distinguish permutations (ordered) from combinations (unordered)
- Use combinations_with_replacement and product(repeat=...)

## Python features introduced
`itertools.product`, `itertools.permutations`, `itertools.combinations`, `combinations_with_replacement`, `repeat= argument to product`, `r-length subsequences`, `Cartesian product for variant matrices`

## MiniERP increment
Add catalog helpers to Products & Inventory: variant_skus(sizes, colors) uses product() to generate every variant SKU, and possible_bundles(products, k) uses combinations() to enumerate k-item bundle offers for the sales module.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from itertools import product, combinations

def variant_skus(base, sizes, colors):
    """Yield 'BASE-SIZE-COLOR' for every size/color combination."""
    # TODO: use product(sizes, colors)
    ...

def possible_bundles(products, k):
    """Yield every unordered k-product bundle using combinations."""
    # TODO: use combinations(products, k)
    ...

- **Test focus:** variant_skus produces every size x color SKU exactly once; possible_bundles yields the correct count of unordered k-combinations with no duplicates and no reordered repeats; both lazy.

</div>
