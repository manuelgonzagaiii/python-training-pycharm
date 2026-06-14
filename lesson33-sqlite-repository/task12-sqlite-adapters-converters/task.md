# Transparent SQLite types: register_adapter and register_converter round-trip

> **Phase:** Files, Persistence & Serialization  •  **Stage:** 33.12 of 13  •  **Type:** `edu`  •  **Status:** skeleton (to be populated)

## What you'll learn
- Explain that Python 3.12+ removed sqlite3's built-in datetime/Decimal handling, so round-tripping rich types now requires you to register your own adapters and converters.
- Write the WRITE side: register_adapter(PyType, fn) so a Python value (Decimal, date, datetime) is serialized to a SQLite-storable form (str/bytes) automatically when bound to a '?' placeholder.
- Write the READ side: register_converter('TYPENAME', fn) so bytes coming back from a column declared TYPENAME are deserialized to the original Python type.
- Open the connection with detect_types=PARSE_DECLTYPES | PARSE_COLNAMES and understand the difference: DECLTYPES keys on the column's declared type in CREATE TABLE; COLNAMES keys on a 'col [TYPE]' alias in the SELECT.
- Recognize that registration is a process-global side effect performed once at import time, and that converters always receive bytes (so you decode()) while adapters return the stored representation.
- Understand why this makes the persistence layer transparent: service/domain code keeps using Decimal money and real dates, never str, with no manual conversion at every call site.

## Python features introduced
`sqlite3.register_adapter`, `sqlite3.register_converter`, `sqlite3.connect(detect_types=...)`, `sqlite3.PARSE_DECLTYPES`, `sqlite3.PARSE_COLNAMES`, `declared column types as adapter/converter keys`, `'name [TYPE]' column-alias syntax for PARSE_COLNAMES`, `decimal.Decimal`, `datetime.date / datetime.datetime`, `bytes <-> str encode()/decode() at the storage boundary`, `module-level registration as process-global side effect`, `module import side effects (registration on import)`

## MiniERP increment
Give the MiniERP SQLite persistence layer transparent domain-type support so money and dates survive a database round-trip with full fidelity. Create erp/persistence/sqlite_types.py exposing register_erp_sqlite_types() that registers: an adapter+converter pair for decimal.Decimal under the declared type MONEY (Decimal -> str via str(d); bytes -> Decimal via Decimal(b.decode())), and pairs for datetime.date (DATE) and datetime.datetime (DATETIME) using ISO 8601 isoformat()/fromisoformat(). Add a connection factory open_connection(path) that calls register_erp_sqlite_types() and opens sqlite3.connect(path, detect_types=PARSE_DECLTYPES | PARSE_COLNAMES). Migrate the products and invoices schema so price/line totals are declared MONEY and timestamps are declared DATETIME (invoice due dates DATE). Now repo code inserts a Product with price=Decimal('19.99') and a created-at datetime and reads them back as the exact same Decimal and datetime objects with no per-call conversion — fixing the float-rounding hazard that storing money as REAL would introduce. This upgrades the persistence layer first built in earlier p12 tasks (sqlite-rowfactory) from string-only columns to type-safe domain columns.

---

<div class="hint" title="Author notes (remove when populated)">

**TODO(author):** replace this stub with the full task description, then put starter code in `task.py` and real checks in `tests/test_task.py`.

- **Starter idea:** Provide erp/persistence/sqlite_types.py with TODO bodies: empty register_erp_sqlite_types() (learner fills in three register_adapter calls and three register_converter calls, keyed on the type names MONEY/DATE/DATETIME) and an open_connection(path: str) that must (a) call register_erp_sqlite_types() and (b) return sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES). Include a tiny demo guarded by if __name__ == '__main__' that creates an in-memory table 'CREATE TABLE p(price MONEY, created DATETIME)', inserts (Decimal('19.99'), datetime.now()), selects it back, and asserts the types/values match. Pre-write the imports (sqlite3, decimal.Decimal, datetime.date, datetime.datetime) and the MONEY/DATE/DATETIME declared-type constants.
- **Test focus:** Round-trip correctness and the detect_types mechanics. Tests open an in-memory connection via open_connection(':memory:'). (1) WRITE+READ via PARSE_DECLTYPES: CREATE TABLE t(price MONEY, due DATE, ts DATETIME); INSERT a Decimal('19.99'), a date, and a datetime bound to '?' placeholders; SELECT back and assert each returned value is isinstance Decimal/date/datetime AND equals the original (not a str, not a float). (2) PARSE_COLNAMES path: SELECT a plain TEXT column aliased as 'x [MONEY]' and assert it comes back as Decimal, proving the colname converter route. (3) Fidelity: assert Decimal('19.99') survives exactly (no 19.989999... float drift) and a datetime with microseconds round-trips. (4) Assert register_erp_sqlite_types() is idempotent (calling it twice does not error and the round-trip still holds). (5) Negative: a connection opened WITHOUT detect_types returns the raw str for the same column, confirming detect_types is what activates the converters.

</div>
