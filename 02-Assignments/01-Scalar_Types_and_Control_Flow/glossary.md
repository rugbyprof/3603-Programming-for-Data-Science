# 📚 Glossary: 02 - Scalar Types and Control Flow

**int**  
Integer values (whole numbers like 5, -2, 100).

**float**  
Decimal numbers like 3.14 or -0.001.

**str**  
A string of characters, e.g. `"hello"`.

**bool**  
Boolean value: `True` or `False`.

**Type Casting**  
Converting a value from one type to another, e.g. `int('21')` turns the string `'21'` into the integer `21`.

**Floor Division (`//`)**  
Division that drops the remainder, e.g. `7 // 2` is `3`.

**Modulo (`%`)**  
Returns the remainder of a division, e.g. `7 % 2` is `1`.

**Comparison Operators**  
Used to compare values: `==`, `!=`, `<`, `>`, `<=`, `>=`.

**Logical Operators**  
Used to combine conditions: `and`, `or`, `not`.

**if / elif / else**  
Used to control the flow of code depending on conditions.

**Truthy / Falsy**  
Non-boolean values that evaluate to `True` or `False` in conditionals (e.g. `0` and `''` are falsy; most other values are truthy).

**Chained Comparison**  
Writing a comparison the way you would on paper, e.g. `0 <= score <= 100`, instead of `score >= 0 and score <= 100`.

**Indentation**  
Whitespace that defines code blocks in Python. Critical for control flow.

**Code Block**  
A group of statements that run together, marked by shared indentation under an `if`/`elif`/`else` (or later, a loop or function). A block can hold as many lines as it needs.

**match / case**  
A Python 3.10+ statement for checking a value against several possible patterns, similar in spirit to a C++ `switch` but able to match strings and combine multiple values per `case` with `|`.

**Conditional Expression ("Ternary")** *(Challenge)*  
A one-line if/else, e.g. `status = 'adult' if age >= 18 else 'minor'`.

**Floating-Point Precision** *(Challenge)*  
The reason `0.1 + 0.2` doesn't print exactly `0.3` — floats are stored in binary, and most decimal fractions can't be represented exactly.
