# 📝 Worksheet: 06 - Foundations

Use this worksheet to reinforce the Jupyter/IPython tooling skills from this module. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧙 Section 1: Magics and Performance

1. What magic command lists every variable currently in memory, along with its type?  
   `Answer:` _______________________

2. What's the difference between a line magic (`%pwd`) and a cell magic (`%%writefile`)?  
   `Answer:` _______________________

---

### ✏️ Task: Timing Comparison

```python
# Build a list of the first 500,000 integers.
# Use %timeit to compare: squaring it with a list comprehension
# vs. squaring it as a NumPy array (numbers ** 2).
```

### 🤖 Explain It

In your own words: why does `%timeit` run your code multiple times instead of just once like `%time`? What would you lose if it only ran once?

---

## 📝 Section 2: Markdown

3. What's the difference between `*italic*` and `**bold**` in Markdown?  
   `Answer:` _______________________

4. Write the Markdown for a 2-item bulleted list where the second item has its own sub-bullet.  
   `Answer:` _______________________

---

### ✏️ Task: Mini Report

```markdown
# Write a Markdown cell with:
# - a level-2 heading
# - a short paragraph
# - a 3-item list
# - one inline LaTeX expression
```

### 🤖 Explain It

In your own words: what's lost if you write an entire notebook as code + comments only, with no Markdown cells at all?

---

## 📂 Section 3: Files and Data I/O

5. What does the `with` keyword do when you open a file, and why is it preferred over a plain `open()`/`.close()` pair?  
   `Answer:` _______________________

6. What's the difference between `json.dump()` and `json.load()`?  
   `Answer:` _______________________

7. Name three things `.info()` tells you about a DataFrame that `.head()` doesn't.  
   `Answer:` _______________________

---

### ✏️ Task: Build, Save, Reload

```python
# Create a dictionary describing yourself (name, major, hobbies as a list).
# Save it to a JSON file.
# Read it back into a NEW variable and confirm it matches the original
# (hint: compare the two dictionaries with ==).
```

### ✏️ Task: CSV Round Trip

```python
# Create a small DataFrame from a dictionary of lists (not a CSV this time —
# use pd.DataFrame(your_dict)).
# Save it to a CSV, then read that CSV back into a new DataFrame.
# Use .equals() to confirm the reloaded DataFrame matches the original.
```

### 🤖 Explain It

In your own words: why does opening a file that doesn't exist raise a specific error (`FileNotFoundError`) instead of Python just quietly giving you an empty result?

---

## 📈 Section 4: Plotting

8. What does `plt.legend()` require in order to show meaningful labels (hint: think about the `plot()` calls before it)?  
   `Answer:` _______________________

9. When would you choose a bar plot over a line plot?  
   `Answer:` _______________________

---

### ✏️ Task: Compare Three Categories

```python
# Given: subjects = ["Math", "Science", "History"]
#        hours_studied = [5, 8, 3]
# Build a bar plot with a title and axis labels.
```

### 🤖 Explain It

In your own words: why does a line plot make sense for `sin(x)` but not for the bar-chart categories (`"Math"`, `"Science"`, `"History"`)? What's different about the two kinds of data?

---

## ⚡ Section 5: Productivity and Getting Help

10. What are the two Jupyter cell modes, and what does each one do?  
    `Answer:` _______________________

11. What's the difference between `help(len)` and `len?`?  
    `Answer:` _______________________

---

### ✏️ Task: Shortcut Drill

```
Using only the keyboard (no mouse):
- Insert 2 new cells below this one.
- Turn one into a Markdown cell and the other into a Code cell.
- Delete one of them.
- Run the remaining cell.
```

### 🤖 Explain It

In your own words: when would you reach for `?` versus `??` versus `help()` versus searching online documentation? Is there a natural order you'd try them in?

---

## 🧾 Submit Checklist

- [ ] I used at least 3 different magic commands.
- [ ] I wrote a Markdown cell with a heading, a list, and LaTeX math.
- [ ] I wrote and read back a text file, a JSON file, and a CSV file.
- [ ] I built at least one plot with a title, axis labels, and (if applicable) a legend.
- [ ] I used `?` or `help()` to look something up instead of guessing.
- [ ] I completed the "Explain It" prompts in my own words.
