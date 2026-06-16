"""Check for stage 11: custom codec error handlers.

Grading policy: validity, not wording. We check each errors= policy and the
custom registered handler. The accented record is built from explicit code
points (chr) so it is unambiguously non-ASCII on disk.
"""

import unittest

import export

ACCENTED = {"name": "Ren" + chr(0x00E9) + "e", "note": "VIP " + chr(0x2014) + " priority"}


class TestCodecHandlers(unittest.TestCase):
    def test_strict_raises_on_non_ascii(self):
        with self.assertRaises(UnicodeEncodeError):
            export.export_record(ACCENTED, encoding="ascii", errors="strict")

    def test_ascii_record_strict_ok(self):
        out = export.export_record({"name": "Renee", "note": "ok"}, encoding="ascii", errors="strict")
        self.assertEqual(out, b"Renee|ok")

    def test_replace_does_not_raise(self):
        out = export.export_record(ACCENTED, encoding="ascii", errors="replace")
        self.assertIsInstance(out, bytes)
        self.assertIn(b"?", out)  # replace inserts '?'

    def test_ignore_drops_bad_chars(self):
        out = export.export_record(ACCENTED, encoding="ascii", errors="ignore")
        self.assertTrue(out.isascii())  # bad characters dropped

    def test_custom_xref_handler(self):
        out = export.export_record({"x": chr(0x2014)}, encoding="ascii", errors="xref")
        self.assertIn(b"&#8212;", out)  # em dash -> XML character reference

    def test_xref_escapes_only_the_bad_chars(self):
        # A multi-field record with one bad char: only that char is escaped; the
        # '|' separator and the ASCII text must pass through untouched. (Catches a
        # handler that escapes error.object -- the whole line -- instead of the slice.)
        out = export.export_record({"a": "X" + chr(0x2014) + "Y", "b": "ok"}, "ascii", "xref")
        self.assertIn(b"&#8212;", out)    # the em dash was escaped
        self.assertIn(b"X", out)          # plain ASCII is left as-is
        self.assertIn(b"|ok", out)        # the separator and ASCII field are intact
        self.assertNotIn(b"&#124;", out)  # the '|' (124) must NOT be escaped


if __name__ == "__main__":
    unittest.main()
