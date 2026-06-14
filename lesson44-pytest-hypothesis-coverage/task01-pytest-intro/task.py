"""From unittest to pytest: plain assert & rich introspection

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import pytest
from erp.sales import Invoice, money

def test_discount_applied():
    inv = Invoice(customer_id=1)
    inv.add_line('SKU-1', qty=2, unit_price=money('10.00'))
    inv.apply_discount(0.10)
    assert inv.total() == pytest.approx(money('18.00'))

def test_negative_qty_rejected():
    with pytest.raises(ValueError):
        Invoice(customer_id=1).add_line('SKU-1', qty=-1, unit_price=money('1.00'))

"""

# Your code here.
