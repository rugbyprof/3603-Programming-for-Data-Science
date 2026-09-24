# 📝 Quiz: 04 - More Functions & Loops

16 questions covering default and keyword arguments, returning tuples, scope, `while` loops, `break` / `continue`, and reading files. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, so don't peek. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning, rather than asking it to solve the question for you.

---

## Section A — Function Extras

**1.** (Code Tracing) What prints?
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ada"))
print(greet("Ada", "Hi"))
```

**2.** (True/False) `def f(a=1, b):` is a valid function definition.

**3.** (Code Tracing) What prints?
```python
def describe(name, major="Undeclared"):
    return f"{name} — {major}"

print(describe(major="Art", name="Ben"))
```

**4.** (Short Answer) In `sorted(scores, reverse=True)`, what kind of argument is `reverse=True`, and what does that tell you about how `sorted` was written?

**5.** (Code Tracing) What prints?
```python
def low_high(nums):
    return min(nums), max(nums)

result = low_high([4, 8, 1])
print(result)
```

**6.** (Code Tracing) What prints?
```python
x = 5

def f():
    x = 100
    return x

print(f(), x)
```

**7.** (Short Answer) Why should a function get its data through parameters instead of reading a global variable?

---

## Section B — While Loops

**8.** (Short Answer) Name the three parts every `while` loop needs.

**9.** (Code Tracing) What prints?
```python
n = 1
while n < 20:
    n = n * 2
print(n)
```

**10.** (Multiple Choice) Which situation is the best fit for a `while` loop?
A) Print every name in a list  
B) Add up every score in a list  
C) Keep rolling a die until you get a 6  
D) Count the vowels in a word

**11.** (Code Tracing) What prints?
```python
for s in [80, 55, 90, 40]:
    if s < 60:
        break
    print(s)
```

**12.** (Code Tracing) What prints?
```python
for s in [80, 55, 90, 40]:
    if s < 60:
        continue
    print(s)
```

---

## Section C — Files

**13.** (Short Answer) What does `with` guarantee when you open a file with `with open("data.txt") as f:`?

**14.** (Code Tracing) What is the value?
```python
line = "Bob,84\n"
line.strip().split(",")
```

**15.** (Short Answer) Why do lines print with an extra blank line between them when you `print(line)` inside `for line in f:`?

**16.** (Code Tracing) What prints if `missing.txt` doesn't exist?
```python
try:
    with open("missing.txt") as f:
        print("opened")
except FileNotFoundError:
    print("no file")
print("done")
```

---

## 🔑 Answer Key

1. `Hello, Ada!` then `Hi, Ada!`
2. **False.** Parameters with defaults must come after parameters without them. This is a `SyntaxError`.
3. `Ben — Art`. Keyword arguments are matched by name, so their order doesn't matter.
4. It's a **keyword argument**. `sorted` has a `reverse` parameter with a **default value** (`False`), which you're overriding.
5. `(1, 8)`. `return a, b` returns one tuple.
6. `100 5`. The `x` inside `f` is local, so the global `x` stays `5`.
7. It makes the function reusable with any data, easy to test, and it can't break when some unrelated global variable changes. (This was the bug in Patient #4 from Module 03b.)
8. **Start** (set up the variable), **condition** (checked before each pass), and **update** (must eventually make the condition `False`).
9. `32`. The values go 1 → 2 → 4 → 8 → 16 → 32, and the loop stops once `n < 20` is `False`.
10. **C.** You don't know how many rolls it will take, only when to stop. The others each go through a collection, which is a job for `for`.
11. `80`. At `55` the loop hits `break` and stops completely.
12. `80` then `90`. `continue` skips `55` and `40` but keeps looping.
13. The file is closed automatically when the block ends, even if an error happens inside it.
14. `['Bob', '84']`. Both are strings. You'd still need `int(...)` for the grade.
15. Each line already ends with a newline character (`"\n"`), and `print()` adds another one. `.strip()` removes the first.
16. `no file` then `done`.
