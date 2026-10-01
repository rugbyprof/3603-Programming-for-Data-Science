# 📝 Quiz: 06 - Foundations

45 questions covering all 8 Foundations notebooks, in order: magic commands, Jupyter workflow, getting help, Markdown, files and paths, data I/O, plotting with NumPy, and timing. Mix of multiple choice, true/false, code-tracing, and short answer.

This is a conceptual self-check. For hands-on practice writing and running real code, see `Foundations_Quiz.ipynb` in this folder.

Try every question on your own first. The Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Magic Commands (01)

**1.** (Multiple Choice) Which magic command shows your current working directory?
A) `%pwd`  B) `%cd`  C) `%ls`  D) `%dir`

**2.** (Short Answer) What's the difference between a line magic (`%pwd`), a cell magic (`%%writefile`), and a shell command (`!ls`)?

**3.** (Code Tracing) A folder contains only `a.csv` and `b.txt`. What kind of value is stored in `files`, and what does it contain?
```python
files = !ls
```

**4.** (True/False) `%cd ..  # go up one folder` moves you to the parent folder.

**5.** (Short Answer) Inside a notebook, why should you install packages with `%pip install` instead of `!pip install`?

**6.** (True/False) `%who` only shows variable *names*, while `%whos` also shows their types and a value summary.

---

## Section B — Jupyter Workflow (02)

**7.** (Multiple Choice) In Command mode, which keyboard shortcut inserts a new cell *below* the current one?
A) `A`  B) `B`  C) `D D`  D) `M`

**8.** (Short Answer) What's the practical difference between Command mode and Edit mode? You press `B` and the letter "b" appears in your code. What happened, and what should you press?

**9.** (Code Tracing) What does this cell display when it runs?
```python
x = 5
x * 2
x * 3
```

**10.** (Short Answer) A cell near the bottom of a notebook shows `[7]`, and the cell above it shows `[9]`. What does that tell you?

**11.** (True/False) If you delete the cell that created the variable `message`, `message` is removed from memory immediately.

**12.** (Short Answer) Why should you **Restart & Run All** before submitting a notebook?

---

## Section C — Getting Help (03)

**13.** (Short Answer) `?` shows a docstring. What does `??` sometimes show that `?` doesn't, and why doesn't it always work?

**14.** (Multiple Choice) The signature is `sorted(iterable, /, *, key=None, reverse=False)`. Which call is valid?
A) `sorted(iterable=nums)`  B) `sorted(nums, None, True)`  C) `sorted(nums, reverse=True)`  D) `sorted()`

**15.** (Code Tracing) What error does this raise, and what does it mean?
```python
numbers = [1, 2, 3]
numbers.mean()
```

**16.** (Short Answer) A long traceback fills the screen. Which line should you read first, and why?

**17.** (Short Answer) What does `dir(obj)` give you that Tab completion doesn't?

---

## Section D — Markdown (04)

**18.** (Short Answer) What's the Markdown syntax for a level-2 heading (like `## Section 2`)?

**19.** (Short Answer) How do you write **inline** LaTeX math in a Markdown cell, versus a **block** equation on its own line(s)?

**20.** (Short Answer) The Markdown text `The item costs $5 and the tax is $2.` renders strangely. Why, and how do you fix it?

**21.** (Short Answer) You typed two lines directly under each other in a Markdown cell, but they render as **one** line. Name two ways to fix it.

**22.** (Short Answer) Why might you add narrative Markdown cells between code cells instead of just writing code comments?

---

## Section E — Files and Paths (05)

**23.** (Code Tracing) What does this print?
```python
with open('x.txt', 'w', encoding='utf-8') as f:
    f.write('hi')

with open('x.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```

**24.** (Multiple Choice) Which file mode adds to the end of an existing file **without** erasing it?
A) `'r'`  B) `'w'`  C) `'a'`  D) `'x'`

**25.** (Code Tracing) What does this print?
```python
from pathlib import Path
p = Path('data') / 'sales_2026.csv'
print(p.name, p.stem, p.suffix)
```

**26.** (Short Answer) Why is it good practice to use a relative path (like `'data/file.csv'`) instead of an absolute path (like `'C:/Users/yourname/...'`) in a notebook you'll share or submit?

