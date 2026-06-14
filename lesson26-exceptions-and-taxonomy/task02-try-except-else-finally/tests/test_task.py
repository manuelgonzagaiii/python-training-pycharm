import unittest

# TODO(author): replace with real checks.
# Test focus: Verify else runs only on success, finally always increments the counter (success, missing-file, and unreadable cases), and OSError is caught while unrelated errors propagate.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
