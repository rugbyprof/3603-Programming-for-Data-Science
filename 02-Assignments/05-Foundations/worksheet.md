# 📝 Worksheet: 06 - Foundations

Use this worksheet to reinforce the Jupyter/IPython tooling skills from this module. There's one section per notebook, in order. Each section ends with an **🤖 Explain It** prompt. Write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧙 Section 1: Magic Commands (01)

1. What magic command lists every variable currently in memory, along with its type?  
   `Answer:` _______________________

2. What's the difference between a line magic (`%pwd`), a cell magic (`%%writefile`), and a shell command (`!ls`)?  
   `Answer:` _______________________

3. Why does `%cd ..  # go up` fail, and how do you fix it?  
   `Answer:` _______________________

---

### ✏️ Task: Write, Run, and Reload

```python
# Use %%writefile to create tools.py containing a function shout(text)
# that returns text in uppercase with "!" on the end.
# Turn on %load_ext autoreload and %autoreload 2, then import tools and call shout().
# Rewrite tools.py so shout() adds "!!!" instead, and call it again WITHOUT restarting.
```

### 🤖 Explain It

In your own words: why can `!pip install` "succeed" while `import` still fails with `ModuleNotFoundError`? Why does `%pip` avoid the problem?

---

## ⚡ Section 2: Jupyter Workflow (02)

4. What are the two Jupyter cell modes, and what key switches to each?  
   `Answer:` _______________________

5. What do the numbers in `[3]`, `[4]`, `[12]` next to code cells tell you, and what *don't* they tell you?  
   `Answer:` _______________________

6. A cell's code ends with three expressions on three lines. How many of their values are displayed?  
   `Answer:` _______________________

---

### ✏️ Task: Shortcut Drill

```
Using only the keyboard (no mouse):
- Insert 2 new cells below this one.
- Turn one into a Markdown cell and the other into a Code cell.
- Move the Code cell above the Markdown cell.
- Delete the Markdown cell, then undo the deletion.
- Run the Code cell.
```

### ✏️ Task: Break It, Then Fix It

```python
# In three separate cells, IN THIS ORDER, type:
#   print(area)
#   width, height = 4, 5
#   area = width * height
# Get it to work by running cells out of order. Then Restart & Run All,
# watch it fail, and fix the ORDER so it runs top to bottom.
```

### 🤖 Explain It

In your own words, using the "recipe and kitchen" idea: why can a notebook look correct on your screen and still fail for your grader?

---

## 📚 Section 3: Getting Help (03)

7. What's the difference between `help(len)` and `len?`? Which one also works in a plain `.py` script?  
   `Answer:` _______________________

8. In the signature `round(number, ndigits=None)`, which argument is required and which is optional? What's the optional one's default?  
   `Answer:` _______________________

9. Name the error type for each: `'5' + 5`, `int('hello')`, `[1, 2][5]`, `{'a': 1}['b']`.  
   `Answer:` _______________________

---

### ✏️ Task: Investigate Without Searching

```python
# Using only ?, Tab/IntelliSense, dir(), and help() (no web searching):
# 1. Find a string method that checks whether a string contains only digits.
# 2. Use a wildcard search (np.*sum*?) to list NumPy functions with "sum" in the name.
# 3. Find out whether np.random.randint's upper limit is included. Prove it with code.
```

### 🤖 Explain It

In your own words: when would you reach for `?` versus `??` versus `help()` versus `dir()` versus the official docs? Is there a natural order you'd try them in?

---

## 📝 Section 4: Markdown (04)

10. What's the difference between `*italic*` and `**bold**` in Markdown?  
    `Answer:` _______________________

11. Write the Markdown for a 2-item bulleted list where the second item has its own sub-bullet.  
    `Answer:` _______________________

12. How do you show a literal price like `$5` in Markdown without it turning into math?  
    `Answer:` _______________________

---

### ✏️ Task: Mini Report

```markdown
# Write a Markdown cell with:
# - a level-2 heading
# - a short paragraph with a line break in the middle
# - a 3-item list
# - one inline LaTeX expression (try the mean, \bar{x})
# - a small table with a right-aligned number column
```

### 🤖 Explain It

In your own words: what's lost if you write an entire notebook as code + comments only, with no Markdown cells at all? When would *generating* Markdown from code (`display(Markdown(...))`) be better than typing it?

---

## 📂 Section 5: Files and Paths (05)

13. What does the `with` keyword do when you open a file, and why is it preferred over a plain `open()`/`.close()` pair?  
    `Answer:` _______________________

14. What's the difference between modes `'w'`, `'a'`, and `'x'`?  
    `Answer:` _______________________

15. For `Path('reports') / 'final.pdf'`, what are the `.name`, `.stem`, `.suffix`, and `.parent`?  
    `Answer:` _______________________

---

### ✏️ Task: Build, Save, Reload

