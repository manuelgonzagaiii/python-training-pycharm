"""Check for stage 7: build and parse canonical SKUs.

Grading policy: validity, not wording. We check the canonical format, the
round-trip, and that malformed input raises ValueError.
"""

import unittest

import text


class TestSku(unittest.TestCase):
    def test_make_sku_canonical(self):
        self.assertEqual(text.make_sku("cat", 42, "xl"), "CAT-0042-XL")

    def test_make_sku_zero_pads_number(self):
        self.assertEqual(text.make_sku("AB", 7, "S"), "AB-0007-S")

    def test_round_trip(self):
        self.assertEqual(text.parse_sku("CAT-0042-XL"), ("CAT", 42, "XL"))

    def test_parse_uppercases_and_converts(self):
        self.assertEqual(text.parse_sku("cat-0042-xl"), ("CAT", 42, "XL"))

    def test_parse_rejects_wrong_segment_count(self):
        with self.assertRaises(ValueError):
            text.parse_sku("CAT-0042")

    def test_parse_rejects_non_numeric_middle(self):
        with self.assertRaises(ValueError):
            text.parse_sku("CAT-XX-XL")


if __name__ == "__main__":
    unittest.main()
