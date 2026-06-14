import unittest

# TODO(author): replace with real checks.
# Test focus: Tests IdentityMap returns a live cached entity then drops it after the strong ref is deleted and gc.collect() runs; tests on_finalize's callback fires when the entity is collected; verifies a deliberately-built cycle is reclaimed by gc.collect().


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
