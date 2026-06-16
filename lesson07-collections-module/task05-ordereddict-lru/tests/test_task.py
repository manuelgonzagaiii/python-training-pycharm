"""Check for task05-ordereddict-lru.

Grading policy: validity, not wording.
"""

import unittest

import catalog


from collections import OrderedDict


def _p(sku):
    return catalog.make_product(sku, "n", 0, 0)


class TestOrderedDictLRU(unittest.TestCase):
    def test_evicts_least_recently_used(self):
        cache = OrderedDict()
        catalog.touch(cache, "A", _p("A"), 2)
        catalog.touch(cache, "B", _p("B"), 2)
        catalog.touch(cache, "C", _p("C"), 2)  # over capacity -> evict A
        self.assertEqual(list(cache), ["B", "C"])

    def test_touch_refreshes_recency(self):
        cache = OrderedDict()
        catalog.touch(cache, "A", _p("A"), 2)
        catalog.touch(cache, "B", _p("B"), 2)
        catalog.touch(cache, "A", _p("A"), 2)   # A is now most-recently used
        catalog.touch(cache, "C", _p("C"), 2)   # evicts B, not A
        self.assertEqual(list(cache), ["A", "C"])


if __name__ == "__main__":
    unittest.main()
