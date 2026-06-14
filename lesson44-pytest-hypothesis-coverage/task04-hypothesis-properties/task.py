"""Property-based testing with Hypothesis

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from decimal import Decimal
from hypothesis import given, assume, strategies as st
from erp.money import money

money_st = st.decimals(min_value=0, max_value=10_000, places=2)

@given(a=money_st, b=money_st)
def test_money_addition_stays_2dp(a, b):
    total = money(a) + money(b)
    assert total == total.quantize(Decimal('0.01'))
# TODO: invoice-sum property, export/import round-trip, inventory state machine

"""

# Your code here.
