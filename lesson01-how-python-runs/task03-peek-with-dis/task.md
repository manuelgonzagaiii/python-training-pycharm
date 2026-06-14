# Stage 3: peek under the hood with `dis`

Stage 2 explained that Python compiles your source into **bytecode**, a list of
simple instructions that the virtual machine then runs. That can feel abstract. In
this stage you make it concrete: you write a one-line function and look at the exact
instructions Python produced for it.

## What you are building

A small sandbox file, `bytecode_demo.py`. It is not part of MiniERP yet. It holds a
preview function, `line_total(quantity, price)`, which returns a quantity multiplied
by a price. (Later in the course this idea becomes a real invoice line total, done
properly with money types. Here it is just a clear thing to disassemble.)

## The key idea: a function carries the code that runs

When you define a function, Python compiles its body into a **code object** and
attaches it to the function. You can reach it as `line_total.__code__`. The code
object is the bytecode plus the constants and names the function needs. In other
words, the function is not the source text you typed; it is the compiled instructions
underneath, and those are what actually execute.

The standard-library module `dis` (short for *disassemble*) prints those
instructions in a form you can read. Calling `dis.dis(line_total)` shows lines such
as `LOAD_FAST`, `BINARY_OP`, and `RETURN_VALUE`. Roughly:

- `LOAD_FAST` puts a local variable (here `quantity`, then `price`) onto a small
  working stack.
- `BINARY_OP` takes the two values off the stack, multiplies them, and puts the
  result back.
- `RETURN_VALUE` hands that result back to whoever called the function.

That is the whole machine in miniature: push values, do an operation, return. The
exact opcode names and numbers differ a little between Python versions, which is the
point of stage 2 (bytecode is an implementation detail, not the language itself).

## Why this is worth knowing

You will almost never read bytecode in day-to-day work. So why look at all?

- It removes the magic. "Compiled to bytecode and run by a VM" stops being a phrase
  and becomes something you have seen with your own eyes.
- It is a real debugging tool for the rare hard question: why two ways of writing the
  same thing behave differently, or where a surprising cost comes from. Knowing
  `dis` exists, and that every function carries a `__code__`, is what separates an
  engineer who can investigate from one who can only guess.

## Your task

Open `bytecode_demo.py`. Fill the one blank so `line_total` returns the quantity
multiplied by the price. Then run it:

```
python bytecode_demo.py
```

Read the disassembly it prints, and find the multiply step and the return. Then
press **Check**.

## What the check verifies, and what it leaves to you

- Enforced: `line_total(quantity, price)` returns the correct product for several
  inputs, including a zero quantity and a non-whole price. This is genuine
  right-or-wrong: a total that is not the product is simply incorrect.
- Your free choice: how you write the multiplication. `quantity * price` and
  `price * quantity` are both accepted. The check does **not** look at the bytecode,
  because there is more than one valid way to express this and the disassembly even
  differs between Python versions. We grade the result, not the keystrokes.

<div class="hint" title="The multiplication">

The multiply operator is `*`. The function should `return` the two parameters
multiplied together.

</div>

Reference: Python documentation, "`dis` — Disassembler for Python bytecode" at
docs.python.org.
