# 📝 Worksheet: 07 - Working with Data (Advanced)

Use this worksheet to reinforce sets, Pandas Series/DataFrames, and the core data-wrangling workflow: load, explore, select, clean, transform, sort/filter. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🎯 Section 1: Sets and Data Structures

1. Why does `{1, 1, 2, 3}` become `{1, 2, 3}`?  
   `Answer:` _______________________

2. When would you reach for a `set` instead of a `list` in a real data-cleaning task?  
   `Answer:` _______________________

---

### ✏️ Task: Series Basics

```python
# Create a Series from a dictionary mapping 4 of your classes to your grade in each.
# Print the Series, then print the average of all grades (hint: .mean()).
```

### 🤖 Explain It

In your own words: how is a Pandas `Series` similar to a Python dictionary, and how is it similar to a list? What does it borrow from each?

---

## 📂 Section 2: Loading and Exploring

3. What does `df.info()` tell you that `df.describe()` doesn't?  
   `Answer:` _______________________

4. If `df.isnull().sum()` shows `Age: 177`, what does that number mean?  
   `Answer:` _______________________

---

### ✏️ Task: First Look at a Dataset

```python
# Load pokemon.csv.
# Print its shape, its columns, and .describe() for just the numeric columns.
# Which column has the most missing values, if any?
```

### 🤖 Explain It

In your own words: why is it worth running `.info()` and `.isnull().sum()` on a dataset *before* you start analyzing it, rather than jumping straight to the questions you actually care about?

---

## 🎯 Section 3: Indexing and Selection

5. Rewrite this using `.loc[]` instead of bracket + `.iloc[]` mixed together — or explain why you can't mix them the way it's written:
```python
df.iloc[df['Age'] < 10]  # this is actually broken — why?
```
   `Answer:` _______________________

6. What's wrong with `df[df['Age'] < 10 and df['Fare'] > 100]`, and how would you fix it?  
   `Answer:` _______________________

---

### ✏️ Task: Titanic Slicing

```python
# Using titanic.csv:
# 1. Select passengers in 3rd class (Pclass == 3) who survived (Survived == 1).
# 2. Of those, show only the Name, Age, and Fare columns.
# 3. Sort the result by Fare, descending.
```

### 🤖 Explain It

In your own words: why does `df.iloc[df['Age'] < 10]` not work, when `df.loc[df['Age'] < 10]` and `df[df['Age'] < 10]` both do?

---

## 🧼 Section 4: Cleaning

7. If a column has the values `['25', 'thirty', '35']`, what happens when you run `pd.to_numeric(col, errors='coerce')` on it?  
   `Answer:` _______________________

8. When would you choose `.dropna()` over `.fillna()`, and vice versa?  
   `Answer:` _______________________

---

### ✏️ Task: Clean a Column

```python
# Using ufo.csv:
# 1. Check .isnull().sum() for the whole dataset.
# 2. Pick the column with the most missing values.
# 3. Decide (and justify in a comment) whether dropping or filling makes more
#    sense for that specific column, then do it.
```

### 🤖 Explain It

In your own words: why might dropping rows with missing data be a bad idea if a large fraction of your dataset has at least one missing value somewhere?

---

## 🧱 Section 5: Column Operations, Sorting, and Filtering

9. What's the difference between `df.rename(columns={'a': 'b'})` and `df.columns = ['b', 'c', 'd']`?  
   `Answer:` _______________________

10. Rewrite this bracket-filter as a `.query()` call:
```python
df[(df['math_score'] >= 80) & (df['science_score'] >= 80)]
```
   `Answer:` _______________________

---

### ✏️ Task: Build a Feature

```python
# Using students.csv:
# 1. Create a "total_score" column (math + science).
# 2. Sort by total_score, descending.
# 3. Print just the top 3 students' first_name and total_score.
```

### 🤖 Explain It

In your own words: what does "feature engineering" mean in the context of `total_score` or `average_score` — why create a new column instead of just computing the value fresh every time you need it?

---

## 🧾 Submit Checklist

- [ ] I created and used a `set`, including at least one set operation (`&`, `|`, or `-`).
- [ ] I loaded a local CSV into a DataFrame and inspected it with `.info()` and `.describe()`.
- [ ] I used both `.loc[]` and `.iloc[]` at least once each.
- [ ] I filtered a DataFrame using a compound condition (`&` or `|`).
- [ ] I cleaned at least one column with `.fillna()`, `.dropna()`, or `pd.to_numeric()`.
- [ ] I created a new column and sorted by it.
- [ ] I completed the "Explain It" prompts in my own words.
