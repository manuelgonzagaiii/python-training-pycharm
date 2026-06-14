import unittest

# TODO(author): replace with real checks.
# Test focus: An 'edu' check verifies that the module imports cleanly with the future import present, that forward-referenced names resolve via get_type_hints, and (where the runner allows) that mypy/pyright exit zero on the annotated modules.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
