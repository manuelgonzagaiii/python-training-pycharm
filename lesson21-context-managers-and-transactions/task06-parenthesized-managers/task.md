# Multiple & Parenthesized Context Managers

> **Phase:** Decorators, Context Managers, Descriptors & Metaclasses  •  **Stage:** 21.6 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Combine several managers in a single parenthesized with statement
- Reason about enter order (left-to-right) and exit order (reverse)
- See that Transaction + switch_actor compose cleanly so an audited, atomic, attributed operation reads as one block

## Python features introduced
`multiple managers in one with (comma-separated)`, `parenthesized context managers (PEP 617 grammar, 3.10+)`, `combining Transaction + switch_actor + redirect_stdout in one with`, `left-to-right enter, reverse exit ordering`, `line-wrapping long with statements`

## MiniERP increment
Composes the phase's managers into the service layer: a single `with (Transaction(repo), switch_actor('alice')):` block wraps a multi-step sale so it is atomic AND correctly attributed in the audit log — the capstone integration of Lessons 1 and 2.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** def checkout(repo, actor: str, cart) -> "Invoice":
    with (
        Transaction(repo) as tx_repo,
        switch_actor(actor),
    ):
        # TODO: reserve_stock(tx_repo, cart); invoice = create_invoice(...)
        #       any raise here rolls the whole thing back
        ...
    return invoice
- **Test focus:** Successful checkout commits all steps and audits them under the right actor; a failure in any step rolls back every prior step and propagates; exit order is reverse of enter order.

</div>
