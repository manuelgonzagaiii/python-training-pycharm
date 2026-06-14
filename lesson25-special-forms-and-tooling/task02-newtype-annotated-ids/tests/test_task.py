import unittest

# TODO(author): replace with real checks.
# Test focus: Tests confirm NewType wrappers behave as the base at runtime (ProductId('x') == 'x') and that Annotated metadata is recoverable via get_type_hints(include_extras=True); a documented case shows passing CustomerId where ProductId is required is a type error.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
