# 📚 Glossary: 01 - Working with Data (Basic)

**List**  
A mutable, ordered collection of items. Created with square brackets `[]`.

**Tuple**  
An immutable, ordered collection of items. Created with parentheses `()`.

**Dictionary**  
A collection of key-value pairs. Created with curly braces `{}`.

**Indexing**  
Accessing elements in lists and tuples using their position.

**Slicing**  
Using `[start:stop]` syntax to get parts of a list or tuple.

**append()**  
List method to add a new item to the end.

**remove()**  
List method to remove an item by value.

**get()**  
Dictionary method to safely retrieve a value by key, with an optional default.

**items()**  
Dictionary method that returns a view of key-value pairs.

**pop()**  
Dictionary method to remove a key and return its value; also works on lists to remove by position.

**Hashable**  
Describes a value that can't change after creation (like a tuple or string) and can therefore be used as a dictionary key or stored in a `set`. Lists are *not* hashable.

**zip()**  
A built-in function that pairs up items from two or more sequences, producing an iterable of tuples.

**\*args**  
A function parameter that collects any number of extra positional arguments into a tuple.

**List Comprehension** *(Challenge)*  
A compact way to build a list from a loop in a single line, e.g. `[n**2 for n in range(10)]`.

**namedtuple** *(Challenge)*  
A `collections` tool that lets you give named fields to positions in a tuple, e.g. `Point(x, y)` instead of a plain `(5, 10)`.
