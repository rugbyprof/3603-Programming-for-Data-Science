# 📝 Quiz: 03b - Containers → Functions

24 questions covering container choice, the loop patterns, nested expressions, function basics, `print` vs. `return`, mutation, and pipelines. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first. The Answer Key is at the bottom, so don't peek. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning, rather than asking it to solve the question for you.

---

## Section A — Containers

**1.** (Short Answer) Why is `scores = [87, 91, 74]` better than `score1 = 87`, `score2 = 91`, `score3 = 74`? Give two reasons.

**2.** (Code Tracing) What prints?
```python
scores = [87, 91, 74, 88, 95]
scores.append(60)
scores.remove(91)
print(scores[1], scores[-1], len(scores))
```

**3.** (Multiple Choice) Which container fits "Student ID → GPA" best?
A) list  B) tuple  C) dictionary  D) set

**4.** (Multiple Choice) Which container fits "an RGB color" best?
A) list  B) tuple  C) dictionary  D) set

**5.** (Short Answer) Give a better description of a tuple than "an immutable list."

**6.** (Code Tracing) What prints?
```python
a = {"OOP", "Database", "Algorithms"}
b = {"Database", "Networks"}
print(a & b)
```

**7.** (Code Tracing) Evaluate one step at a time. What is the value?
```python
students = [
    {"name": "Alice", "grade": 91},
    {"name": "Bob",   "grade": 84}
]
students[-1]["name"][0]
```

---

## Section B — Patterns

**8.** (Short Answer) Accumulate and Count both start at `0`. What's the difference in how they update?

**9.** (Code Tracing) What prints?
```python
nums = [4, -2, 7, -5, 3]
x = []
for n in nums:
    if n < 0:
        x.append(n)
print(x)
```

**10.** (Multiple Choice) Which pattern is question 9?
A) Accumulate  B) Count  C) Filter  D) Best So Far

**11.** (Short Answer) When finding the maximum with the Best So Far pattern, why should `best` start at the first item instead of `0`?

---

## Section C — Function Basics

**12.** (Code Tracing) What prints when this cell runs?
```python
def square(x):
    return x * x
```

**13.** (Short Answer) In `def area(width, height):` and `area(3, 5)`, which are the parameters and which are the arguments?

**14.** (Code Tracing) What prints?
```python
def square(x):
    return x * x

print(square(3) + square(square(2)))
```

**15.** (Code Tracing) What prints? (Careful!)
```python
def double(x):
    print(x * 2)

result = double(5)
print(result)
```

**16.** (True/False) `print()` gives a value back to the program so it can be used in later calculations.

**17.** (Code Tracing) What prints?
```python
def check(x):
    return "big"
    return "small"

print(check(1))
```

**18.** (Short Answer) Give three reasons functions are useful *besides* avoiding copy/paste.

---

## Section D — Functions + Containers

**19.** (Short Answer) Find the bug:
```python
def total(numbers):
    result = 0
    for n in numbers:
        result += n
        return result
```

**20.** (Code Tracing) What prints?
```python
def add_one(values):
    values.append(1)
    return values

a = [5]
b = add_one(a)
print(a)
```

**21.** (Code Tracing) What prints?
```python
nums = [3, 1, 2]
x = nums.sort()
print(x, nums)
```

**22.** (Multiple Choice) `frequency(["a", "b", "a"])` from Notebook 05 turns a list into a...
A) number  B) bool  C) list  D) dictionary

**23.** (Short Answer) Write the contract (IN / OUT / DOES) for a function `count_above(numbers, threshold)`.

**24.** (Code Tracing) Given the functions from Notebook 06, what prints?
```python
numbers = [10, -3, 20, 30]
clean = remove_negatives(numbers)
print(above(clean, average(clean)))
```

---

## 🔑 Answer Key

1. Any two of: it scales to any number of items; you can loop over it; adding or removing a score doesn't mean changing the code; one name for the whole group.
2. `74 60 5`. After the append and remove, the list is `[87, 74, 88, 95, 60]`.
3. **C** — dictionary. You look a GPA up by ID.
4. **B** — tuple. It's one color with three fixed parts (red, green, blue).
5. A record whose parts have fixed meanings by position, such as `(latitude, longitude)`. It's one thing with several parts.
6. `{'Database'}`
7. `'B'`. `students[-1]` is `{"name": "Bob", ...}`, `["name"]` is `"Bob"`, and `[0]` is `"B"`.
8. Accumulate adds **the item** (`total += item`). Count adds **1** (`count += 1`) when the item passes a test.
9. `[-2, -5]`
10. **C** — Filter.
11. If every number is negative, nothing is ever greater than `0`, so the function wrongly returns `0`. Starting at the first item means `best` is always a real value from the list.
12. Nothing. `def` only *defines* the function, and nothing runs until it's called.
13. Parameters: `width`, `height`. Arguments: `3`, `5`.
14. `25`. `square(3)` is 9, `square(square(2))` is `square(4)`, which is 16, and 9 + 16 = 25.
15. `10` and then `None`. `double` *prints* 10 but doesn't return anything, so `result` is `None`.
16. **False.** `print()` shows a value to the human; `return` gives it back to the program.
17. `big`. `return` ends the function, so the second `return` never runs.
18. Any three of: naming/readability, fixing a bug in one place, testing pieces separately, hiding details, building bigger things out of smaller functions.
19. `return result` is indented inside the loop, so the function returns after the first item. Move it out one level.
20. `[5, 1]`. `values` and `a` are the same list, so appending inside the function changes `a`.
21. `None [1, 2, 3]`. `.sort()` changes the list in place and returns `None`.
22. **D** — dictionary.
23. IN: a list of numbers and a number. OUT: an int. DOES: returns how many numbers are greater than `threshold`.
24. `[30]`. `clean` is `[10, 20, 30]` and the average is `20.0`. `above` keeps numbers *strictly* greater than the cutoff, so `20` is left out. (This is a boundary case, exactly the kind the Test Designer section warns about.)
