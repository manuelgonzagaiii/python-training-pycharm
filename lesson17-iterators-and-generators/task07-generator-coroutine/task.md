# Generators as coroutines: send, throw, close

> **Phase:** Iterators, Generators & Functional Tools  •  **Stage:** 17.7 of 8  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use yield as an expression to receive values pushed in with send()
- Prime a coroutine before sending it data
- Inject exceptions with throw() and handle GeneratorExit on close()
- Build a running-total accumulator coroutine that holds state between sends

## Python features introduced
`generator.send()`, `value of a yield expression`, `priming a generator (first next/send None)`, `generator.throw()`, `generator.close()`, `GeneratorExit`, `try/finally cleanup in generators`, `stateful accumulator coroutine`

## MiniERP increment
Add a running_total() coroutine to the reporting module that you feed sale amounts into via send() and that emits the running revenue total after each — used by the live dashboard to update totals incrementally; close() flushes a final summary via try/finally.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def running_total():
    """Coroutine: send() an amount, receive the running total back."""
    total = 0.0
    try:
        while True:
            amount = yield total      # value arrives via .send(amount)
            # TODO: add amount to total so the NEXT yield returns the new running total
            ...
    except GeneratorExit:
        # TODO: final cleanup/flush when .close() is called
        ...

- **Test focus:** Coroutine must be primed; each send(amount) returns the correct running total; throw() surfaces an injected error; close() triggers the GeneratorExit/finally path without raising.

</div>
