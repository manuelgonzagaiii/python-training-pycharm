"""Transparent SQLite types: register_adapter and register_converter round-trip

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: Provide erp/persistence/sqlite_types.py with TODO bodies: empty register_erp_sqlite_types() (learner fills in three register_adapter calls and three register_converter calls, keyed on the type names MONEY/DATE/DATETIME) and an open_connection(path: str) that must (a) call register_erp_sqlite_types() and (b) return sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES). Include a tiny demo guarded by if __name__ == '__main__' that creates an in-memory table 'CREATE TABLE p(price MONEY, created DATETIME)', inserts (Decimal('19.99'), datetime.now()), selects it back, and asserts the types/values match. Pre-write the imports (sqlite3, decimal.Decimal, datetime.date, datetime.datetime) and the MONEY/DATE/DATETIME declared-type constants.
"""

# Your code here.
