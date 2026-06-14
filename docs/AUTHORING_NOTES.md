# MiniERP — Authoring Conventions & Continuity Rules

These are **binding decisions** for populating the course stage-by-stage. They
come from the curriculum coherence review (which flagged 3 blocker, 3 major, and
4 minor continuity issues against the auto-designed blueprint). The skeleton's
folder structure is sound; these rules govern the *content* you write into each
`task.md` / `task.py` / `tests/test_task.py`.

> Rule of thumb: **build a thing once, then extend it.** A later phase must never
> silently re-create something an earlier phase already built.

---

## 1. One package import root: `minierp`

The auto-design drifted between `mini_erp/`, `core/`, `erp/`, and `minierp/`.
**Canonical root is `minierp`** (also the distribution name).

Flat phase → package phase:

- **Phases p01–p10 (lessons 1–27):** code lives in **flat top-level modules**
  (`money.py`, `text.py`, `catalog.py`, `pricing.py`, `rules.py`, `inventory.py`,
  `domain.py`, `errors.py`, `logging_setup.py`, …). Packages are not taught yet.
- **Phase p11 (lessons 28–30):** the packaging phase **moves the existing flat
  modules into the `minierp` package** — it does **not** invent new toy modules.
  (Fixes BLOCKER: p11 must consolidate, not recreate, money/catalog/pricing.)

Canonical subpackage layout (target by p18):

```
minierp/
  __init__.py            # __version__
  core/                  # config, errors, logging, money, text utils
  domain/                # Product, Customer, Invoice, LineItem, Money, enums
  services/             # catalog, pricing, inventory, sales, payments,
                         # reporting, users/auth, audit, repository
  persistence/           # sqlite repo, import/export, backups
  concurrency/           # threads, processes, async helpers
  net/                   # sockets, stdlib http (low level)
  web/                   # stdlib API first, then FastAPI app
  cli/                   # argparse → Typer
  tui/                   # curses → Textual
  gui/                   # tkinter MVC
  plugins/               # entry-point plugin system
```

Whenever an earlier-phase stage references a path like `erp/web` or `core/...`,
write it as a `minierp.*` subpackage instead. (Fixes BLOCKER: cross-phase naming.)

## 2. One `Money` value object: integer **minor units**

`Money` is defined once and carried forward — never re-represented.

- **p02 (lesson 03 numbers-and-money):** Decimal helpers for *parsing/formatting*
  at the I/O boundary (string ⇄ amount), plus rounding rules.
- **p05 (lesson 14 value-objects):** introduce `Money` as a **frozen, slotted
  dataclass storing integer minor units (cents)**. The `__bytes__` / `struct`
  packing stages depend on this 8-byte integer representation.
- **p06 (lesson 14/16):** **extend the same `Money`** (ordering, arithmetic,
  `dataclasses.replace`). Do **not** redefine it with a `Decimal` field.
- Never claim Money "replaces ad-hoc float prices" — the course **never uses
  float for money**. The correct framing: "consolidates the p02 Decimal helpers
  and the p05 `Money` class into the canonical value object."

(Fixes MAJOR: triple Money definition / cents-vs-Decimal conflict / false float claim.)

## 3. One `@audit` decorator

A single audit-logging decorator, named **`@audit`** (not `@audited`).

- **p07 (lesson 20):** build a minimal `@audit` to demonstrate `functools.wraps`.
- **p08 (lesson 20/21):** promote it to the parametrized milestone version and
  say it **supersedes** the p07 one.
- **p09 (lesson 24):** **add `ParamSpec`/`Concatenate` typing to the existing
  `@audit`** — do not introduce a fresh decorator.

(Fixes MINOR: audit decorator introduced three times under two names.)

## 4. One generic `Repository[T]`

- **p06:** introduce the abstract generic `Repository[T]` (`abc.ABC`) +
  `InMemoryRepository`.
- **p09:** the **typing pass** — add precise type params/variance and `@overload`
  to the **existing** `Repository[T]`. Frame as "type the p06 container," not
  "replace ad-hoc per-entity stores."
- **p12:** swap the backend to SQLite **behind the same interface**
  (`SqliteRepository`), not a parallel re-implementation.

(Fixes MINOR: Repository redundancy across p06/p09/p12.)

## 5. One typing baseline; CI wires it, doesn't recreate it

- **p09 (lesson 25):** establish the strict-typed core: pass `mypy --strict` and
  pyright strict, **ship `py.typed`**.
- **p16 (lesson 45):** **wire the existing mypy/pyright checks into the CI /
  pre-commit gate** and fix defects introduced by p10–p15. Do **not** re-add
  `py.typed` or "introduce" pyright config for the first time.

(Fixes MINOR: duplicated py.typed / type-config deliverables.)

## 6. Forward-reference fixes

- **p13 async repository (BLOCKER):** the `async-comprehensions` stage consumes an
  async customer stream. **Add a preceding p13 stage** `async-repository`
  (`AsyncCustomerRepo` as an async generator over the p12 SQLite repo via
  `loop.run_in_executor`), **or** rewire `async-comprehensions` to consume an
  already-built stream (`stream_report_rows()` / `stream_audit_events()` from the
  `async-with-for-gen` stage). Decision: **add the `async-repository` stage** when
  populating lesson 36.
- **p14 httpx wording (MAJOR):** the `httpx-client` stage must not claim the TUI
  exists "from earlier phases" — the TUI is first built in p15. Reword to: "used
  by the CLI now, and by the TUI/GUI built in the next phase."
- **p13 lock-vs-SQLite (MINOR):** add one clause clarifying that the in-memory
  structures being locked are **process-local counters/caches** (ID allocation,
  stock cache) layered over the p12 SQLite repo — both coexist.

## 7. p02 geometry helpers location (MAJOR)

The `complex-bin-coordinates` stage (lesson 04) must keep its helpers in the
**flat p02 module as generic 2-D coordinate functions** over complex numbers.
Do **not** place them under `minierp/inventory/` — that package does not exist
until p11. Defer the "spatial query for Inventory" framing to p03/p04 or p11.

---

## Stdlib-first → OSS ordering (confirmed correct — keep it)

The review confirmed the dependency arc is right; preserve it when populating:

| Capability | Stdlib first | Then OSS |
|------------|--------------|----------|
| Web server | `http.server`, `wsgiref` | FastAPI + uvicorn |
| HTTP client | `urllib`, `http.client` | httpx |
| Templating | hand-built strings, `string.Template` | Jinja2 |
| Tests | `unittest` + `unittest.mock`, `doctest` | pytest + hypothesis + coverage |
| CLI | `argparse` | Typer / Click |
| TUI | `curses` | Rich / Textual |
| DB | `sqlite3` | (stays stdlib; SQLAlchemy optional) |
| Email | `smtplib` + local `aiosmtpd`/MailHog | — |

No paid services anywhere. External systems always use an OSS stand-in.

---

## Per-stage populate checklist

When filling a stage, replace all three stubs and remove the skeleton status line:

1. **`task.md`** — real description (concept → instructions → what to implement),
   a worked example, and a `<div class="hint">` with a genuine hint. Keep the
   "Python features introduced" list accurate.
2. **`task.py`** — starter code with `# TODO` holes the learner fills. For
   `framework` lessons, remember code **propagates forward**: the next stage's
   `task.py` should start from this stage's intended solution.
3. **`tests/test_task.py`** (edu) — real `unittest` checks; remove the skipped
   placeholder. Tests must pass only when the stage is correctly solved.
4. Verify the stage in isolation: `cd <task dir> && python -m unittest`.
