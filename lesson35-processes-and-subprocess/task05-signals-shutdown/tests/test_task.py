import unittest

# TODO(author): replace with real checks.
# Test focus: Raising SIGINT/SIGTERM (via signal.raise_signal) sets the Event and triggers a drain-then-stop without losing in-flight jobs; handler does no heavy work.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
