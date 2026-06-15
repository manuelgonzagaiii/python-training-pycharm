"""Check for stage 6: report the running Python version.

Grading policy: the wording of the version line is the learner's
free choice. The rule we enforce is that the value is read live from the
interpreter (sys.version_info), not hard-coded. We prove that by computing the
real running version here in the test and requiring it to appear in the output.
"""

import subprocess
import sys
import unittest
from pathlib import Path

import main

TASK_DIR = Path(__file__).resolve().parent.parent


def live_version_triple():
    v = sys.version_info
    return "{0}.{1}.{2}".format(v.major, v.minor, v.micro)


class TestVersionLine(unittest.TestCase):
    def test_welcome_still_valid(self):
        self.assertIsInstance(main.welcome(), str)
        self.assertTrue(main.welcome().strip(), "welcome() must still return a non-empty string.")

    def test_python_line_is_a_non_empty_string(self):
        line = main.python_line()
        self.assertIsInstance(line, str, "python_line() must return a string.")
        self.assertTrue(line.strip(), "python_line() must return a non-empty line.")

    def test_python_line_reports_the_live_version(self):
        line = main.python_line()
        self.assertIn(
            live_version_triple(),
            line,
            "python_line() must report the ACTUAL running version, built from "
            "sys.version_info (major.minor.micro). Do not hard-code the number.",
        )

    def test_running_the_file_prints_welcome_and_version(self):
        proc = subprocess.run(
            [sys.executable, "main.py"],
            cwd=str(TASK_DIR),
            capture_output=True,
            text=True,
        )
        self.assertIn(main.welcome().strip(), proc.stdout, "Start-up should print the welcome line.")
        self.assertIn(live_version_triple(), proc.stdout, "Start-up should print the live Python version.")

    def test_importing_has_no_output(self):
        proc = subprocess.run(
            [sys.executable, "-c", "import main"],
            cwd=str(TASK_DIR),
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.stdout, "", "Importing main must print nothing; keep run code behind the guard.")


if __name__ == "__main__":
    unittest.main()
