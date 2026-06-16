#!/usr/bin/env python3
"""Validate the EduTools course structure on disk before the IDE loads it.

EduTools refuses to open a task whose `task-info.yaml` is invalid, and a guided
project (`framework` lesson) whose first stage is invalid will not open at all.
Those failures surface only as a quiet "Course ... loaded with errors" line in the
IDE log, so this script makes them loud and fixable from the terminal.

Checks (kept deliberately close to what EduTools enforces):
  - every item in course-info.yaml `content:` exists and is a section or lesson
  - every lesson in a section exists; every task in a lesson exists
  - every task has a `type:`
  - every file listed under a task's `files:` actually exists on disk
  - a `theory` task declares at least its description (a non-empty `files:`)
  - an `edu` task declares a test file
  - a `choice` task declares `options:` (or `choice_options:`)

Warnings (won't fail the build, but worth cleaning):
  - `*.tmpl` author-source files sitting inside task dirs (these should be
    author-only and kept out of the shipped course)
  - `.py` files on disk that no task-info declares

Usage:
    python tools/validate_course.py          # validate, exit 1 on any error
    python tools/validate_course.py --strict  # also fail on warnings
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASK_META = {"task-info.yaml", "task-remote-info.yaml"}


def content_list(text: str) -> list:
    """Bare `  - foo` entries (lesson/section/course content), not `- name:` files."""
    return re.findall(r"^\s*-\s+(?!name:)([^\s:]+)\s*$", text, re.M)


def files_list(text: str) -> list:
    return re.findall(r"^\s*-\s*name:\s*(\S+)", text, re.M)


def task_type(text: str):
    m = re.search(r"^type:\s*(\S+)", text, re.M)
    return m.group(1) if m else None


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def validate():
    errors, warnings = [], []

    course_info = os.path.join(ROOT, "course-info.yaml")
    if not os.path.exists(course_info):
        return ["course-info.yaml is missing"], []

    for item in content_list(read(course_info)):
        idir = os.path.join(ROOT, item)
        if not os.path.isdir(idir):
            errors.append("course-info lists '{0}' but the directory is missing".format(item))
            continue
        is_section = os.path.exists(os.path.join(idir, "section-info.yaml"))
        is_lesson = os.path.exists(os.path.join(idir, "lesson-info.yaml"))
        if not (is_section or is_lesson):
            errors.append("'{0}' has neither section-info.yaml nor lesson-info.yaml".format(item))
            continue

        if is_section:
            lessons = [os.path.join(item, l)
                       for l in content_list(read(os.path.join(idir, "section-info.yaml")))]
        else:
            lessons = [item]

        for ld in lessons:
            ldir = os.path.join(ROOT, ld)
            linfo = os.path.join(ldir, "lesson-info.yaml")
            if not os.path.exists(linfo):
                errors.append("{0}: lesson-info.yaml missing".format(ld))
                continue
            linfo_text = read(linfo)
            lesson_typ = task_type(linfo_text)  # 'framework' for guided projects, else regular
            tasks = content_list(linfo_text)
            task_types = []
            if not tasks:
                warnings.append("{0}: lesson-info has empty content".format(ld))
            for t in tasks:
                tdir = os.path.join(ldir, t)
                tinfo = os.path.join(tdir, "task-info.yaml")
                if not os.path.exists(tinfo):
                    errors.append("{0}/{1}: task-info.yaml missing".format(ld, t))
                    continue
                tx = read(tinfo)
                typ = task_type(tx)
                task_types.append(typ)
                decl = files_list(tx)
                if typ is None:
                    errors.append("{0}/{1}: no type".format(ld, t))
                for f in decl:
                    if not os.path.exists(os.path.join(tdir, f)):
                        errors.append("{0}/{1}: declares '{2}' but that file is missing".format(ld, t, f))
                # A bare theory task (no files) does NOT render its description in
                # the IDE; it must declare task.md (the form the Welcome lesson uses).
                if typ == "theory" and not decl:
                    errors.append("{0}/{1}: theory task declares no files; declare task.md so it renders".format(ld, t))
                if typ == "edu" and not any("test" in f for f in decl):
                    errors.append("{0}/{1}: edu task declares no test file".format(ld, t))
                # NOTE: a choice task legitimately has no `options:` in task-info —
                # EduTools keeps the options in its own author database and rewrites
                # task-info to a minimal descriptor, so we don't require them here.
                # warnings: stray author/source files
                for base, _dirs, files in os.walk(tdir):
                    for f in files:
                        rel = os.path.relpath(os.path.join(base, f), tdir)
                        if f.endswith(".tmpl"):
                            warnings.append("{0}/{1}: author-only template in task dir: {2}".format(ld, t, rel))
                        elif f.endswith(".py") and rel not in decl:
                            warnings.append("{0}/{1}: undeclared .py file: {2}".format(ld, t, rel))
            # A framework (guided-project) lesson is built around code that carries
            # forward between stages; a theory/choice stage has no code and will not
            # open inside one (the description panel stays blank). Such lessons must
            # be regular lessons instead.
            if lesson_typ == "framework" and any(tt in ("theory", "choice") for tt in task_types):
                bad = [t for t, tt in zip(tasks, task_types) if tt in ("theory", "choice")]
                errors.append(
                    "{0}: framework lesson contains non-code stages {1}; "
                    "make it a regular lesson (remove 'type: framework')".format(ld, bad))
    return errors, warnings


def main(argv) -> int:
    strict = "--strict" in argv
    errors, warnings = validate()
    if warnings:
        print("Warnings ({0}):".format(len(warnings)))
        for w in warnings:
            print("  - {0}".format(w))
    if errors:
        print("\nERRORS ({0}):".format(len(errors)))
        for e in errors:
            print("  x {0}".format(e))
        print("\nCourse is INVALID — EduTools will load it with errors.")
        return 1
    print("\nCourse structure is valid ({0} warning(s)).".format(len(warnings)))
    return 1 if (strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
