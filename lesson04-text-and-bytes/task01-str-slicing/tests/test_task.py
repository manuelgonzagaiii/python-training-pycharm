"""Check for stage 1: string indexing and slicing.

Grading policy: validity, not wording. Any correct slicing passes, however you
write it.
"""

import unittest

import text


class TestSlicing(unittest.TestCase):
    def test_prefix_default(self):
        self.assertEqual(text.sku_prefix("AB-1234-XL"), "AB")

    def test_prefix_custom_length(self):
        self.assertEqual(text.sku_prefix("AB-1234-XL", 4), "AB-1")

    def test_suffix_default(self):
        self.assertEqual(text.sku_suffix("AB-1234-XL"), "XL")

    def test_suffix_custom_length(self):
        self.assertEqual(text.sku_suffix("AB-1234-XL", 4), "4-XL")

    def test_reversed(self):
        self.assertEqual(text.reversed_code("ABC123"), "321CBA")

    def test_short_string_clamps_without_error(self):
        # Slicing past the end clamps; it must not raise IndexError.
        self.assertEqual(text.sku_prefix("A", 2), "A")
        self.assertEqual(text.sku_suffix("A", 2), "A")


if __name__ == "__main__":
    unittest.main()
