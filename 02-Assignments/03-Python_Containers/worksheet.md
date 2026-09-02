# 📝 Worksheet: 01 - Working with Data

Use this worksheet to review and reinforce your understanding of Python's core data containers. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Lists

1. What method adds an item to the end of a list?  
   `Answer:` ____________________________

2. How can you remove an item from a list by value? By position?  
   `Answer:` ____________________________

3. What's the result of this code?

```python
nums = [2, 4, 6]
nums.append(8)
print(nums)
```

   `Answer:` ____________________________

4. What does `my_list[1:4]` return, given `my_list = [10, 20, 30, 40, 50]`?  
   `Answer:` ____________________________

4a. Given `a = [1, 2]` and `b = [3, 4]`, what is the result of `a + b`? Of `a.append(b)`? Of `a.extend(b)`?  
   `Answer:` ____________________________

4b. Given `grid = [[1, 2], [3, 4]]`, how do you access the value `3`?  
   `Answer:` ____________________________

4c. List three different ways to remove an item from a list.  
   `Answer:` ____________________________

---

### ✏️ Task: List Practice

```python
# Create a list of your top 3 favorite foods.
# Add another food to the list.
# Remove one item and print the list.
```

### ✏️ Task: Slicing and Sorting

```python
# Given: numbers = [42, 17, 8, 99, 23, 4]
# 1. Print the first three numbers using slicing.
# 2. Print the numbers sorted from smallest to largest.
# 3. Print the numbers sorted from largest to smallest.
```

### ✏️ Task: Filtering

```python
# Given: temps = [55, 72, 90, 43, 88, 67, 101]
# Build a new list called "hot" containing only temps over 85.
# Print "hot".
```

### ✏️ Task: Combine Lists Three Ways

```python
# Given: morning = ['eggs', 'toast']
#        extras  = ['jam', 'coffee']
# 1. Use + to make a new list "breakfast" without changing "morning".
# 2. On a fresh copy of "morning", use .append(extras) and print the result.
#    Notice how many items the list has now, and why.
# 3. On another fresh copy, use .extend(extras) and print the result.
```

### ✏️ Task: 2D List (grid)

```python
# board = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# 1. Print the value in row 2, column 0.
# 2. Change the center value to 0.
# 3. Loop over the board and print each row on its own line.
```

### ✏️ Task: Deleting Items

```python
# Given: queue = ['Ana', 'Ben', 'Cy', 'Dana', 'Eve']
# 1. Remove 'Cy' by value.
# 2. Use .pop() to remove and capture the last person into a variable "served".
# 3. Use del to remove the first person.
# 4. Print the remaining queue and "served".
```

### ✏️ Task: Iterate by Index

```python
# Given: prices = [10, 20, 30, 40]
# 1. Use "for i in range(len(prices)):" to print each item as "0: 10", "1: 20", ...
# 2. Using the index, add 5 to every price in place, then print the list.
# 3. Rewrite step 1 using enumerate() instead.
```

### 🤖 Explain It

In your own words: what's the difference between a list and a slice of a list? Is slicing a list the same as modifying it? And when you write `a.append(b)` versus `a.extend(b)`, what ends up in `a` each way?

---

## 🔒 Section 2: Tuples

5. What is a key difference between a list and a tuple?  
   `Answer:` ____________________________

6. Can you change the contents of a tuple once it is created? Why or why not?  
   `Answer:` ____________________________

7. What does `first, *rest = (10, 20, 30, 40)` assign to `first` and `rest`?  
   `Answer:` ____________________________

---

### ✏️ Task: Tuple Practice

```python
# Create a tuple with your favorite 3 numbers.
# Unpack it into three variables and print each.
```

### ✏️ Task: Unpacking with *rest

```python
# Given: race_times = (9.58, 9.63, 9.69, 9.71, 9.74)
# Unpack this into "winner" (the first time) and "others" (everything else).
# Print both.
```

### ✏️ Task: Tuples as Dictionary Keys

```python
# Build a dictionary called "distances" where the keys are (city1, city2)
# tuples and the values are the distance in miles between them.
# Add at least two entries, then look up and print one of them.
```

### 🤖 Explain It

In your own words: why does Python allow a tuple to be a dictionary key, but not a list? What property makes that possible?

---

## 🔑 Section 3: Dictionaries

8. What does the `.get()` method do differently from accessing a key directly with `[]`?  
   `Answer:` ____________________________

9. How do you loop through both keys and values in a dictionary?  
   `Answer:` ____________________________

10. How would you remove a key from a dictionary and also capture the value it held?  
    `Answer:` ____________________________

