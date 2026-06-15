# Welcome

## Why this course exists

Learning Python has never looked easier. There is a tutorial for everything, and
an AI assistant will finish the line of code you started before you have decided
whether you wanted it. A lot of that is real progress. But it has a side effect I
keep seeing: people can produce working Python without being able to explain a
single thing it does. The code runs, right up until the day it does not, and then
there is nothing to fall back on, because the understanding was never there.

This course is built the other way around. You will write every line of a real
application yourself, and for each one you will understand what it is, why it
exists, and what would break without it. No copy-paste. No black boxes. The day
Python stops being magic to you, everything changes: you stop fearing errors
because you finally know where they live, and you start designing programs
deliberately instead of assembling them from snippets you found.

Here is the part worth saying plainly. An AI can write code, but it cannot care
whether the code is right. It answers exactly what you ask. If you do not
understand the language, you will not even know what to ask for, and you will not
recognise a bad answer when it is handed to you. The developer who will matter is
not the one who prompts the fastest. It is the one who understands the craft
deeply enough to out-think the autocomplete and out-design it.

So we are going to do this the slow way, on purpose.

<!-- AUTHOR NOTE (HTML comment — not shown to students): The strongest welcomes
are personal. If you have a story about why you built this, or how you learned
Python the hard way, this is the place for it — replace or extend the paragraphs
above in your own voice. I did not invent one for you on purpose. -->

## What you'll build

By the end of this course you will have built **MiniERP**, a small-business ERP
(enterprise resource planning) suite — the kind of back-office system a small
company uses to run itself. You grow it one small step at a time, and it ends up
covering real ground: products and inventory, customers, sales and invoicing,
payments, reporting and analytics, users and roles, an audit log, and import and
export.

The interesting part is that MiniERP has **one shared core and four front-ends**:
a command-line interface, a web interface (an HTTP API with a simple HTML UI), a
desktop GUI, and a text UI. Building four faces on one core is deliberate. It
forces you to keep the business logic separate from how it is displayed, and
along the way it exercises far more of Python than a single-screen app ever
would.

## Who this course is for

You do not need to know Python yet. The course starts from the absolute basics —
installing it, what an interpreter is — and goes all the way to the advanced,
rarely-used corners, so that you are never blindsided by an unfamiliar feature in
real work. If you already write code in another language, you will move faster
through the early lessons; if you are new, nothing is skipped.

It targets **Python 3.14**, the latest version. Installing it is the very first
thing you do, in Lesson 1.

## Before you start

You need almost nothing to begin:

- **Python 3.14** — you install it in Lesson 1. Until then, any terminal will do.
- **A JetBrains IDE with the EduTools plugin** — you already have it, or you could
  not be reading this.

The automatic **Check** button that grades your work uses `unittest`, which comes
built into Python itself. There is nothing extra to install and nothing to pay
for, ever. Where the course later needs something like a database or email, it
uses a free, open-source stand-in that runs entirely on your own machine.

## How the course is organised

This is a **guided project**, not a pile of unrelated exercises. It is one
application that grows as you go. The course is grouped into **phases**; each
phase has a few **lessons**; each lesson is made of small **stages** you complete
in order. Within a lesson, the code you write in one stage carries forward into
the next — you are always working on the same, steadily improving MiniERP.

The early phases use **only the standard library**, so you see how Python actually
works underneath. Later phases bring in the popular open-source tools you will
meet in real projects, but only once you understand the version you could write
yourself.

## How to do a stage

1. **Read the description first.** Every stage explains *what* you are about to
   build and, more importantly, *why* — the problem it solves and how a good
   engineer thinks about it. Read it before you touch the code. The understanding
   is the point; the typing is the easy part.
2. **Fill in the blanks.** The code file has highlighted blanks for the parts you
   need to write. Click into each one and type your answer. The rest of the file
   is already written so the program runs.
3. **Press Check.** The grader runs and tells you, in plain language, what is
   correct and what still needs work.
4. **Stuck? Peek the solution.** Use **Peek author's solution** to reveal a
   correct answer, or **Reset task** to start the file over. There is no penalty
   for looking — but try first, because the attempt is where the learning is.

## How marking works — you have real design freedom

This course is graded like a country with fair laws: **strict about what is
genuinely right or wrong, free about everything else.**

- If you enter something **invalid** — a version number that does not exist, a
  value outside an allowed set, a wrong type, something that would break the
  program — the check fails. That is a real mistake, and catching it is part of
  learning.
- If you make a **valid design choice** that simply differs from the author's — a
  different but sensible name, your own wording for a message, a structure you
  prefer — the check **passes**. There is usually more than one correct answer.

So you and another learner can hand in different-looking programs and both be
right. The goal is for you to learn to make sound decisions and design software in
your own way, not to memorise one official version.

## Seeing MiniERP run

The Check only inspects your code. To actually *see* the program run, open a
terminal in the stage you are working on and run it yourself, for example:

```
python main.py
```

Some early stages intentionally do very little on screen — the description tells
you what to expect and why.

## Getting the most out of this

In a world where tools can generate code for you, the valuable skill is no longer
typing — it is understanding. As you work, keep asking yourself:

- What is this line, file, or setting for?
- What would break if it were missing or wrong?
- Why is this the recommended way, and what are the alternatives?

If you can answer those, you are becoming a designer of software, not just a
writer of it. That is exactly what this course is built to develop.

When you are ready, open the first lesson, **How Python Runs Your Code**, and
let's get our hands dirty.

*— [add your name here]*
