import unittest

# TODO(author): replace with real checks.
# Test focus: is_frozen() reads sys.frozen safely (False from source); resource_path resolves an existing bundled asset under both branches (monkeypatched sys.frozen/_MEIPASS); --add-data covers templates and schema; no absolute paths leak.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
