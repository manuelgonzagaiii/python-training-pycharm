# Stage 7: PEP 8 and the Zen of Python

Style is not decoration. It is how you communicate intent to the next person who reads
your code, including future you. Python has a shared style guide so that code from
different authors looks like it came from one hand. This stage pins down the
conventions every later MiniERP module will follow.

## PEP 8: the style guide

PEP 8 is the official style guide for Python code. The rules you will use constantly:

- Indent with **4 spaces**, never tabs.
- Name functions and variables in **snake_case**: lowercase words joined by
  underscores, like `line_total` and `display_name`.
- Name classes in **CapWords** (also called PascalCase), like `Invoice` or
  `CustomerAccount`. You will use this when classes arrive.
- Constants go in **UPPER_SNAKE_CASE**, like `MAX_RETRIES`.
- Put **two blank lines** between top-level functions and classes (you have already
  been doing this in `main.py`).
- Keep lines reasonably short. This course uses a limit of 88 columns, the common
  modern default.

Hyphens are never allowed in names (`line-total` is not a name at all; Python would
read it as `line` minus `total`). camelCase (`lineTotal`) and CapWords (`LineTotal`)
are valid Python but wrong for a function by PEP 8 convention, so other Python
programmers will read them as a mistake.

You will not memorise every rule. Later in the course you add tools (ruff and an
auto-formatter) that apply PEP 8 for you. Knowing the core rules now means you can read
and write idiomatic code from the start.

## The Zen of Python

Type `import this` in the REPL and Python prints the **Zen of Python**: a short list of
guiding aphorisms by Tim Peters. A few that shape good Python:

- Readability counts.
- Explicit is better than implicit.
- Simple is better than complex.
- There should be one obvious way to do it.

These are the values behind the style rules. When two solutions both work, the Zen is
the tie-breaker: choose the one that is clearer and more explicit. That instinct is
what separates an engineer who designs from one who merely makes it run.

## House rule for MiniERP

Every module you write from here on follows PEP 8: snake_case for functions and
variables, CapWords for classes, 4-space indentation, two blank lines between
top-level definitions. Consistency across the four interfaces depends on it.

## Question

Which name is the PEP 8 compliant way to name a function that totals an invoice line?
