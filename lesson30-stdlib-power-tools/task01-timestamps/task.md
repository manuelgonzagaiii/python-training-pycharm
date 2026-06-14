# Timestamps with datetime and zoneinfo

> **Phase:** Modules, Packages & Standard-Library Power Tools  •  **Stage:** 30.1 of 9  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Create timezone-aware datetimes and avoid naive-datetime bugs
- Convert between UTC and a named zone using zoneinfo.ZoneInfo
- Compute durations and due dates with timedelta
- Serialize/parse timestamps with isoformat/strptime
- Use the calendar module to reason about months and weekdays

## Python features introduced
`datetime.datetime`, `datetime.date`, `datetime.time`, `datetime.timedelta`, `datetime.timezone`, `timezone-aware vs naive datetimes`, `datetime.now(timezone.utc)`, `zoneinfo.ZoneInfo`, `isoformat()`, `strptime / strftime`, `calendar module (monthrange, day_name)`

## MiniERP increment
Give domain records real lifecycle timestamps: add a timestamps module providing now_utc() (aware UTC), to_local(dt, tz) via zoneinfo, and a Timestamped base/mixin so products, customers, and invoices carry created_at/updated_at. Add due_date(invoice, net_days) using timedelta and a month-end helper via calendar. Records are now time-aware.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** minierp/domain/timestamps.py with now_utc(), to_local(), due_date(); learner implements them using timezone-aware datetime + zoneinfo + timedelta + calendar.monthrange.
- **Test focus:** now_utc() is tz-aware UTC; to_local converts correctly across a known offset; due_date adds net_days; calendar-based month-end is correct; isoformat round-trips.

</div>
