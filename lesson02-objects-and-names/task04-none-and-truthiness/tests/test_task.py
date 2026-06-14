"""Check for stage 4: None and truthiness via display_name().

Grading policy (CLAUDE.md A7): the behaviour is the rule (a real name is kept; a
missing one becomes a non-empty fallback), but the exact fallback word is the
learner's choice. We assert the fallback is consistent and non-empty rather than
demanding the literal 'Guest'.
"""

import unittest

import main


class TestDisplayName(unittest.TestCase):
    def test_real_name_is_returned(self):
        self.assertEqual(main.display_name("Ada"), "Ada")

    def test_surrounding_whitespace_is_trimmed(self):
        self.assertEqual(main.display_name("  Bob  "), "Bob")

    def test_missing_values_fall_back_consistently(self):
        none_case = main.display_name(None)
        empty_case = main.display_name("")
        blank_case = main.display_name("   ")
        for result in (none_case, empty_case, blank_case):
            self.assertIsInstance(result, str)
            self.assertTrue(result.strip(), "A missing name must fall back to a non-empty default.")
        self.assertEqual(
            {none_case, empty_case, blank_case},
            {none_case},
            "All missing inputs (None, '', whitespace) should give the same fallback.",
        )
        self.assertNotEqual(none_case, "", "The fallback must not be an empty string.")


if __name__ == "__main__":
    unittest.main()
