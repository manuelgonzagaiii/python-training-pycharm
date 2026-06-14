# Stage 5: the entry point and the `__main__` guard

You have read how Python turns your code into something the machine runs. Now you
write the first real file of MiniERP, the application you will grow throughout this
course.

## What you are building

A file named `main.py`. Think of it as the front door of the program: it is the
file you run to start MiniERP. Right now it does just two things.

- It defines a function `welcome()` that returns the line shown at start-up.
- It runs the program (prints that line) only when you launch this file yourself.

## The one idea behind this stage

A Python file always has two possible roles, and they pull in opposite directions:

- As a **library**: other files `import` it to reuse the functions inside it.
- As a **program**: you run it to make something happen.

Here is the problem. When you import a file, Python executes every line at the top
level of that file, top to bottom. So if `main.py` simply had `print(welcome())`
sitting at the top level, then the moment any other part of MiniERP imported
`main` to reuse `welcome()`, the start-up banner would print as an unwanted side
effect. That is a real bug in real projects: a library that does things just by
being imported.

The fix is a fence. Every module has a built-in variable called `__name__`. Python
sets it for you:

- When you run the file directly (`python main.py`), `__name__` is the string
  `"__main__"`.
- When the file is imported by another file, `__name__` is the module's own name
  (here, `"main"`).

So the line

```python
if __name__ == "__main__":
    print(welcome())
```

means: *run this part only if I am the file the user launched, not when I am being
imported*. The mental model: code that **defines** things lives outside the guard
so it can be reused; code that **does** things lives inside the guard so it runs
only on purpose.

## Why split `welcome()` out instead of writing one print line

Two reasons, both about design rather than typing fewer characters.

- **Reuse.** A function can be called from anywhere: the web interface, the
  desktop interface, a test. A bare `print` can only be run.
- **Testing.** A function that *returns* a value can be checked automatically (the
  test below calls `welcome()` and inspects what comes back). Code that only prints
  is much harder to check. Returning data and deciding to print it are two separate
  responsibilities, and keeping them separate is a habit that pays off for the
  whole project.

This separation (compute a value here, decide to show it there) is the seed of the
"shared core, many front-ends" design that MiniERP is built on.

## Your task

Open `main.py`. Fill in the two blanks:

1. Make `welcome()` return a short, non-empty line of text. The wording is yours.
2. Complete the `if` condition so the print runs only when the file is launched
   directly.

Run it with `python main.py`: you should see your line. Then press **Check**.

## What the check verifies, and what it leaves to you

This follows the project's grading rule: it judges whether your program is valid
and works, not whether it matches our wording.

- Enforced (these are the rules): `welcome()` must return a non-empty string;
  importing `main` must print nothing; running `main.py` must print your welcome
  line. The guard is what makes the second and third both true at once.
- Your free choice: the actual welcome text. "Welcome to MiniERP", "MiniERP is
  starting", or anything else non-empty all pass.

<div class="hint" title="If you are stuck on welcome()">

A function returns a value with the `return` keyword. A line of text is written
inside quotes, for example `return "MiniERP ready"`.

</div>

<div class="hint" title="If you are stuck on the guard">

Compare the built-in name to the special string for a directly-run file:
`__name__ == "__main__"`. Note the double underscores on both.

</div>

Reference: Python documentation, "`__main__` — Top-level code environment" at
docs.python.org.
