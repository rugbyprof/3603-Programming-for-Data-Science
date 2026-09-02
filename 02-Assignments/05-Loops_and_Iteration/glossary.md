# 📚 Glossary: 05 - Loops and Iteration

**for loop**  
Repeats a block of code once for each item in a sequence (a "for-each" loop — Python doesn't require you to manage an index).

**while loop**  
Repeats a block of code as long as a condition is `True`.

**range(start, stop, step)**  
Generates a sequence of numbers, stop-exclusive.

**enumerate()**  
Wraps a sequence so a `for` loop gets both the index and the value at once: `for i, item in enumerate(items):`.

**break**  
Immediately exits the loop entirely.

**continue**  
Skips the rest of the current iteration and moves on to the next one.

**Infinite Loop**  
A `while` loop whose condition never becomes `False`, so it never stops on its own. Interrupt the kernel/cell to escape one.

**Sentinel Value**  
A special value (like `'quit'`) that signals a loop should stop, typically checked in a `while True:` loop with `break`.

**with**  
A context manager, used here for opening files. Guarantees the file gets closed automatically, even if an error happens inside the block.

**open()**  
Function used to open files. Needs a mode like `'r'` (read) or `'w'` (write).

**try / except**  
Catches an error instead of letting it crash the program — e.g. `except FileNotFoundError:` when a file might not exist.

**strip()**  
Removes whitespace (including the trailing newline) from the beginning/end of a string.

**split()**  
Splits a string into a list, on whitespace by default or on a given separator.

**Walrus Operator (`:=`)** *(Challenge)*  
Assigns a value and returns it in the same expression, e.g. `while (word := input()) != 'quit':`.
