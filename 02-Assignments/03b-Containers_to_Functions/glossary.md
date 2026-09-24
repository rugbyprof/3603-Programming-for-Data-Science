# 📚 Glossary: 03b - Containers → Functions

**Container**  
A value that holds other values. The four built-in containers are list, tuple, dictionary, and set.

**List**  
An ordered, changeable collection: *a bunch of things*. `[87, 91, 74]`

**Tuple**  
An ordered collection that can't be changed, used for *one thing with several fixed parts*. Each position has a fixed meaning. `(33.91, -98.49)`

**Dictionary**  
A collection of key → value pairs, used to *look something up by name*. `{"Bob": 84}`

**Set**  
An unordered collection with no duplicates, used when you only care *whether* something is there. `{"OOP", "Database"}`

**Index**  
A position in a list or tuple. The first index is `0`, and `-1` is the last item.

**Nested container**  
A container inside another container, such as a list of dictionaries.

**Trace**  
Running code by hand, writing down the value of every variable after each step.

**Accumulate pattern**  
Start at `0` and add each item to a running total. Produces a number.

**Count pattern**  
Start at `0` and add `1` each time an item passes a test. Produces a number.

**Filter pattern**  
Start with `[]` and `.append()` each item that passes a test. Produces a new list.

**Best So Far pattern**  
Start with the first item, and replace it whenever a better item shows up. Used for max/min.

**Function**  
A named, reusable block of code that takes inputs and (usually) returns an output.

**Define (a function)**  
Create it with `def`. Nothing inside it runs yet.

**Call (a function)**  
Run it by writing its name followed by parentheses: `square(10)`.

**Parameter**  
The placeholder name in a function's definition. In `def square(x):`, `x` is the parameter.

**Argument**  
The actual value passed in when you call a function. In `square(10)`, `10` is the argument.

**Return value**  
The value a function sends back to the code that called it. The call gets replaced by this value.

**`print()` vs. `return`**  
`print()` shows a value to the human. `return` gives a value back to the program.

**`None`**  
Python's "nothing" value. A function with no `return` gives back `None`.

**Contract**  
A description of what goes **in**, what comes **out**, and what the function **does**. Usually written in a docstring.

**Docstring**  
A triple-quoted string on the first line of a function's body that documents it. `help()` shows it.

**Mutation**  
Changing a container in place (for example `.append()` or `.sort()`). A list passed into a function is the *same* list, so mutating it inside the function changes it for the caller too.

**Refactor**  
Restructuring code (for example, splitting a blob into functions) without changing what it does.

**Pipeline**  
A chain of functions where the output of one step becomes the input to the next.

**Test case (normal / boundary / weird)**  
A normal input checks the usual case, a boundary input checks the edges (one item, exactly equal to a cutoff), and a weird input checks unusual cases (an empty list).
