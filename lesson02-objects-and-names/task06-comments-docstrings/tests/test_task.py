"""Check for stage 6: comments and docstrings.

Grading policy (CLAUDE.md A7): the wording of every docstring is the learner's
choice. The rule is that the documentation exists and is reachable at runtime: the
module has a non-empty docstring naming the product, and each public helper carries a
non-empty docstring.
"""

import unittest

import main


class TestDocumentation(unittest.TestCase):
    def test_module_has_a_docstring_naming_the_product(self):
        self.assertIsInstance(main.__doc__, str, "The module must have a docstring.")
        self.assertTrue(main.__doc__.strip(), "The module docstring must not be empty.")
        self.assertIn(
            "MiniERP",
            main.__doc__,
            "The module docstring should say what the program is (mention MiniERP).",
        )

    def test_every_public_helper_is_documented(self):
        for func in (main.welcome, main.python_line, main.describe,
                     main.same_object, main.display_name, main.banner):
            with self.subTest(function=func.__name__):
                self.assertIsInstance(func.__doc__, str, f"{func.__name__} needs a docstring.")
                self.assertTrue(func.__doc__.strip(), f"{func.__name__}'s docstring must not be empty.")


if __name__ == "__main__":
    unittest.main()
