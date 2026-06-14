# Stage 5: talking to the user with print, and a real banner

So far MiniERP prints a couple of plain lines. In this stage you build a proper
start-up banner, and along the way you learn how `print` and `input` really behave and
why good programs keep input and output at the edges.

## print does more than you think

`print` has useful options beyond the value to show:

- `sep` controls what goes between several values. `print("a", "b", sep="-")` prints
  `a-b`.
- `end` controls what goes at the end. By default it is a newline (`"\n"`); set
  `end=""` to print without moving to the next line.

```
>>> print("3", "5", sep=" x ")
3 x 5
>>> print("loading", end="...")
loading...
```

Reaching for `sep` and `end` is cleaner than gluing strings together by hand.

## input always gives you a string

`input(prompt)` reads one line the user types and returns it as a **string**, always.
If you ask for a quantity and the user types `30`, you get the string `"30"`, not the
number `30`. Converting and validating that text is the caller's job (you will do real
parsing later). Two things follow:

- Never assume `input()` gave you a number; convert it on purpose.
- Trim it with `.strip()`, because the user may add stray spaces.

## Keep input and output at the edges

This is the design idea of the stage. A function that **returns** a value is easy to
reuse and easy to test. A function that **prints** can only be run, and to test it you
have to capture what it wrote. So the rule MiniERP follows is:

> Functions compute and return. The entry point decides what to print.

That is why the banner is built by a function that returns a string, and the printing
happens only in the `__main__` block. The same `banner` function will later feed the
web page, the desktop window, and the text interface, none of which want it to `print`
to the console. Build the value once; let each caller decide what to do with it. This
separation is the backbone of MiniERP's "one core, many faces" design.

## What you are building

`banner(title, width=40)`: return a three-line string made of a rule line, the title
centered, and another rule line, joined by newlines. Then wire the start-up block to
print the banner for `"MiniERP"` followed by the version line. This is the actual
welcome banner the phase set out to build.

The pieces:

- `"=" * width` repeats a character to make a rule line of the right length.
- `title.center(width)` pads the title with spaces on both sides so it sits in the
  middle of a field `width` wide. This is a ready-made string method; you do not need
  to compute the padding yourself.
- `"\n".join([...])` joins a list of lines into one string with newlines between them.

`width=40` is a **default argument**: callers can say `banner("MiniERP")` and get a
40-wide banner, or override it with `banner("MiniERP", 20)`.

## Your task

Open `main.py`. Fill the blanks in `banner` (the rule line, the centered title, and the
join), then complete the start-up block so it prints the banner for `"MiniERP"`. Run
`python main.py` to see it, then press Check.

## What the check verifies, and what it leaves to you

- Enforced: `banner` returns exactly three lines; the rule lines and the centered
  title are each `width` columns wide; the title appears centered; the default width is
  40; and importing the module still prints nothing while running it prints the banner
  and the live version. The structure and the "no I/O on import" rule are the law here.
- Your free choice: which character makes the rule line. The solution uses `"="`, but
  `"-"` or `"*"` pass too, since the check only requires a single repeated visible
  character.

<div class="hint" title="The three blanks in banner">

`rule = "=" * width`, then `middle = title.center(width)`, then
`return "\n".join([rule, middle, rule])`.

</div>

<div class="hint" title="Wiring the banner in">

Inside the guard, call `print(banner("MiniERP"))` on its own line, above the existing
version print.

</div>

Reference: Python documentation, "Built-in Functions: print(), input()" and
"str.center" in the string methods, at docs.python.org.
