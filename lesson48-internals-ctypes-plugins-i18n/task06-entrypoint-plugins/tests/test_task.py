import unittest

# TODO(author): replace with real checks.
# Test focus: Tests discover with a monkeypatched/fake entry_points result: loads valid plugins, skips ones that raise on load, and rejects objects not matching the ErpPlugin Protocol; verifies plugin commands are registered into a passed registry.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
