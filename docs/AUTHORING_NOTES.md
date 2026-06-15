# MiniERP: authoring conventions and continuity rules

These are the rules for writing each stage of the course. The guided project grows one
codebase across many lessons, so consistency between stages matters more than anything
else. The golden rule:

> Build a thing once, then extend it. A later stage must never quietly re-create
> something an earlier stage already built.

Read this before populating any stage. The per-stage checklist is at the end.

## 1. One package import root: `minierp`

Use a single import root everywhere: `minierp` (also the distribution name). Do not let
`mini_erp`, `core`, or `erp` creep in as alternative roots.

The project changes shape once, on purpose:

- Phases 1 to 10 (lessons 1 to 27): code lives in flat top-level modules
  (`money.py`, `text.py`, `catalog.py`, `pricing.py`, `rules.py`, `inventory.py`,
  `domain.py`, `errors.py`, `logging_setup.py`, and so on). Packages are not taught yet.
- Phase 11 (lessons 28 to 30) is the packaging phase. It **moves the existing flat
  modules into the `minierp` package**. It does not invent new modules to package, and
  it does not rebuild money, catalog, or pricing from scratch; those already exist.

Target package layout by phase 18:

```
minierp/
  __init__.py            # __version__
  core/                  # config, errors, logging, money, text utilities
  domain/                # Product, Customer, Invoice, LineItem, Money, enums
  services/              # catalog, pricing, inventory, sales, payments,
                         # reporting, users/auth, audit, repository
  persistence/           # sqlite repo, import/export, backups
  concurrency/           # threads, processes, async helpers
  net/                   # sockets, low-level stdlib http
  web/                   # stdlib API first, then the FastAPI app
  cli/                   # argparse, then Typer
  tui/                   # curses, then Textual
  gui/                   # tkinter, MVC split
  plugins/               # entry-point plugin system
```

Whenever an earlier stage refers to a path like `erp/web`, write it as a `minierp`
subpackage (`minierp.web`).

## 2. One `Money` value object: integer minor units

`Money` is defined once and carried forward, never re-represented.

- Lesson 3 (numbers and money): Decimal helpers for parsing and formatting at the
  input/output boundary (string to amount and back), plus the rounding rules.
- Lesson 14 (value objects): introduce `Money` as a frozen, slotted dataclass that
  stores integer minor units (cents). The `__bytes__` and `struct` packing stages
  depend on this integer representation.
- Lesson 14 onward: extend that same `Money` (ordering, arithmetic,
  `dataclasses.replace`). Do not redefine it with a `Decimal` field.

The course never uses `float` for money, so never describe `Money` as "replacing float
prices". The correct framing is that it consolidates the Decimal helpers and the value
object into one type.

## 3. One `@audit` decorator

A single audit-logging decorator named `@audit` (not `@audited`).

- Lesson 20: build a minimal `@audit` to demonstrate `functools.wraps`.
- Lesson 20/21: promote it to the parametrized version, and say it supersedes the first.
- Lesson 24: add `ParamSpec`/`Concatenate` types to that same `@audit`.

## 4. One generic `Repository[T]`

- Lesson 14: introduce the abstract generic `Repository[T]` (`abc.ABC`) with an
  in-memory implementation.
- Lesson 24: the typing pass. Add precise type parameters, variance, and `@overload` to
  the existing `Repository[T]`. Frame it as typing the existing container, not replacing
  per-entity stores.
- Lesson 33: swap the backend to SQLite behind the same interface. Not a parallel
  re-implementation.

## 5. One typing baseline; CI wires it, it does not recreate it

- Lesson 25: establish the strict-typed core. Pass `mypy --strict` and pyright strict,
  and ship a `py.typed` marker.
- Lesson 45: wire the existing mypy/pyright checks into the CI and pre-commit gate, and
  fix defects introduced by lessons 26 to 42. Do not re-add `py.typed` or introduce the
  type-checker config for the first time here.

## 6. Forward-reference fixes

These ordering issues must be handled when populating:

- Lesson 36 (async core): the `async-comprehensions` stage consumes an async customer
  stream, so add an `async-repository` stage before it (an `AsyncCustomerRepo` async
  generator over the SQLite repo via `loop.run_in_executor`), or rewire it to consume a
  stream that an earlier stage already built (`stream_report_rows` /
  `stream_audit_events`). Decision: add the `async-repository` stage.
- Lesson 39 (httpx client): the TUI does not exist until lesson 41, so do not say the
  TUI consumes the client "from earlier phases". Word it as "used by the CLI now, and by
  the TUI and GUI built next".
- Lesson 34 (locks): clarify that the in-memory structures being locked are
  process-local counters and caches (ID allocation, stock cache) layered over the SQLite
  repository, so persistence and in-memory shared state clearly coexist.

## 7. Lesson 4 geometry helpers stay flat

The `complex-bin-coordinates` stage keeps its helpers in the flat lesson-4 module as
generic 2-D coordinate functions over complex numbers. Do not place them under
`minierp/inventory/`; that package does not exist until lesson 28. Defer the "spatial
query for Inventory" framing to a later phase.

## Stdlib first, then open source

Keep this ordering when populating. Teach the standard-library version first so the
learner understands the mechanics, then introduce the open-source tool.

| Capability  | Standard library first         | Then open source            |
|-------------|--------------------------------|-----------------------------|
| Web server  | `http.server`, `wsgiref`       | FastAPI + uvicorn           |
| HTTP client | `urllib`, `http.client`        | httpx                       |
| Templating  | hand-built, `string.Template`  | Jinja2                      |
| Tests       | `unittest`, `doctest`          | pytest, hypothesis, coverage|
| CLI         | `argparse`                     | Typer / Click               |
| TUI         | `curses`                       | Rich / Textual              |
| Database    | `sqlite3`                      | (stays stdlib; SQLAlchemy optional) |
| Email       | `smtplib` + local `aiosmtpd`   | (no external mail service)  |

No paid services anywhere. When an external system is needed, use an open-source
stand-in that runs on the learner's own machine.

## Per-stage populate checklist

When filling a stage, replace all three stubs and remove the skeleton status line:

1. `task.md`: the real description. Lead with the reasoning (what it is, why it exists,
   the trade-offs, the mental model), then the instructions, then a worked example, and
   a genuine hint. Keep the "Python features introduced" list accurate. State plainly
   which parts of the answer are the learner's free choice and which the check insists on.
2. The solution: author it as `<realname>.tmpl` with `[[PH:hint]]answer[[/PH]]` markers
   over the real learning points, then run `tools/build_placeholders.py` to produce the
   clean file and the placeholder offsets. In a framework lesson the file carries
   forward, so blank only what is new in this stage.
3. `tests/test_task.py` (graded stages): real `unittest` checks that grade validity, not
   exact wording. A different valid answer must pass; an invalid value must fail. Remove
   the skipped placeholder test.
4. Verify the stage in isolation: `cd <task dir> && python -m unittest discover -s tests`.
   Then drop a `.populated` marker in the lesson directory so the scaffolder leaves it
   alone.
