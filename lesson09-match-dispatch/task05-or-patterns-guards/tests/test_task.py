import unittest

# TODO(author): replace with real checks.
# Test focus: HELP and REPORT share the read-only branch; PRICE with args routes to pricing; PRICE without args hits the usage guard; unknown verbs fall through.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
