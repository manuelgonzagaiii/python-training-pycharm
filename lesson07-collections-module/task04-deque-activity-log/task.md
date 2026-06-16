# Stage 4: a bounded activity log with deque

MiniERP keeps a running activity log — "received 12 of B-010", "sold 2 of A-001",
"price changed on A-002". For an on-screen "recent activity" panel you do not want this to
grow without limit; you want the **last N** events and nothing older. A plain list can do
it, but trimming it yourself (`log.pop(0)` once it is too long) is both fiddly and slow:
removing from the front of a list shifts every remaining element down one slot, so it costs
more the longer the list gets.

`collections.deque` (a "double-ended queue", pronounced "deck") is built for exactly this.
It adds and removes from **either end** in constant time, and — the feature that matters
here — it can be given a maximum length:

```
>>> from collections import deque
>>> log = deque(maxlen=3)        # a bounded ring buffer
>>> for event in ["a", "b", "c", "d"]:
...     log.append(event)        # appending past the limit drops the oldest, automatically
>>> list(log)
['b', 'c', 'd']
```

When a `deque` with a `maxlen` is full and you append, it discards the item at the opposite
end to make room — no manual trimming, no length check. That single line of behaviour is the
whole reason to choose it for a capped log. (A `deque` is also the right structure for a
plain FIFO queue or a stack; the bounded ring buffer is just the use MiniERP needs first.)

## Your task

In `catalog.py`, finish two functions:

1. `new_activity_log(capacity)` — return a `deque` bounded to `capacity` (set its
   `maxlen`).
2. `record_event(log, message)` — append `message` to the log. Past capacity, the oldest
   event drops on its own; you do not handle that.

`recent_events(log)` (newest first) is already written for you.

## Worked example

```
>>> import catalog
>>> log = catalog.new_activity_log(3)
>>> for m in ["received A-001", "sold A-002", "priced B-010", "sold A-001"]:
...     catalog.record_event(log, m)
>>> len(log)                      # capped at 3; the first event has been dropped
3
>>> catalog.recent_events(log)    # newest first
['sold A-001', 'priced B-010', 'sold A-002']
```

## What the check verifies, and what it leaves to you

- Enforced: the log keeps only the last `capacity` events (its `maxlen` is set), and an
  append past the limit drops the oldest; `record_event` adds to the end.
- Your free choice: `capacity` is whatever the caller passes — the check builds logs of
  several sizes — and the messages are free text. What is fixed is the bounded-ring
  behaviour.

<div class="hint" title="If you are stuck">

`new_activity_log` returns `deque(maxlen=capacity)`. `record_event` is `log.append(message)` —
the `maxlen` handles the dropping.

</div>

Reference: Python documentation, "collections.deque" (the `maxlen` parameter) at
docs.python.org.
