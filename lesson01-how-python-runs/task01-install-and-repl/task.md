# Stage 1: install Python 3.14 and meet the REPL

Welcome to the course. Over these lessons you will build **MiniERP**, a small
business management system, one small step at a time. Each step teaches a piece of
Python and adds something real to the application. By the end you will not just know
the syntax; you will understand why each piece exists and how to design with it.

This first stage has no code to submit. It gets your tools ready and introduces the
single most useful habit for learning Python: trying things out interactively.

## What "running Python" actually means

Python is a language. To run a Python program you need a program that reads your code
and carries out its instructions. That program is called an **interpreter**, and the
standard one is **CPython** (the reference implementation, written in C). When people
say "install Python", they mean install this interpreter.

This course targets **Python 3.14**, the latest stable version. Always use the modern
version: newer Python is faster, has clearer error messages, and includes features
the course relies on.

## Install it

1. Download Python 3.14 from python.org (or install it with a version manager such as
   `pyenv`, or your operating system's package manager).
2. Open a terminal and confirm it:

   ```
   python --version
   ```

   You should see `Python 3.14.x`. On some systems the command is `python3`, and on
   Windows there is a launcher called `py`. If `python` shows an older version, use
   `python3` or `py` so you are on 3.14.

> Note: the machine this course was written on still had Python 3.9. Installing 3.14
> is part of getting set up; do not skip it.

## Meet the REPL

Type `python` on its own and press Enter. You are now in the **REPL**: Read, Evaluate,
Print, Loop. It reads one line, runs it, prints the result, and waits for the next.
The prompt looks like `>>>`.

Try these, one line at a time:

```
>>> 2 + 2
4
>>> _
4
>>> import sys
>>> sys.version
```

Two things to notice:

- In the REPL, typing a bare expression like `2 + 2` shows its result immediately.
  This is a convenience of the REPL only. A file you run does **not** print results
  on its own; you have to ask it to print. Keep that difference in mind, because it
  trips up beginners constantly.
- The underscore `_` holds the result of the last expression. It is handy for quick
  experiments.

`import sys` then `sys.version` shows you the exact interpreter you just launched. In
stage 6 you will read that same information from inside a program.

To leave the REPL, type `exit()` or press Ctrl-D (Ctrl-Z then Enter on Windows).

## Why the REPL matters

The REPL is your laboratory. When you are unsure what a piece of Python does, you do
not guess and you do not search first; you open the REPL and try it. That habit, of
checking reality directly, is what this whole course is training. An engineer who can
test an idea in ten seconds learns far faster than one who only reads about it.

## Before you continue

Confirm you can: see `Python 3.14.x` from `python --version`, start the REPL,
evaluate `2 + 2`, and exit. Then move to the next stage.

Reference: Python documentation, "The Python Tutorial: Using the Python Interpreter"
at docs.python.org.
