"""Check for stage 8: bytes, codecs, and base64.

Grading policy: validity, not wording. We check the encode/decode round-trips,
that encoding produces bytes, and the multibyte length fact.
"""

import unittest

import text


class TestBytesAndCodecs(unittest.TestCase):
    def test_encode_returns_bytes(self):
        self.assertIsInstance(text.encode_record("x"), bytes)

    def test_encode_decode_round_trip(self):
        original = "caf" + chr(0x00E9) + " " + chr(0x20AC) + "5"  # "café €5"
        self.assertEqual(text.decode_record(text.encode_record(original)), original)

    def test_multibyte_length(self):
        # one character, but two UTF-8 bytes
        accented = chr(0x00E9)  # composed e-acute
        self.assertEqual(len(accented), 1)
        self.assertEqual(len(text.encode_record(accented)), 2)

    def test_b64_round_trip(self):
        original = "caf" + chr(0x00E9)
        self.assertEqual(text.from_b64(text.to_b64(original)), original)

    def test_b64_output_is_ascii(self):
        self.assertTrue(text.to_b64("caf" + chr(0x00E9)).isascii())


if __name__ == "__main__":
    unittest.main()
