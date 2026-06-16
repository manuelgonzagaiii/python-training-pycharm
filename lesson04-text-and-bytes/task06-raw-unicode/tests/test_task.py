"""Check for stage 6: raw strings, escapes, and Unicode normalization.

Grading policy: validity, not wording. We check normalization equality, the
named escape, and the ord/chr round-trip. The two "cafe" forms are built from
explicit code points (via chr) so they are unambiguously different on disk.
"""

import unittest

import text


class TestUnicode(unittest.TestCase):
    def test_normalize_makes_equal_forms_equal(self):
        precomposed = "caf" + chr(0x00E9)        # composed e-acute  (one code point)
        combining = "cafe" + chr(0x0301)         # e + combining acute (two code points)
        self.assertNotEqual(precomposed, combining)  # different code points...
        self.assertEqual(  # ...the same string after NFKC normalization
            text.normalize_unicode(precomposed),
            text.normalize_unicode(combining),
        )

    def test_currency_symbol_euro(self):
        self.assertEqual(text.currency_symbol("EUR"), chr(0x20AC))  # euro sign

    def test_code_points_basic(self):
        self.assertEqual(text.code_points("AB"), [65, 66])

    def test_code_points_round_trip(self):
        original = "x" + chr(0x00FF) + "z"  # x, y-with-diaeresis, z
        self.assertEqual("".join(chr(cp) for cp in text.code_points(original)), original)


if __name__ == "__main__":
    unittest.main()
