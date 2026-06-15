# Python by Building MiniERP — a JetBrains EduTools Guided Project

Learn Python the way professionals actually use it: by **building one real
application, one stage at a time**. Over the course you grow **MiniERP** — a
small-business ERP suite — from a single script into a packaged, tested,
multi-interface product. The course is **standard-library-first** (so you learn
how Python really works) and only then layers in popular **free / open-source**
tools. It targets **Python 3.14** and deliberately tries to leave *no* language
or standard-library feature unexplored — including the rare corners.

> **Status:** Skeleton. The lesson/stage structure and blueprint are generated;
> task descriptions, starter code, and tests are populated section by section.

## What you build: MiniERP

A small-business ERP covering the modules a real business app needs:

- **Products & Inventory** · **Customers** · **Sales & Invoicing** · **Payments**
- **Reporting / Analytics** · **Users & Roles** · **Audit log** · **Import / Export**

…exposed through **four interfaces over one shared core**:

| Interface | Built with (stdlib first → OSS later) |
|-----------|----------------------------------------|
| CLI       | `argparse` → Typer / Click |
| Web       | `http.server` JSON API → FastAPI + uvicorn + Jinja2 |
| Desktop   | `tkinter` (ttk) |
| Text UI   | `curses` → Rich / Textual |

## How the course is structured

The course is a sequence of **guided projects** (EduTools *framework lessons*).
Each one is a phase of Python — from "how the interpreter runs your code" to
metaprogramming and packaging — and each phase's stages move MiniERP forward.

See **[CURRICULUM.md](CURRICULUM.md)** for the full blueprint: every phase,
lesson, and stage, the Python features it teaches, and the MiniERP increment it
delivers.

## Dependency policy (important)

Everything here is runnable with **no paid subscriptions, services, or
proprietary systems**. Phases 1–~12 are **pure standard library**. Later phases
introduce only **free, open-source** libraries, and whenever an external system
is needed we use an OSS stand-in:

- **Database:** `sqlite3` (stdlib) — no server to run.
- **Email/SMTP:** a local [`aiosmtpd`](https://pypi.org/project/aiosmtpd/) or
  MailHog instance — never a real mail provider.
- **Web/test/quality stack:** FastAPI, uvicorn, httpx, Jinja2, pydantic,
  SQLAlchemy, pytest, hypothesis, coverage, ruff, mypy — all OSS.
- **Packaging/release:** `build`, Docker, PyInstaller, Sphinx/MkDocs — all OSS.

## Getting started (for learners)

1. **Install Python 3.14** (this repo's machine still has 3.9 — install 3.14 via
   [python.org](https://www.python.org/downloads/), `pyenv`, or your package
   manager). Stage 1 of the course walks you through verifying it.
2. **Open the course in PyCharm** (or IntelliJ) with the **JetBrains Academy /
   EduTools** plugin. The Course view shows lessons and stages; click **Check**
   to validate each stage.
3. Work stage by stage. Your code in one stage carries into the next.

## For authors (this repo)

Read `docs/AUTHORING_NOTES.md` (continuity rules and the per-stage populate checklist)
before writing any stage.

The skeleton is generated from a manifest so it stays consistent:

```bash
# 1) Design / update the blueprint  ->  tools/curriculum.json
#    (produced by the curriculum-design workflow)
# 2) Materialise the EduTools skeleton:
python tools/scaffold_course.py            # generate lessons, stages, configs, CURRICULUM.md
python tools/scaffold_course.py --dry-run  # preview without writing
python tools/scaffold_course.py --clean    # rebuild generated lessonNN-* dirs from scratch
```

Then **populate section by section**: replace each stage's `task.md`, `task.py`,
and `tests/test_task.py` stubs with the real description, starter code, and checks.

### Layout

```
course-info.yaml            # course metadata + ordered lesson list
CURRICULUM.md               # generated human-readable blueprint
lessonNN-<slug>/
  lesson-info.yaml          # type: framework (a guided project), ordered stages
  taskNN-<slug>/
    task-info.yaml          # task type (edu/theory/output/choice) + file visibility
    task.md                 # stage description (shown to the learner)
    task.py                 # starter code
    tests/test_task.py      # checks (edu stages)
tools/
  scaffold_course.py        # skeleton generator
  curriculum.json           # the manifest (source of truth)
```
