# Stage 7: break, continue, pass, and the loop else

Before moving on to the dispatcher, this is a checkpoint on the loop-control tools the
last two stages used. Getting these exactly right is what lets you reason about a loop's
behaviour instead of guessing.

## The four keywords

- **`break`** exits the nearest enclosing loop immediately. Nothing after it in the loop
  body runs, and the loop's `else` (if any) is skipped. You used it in `find_in_catalog`
  to stop on the first match and in `all_lines_valid` to stop on the first bad line.
- **`continue`** skips the rest of the current pass and jumps to the next iteration. The
  loop keeps going. You used it to skip catalog records that did not match the SKU.
- **`pass`** does nothing at all. It is a placeholder for somewhere the grammar needs a
  statement but you have no action — an empty branch, a stub function, a "nothing to do
  here" marker. It is not a loop-control keyword; it neither exits nor skips.

## The loop `else` clause

Both `for` and `while` can carry an `else`. The rule is the same for each and is the one
people get wrong most often:

> The `else` runs only if the loop finished **without** executing a `break`.

It has nothing to do with whether the loop body ran, and nothing to do with the `if`
inside the loop. Think of it as the "ran to completion / nothing interrupted me" branch.
That is why `find_in_catalog` puts its `raise` in the `else`: reaching the `else` means
the search walked the entire catalog and never broke out with a match, i.e. the SKU is
not there.

The quickest way to remember it: a `break` and the loop `else` are opposites — exactly one
of them "wins" each time the loop runs.

## Question

For a `for` or `while` loop that has an `else:` clause, when does the `else` clause run?
