import unittest

# TODO(author): replace with real checks.
# Test focus: Re-raised NotFoundError/ValidationError have __cause__ set to the original built-in; the suppression variant (from None) leaves __cause__ None with __suppress_context__ True.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
