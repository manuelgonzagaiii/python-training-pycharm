"""Check for task04-deque-activity-log.

Grading policy: validity, not wording.
"""

import unittest

import catalog


class TestDequeActivityLog(unittest.TestCase):
    def test_bounded_drops_oldest(self):
        log = catalog.new_activity_log(3)
        for i in range(5):
            catalog.record_event(log, "e%d" % i)
        self.assertEqual(len(log), 3)
        self.assertEqual(list(log), ["e2", "e3", "e4"])

    def test_maxlen_set(self):
        self.assertEqual(catalog.new_activity_log(4).maxlen, 4)

    def test_recent_events_newest_first(self):
        log = catalog.new_activity_log(10)
        for msg in ["a", "b", "c"]:
            catalog.record_event(log, msg)
        self.assertEqual(catalog.recent_events(log), ["c", "b", "a"])


if __name__ == "__main__":
    unittest.main()
