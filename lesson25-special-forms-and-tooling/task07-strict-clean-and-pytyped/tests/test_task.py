import unittest

# TODO(author): replace with real checks.
# Test focus: An 'edu' check verifies the py.typed marker exists in the package and that the annotated modules import and pass get_type_hints without resolution errors; where the runner supports it, mypy --strict and pyright are invoked and required to exit zero on the package.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
