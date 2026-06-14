import unittest

# TODO(author): replace with real checks.
# Test focus: make_zip_backup creates an archive whose namelist includes the db and exports; extractall into a tmp dir reproduces the files byte-for-byte; a tarfile w:gz variant round-trips; the filename carries a parseable timestamp.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
