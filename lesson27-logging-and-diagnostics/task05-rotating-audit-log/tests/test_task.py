import unittest

# TODO(author): replace with real checks.
# Test focus: audit() emits a single parseable JSON line containing actor/action/entity/op_id; the audit logger does not propagate to the root/console; rotation config (maxBytes/backupCount) is set on its handler.


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
