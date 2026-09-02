# 📚 Glossary: 04 - Functions

**Function**  
A named, reusable block of code defined with `def`, optionally accepting parameters and returning a value.

**Parameter**  
A named input a function expects, listed in its `def` line, e.g. `name` in `def greet(name):`.

**Argument**  
The actual value passed in when a function is called, e.g. `'Ada'` in `greet('Ada')`.

**`return`**  
Sends a value back to the code that called the function. A function with no `return` (or a bare `return`) returns `None`.

**Default Parameter Value**  
A fallback value a parameter uses if no argument is given for it, e.g. `greeting='Hello'` in `def greet(name, greeting='Hello'):`. The same underlying idea as `dictionary.get(key, default)`.

**Local Scope**  
Variables created inside a function exist only inside that function and disappear once it finishes running.

**Global Scope**  
Variables created outside any function, visible throughout the file (but not automatically writable from inside a function without extra steps).

**Positional Argument**  
An argument matched to a parameter by its position/order in the function call.

**Keyword Argument**  
An argument matched to a parameter by name, e.g. `greet(name='Ada')` — order doesn't matter.

**`*args`**  
Collects any number of extra positional arguments into a tuple inside the function.

**`**kwargs`**  
Collects any number of extra keyword arguments into a dictionary inside the function.

**`type()`**  
Returns the exact type of a value, e.g. `type(5)` is `int`.

**`isinstance()`**  
Checks whether a value is an instance of a given type (or one of several types), and — unlike `type(x) == int` — also recognizes subclasses.

**Overloading (and why Python doesn't have it)**  
In languages like C++, you can define multiple functions with the same name but different parameter types. Python only allows one `def` per name in a scope, so type-based branching (`isinstance()` checks) is how Python code gets similar behavior.

**Duck Typing**  
Writing code that just tries to use a value the way it expects (e.g. calling `len()` on it) rather than checking its type first — "if it walks like a duck and quacks like a duck." Named after the idea that behavior matters more than declared type.

**Unpacking Into a Call** *(Challenge)*  
Using `*` or `**` when *calling* a function to spread a list into positional arguments or a dict into keyword arguments, e.g. `add3(*[1, 2, 3])`.

**Mutable Default Gotcha** *(Challenge)*  
A default parameter value is evaluated once, when the function is defined — not on every call. Using a mutable default like `[]` means every call without that argument shares the *same* list.
