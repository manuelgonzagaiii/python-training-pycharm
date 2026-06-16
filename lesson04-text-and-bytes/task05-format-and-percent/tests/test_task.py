"""Check for stage 5: str.format/format_map, %-formatting, and string.Template.

Grading policy: validity, not wording. We check the rendered output and the
documented behaviour (missing keys raise; unknown $placeholders survive).
"""

import unittest

import text


class TestTemplating(unittest.TestCase):
    def test_invoice_header_fills_named_fields(self):
        out = text.render_invoice_header({"invoice_no": "INV-1", "customer": "Acme"})
        self.assertIn("INV-1", out)
        self.assertIn("Acme", out)

    def test_invoice_header_missing_key_raises(self):
        with self.assertRaises(KeyError):
            text.render_invoice_header({"invoice_no": "INV-1"})  # no 'customer'

    def test_render_email_substitutes_known(self):
        out = text.render_email("Hi $name, order $order is ready", name="Sam", order="42")
        self.assertIn("Sam", out)
        self.assertIn("42", out)

    def test_render_email_leaves_unknown_intact(self):
        out = text.render_email("Hi $name from $company", name="Sam")
        self.assertIn("Sam", out)
        self.assertIn("$company", out)  # safe_substitute does not raise or drop it


if __name__ == "__main__":
    unittest.main()
