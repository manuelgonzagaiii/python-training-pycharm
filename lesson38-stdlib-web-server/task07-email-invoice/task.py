"""Emailing an invoice with email + smtplib

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: from email.message import EmailMessage
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
"""

# Your code here.
