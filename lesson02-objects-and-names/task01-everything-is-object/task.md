# Stage 1: everything is an object

This lesson is the conceptual heart of Python. If you understand the few ideas here,
a huge amount of the language stops being surprising. There is no code to submit in
this stage; you will use the REPL to inspect the `main.py` you already wrote.

## The one big idea

In Python, every value is an **object**. Not just the obvious things like the number
`42` or the string `"MiniERP"`, but also your functions, the module itself, classes,
and even types. There is no separate category of "primitive" values sitting outside
the object system, the way some languages have. Everything is an object.

Every object has three things:

- A **type**: what kind of thing it is. You ask with `type(x)`.
- An **identity**: which specific object it is, a number you can read with `id(x)`.
  Think of it as the object's address. (More on this in stage 3.)
- A **value**: the data it holds.

## See it with your own code

Open the REPL in the folder that has your `main.py` from lesson 1 and try this:

```
>>> import main
>>> type(42)
<class 'int'>
>>> type("MiniERP")
<class 'str'>
>>> type(main.welcome)
<class 'function'>
>>> type(main)
<class 'module'>
```

Look at the last two. `main.welcome` is your function, and Python says its type is
`function`. The module `main` is itself an object of type `module`. Your own code is
made of objects.

Because functions are objects, they can carry information you can read:

```
>>> main.welcome.__name__
'welcome'
>>> main.welcome.__doc__
'Return the line shown when MiniERP starts.'
>>> type(main.welcome()).__name__
'str'
```

`__name__` and `__doc__` are **attributes**: pieces of data attached to an object. The
double underscores mark them as part of Python's built-in machinery (people say
"dunder", short for double underscore). You will meet many more of them. For now the
point is simply that they exist and that you can read them, because a function is an
object like any other.

## Why this matters for design

This is not trivia. It is the reason Python is so flexible:

- Because functions are objects, you can pass a function to another function, store it
  in a list, or return it from a function. Later that lets you build things like the
  command dispatcher and the plugin system in MiniERP.
- Because everything has a `type`, you can ask any value what it is at runtime, which
  is exactly what you do in the next stage.
- Because objects carry attributes like `__doc__`, your documentation is not just for
  humans reading the source; it is data the program itself can read (tools and `help()`
  use it).

The mental model to carry forward: a Python program is a web of objects referring to
each other, and names (variables) are just labels you attach to those objects. The
next stage makes that name-versus-object distinction precise, because getting it wrong
is the single most common source of confusion for newcomers.

Reference: Python documentation, "The Python Language Reference: Data model" at
docs.python.org.
