# 📚 Glossary: 03 - Strings and Text

**String (`str`)**  
An immutable, ordered sequence of characters. Created with `'...'`, `"..."`, or `'''...'''`.

**Escape Character**  
A backslash `\` followed by a character, used to insert something that would otherwise be hard to type directly — e.g. `\n` (newline), `\t` (tab), `\'` (literal quote).

**Triple-Quoted String**  
A string wrapped in `'''` or `"""`, which can span multiple lines without needing `\n`.

**Immutable**  
Cannot be changed after creation. Strings, like tuples, are immutable — `.replace()` and similar methods return a *new* string rather than modifying the original.

**Concatenation**  
Joining strings together with `+`, e.g. `'Py' + 'thon'`.

**`.upper()` / `.lower()` / `.title()`**  
Return a new string with changed letter casing.

**`.strip()` / `.lstrip()` / `.rstrip()`**  
Remove whitespace (or other specified characters) from both ends, the left end, or the right end of a string.

**`.split()`**  
Breaks a string into a list of pieces, splitting on whitespace by default or on a given separator.

**`.join()`**  
The reverse of `.split()` — glues a list of strings together with a separator: `'-'.join(['a', 'b'])` → `'a-b'`.

**`.find()` / `in`**  
`.find()` returns the index where a substring starts (or `-1` if not found). `in` gives a simpler `True`/`False` membership check.

**`.replace()`**  
Returns a new string with all occurrences of one substring swapped for another.

**Boolean Check Methods**  
String methods that return `True`/`False`, like `.isdigit()`, `.isalpha()`, `.startswith()`, `.endswith()`.

**f-string**  
A string literal prefixed with `f`, where anything inside `{}` is evaluated and inserted, e.g. `f'{name} is {age}'`.

**Format Spec**  
The part after a `:` inside an f-string's `{}` that controls display — decimal places (`:.2f`), thousands separators (`:,`), or alignment (`:>10`, `:<10`, `:^10`).

**Raw String** *(Challenge)*  
A string prefixed with `r` that disables escape-character processing entirely, e.g. `r'C:\Users'`.
