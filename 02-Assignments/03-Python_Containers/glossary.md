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
List method to add a new item to the end. Adds its argument as a *single* element — `[1,2].append([3,4])` gives `[1, 2, [3, 4]]`.

**extend()**  
List method that adds *each item* of an iterable to the end, in place — `[1,2].extend([3,4])` gives `[1, 2, 3, 4]`. Compare with `+`, which builds a new list instead of modifying an existing one.

**remove()**  
List method to remove an item by value.

**del**  
A statement (not a method) that deletes something by index or slice: `del mylist[0]`. Can also delete a dictionary key: `del d['name']`.

**clear()**  
List and dictionary method that removes every item, leaving an empty container.

**Nested List (2D List)**  
A list whose items are themselves lists, forming a grid of rows and columns. Reach a single value with two indexes: `grid[row][col]`.

**enumerate()**  
A built-in that yields `(index, item)` pairs while looping, so you get the position and the value together: `for i, x in enumerate(seq):`.

**range(len(seq))**  
A loop pattern that produces the valid index positions `0, 1, ... len(seq)-1`, used when you need each item's index (for example to modify the list in place).

**get()**  
Dictionary method to safely retrieve a value by key, with an optional default.

**items()**  
Dictionary method that returns a view of key-value pairs.

**List of Dictionaries (records)**  
A list where every item is a dictionary sharing the same keys. Each dictionary is one "row" and the keys act like column headers — the standard shape for tabular data. Access a field with `data[row_index]['key']`.

**Row-number key**  
Wrapping a list of records in a dictionary keyed by position (`{i: row for i, row in enumerate(rows)}`) so a record can be looked up directly by its row number instead of scanning the list.

**Aliasing**  
When two names refer to the *same* object in memory. Storing a dictionary in both a list and another dictionary means a change through one name is visible through the other — they are not copies.

**JSON**  
JavaScript Object Notation — a text format for exchanging data. Its objects map to Python `dict`s, its arrays to `list`s, and `true`/`false`/`null` to `True`/`False`/`None`. A JSON document is just nested lists and dictionaries.

**json module**  
Python's built-in library for JSON. `json.loads(text)` parses JSON text into Python objects; `json.dumps(obj)` serializes Python objects back to JSON text.

**GeoJSON**  
A JSON format for geographic data. A `FeatureCollection` holds a list of `Feature` objects, each with a `geometry` (type plus `coordinates`, ordered `[longitude, latitude]`) and a `properties` dictionary. Read it with ordinary list/dict indexing.

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