```python
# Create a dictionary describing yourself (name, major, hobbies as a list).
# Save it to a JSON file with indent=2 (use pathlib to build the path).
# Read it back into a NEW variable and confirm it matches the original with ==.
# Then add a tuple to the dictionary and repeat. Does it still match? Why not?
```

### ✏️ Task: Find Files

```python
# Write three small .txt files into a folder using a loop.
# Use glob('*.txt') to find them WITHOUT typing their names, and print each
# file's name and size in bytes.
```

### 🤖 Explain It

In your own words: why does `csv.reader` give you `'90'` instead of `90`, and why does splitting a CSV line on `','` break on a value like `"Smith, John"`?

---

## 📊 Section 6: Data Input and Output (06)

16. Name three things `.info()` tells you about a DataFrame that `.head()` doesn't.  
    `Answer:` _______________________

17. What does `index=False` do in `df.to_csv(...)`, and what happens if you forget it?  
    `Answer:` _______________________

18. When would you use `pd.json_normalize()` instead of `pd.read_json()`?  
    `Answer:` _______________________

---

### ✏️ Task: CSV Round Trip

```python
# Create a small DataFrame from a dictionary of lists (use pd.DataFrame(your_dict)).
# Save it to a CSV, then read that CSV back into a new DataFrame.
# Use .equals() to confirm the reloaded DataFrame matches the original.
```

### ✏️ Task: Convert Between Formats

```python
# Take the same DataFrame and save it as JSON (orient='records') and as Excel.
# Read the Excel file back and convert it to a CSV.
# Print the raw text of the JSON and CSV files and compare them.
```

### 🤖 Explain It

In your own words: what information can get lost or changed when converting Excel → CSV, or CSV → DataFrame? Give two examples.

---

## 📈 Section 7: Plotting with NumPy (07)

19. What's the difference between `[1, 2, 3] * 2` and `np.array([1, 2, 3]) * 2`?  
    `Answer:` _______________________

20. What does `plt.legend()` require in order to show meaningful labels (hint: think about the `plot()` calls before it)?  
    `Answer:` _______________________

21. Which chart would you use for: comparing categories, change over time, a relationship between two numbers, and the distribution of one number?  
    `Answer:` _______________________

---

### ✏️ Task: Compare Three Categories

```python
# Given: subjects = ["Math", "Science", "History"]
#        hours_studied = [5, 8, 3]
# Build a bar plot with a title and axis labels (with units).
# Save it to a PNG file, then display it.
```

### ✏️ Task: Distribution

```python
# Generate 200 test scores with np.random.normal(75, 10, size=200).
# Plot a histogram and mark the mean with a vertical dashed line and a legend.
# Then show the same data as a box plot side by side, using subplots.
```

### 🤖 Explain It

In your own words: why does a line plot make sense for `sin(x)` or monthly revenue but not for the categories `"Math"`, `"Science"`, `"History"`? What's different about the two kinds of data?

---

## ⏱️ Section 8: Timing and Performance (08)

22. What's the difference between `%time`, `%timeit`, `%%time`, and `%%timeit`?  
    `Answer:` _______________________

23. Name two things that make a timing comparison **unfair**.  
    `Answer:` _______________________

24. What does `%prun` tell you that `%timeit` doesn't?  
    `Answer:` _______________________

---

### ✏️ Task: Timing Comparison

```python
# Build a list of the first 500,000 integers, and a NumPy array of the same.
# Use %timeit -o to compare squaring the list with a comprehension
# vs. squaring the array (numbers ** 2).
# Confirm both give the same values, then print how many times faster NumPy is.
```

### ✏️ Task: Find the Repeated Work

```python
# This function is slow. Time it, find the repeated work, fix it, and time it again:
def above_average(values):
    return [v for v in values if v > sum(values) / len(values)]
```

### 🤖 Explain It

In your own words: why does `%timeit` run your code many times instead of just once like `%time`? And why should you "measure first" instead of rewriting code that just *looks* slow?

---

## 🧾 Submit Checklist

- [ ] I used at least 3 different magic commands, including one cell magic and one `!` shell command.
- [ ] I fixed a notebook that only worked when run out of order, and I can explain why it failed.
- [ ] I ran **Restart & Run All** on my notebooks before submitting.
- [ ] I used `?`, `help()`, or `dir()` to look something up instead of guessing.
- [ ] I wrote a Markdown cell with a heading, a list, a table, and LaTeX math.
- [ ] I wrote and read back a text file, a JSON file, and a CSV file using `pathlib` paths.
- [ ] I loaded data with Pandas and converted it between at least two formats.
- [ ] I built at least one plot with a title, axis labels, and (if applicable) a legend, and saved it to a file.
- [ ] I timed two approaches fairly with `%timeit`.
- [ ] I uploaded each notebook's `NN-OutputFiles` folder along with the notebook.
- [ ] I completed the "Explain It" prompts in my own words.
