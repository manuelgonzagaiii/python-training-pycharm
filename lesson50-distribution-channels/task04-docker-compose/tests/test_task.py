import unittest

# TODO(author): replace with real checks.
# Test focus: compose defines the three expected services; app depends_on the mail/db with healthchecks; a named volume backs the SQLite path; secrets come from env_file not literals; the web port is mapped.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
