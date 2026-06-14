import unittest

# TODO(author): replace with real checks.
# Test focus: Verify the descriptor round-trips values per-instance (two entities don't share state) and that distinct-but-equal entities are kept distinct (identity keying, not __eq__ keying). Verify _storage shrinks after an entity is del'd and gc.collect() runs — i.e. no leak — by asserting len(_storage) drops to 0 and that the entity is gone from the WeakKeyDictionary. Verify the InstanceRegistry callback fires on collection: live_count returns to its baseline and an 'evicted' audit entry is appended after del + gc.collect(). Verify that dereferencing safe_view(entity) after the entity is collected raises weakref.ReferenceError. Use gc.collect() to force deterministic collection and assert WeakKeyDictionary keys reflect only still-live instances; confirm the descriptor also works on a slotted dataclass (which has no usable instance __dict__).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
