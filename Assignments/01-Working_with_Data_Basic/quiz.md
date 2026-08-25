# 📝 Quiz: 01 - Working with Data

20 questions covering lists, tuples, dictionaries, and the "going further" topics from the Challenge sections. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Lists

**1.** (Multiple Choice) Which of these creates an empty list?
A) `[]`  B) `{}`  C) `()`  D) `set()`

**2.** (Code Tracing) What prints?
```python
nums = [1, 2, 3]
nums.append(4)
print(nums)
```

**3.** (Short Answer) What's the difference between `.remove()` and `.pop()` on a list?

**4.** (Code Tracing) What prints?
```python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[1:4])
```

**5.** (True/False) Lists preserve the order items were added in.

**6.** (Short Answer) You want a new list containing only the items from an existing list that meet some condition (like "score >= 60"). Describe the pattern you'd use to build it.

---

## Section B — Tuples

**7.** (Multiple Choice) Which of these creates a tuple containing exactly one item?
A) `(5)`  B) `(5,)`  C) `[5]`  D) `tuple(5)`

**8.** (True/False) You can change the value of an element inside a tuple after it's created.

**9.** (Code Tracing) What prints?
```python
point = (3, 7)
x, y = point
print(y, x)
```

**10.** (Short Answer) Why can tuples be used as dictionary keys, but lists cannot?

**11.** (Code Tracing) What does `rest` equal?
```python
scores = (100, 90, 80, 70)
first, *rest = scores
print(rest)
```

**12.** (Short Answer) When a function is defined with `def total(*args):`, what type of object is `args` inside the function?

---

## Section C — Dictionaries

**13.** (Multiple Choice) Which method safely retrieves a value without raising an error if the key is missing?
A) `dict[key]`  B) `.get(key)`  C) `.pop(key)`  D) `.items()`

**14.** (Code Tracing) What prints (order doesn't matter)?
```python
d = {'a': 1, 'b': 2}
for k, v in d.items():
    print(k, v)
```

**15.** (Short Answer) You have `names = ['Ana', 'Ben']` and `scores = [90, 85]`. Describe two different ways to combine them into a single dictionary.

**16.** (True/False) A dictionary can have two identical keys with different values.

**17.** (Code Tracing) What prints?
```python
student = {'name': 'Ana', 'grades': {'math': 90, 'art': 85}}
print(student['grades']['math'])
```

---

## Section D — Going Further (Bonus)

**18.** (Short Answer) Rewrite this loop as a one-line list comprehension:
```python
squares = []
for n in range(5):
    squares.append(n ** 2)
```

**19.** (Short Answer) What does `zip(names, scores)` produce when you loop over it?

**20.** (Short Answer) What's one advantage of `collections.namedtuple` over a plain tuple?

---

## ✅ Answer Key

1. **A** — `[]` (also `list()`, but that wasn't an option here). `{}` is an empty dict, `()` is an empty tuple, `set()` is an empty set.
2. `[1, 2, 3, 4]`
3. `.remove(value)` deletes the first item that *matches a value*; `.pop(index)` deletes and *returns* the item at a given position (default: the last one).
4. `['b', 'c', 'd']` — slicing is start-inclusive, stop-exclusive.
5. **True**.
6. Loop over the original list, check the condition with `if`, and `.append()` matching items to a new (initially empty) list. (A list comprehension does the same thing in one line.)
7. **B** — `(5,)`. Without the trailing comma, `(5)` is just the integer `5` in parentheses.
8. **False** — tuples are immutable.
9. `7 3`
10. Tuples are immutable, which makes them *hashable*. Dictionary keys must be hashable, and lists (being mutable) are not.
11. `[90, 80, 70]` — `*rest` collects everything left over as a list.
12. A tuple.
13. **B** — `.get(key)`. `dict[key]` raises `KeyError` if missing; `.pop(key)` also raises `KeyError` if missing (and removes the item); `.items()` doesn't take a key at all.
14. `a 1` and `b 2` (in insertion order, since Python 3.7+ dicts preserve it).
15. (1) Loop with `zip(names, scores)` and assign each pair into a new dict. (2) `dict(zip(names, scores))` does it in one line.
16. **False** — keys are unique; assigning to an existing key overwrites its value.
17. `90`
18. `squares = [n ** 2 for n in range(5)]`
19. An iterable of tuples, pairing up corresponding items: `('Ana', 90)`, `('Ben', 85)`, etc.
20. You can access fields by name (`p.x`) instead of only by position (`p[0]`), which makes the code more self-documenting.
