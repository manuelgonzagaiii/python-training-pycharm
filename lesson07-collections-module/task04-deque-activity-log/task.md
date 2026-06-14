# deque: a bounded recent-activity log

> **Phase:** Built-in Data Structures: The In-Memory Catalog & Inventory  •  **Stage:** 7.4 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Use a deque(maxlen=N) as a fixed-size ring buffer that drops oldest entries
- Add/remove from both ends in O(1)
- Contrast deque with a list for queue workloads
- Rotate entries for a simple scheduling/display effect

## Python features introduced
`collections.deque`, `maxlen (auto-eviction)`, `appendleft/append`, `popleft/pop`, `rotate`, `extendleft`, `O(1) ends vs O(n) list.insert(0)`, `deque as a ring buffer`

## MiniERP increment
Adds an ActivityLog backed by deque(maxlen=...) recording the last N catalog changes (add/reprice/stock-move), and record_event / recent_events — the audit-log seed the dedicated Audit phase will build on.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** # catalog.py (continued)
from collections import deque

def new_activity_log(capacity: int) -> deque[str]:
    """Return a bounded deque that keeps only the last `capacity` events."""
    ...

def record_event(log: deque[str], message: str) -> None:
    """Append an event; oldest entries fall off automatically at capacity."""
    ...
- **Test focus:** new_activity_log enforces maxlen; once full, recording a new event evicts the oldest (length stays at capacity, oldest gone, newest present in order).

</div>
