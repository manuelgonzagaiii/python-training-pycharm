# Property-based testing with Hypothesis

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 44.4 of 5  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Express invariants ('total never negative', 'export then import is identity') instead of single examples
- Generate domain values with built-in and composite strategies, including Decimal money
- Use assume and @example to shape and pin inputs
- Read a shrunk counterexample and turn it into a fixed regression test
- Model a sequence of inventory operations with a stateful machine

## Python features introduced
`hypothesis @given`, `strategies: integers, decimals, text, lists, sampled_from, builds, composite`, `assume() to discard invalid inputs`, `@example for pinned regression cases`, `settings (max_examples, deadline) and profiles`, `shrinking to a minimal counterexample`, `stateful testing with RuleBasedStateMachine (intro)`

## MiniERP increment
Add tests/test_properties.py asserting MiniERP invariants: money arithmetic round-trips at 2dp, an invoice total equals the sum of its lines for any generated basket, and CSV export->import is a round-trip identity for arbitrary customer records. Add a small RuleBasedStateMachine that applies random receive/issue operations to Inventory and asserts quantity never goes negative — surfacing any invariant bug as a minimal counterexample.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from decimal import Decimal
from hypothesis import given, assume, strategies as st
from erp.money import money

money_st = st.decimals(min_value=0, max_value=10_000, places=2)

@given(a=money_st, b=money_st)
def test_money_addition_stays_2dp(a, b):
    total = money(a) + money(b)
    assert total == total.quantize(Decimal('0.01'))
# TODO: invoice-sum property, export/import round-trip, inventory state machine

- **Test focus:** Checks confirm @given with non-trivial strategies drives real domain code, at least one round-trip/invariant property and one @example or stateful machine exist, and the properties pass (Hypothesis finds no counterexample) against the current code.

</div>