**27.** (Code Tracing) `scores.csv` contains the two lines `Name,Score` and `Alice,90`. What does this print, and why might that cause a problem?
```python
import csv
with open('scores.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))
print(rows[1])
```

**28.** (True/False) After saving `{'point': (3, 4)}` with `json.dump` and reading it back with `json.load`, you get back exactly the same dictionary.

---

## Section F — Data Input and Output (06)

**29.** (Short Answer) What does `pd.read_csv('file.csv')` return?

**30.** (Multiple Choice) Which DataFrame method shows summary statistics (mean, standard deviation, min/max, etc.)?
A) `.head()`  B) `.info()`  C) `.describe()`  D) `.columns()`

**31.** (Short Answer) You save a DataFrame with `df.to_csv('out.csv')`, read it back, and find an extra `Unnamed: 0` column. What caused it, and how do you prevent it?

**32.** (Short Answer) What does JSON written with `orient='records'` look like, and why is it usually the layout you want?

**33.** (Short Answer) After `pd.read_csv`, the ZIP code `02108` shows up as `2108`. Why, and how do you fix it?

**34.** (Short Answer) What does `pd.read_excel('file.xlsx', sheet_name=None)` return?

---

## Section G — Plotting with NumPy and Matplotlib (07)

**35.** (Code Tracing) What do these two lines print?
```python
print([1, 2] * 2)
print(np.array([1, 2]) * 2)
```

**36.** (Matching) Choose the best chart (line, bar, scatter, or histogram) for each question:
a) Which department sold the most?
b) How did daily website visits change over a month?
c) Is there a relationship between price and units sold?
d) What is the distribution of customer order values?

**37.** (Short Answer) A histogram and a bar chart both draw rectangles. What's the difference in what they show?

**38.** (Short Answer) You call `plt.show()` and then `plt.savefig('chart.png')`, and the saved image is blank. Why?

**39.** (Short Answer) On a box plot, what does the line **inside** the box represent, and what do the dots **beyond** the whiskers represent?

---

## Section H — Timing and Performance (08)

**40.** (Short Answer) What's the difference between `%time` and `%timeit`, and why is `%timeit` more trustworthy for comparisons?

**41.** (Short Answer) Why is a NumPy vectorized operation like `arr ** 2` usually much faster than a Python `for` loop doing the same calculation element by element?

**42.** (True/False) A variable created inside a `%%timeit` cell is available in the cells after it.

**43.** (Short Answer) What's unfair about comparing `%timeit np.array(my_list) ** 2` against `%timeit arr ** 2` to decide whether squaring is fast?

**44.** (Short Answer) Why is `[s / max(scores) for s in scores]` slow for large lists? How would you fix it, and roughly what happens to its runtime when the list doubles in size?

**45.** (Multiple Choice) What does `%prun` show you?
A) Only the total time of the cell  B) How much time was spent in each function called  C) How much memory each variable uses  D) The source code of a function

---

## ✅ Answer Key

