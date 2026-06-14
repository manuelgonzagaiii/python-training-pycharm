# Capstone: End-to-End Integration Across All Four Interfaces

> **Phase:** Packaging, Distribution & Capstone Release  •  **Stage:** 51.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Drive one complete business flow — create product, add stock, register customer, raise invoice, take payment, run a report, read the audit log — across CLI, Web, GUI-service and TUI-service paths
- Prove all four interfaces operate on the *same shared core* and yield consistent state
- Use a throwaway SQLite database and proper seed/teardown for a hermetic test
- Aggregate independent assertions and surface them together (ExceptionGroup/except*)

## Python features introduced
`integration testing`, `subprocess (drive the CLI / frozen exe)`, `http.client or httpx (drive the web API)`, `shared service-layer calls (gui/tui paths)`, `temp SQLite DB fixtures (tempfile)`, `seed & teardown`, `asserting cross-interface consistency`, `ExceptionGroup for aggregated checks`

## MiniERP increment
The capstone integration: a single end-to-end test that exercises MiniERP's full sales-to-payment-to-report flow through every front-end and asserts the shared core stays consistent — the definitive proof that the assembled, packaged MiniERP works as one product before release.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide a fixtured run_business_flow(interface) harness and assert_consistent(states); learner wires the per-interface drivers (subprocess CLI, http client web, direct service for gui/tui) and the cross-checks.
- **Test focus:** The flow completes on each interface against a temp DB; final product stock, invoice balance, payment total, report figures and audit entries match across all four; failures aggregate via ExceptionGroup.

</div>
