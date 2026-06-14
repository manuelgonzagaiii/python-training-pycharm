import unittest

# TODO(author): replace with real checks.
# Test focus: Checks confirm a conftest.py exists with at least one shared fixture, that fixtures of differing scope are used, and that tmp_path + monkeypatch (or capsys/caplog) are exercised in real service tests.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
