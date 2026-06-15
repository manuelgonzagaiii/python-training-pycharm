"""Check for stage 5: the entry point and the __main__ guard.

Grading policy: this validates that the program is correct, not
that it matches one exact wording. The welcome text is the learner's free choice;
the rules we enforce are that welcome() returns a real non-empty string and that
importing the module produces no output (the run code must sit behind the guard).
"""

import subprocess
import sys
import unittest
from pathlib import Path

import main

TASK_DIR = Path(__file__).resolve().parent.parent


class TestEntryPoint(unittest.TestCase):
    def test_welcome_returns_non_empty_string(self):
        result = main.welcome()
        self.assertIsInstance(result, str, "welcome() must return a string.")
        self.assertTrue(
            result.strip(),
            "welcome() must return a non-empty line. The exact words are up to you.",
        )

    def test_importing_has_no_output(self):
        # Importing the module must print nothing. If it prints, the run code is
        # not protected by the `if __name__ == "__main__":` guard.
        proc = subprocess.run(
            [sys.executable, "-c", "import main"],
            cwd=str(TASK_DIR),
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            proc.stdout,
            "",
            "Importing main printed something. Put the print() behind the __main__ guard.",
        )

    def test_running_the_file_prints_the_welcome_line(self):
        proc = subprocess.run(
            [sys.executable, "main.py"],
            cwd=str(TASK_DIR),
            capture_output=True,
            text=True,
        )
        self.assertIn(
            main.welcome().strip(),
            proc.stdout,
            "Running main.py should print the line that welcome() returns.",
        )


if __name__ == "__main__":
    unittest.main()
