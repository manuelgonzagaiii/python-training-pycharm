# patch(), patch.object & autospec: faking the clock, SMTP and files

> **Phase:** Testing, Quality & Tooling  •  **Stage:** 43.5 of 6  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Patch a name in the module under test rather than where it is defined
- Use patch as both a decorator and a context manager and understand the injected mock argument order
- Make a mock that respects the real signature with autospec so wrong calls fail in the test
- Fake the clock, environment variables, and file I/O for deterministic tests

## Python features introduced
`unittest.mock.patch (decorator and context-manager forms)`, `patch.object`, `patch.dict`, `the 'where to patch' rule (patch where a name is looked up)`, `autospec=True / create_autospec for signature-faithful mocks`, `mock_open for filesystem reads/writes`, `freezing time by patching datetime.now / time.time`

## MiniERP increment
Add tests/test_notifications.py for the invoice-email notifier and tests/test_export.py for CSV export. patch the SMTP client (with autospec against the real send_message signature), patch datetime.now so the generated invoice timestamp is deterministic, use mock_open to assert the CSV written for an export, and patch.dict on os.environ to fake the configured sender address.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** import unittest
from unittest.mock import patch, mock_open, create_autospec
from erp.notify import Notifier

class NotifierTests(unittest.TestCase):
    @patch('erp.notify.smtplib.SMTP', autospec=True)
    def test_invoice_email_sent(self, smtp_cls):
        Notifier().send_invoice(invoice_id=1)
        smtp_cls.return_value.send_message.assert_called_once()
    # TODO: patch datetime.now, use mock_open for export, patch.dict os.environ

- **Test focus:** Checks confirm patch targets the module-under-test namespace (not the stdlib origin), autospec is used somewhere, time is frozen via patching, and mock_open/patch.dict are each used once against real export/config code.

</div>