11. In a list of dictionaries like `people = [{'name': 'Ana'}, {'name': 'Ben'}]`, how do you get Ben's name?  
    `Answer:` ____________________________

12. If the same dictionary object is stored in both a list and another dictionary, and you change it through one, does the other see the change? Why?  
    `Answer:` ____________________________

---

### ✏️ Task: Dictionary Practice

```python
# Create a dictionary with keys: 'name', 'age', and 'hobby'.
# Print each key and value in the format "key: value".
```

### ✏️ Task: Build from Two Lists

```python
# Given: products = ['pen', 'notebook', 'eraser']
#        prices = [1.50, 3.25, 0.75]
# Build a dictionary mapping each product to its price.
# Print the total cost of all products (hint: sum the .values()).
```

### ✏️ Task: Nested Dictionaries

```python
# Given:
# inventory = {
#     'apples': {'count': 50, 'price': 0.50},
#     'bananas': {'count': 30, 'price': 0.25},
# }
# Loop through inventory and print a line for each fruit like:
# "apples: 50 units at $0.50"
```

### ✏️ Task: List of Dictionaries (table rows)

```python
# roster = [
#     {'name': 'Alex', 'major': 'CS'},
#     {'name': 'Ana',  'major': 'Math'},
#     {'name': 'Ben',  'major': 'History'},
# ]
# 1. Loop over roster and print "name - major" for each student.
# 2. Add a new student record to the list.
# 3. Build and print a list of just the names of everyone majoring in 'CS'.
```

### ✏️ Task: Update a Record by Row Number

```python
# Using the roster above:
# 1. Build a dict "by_row" mapping each row number to its record
#    (hint: {i: row for i, row in enumerate(roster)}).
# 2. Change the major of the student in row 2 to 'CS'.
# 3. Print roster[2] and explain why it changed too.
```

### 🤖 Explain It

In your own words: what's the difference between `student['gpa']` and `student.get('gpa')` when `'gpa'` isn't in the dictionary? Which would you use, and when? Also: why does changing `by_row[2]` also change `roster[2]`?

---

## 🚀 Section 4: Going Further (Optional)

These pair with the "🔥 Challenge" sections in the notebooks — skip if you haven't gotten there yet.

### ✏️ Task: List Comprehension

```python
# Rewrite this loop as a one-line list comprehension:
# cubes = []
# for n in range(6):
#     cubes.append(n ** 3)
```

### ✏️ Task: namedtuple

```python
# Create a namedtuple called "Book" with fields "title" and "author".
# Make one instance and print both fields by name.
```

### ✏️ Task: Word Counter

```python
# text = "to be or not to be that is the question"
# Build a dictionary counting how many times each word appears.
# (Try it by hand first, then check yourself with collections.Counter.)
```

### ✏️ Task: Parse Some JSON

```python
import json
raw = '''
{
  "course": "Programming for Data Science",
  "online": true,
  "instructor": null,
  "students": [
    {"name": "Alex", "grade": 91},
    {"name": "Ana",  "grade": 88}
  ]
}
'''
# 1. Use json.loads(raw) to turn this into Python objects.
# 2. Print the course name and the second student's grade.
# 3. Print the Python type of the value that came from "online" and from "instructor".
```

### ✏️ Task: Walk a GeoJSON FeatureCollection

```python
geo = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [-98.529, 33.878]},
         "properties": {"name": "Bolin Hall"}},
        {"type": "Feature",
         "geometry": {"type": "Point", "coordinates": [-98.531, 33.876]},
         "properties": {"name": "Moffett Library"}},
    ],
}
# Loop over geo["features"] and print each building's name with its
# latitude and longitude. Remember: coordinates are [longitude, latitude].
```

---

## 🧾 Submit Checklist

- [ ] I practiced creating, slicing, sorting, and filtering lists.
- [ ] I can explain the difference between `+`, `append()`, and `extend()`.
- [ ] I built and traversed a nested (2D) list.
- [ ] I removed list items with `remove()`, `pop()`, and `del`.
- [ ] I looped by index with `range(len(...))` and with `enumerate()`.
- [ ] I understand how tuples are different from lists, and why that makes them hashable.
- [ ] I accessed, looped through, updated, and removed items from a dictionary.
- [ ] I built a dictionary from two separate lists.
- [ ] I worked with at least one nested dictionary.
- [ ] I processed a list of dictionaries as table rows and updated a record by row number.
- [ ] I parsed JSON with `json.loads()` and walked a GeoJSON FeatureCollection.
- [ ] I completed the "Explain It" prompts in my own words.
