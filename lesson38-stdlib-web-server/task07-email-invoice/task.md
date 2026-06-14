# Emailing an invoice with email + smtplib

> **Phase:** Networking & the Web  •  **Stage:** 38.7 of 7  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Build a multipart email with plain-text and HTML alternatives and an attachment
- Set standard headers (From/To/Subject/Message-ID) correctly
- Send the message via smtplib.SMTP.send_message
- Test email end-to-end against a local OSS SMTP sink (aiosmtpd) instead of a real provider

## Python features introduced
`email.message.EmailMessage`, `set_content / add_alternative (text + HTML)`, `add_attachment with maintype/subtype (PDF/CSV bytes)`, `smtplib.SMTP`, `send_message`, `MIME multipart structure`, `email.utils.formataddr / make_msgid`, `talking to a local aiosmtpd server (OSS)`

## MiniERP increment
Adds erp/mail/invoice_mail.py: builds an invoice email (text + HTML body, optional CSV/PDF attachment) from a Sales invoice and sends it through smtplib. Delivers the phase's 'email invoices to a local OSS mail server' milestone; the service layer logs the send to the audit log.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** from email.message import EmailMessage
import smtplib

def build_invoice_email(invoice, sender, recipient) -> EmailMessage:
    msg = EmailMessage()
    msg["Subject"] = f"Invoice {invoice.number}"
    msg["From"] = sender
    msg["To"] = recipient
    # TODO: set_content(plain text); add_alternative(html, subtype='html')
    # TODO: add_attachment(csv_bytes, maintype='text', subtype='csv', filename=...)
    raise NotImplementedError

def send(msg, host="127.0.0.1", port=8025):
    with smtplib.SMTP(host, port) as s:
        s.send_message(msg)
- **Test focus:** Run an in-process aiosmtpd controller capturing messages, send a built invoice email to it, and assert the received message's Subject/To, the presence of both text/plain and text/html parts, and the CSV attachment filename and bytes.

</div>
