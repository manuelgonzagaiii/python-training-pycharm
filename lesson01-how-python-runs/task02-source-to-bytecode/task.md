# Stage 2: source, bytecode, and the virtual machine

This stage explains what happens between you pressing Run and your program doing
something. There is no code to submit. The goal is a correct mental model, because
almost every later "why did that happen?" traces back to this picture.

## The pipeline

When CPython runs your file, it goes through these steps:

1. **Source** — the text you wrote, for example `main.py`.
2. **Parse** — Python reads the text and builds a tree that represents its structure,
   called an AST (abstract syntax tree). This is where syntax errors are caught.
3. **Compile to bytecode** — the tree is turned into **bytecode**: a long list of
   small, simple instructions (load this value, add, call that function, return).
4. **Execute on the virtual machine** — CPython's **virtual machine** is a loop that
   reads those instructions one by one and performs them.

So the common belief that "Python is interpreted line by line" is not quite right.
Your code is first compiled (to bytecode), and then a virtual machine runs the
bytecode. It is also not compiled all the way down to native machine code the way C
is. Python sits in between, and that middle ground is what gives it both its
flexibility and its speed characteristics.

## Where the compiled code is cached

You may have seen a `__pycache__` folder appear with files ending in `.pyc`. Those are
the compiled bytecode, saved so Python does not have to recompile an unchanged file
every time. It is purely a cache.

- You never edit these files.
- Deleting `__pycache__` is always safe; Python simply rebuilds it on the next run.
- It belongs in `.gitignore` (this project already ignores it), because it is
  generated, not source.

## Language versus implementation

Two words people mix up:

- **Python** is the language: the rules, the grammar, what the keywords mean. This is
  defined in the language reference.
- **CPython** is one **implementation** of those rules: the actual program that runs
  your code, including the bytecode and the virtual machine.

Bytecode is a detail of CPython, not part of the language. Other implementations
exist, such as PyPy (which can run some programs much faster). They follow the same
language but do the work differently. The practical takeaway: rely on documented
language behaviour, not on the exact bytecode, because the bytecode can change between
versions and between implementations.

## Why this matters for MiniERP

Every module you write for MiniERP travels this same path: your source becomes
bytecode and runs on the virtual machine. Because of that, you can disassemble your
own functions and look at what the machine will do. That is exactly the hands-on tool
you use in the next stage.

Reference: Python documentation, "Design and History FAQ" and the `dis` module page
at docs.python.org.
