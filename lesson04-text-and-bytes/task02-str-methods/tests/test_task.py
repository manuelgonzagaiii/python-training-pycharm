"""Check for stage 2: the string method toolbox.

Grading policy: validity, not wording. We check the cleaned/normalized output,
not how you produced it.
"""

import unittest

import text


class TestStringMethods(unittest.TestCase):
    def test_clean_name_collapses_and_titlecases(self):
        self.assertEqual(text.clean_name("  john   smith "), "John Smith")

    def test_clean_name_single_word(self):
        self.assertEqual(text.clean_name("WIDGET"), "Widget")

    def test_normalize_key_casefolds_and_strips(self):
        self.assertEqual(text.normalize_key("  Café "), "café")

    def test_normalize_key_is_case_insensitive(self):
        # casefold is more aggressive than lower: it folds the German sharp s,
        # so "Straße" and "STRASSE" become the same key.
        self.assertEqual(text.normalize_key("Straße"), text.normalize_key("STRASSE"))

    def test_parse_csv_line_trims_fields(self):
        self.assertEqual(text.parse_csv_line("a, b ,c"), ["a", "b", "c"])

    def test_parse_csv_line_single_field(self):
        self.assertEqual(text.parse_csv_line("solo"), ["solo"])


if __name__ == "__main__":
    unittest.main()
