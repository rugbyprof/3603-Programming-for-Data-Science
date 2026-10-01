# 📝 Quiz: 01 - Working with Data

30 questions covering lists, tuples, dictionaries, tabular data, JSON, and the "going further" topics from the Challenge sections. Mix of multiple choice, true/false, code-tracing, and short answer.

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

## Section E — Lists in Depth

**21.** (Code Tracing) What prints?
```python
a = [1, 2]
b = [3, 4]
a.append(b)
print(a)
```

**22.** (Multiple Choice) Given `a = [1, 2]` and `b = [3, 4]`, which produces `[1, 2, 3, 4]` **and** modifies `a` in place?
A) `a + b`  B) `a.append(b)`  C) `a.extend(b)`  D) `a.append(*b)`

**23.** (Code Tracing) What prints?
```python
grid = [[1, 2, 3], [4, 5, 6]]
print(grid[1][0])
```

**24.** (Code Tracing) What prints?
```python
items = ['a', 'b', 'c', 'd']
items.pop(1)
del items[0]
print(items)
```

**25.** (Short Answer) Name one situation where `for i in range(len(mylist)):` is the right choice over `for item in mylist:`.

---

## Section F — Tables & JSON

**26.** (Code Tracing) What prints?
```python
people = [
    {'name': 'Ana', 'major': 'CS'},
    {'name': 'Ben', 'major': 'Math'},
]
print(people[1]['major'])
```

**27.** (Short Answer) You have a list of student records and want to change the major of the student in row 2. Assuming `roster` is the list, write the one line that does it.

**28.** (Code Tracing) What prints?
```python
roster = [{'major': 'CS'}, {'major': 'Math'}]
by_row = {i: row for i, row in enumerate(roster)}
by_row[0]['major'] = 'Data Science'
print(roster[0]['major'])
```

**29.** (Multiple Choice) In JSON, the value `null` becomes which Python value after `json.loads()`?
A) `0`  B) `''`  C) `None`  D) `False`

**30.** (Short Answer) In a GeoJSON `Point`, the coordinates are written as `[-98.5, 33.9]`. Which number is the latitude?


