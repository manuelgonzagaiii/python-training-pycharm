"""Check for stage 5: the welcome banner (and keeping I/O at the edges).

Grading policy: the banner's look is partly the learner's choice
(any single rule character is fine), but the structure is the rule: three lines, the
correct width, and a centered title. We also re-check the lesson-1 contract that
importing the module stays silent.
"""

import subprocess
import sys
import unittest
from pathlib import Path

import main

TASK_DIR = Path(__file__).resolve().parent.parent


class TestBanner(unittest.TestCase):
    def test_banner_has_three_lines_of_the_right_width(self):
        out = main.banner("MiniERP", 10)
        self.assertIsInstance(out, str)
        lines = out.split("\n")
        self.assertEqual(len(lines), 3, "The banner must be exactly three lines.")
        self.assertEqual(len(lines[0]), 10, "Top rule must be width columns wide.")
        self.assertEqual(len(lines[2]), 10, "Bottom rule must be width columns wide.")
        self.assertEqual(len(lines[1]), 10, "The centered title line must be width columns wide.")

    def test_rule_lines_are_one_repeated_non_space_character(self):
        lines = main.banner("MiniERP", 10).split("\n")
        self.assertEqual(lines[0], lines[2], "Top and bottom rules should match.")
        self.assertEqual(len(set(lines[0])), 1, "A rule should be one repeated character.")
        self.assertNotEqual(lines[0][0], " ", "A rule should be a visible character, not spaces.")

    def test_title_is_present_and_centered(self):
        lines = main.banner("MiniERP", 40).split("\n")
        self.assertIn("MiniERP", lines[1])
        self.assertEqual(lines[1], "MiniERP".center(40), "The title line should be the title centered in width.")

    def test_default_width_is_used(self):
        # banner(title) with no width must still produce a valid wide banner.
        lines = main.banner("MiniERP").split("\n")
        self.assertEqual(len(lines[0]), 40, "The default width should be 40.")

    def test_importing_stays_silent(self):
        proc = subprocess.run(
            [sys.executable, "-c", "import main"],
            cwd=str(TASK_DIR),
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.stdout, "", "Importing main must print nothing (keep run code behind the guard).")

    def test_running_prints_banner_and_version(self):
        proc = subprocess.run(
            [sys.executable, "main.py"],
            cwd=str(TASK_DIR),
            capture_output=True,
            text=True,
        )
        v = sys.version_info
        self.assertIn("MiniERP", proc.stdout, "Start-up should print the banner with the title.")
        self.assertIn(
            "{0}.{1}.{2}".format(v.major, v.minor, v.micro),
            proc.stdout,
            "Start-up should still print the live Python version.",
        )


if __name__ == "__main__":
    unittest.main()
