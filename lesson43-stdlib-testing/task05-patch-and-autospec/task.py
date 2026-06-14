"""patch(), patch.object & autospec: faking the clock, SMTP and files

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: import unittest
from unittest.mock import patch, mock_open, create_autospec
from erp.notify import Notifier

class NotifierTests(unittest.TestCase):
    @patch('erp.notify.smtplib.SMTP', autospec=True)
    def test_invoice_email_sent(self, smtp_cls):
        Notifier().send_invoice(invoice_id=1)
        smtp_cls.return_value.send_message.assert_called_once()
    # TODO: patch datetime.now, use mock_open for export, patch.dict os.environ

"""

# Your code here.
