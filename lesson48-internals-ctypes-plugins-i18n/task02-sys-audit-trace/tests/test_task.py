import unittest

# TODO(author): replace with real checks.
# Test focus: Tests install_audit_hook captures an 'open' audit event when a file is opened; tests CallCounter records call counts for functions invoked inside the with-block and detaches the tracer (sys.gettrace() is None) on exit.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
