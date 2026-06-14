# Stage 6: comments, docstrings, and self-documenting code

Code is read far more often than it is written. This stage covers the two ways Python
lets you explain code, when to use each, and the habit MiniERP follows from here on.

## Comments versus docstrings

They look similar but serve different audiences.

- A **comment** starts with `#`. It is for someone reading the source. Python ignores
  it completely; it does not exist once the program runs. Use comments to explain
  **why** a line does something non-obvious, not to restate what the code plainly says.
- A **docstring** is a string literal placed as the first statement of a module,
  function, or class. It is for someone *using* the thing, and unlike a comment it
  survives into the running program: Python stores it on the object as `__doc__`.

```
>>> import main
>>> main.welcome.__doc__
'Return the line shown when MiniERP starts.'
>>> main.__doc__[:7]
'MiniERP'
```

Because docstrings are real data, tools can read them. `help(main)` prints the module
docstring and every function's docstring. The documentation site you build much later
(the Sphinx phase) is generated from these. A `#` comment can do none of that. So the
guideline is: explain the *why* of a tricky line with a comment, and describe *what a
function does and returns* with a docstring.

## What a good docstring looks like (PEP 257)

PEP 257 is the convention for docstrings. The essentials:

- Use triple double-quotes: `"""like this"""`, even for one line, so it is easy to
  extend later.
- The first line is a short summary written as an instruction: "Return the trimmed
  name" rather than "This function returns...".
- For something with more to say, put the one-line summary, a blank line, then the
  details. The module docstring you write below uses that shape.

A module docstring sits at the very top of the file, before any imports. It is the
first thing a reader (and `help()`) sees, so it should say what the file is for in a
sentence or two.

## Why bother, honestly

Skipping docstrings feels faster for about a week. Then you (or a teammate) open the
file and have to read every function body to remember what it does. Docstrings are the
difference between code you can use from its interface and code you have to reverse
engineer. For a project with four front-ends sharing one core, that clarity is not
optional. This is also why best-practice tools and this course treat an undocumented
public function as unfinished.

## What you are doing

The helpers in `main.py` already carry one-line docstrings; read them as examples of
the style. Your job is the **module docstring**: the file currently needs a clear 2 to
3 line summary at the very top describing what MiniERP is and what running this file
does. Write it in the blank provided.

## Your task

Open `main.py` and fill the module docstring at the top of the file. Make it a
non-empty summary that names the product (MiniERP) and says what the file is.

## What the check verifies, and what it leaves to you

- Enforced: the module has a non-empty docstring that mentions MiniERP, and every
  public helper (`welcome`, `python_line`, `describe`, `same_object`, `display_name`,
  `banner`) has a non-empty docstring. The habit is the rule.
- Your free choice: the actual words. Any clear, non-empty description that names the
  product passes; there is no required sentence.

<div class="hint" title="Where it goes">

The module docstring must be the very first thing in the file, a triple-quoted string
above `import sys`. A first line plus a sentence or two is plenty.

</div>

Reference: Python documentation, "PEP 257 - Docstring Conventions" and
"Built-in Functions: help()" at docs.python.org.
