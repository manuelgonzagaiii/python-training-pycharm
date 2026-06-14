# Stage 6: report the running Python version

In the last stage you built `main.py` with a `welcome()` function and a `__main__`
guard. Now you extend that same file so start-up also reports which Python is
running it. This finishes the goal of the phase: a banner with a welcome line and a
live version line.

## What you are building

A second function, `python_line()`, that returns text such as
`Running on Python 3.14.3`, and one extra print in the start-up block so the banner
shows both lines.

## The key idea: a program can inspect the interpreter running it

In stage 2 you learned that your code is run by an interpreter (CPython). That
interpreter is not hidden from your program. The standard-library module `sys`
gives you a window into it, and `sys.version_info` tells you exactly which version
is running right now.

`sys.version_info` is a small structured value (a named tuple) with fields you can
read by name:

- `.major` (for example, `3`)
- `.minor` (for example, `14`)
- `.micro` (for example, `3`)

So `version.major`, `version.minor`, and `version.micro` together describe the
running version.

## Why read it live instead of writing "3.14"

This is the real lesson, and it is a design habit, not a trick.

- If you hard-code `"3.14.3"` into the text, the line becomes a **lie** the moment
  the program runs on a different Python. The message would claim 3.14.3 while
  actually running on something else.
- Reading `sys.version_info` means the line is always true, on any machine, with no
  edits. The program reports a fact about itself instead of repeating a guess.

This idea (let the program ask the system for the truth rather than baking in a
value) comes back many times in MiniERP: reading the current date, the logged-in
user, the database location. Hard-coded facts rot; live facts stay correct.

A neat way to build the text is an f-string, a string with an `f` in front whose
`{ }` slots are filled with real values:

```python
f"Running on Python {version.major}.{version.minor}.{version.micro}"
```

`version.major` and friends are read at the moment the line runs, so the result
follows whatever interpreter is in charge.

> Note: there is also `platform.python_version()`, which returns the version as a
> ready-made string. It is fine to know about, but here we use `sys.version_info`
> on purpose, because reading the individual fields teaches what the value really
> is. Building the string yourself is the modern, explicit approach.

## Your task

Open `main.py`. It already contains your `welcome()` and the guard.

1. Finish `python_line()` so it returns a non-empty line that includes the running
   version, built from `version.major`, `version.minor`, and `version.micro`.
2. In the start-up block, add a line that prints `python_line()` after the welcome.

Run `python main.py`: you should see two lines. Then press **Check**.

## What the check verifies, and what it leaves to you

- Enforced: `python_line()` returns a non-empty string that contains the **actual**
  running version (the check computes the real `major.minor.micro` itself and looks
  for it), and start-up prints both the welcome and the version. This is the
  "format must be real" rule: a made-up or hard-coded version that does not match
  the live interpreter fails.
- Your free choice: the wording around the number. "Running on Python 3.14.3",
  "Python 3.14.3", or "Interpreter: 3.14.3" all pass, because all of them contain
  the true version.

<div class="hint" title="Building the line">

Use an f-string and read the fields off the `version` value:
`f"Running on Python {version.major}.{version.minor}.{version.micro}"`.

</div>

<div class="hint" title="Printing both lines">

The welcome is already printed. Add a second `print(...)` on the next line, calling
`python_line()`, at the same indentation, inside the guard.

</div>

Reference: Python documentation, "`sys.version_info`" at docs.python.org.
