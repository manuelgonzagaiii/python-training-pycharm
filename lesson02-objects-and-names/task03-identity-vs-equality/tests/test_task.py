"""Check for stage 3: identity versus equality via same_object().

Grading policy (CLAUDE.md A7): identity is genuinely right or wrong, so this is
strict. We use two equal-but-distinct lists to prove the function tests identity
(is), not equality (==), without depending on any interning behaviour.
"""

import unittest

import main


class TestSameObject(unittest.TestCase):
    def test_same_object_is_true_for_one_object(self):
        x = ["p"]
        self.assertIs(main.same_object(x, x), True, "A value is the same object as itself.")

    def test_equal_but_distinct_objects_are_not_the_same(self):
        x = ["p"]
        y = ["p"]
        self.assertEqual(x, y, "Sanity: the two lists are equal in value.")
        self.assertIs(
            main.same_object(x, y),
            False,
            "Equal value is not the same object. same_object must use is, not ==.",
        )

    def test_none_is_the_same_object_as_none(self):
        self.assertIs(main.same_object(None, None), True, "There is only one None object.")


if __name__ == "__main__":
    unittest.main()
