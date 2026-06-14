import unittest

# TODO(author): replace with real checks.
# Test focus: Round-trip: `dump_snapshot` then `load_snapshot` on a `Snapshot` holding `Product`/`Customer`/`Money` reconstructs equal objects, and `Money` (with `__slots__`, no no-arg `__init__`) survives the round-trip via `__getnewargs_ex__`. Security: feed the loader bytes that reference a disallowed global (craft a payload whose `__reduce__` returns `(os.system, ('echo pwned',))`, or pickle an object of a non-allowlisted class) and assert `load_snapshot` raises `pickle.UnpicklingError` *without* executing the payload (use a sentinel/flag that must remain untouched). Assert `find_class` permits an allowlisted name and rejects `os.system` / `builtins.eval` by fully-qualified name. Confirm snapshots are written/read via `pickle.Pickler`/`pickle.Unpickler` (not `dumps`/`loads`) and at `HIGHEST_PROTOCOL`. Optionally assert that a plain `pickle.loads` of the malicious payload *would* have run it, to make the contrast explicit (run in a guarded subprocess or with a harmless sentinel command).


class TestCase(unittest.TestCase):
    @unittest.skip("skeleton: this task has not been populated yet")
    def test_placeholder(self):
        self.fail("populate this task")