1. **A**: `%pwd`.
2. `%` applies to just that one line. `%%` applies to the entire cell and must be the cell's first line. `!` sends the line to your operating system's shell, so it can run any shell command.
3. A list of strings (IPython's `SList`, one item per output line): `['a.csv', 'b.txt']`.
4. **False**. IPython treats `# go up one folder` as part of the folder name, so the command fails. Put comments on their own line.
5. `%pip` installs into the exact Python environment the notebook's kernel is using. `!pip` runs whichever `pip` the shell finds first, which may belong to a different Python, so the install "works" but the import still fails.
6. **True**.
7. **B**: `B`.
8. In Edit mode, keystrokes type into the cell. In Command mode, keystrokes are shortcuts that act on whole cells. If `B` typed a "b", you were in Edit mode. Press `Esc` to switch to Command mode and try again.
9. `15`. Only the value of the **last** line is displayed automatically. Use `print()` to show more than one result.
10. Execution counts show the order cells were **run in**, not their position. The lower cell ran before the upper one, so the notebook was run out of order and may not work top to bottom.
11. **False**. The variable lives in the kernel until you restart it (or delete it with `%xdel`/`%reset`). The notebook is the recipe; the kernel is the kitchen.
12. Restarting wipes every variable, and Run All executes the cells top to bottom. That catches cells that only worked because of leftover variables or out-of-order runs. It's also what happens when someone else (like your grader) runs the notebook.
13. `??` tries to show the actual Python **source code**, not just the docstring. It doesn't always work because many built-ins and much of NumPy are written in C, so there's no Python source to display.
14. **C**. Arguments before `/` must be passed by position (so A is invalid), and arguments after `*` must be passed by name (so B is invalid). D is missing the required argument.
15. `AttributeError: 'list' object has no attribute 'mean'`. A Python list doesn't have a `.mean()` method. Use `np.mean(numbers)` or convert it with `np.array(numbers).mean()`.
16. The **last** line. It names the error type and says what went wrong. The lines above it show where it happened.
17. A real Python list of **every** name, which you can filter with a list comprehension, including the double-underscore (dunder) names that completion usually hides.
18. `## Section 2`
19. Inline: wrap it in single dollar signs, e.g. `$E = mc^2$`. Block: wrap it in double dollar signs, e.g. `$$ ... $$`.
20. `$` starts LaTeX math, so `5 and the tax is ` is treated as an equation. Escape each one with a backslash: `\$5` and `\$2`.
21. Put a blank line between them (a new paragraph), or force a line break with `<br>` (or two trailing spaces at the end of the first line).
22. Narrative Markdown explains the *why* and tells a story around the results as readable formatted text. Code comments are only visible when reading the raw code, not when someone (or you, later) is skimming a report-style notebook.
23. `hi`
24. **C**: `'a'` (append). `'w'` erases the file first, and `'x'` refuses to open a file that already exists.
25. `sales_2026.csv sales_2026 .csv`
26. An absolute path is specific to one person's computer and folder structure. It breaks the moment anyone else (including your grader, or you on another machine) runs the notebook. A relative path works wherever the notebook and its data keep the same arrangement.
27. `['Alice', '90']`. The score is the **string** `'90'`, not the number 90, so math on it fails or gives wrong results until you convert it with `int()`.
28. **False**. JSON has no tuples, so `(3, 4)` comes back as the list `[3, 4]`. (Dictionary keys also come back as strings.)
29. A Pandas DataFrame.
30. **C**: `.describe()`.
31. Pandas wrote the DataFrame's index (0, 1, 2...) as an extra column. Prevent it with `df.to_csv('out.csv', index=False)`.
32. A list with one dictionary per row, e.g. `[{"Name": "Alice", "Score": 90}, ...]`. That's how most APIs share data, and it's easy for other programs to read. The default layout is column-by-column, keyed by the index.
33. CSV files have no types, so Pandas guesses that the column is a number, and numbers don't keep leading zeros. Read it as text: `pd.read_csv('file.csv', dtype={'Zip': str})`.
34. A dictionary that maps each sheet's name to a DataFrame of that sheet.
35. `[1, 2, 1, 2]` (list `*` repeats the list), then `[2 4]` (array `*` multiplies every element).
36. a) bar, b) line, c) scatter, d) histogram.
37. A histogram shows the **distribution** of one numeric variable by grouping values into ranges (bins). A bar chart compares amounts across separate **categories**.
38. `plt.show()` finishes the figure and clears it, so `savefig` afterwards saves an empty figure. Call `plt.savefig()` **before** `plt.show()`.
39. The line inside the box is the **median**. Dots beyond the whiskers are **possible outliers**: values unusually far from the rest (more than 1.5 × IQR beyond the box).
40. `%time` runs the code once. `%timeit` runs it many times and reports the mean ± standard deviation. A single run can be thrown off by other programs, caching, or one-time setup. Averaging many runs smooths that out.
41. NumPy runs the loop in compiled code, with one call from Python for the whole array. A Python loop handles one element at a time, with interpreter overhead (type checks, lookups) on every pass.
42. **False**. `%%timeit` runs the cell many times in a temporary space, and its variables don't survive. `%%time` runs the cell normally, so its variables do.
43. The first version also **converts the list to an array** every time, so it measures conversion plus squaring, while the second measures squaring only. Create the array once, outside the timing, and compare the same work.
44. `max(scores)` scans the whole list on **every** pass, so the work is *n* × *n*. Compute `top = max(scores)` once, before the loop. When the list doubles, the slow version takes about **4x** as long (quadratic). The fixed version takes about 2x (linear).
45. **B**. `%prun` profiles the statement and reports the calls and time spent in each function (`ncalls`, `tottime`, `cumtime`).
