# Pre-configuring callables: partial & partialmethod

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 19.2 of 11  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Bind report parameters ahead of time with partial()
- Build named report variants (e.g. top-10 page) by freezing kwargs
- Attach pre-configured methods to a class with partialmethod
- Prefer partial over throwaway lambdas for readability

## Python features introduced
`functools.partial`, `freezing positional and keyword args`, `partial of a stdlib function`, `functools.partialmethod`, `partial as a clean alternative to lambdas`, `introspecting partial.func/args/keywords`

## MiniERP increment
Add pre-configured report builders to the reporting module: use functools.partial to derive first_page = partial(build_report, page_no=1) and SKU-scoped variants, and use partialmethod on a ReportService class to expose convenience methods like .top_sellers() built from the generic pipeline.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from functools import partial, partialmethod

# build_report(ledger, *, sku=None, page_no=None, page_size=50) from Lesson 2

def make_first_page(build_report):
    # TODO: return partial(build_report, page_no=1, page_size=10)
    ...

class ReportService:
    def report(self, *, sku=None, page_no=None):
        ...
    # TODO: top_sellers = partialmethod(report, page_no=1)

- **Test focus:** make_first_page returns a partial that injects page_no/page_size and forwards the rest; the partial's frozen keywords are introspectable; ReportService.top_sellers() dispatches to report() with the bound arguments.

</div>
