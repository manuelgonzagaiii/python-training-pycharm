# Stage 7: isolate dependencies with a virtual environment

This is the last stage of the lesson, and the last one with no code to submit. You set
up a clean, isolated home for MiniERP's dependencies. Every later phase that installs
a package (pytest, FastAPI, Textual, and others) installs it here.

## The problem: one shared Python is a trap

When you install Python, it comes with one global set of installed packages. If every
project shared that one set, you would hit these problems:

- Project A needs version 1 of a library; project B needs version 2. They cannot both
  win in one shared location.
- A package you installed to try something stays around and pollutes every project.
- You cannot tell which packages your project actually needs versus what happens to be
  installed on your machine, so the project is hard to reproduce on someone else's
  computer.

## The solution: a virtual environment

A **virtual environment** is a private copy of the Python setup for one project: its
own folder of installed packages, separate from the global one and from every other
project. The standard tool to make one is the `venv` module, which ships with Python.

Create one in the project folder:

```
python -m venv .venv
```

That makes a `.venv` directory. Activate it so this terminal uses it:

- macOS / Linux: `source .venv/bin/activate`
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`

Your prompt now shows `(.venv)`. To leave it later, type `deactivate`.

Why `python -m venv` rather than a bare command? Running a tool with `python -m`
guarantees you use the tool belonging to *that* Python, instead of whatever a bare
name on your `PATH` happens to point at. The same reasoning applies to pip below.

## Installing packages with pip

`pip` is Python's package installer. Inside the activated environment:

```
python -m pip install --upgrade pip
python -m pip list
```

`pip list` shows what is installed. Packages land in the environment's `site-packages`
folder, which is separate from the **standard library** (the modules that always come
with Python, such as `sys` and `dis`, which you have already used). That distinction
matters in this course:

- **Standard library**: always available, nothing to install.
- **Third-party packages**: must be installed with pip, into your environment.

When a project does need third-party packages, their names and versions are recorded
in a `requirements.txt` file so anyone can recreate the same environment with one
command. You will meet that file when the first dependency appears.

## MiniERP needs nothing extra yet, and that is the point

Everything you have written so far uses only the standard library, so right now your
`.venv` has no third-party packages at all. That is deliberate. This course is
standard-library-first: you learn how Python itself works before reaching for outside
tools. Later phases add open-source libraries on purpose, once you understand what
they are doing for you, and they install cleanly into the environment you just made.

## Before you continue

Confirm you have created and activated `.venv` for this project. Then you are done with
the lesson: you understand how Python runs your code, you have written MiniERP's entry
point, and you have a clean environment to grow it in.

Reference: Python documentation, "`venv` — Creation of virtual environments" and the
Python Packaging User Guide at docs.python.org and packaging.python.org.
