# Isolating units with Mock, MagicMock & side_effect

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 43.4 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Replace a real collaborator with a Mock so a unit test does not hit the network, a clock, or the disk
- Program a mock's return_value and side_effect, including raising exceptions and returning a sequence
- Verify interactions: that the code under test called the collaborator correctly
- Distinguish Mock from MagicMock (dunder support)

## Python features introduced
`unittest.mock.Mock`, `unittest.mock.MagicMock`, `return_value`, `side_effect (value, exception, iterable, callable)`, `assert_called_once_with / assert_called / call_count / call_args`, `mock.call and call-list assertions`, `configuring nested attributes/methods on a Mock`

## MiniERP increment
Add tests/test_payments.py for the Payments service. The external payment gateway is replaced by a Mock whose charge() returns a fake authorization, then a Mock whose side_effect raises a GatewayTimeout so you can test the retry/failure path — verifying the service recorded the payment and wrote the audit entry exactly once via assert_called_once_with.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import unittest
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

- **Test focus:** Checks confirm a Mock/MagicMock is injected as the gateway, that both return_value and side_effect (raising) paths are tested, and that an interaction assertion (assert_called_once_with / call_args) is present.

</div>
