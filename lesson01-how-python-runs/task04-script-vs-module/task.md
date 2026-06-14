# Stage 4: running a script versus importing a module

There is no code to submit here. This stage sets up a rule that MiniERP follows for
the rest of the course, and explains the bug it prevents. The next stage puts the rule
into practice.

## Two ways to use the same file

A Python file can be used in two different ways:

- **Run it as a script:** `python main.py`. Python executes the file from top to
  bottom.
- **Import it as a module:** another file says `import main` to reuse the functions
  inside it.

Here is the part that surprises people: **importing a module also runs it**. When you
import a file, Python executes every statement at its top level, top to bottom, so it
can create the functions and values defined there. The difference is intent. When you
run a script you mean "do the work". When you import a module you mean "give me your
definitions" but Python still runs the top-level lines to build them.

## The bug this creates

Suppose `main.py` had this at the top level, not inside any guard:

```python
def welcome():
    return "Welcome to MiniERP"

print(welcome())   # top level: runs on import too
```

Now another file does `import main` just to reuse `welcome()`. Because importing runs
the top-level lines, the `print` fires as an unwanted side effect. Tools that scan
your code, test runners, and other modules would all trigger that print just by
importing the file. A file that does things merely by being imported is a classic
defect.

The rule MiniERP will follow from now on:

> Modules **define** things at the top level (functions, classes, constants) and have
> **no visible side effects** when imported. Only the program's entry point actually
> **does** things, and even then only when it is launched directly.

The next stage shows the mechanism that enforces this: the `if __name__ == "__main__":`
guard. Top-level code runs once per process when the module is first imported or run;
the guard is what lets a single file be both a safe library and a runnable program.

## Two ways to launch, briefly

- `python main.py` runs the file by its path.
- `python -m main` runs it as a module by name (Python finds it on its search path,
  `sys.path`). You will use `-m` often later, for example `python -m venv` in stage 7
  and `python -m pytest` much later.

Both are normal. The point for now is simply that "run" and "import" are different
intents over the same file, and good modules behave well under both.

Reference: Python documentation, "The import system" and "`__main__`" at
docs.python.org.
