"""Check for stage 3: f-strings and self-documenting output.

Grading policy: validity, not wording. We check the interpolated content and the
self-documenting structure, not the exact spacing.
"""

import unittest
from decimal import Decimal

import text


class TestFStrings(unittest.TestCase):
    def test_debug_line_labels_each_value(self):
        line = text.debug_line("AB-1", 3, Decimal("9.99"))
        for label in ("sku=", "qty=", "price="):
            self.assertIn(label, line, "debug_line should self-document each name")

    def test_debug_line_includes_values(self):
        line = text.debug_line("AB-1", 3, Decimal("9.99"))
        self.assertIn("AB-1", line)
        self.assertIn("3", line)
        self.assertIn("9.99", line)

    def test_debug_line_uses_repr_quoting(self):
        # The {x=} form uses repr by default, so a string value is quoted.
        self.assertIn("'AB-1'", text.debug_line("AB-1", 3, Decimal("9.99")))

    def test_receipt_line_has_name_and_money(self):
        line = text.receipt_line("Widget", Decimal("9.99"))
        self.assertIn("Widget", line)
        self.assertIn("$9.99", line)


if __name__ == "__main__":
    unittest.main()
