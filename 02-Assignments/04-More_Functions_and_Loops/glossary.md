# 📚 Glossary: 04 - More Functions & Loops

**Default parameter value**  
A fallback value for a parameter, used when the caller doesn't pass one. `def count_above(numbers, threshold=70):`

**Positional argument**  
An argument matched to a parameter by its **position** in the call. `describe("Ada", "Math")`

**Keyword argument**  
An argument matched to a parameter by **name**, so the order doesn't matter. `sorted(scores, reverse=True)`

**Returning multiple values**  
`return a, b` returns **one tuple** `(a, b)`, which the caller usually unpacks: `lo, hi = low_high(nums)`.

**Unpacking**  
Assigning the parts of a tuple (or list) to several names at once. `name, grade = "Alice,91".split(",")`

**Scope**  
Where a variable exists and can be used.

**Local variable**  
A variable created inside a function. It exists only while that function call is running.

**Global variable**  
A variable created outside any function. A function *can* read one, but it should get its data from its parameters instead.

**`while` loop**  
Repeats its body as long as a condition is `True`. Needs a **start**, a **condition**, and an **update**.

**Infinite loop**  
A loop whose condition never becomes `False`. Stop it with the Interrupt / Stop button.

**`break`**  
Leaves the loop immediately.

**`continue`**  
Skips the rest of the loop body for this pass and moves on to the next one.

**Sentinel value**  
A special value that means "stop here," like `-1` at the end of a list of readings or the word `done` typed by a user.

**`with open(...) as f:`**  
Opens a file and closes it automatically when the block ends, even if an error happens inside.

**`.strip()`**  
Removes whitespace (spaces, tabs, and the newline `"\n"`) from both ends of a string.

**`.split(",")`**  
Breaks a string into a list wherever the separator appears. `"Alice,91".split(",")` → `['Alice', '91']`

**Exception**  
An error that happens while the program runs, such as `FileNotFoundError` or `ValueError`.

**`try` / `except`**  
Runs code that might fail. If the named exception happens, the `except` block runs instead of crashing.

**`FileNotFoundError`**  
The exception raised when you try to open a file that doesn't exist.

**`ValueError`**  
The exception raised when a value has the right type but the wrong content, such as `int("absent")`.
