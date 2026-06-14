"""Isolating units with Mock, MagicMock & side_effect

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import unittest
from unittest.mock import Mock
from erp.payments import PaymentService, GatewayTimeout

class PaymentServiceTests(unittest.TestCase):
    def test_successful_charge_records_payment(self):
        gateway = Mock()
        gateway.charge.return_value = {'auth': 'OK123'}
        service = PaymentService(gateway=gateway)
        service.pay(invoice_id=1, amount='25.00')
        gateway.charge.assert_called_once_with(amount='25.00')
    # TODO: second test with side_effect=GatewayTimeout

"""

# Your code here.
