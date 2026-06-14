import unittest

# TODO(author): replace with real checks.
# Test focus: list_backups returns newest-first; prune_backups(keep=N) deletes exactly the oldest beyond N and returns them; restore extracts to temp and os.replaces the live db; a corrupted zip is caught by testzip before any restore happens.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
