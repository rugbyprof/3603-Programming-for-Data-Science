# 📝 Quiz: 07 - Working with Data (Advanced)

22 questions covering sets, Pandas Series/DataFrames, loading/exploring data, indexing/selection, cleaning, column operations, sorting/filtering, and a "going further" bonus. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Sets

**1.** (Code Tracing) What prints?
```python
s = {1, 2, 2, 3}
print(len(s))
```

**2.** (Short Answer) What's the key difference between a `set` and a `list`?

**3.** (Code Tracing) What prints?
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)
```

---

## Section B — Series and DataFrames

**4.** (Short Answer) What's the difference between a Pandas `Series` and a `DataFrame`?

**5.** (Code Tracing) What prints?
```python
s = pd.Series({'a': 1, 'b': 2})
print(s['a'])
```

**6.** (Short Answer) What does `df.shape` return?

**7.** (Short Answer) If you add two `Series` together and one has a label the other doesn't, what happens at that label?

---

## Section C — Loading and Exploring Data

**8.** (Multiple Choice) Which method shows summary statistics (mean, std, min/max) for numeric columns?
A) `.head()`  B) `.columns`  C) `.describe()`  D) `.shape`

**9.** (Short Answer) What's the difference between what `.head()` and `.info()` each tell you about a DataFrame?

**10.** (Short Answer) How do you count how many missing values are in *each column* of a DataFrame?

---

## Section D — Indexing and Selection

**11.** (Short Answer) What's the difference between `.loc[]` and `.iloc[]`?

**12.** (Short Answer) Is `df.loc[0:4]` inclusive or exclusive of row `4`? What about `df.iloc[0:4]` and position `4`?

**13.** (Short Answer) What symbols does Pandas require for combining conditions when filtering a DataFrame (instead of the `and`/`or` keywords)?

**14.** (Short Answer) What does `df[df['Age'] < 10]` return?

---

## Section E — Cleaning

**15.** (Short Answer) What's the difference between `.dropna()` and `.fillna()`?

**16.** (Short Answer) What does `pd.to_numeric(col, errors='coerce')` do to a value like `'ninety'` in that column?

**17.** (True/False) `NaN` and an empty string `""` are always treated identically by `.isnull()`.

---

## Section F — Column Operations, Sorting, and Filtering

**18.** (Short Answer) How do you create a new column that's the sum of two existing numeric columns?

**19.** (Short Answer) What does `.apply()` do that you could also do with a `for` loop over rows — and why is `.apply()` usually preferred?

**20.** (Short Answer) What does `ascending=False` do inside `df.sort_values(by='score', ascending=False)`?

**21.** (Short Answer) What's the main advantage of `.query()` over bracket-based boolean filtering (`df[df['col'] > 5]`)?

---

## Section G — Going Further (Bonus)

**22.** (Short Answer) What do the `usecols` and `nrows` arguments to `pd.read_csv()` do, and when would you reach for them?

---

## ✅ Answer Key

1. `3` — the duplicate `2` is dropped.
2. A `set` is unordered and only holds unique values (no duplicates); a `list` is ordered and allows duplicates.
3. `{2, 3}` — the intersection: values present in both.
4. A `Series` is one-dimensional (a single labeled column); a `DataFrame` is two-dimensional (a full table made of multiple Series sharing an index).
5. `1`
6. A tuple of `(number_of_rows, number_of_columns)`.
7. It becomes `NaN` — Pandas aligns by label, and there's nothing to add at a label that only exists in one of the two Series.
8. **C** — `.describe()`.
9. `.head()` shows the actual first few rows of data; `.info()` shows structural metadata — column names, data types, and non-null counts — not the data values themselves.
10. `df.isnull().sum()`
11. `.loc[]` selects by label (row/column names); `.iloc[]` selects by integer position, regardless of what the labels are.
12. `.loc[0:4]` **is** inclusive of `4`. `.iloc[0:4]` is **not** inclusive of position `4` (stop-exclusive, like a normal Python slice).
13. `&` for "and" and `|` for "or" (with parentheses around each condition) — not the `and`/`or` keywords.
14. A filtered DataFrame containing only the rows where the `Age` column is less than `10`.
15. `.dropna()` removes rows (or columns) that contain missing values; `.fillna()` keeps every row but replaces missing values with something else.
16. It becomes `NaN` — `errors='coerce'` converts anything that isn't a valid number into a missing value instead of raising an error.
17. **False** — `NaN` is a true missing-value marker; an empty string `""` is a valid (if unhelpful) string value, and `.isnull()` does not flag it as missing.
18. `df['new_col'] = df['col_a'] + df['col_b']`
19. `.apply()` runs a function once per value (or per row, with `axis=1`) without you writing the loop yourself — it's more concise, and Pandas can often execute it faster than an equivalent explicit Python loop.
20. It sorts from largest to smallest instead of the default smallest-to-largest.
21. `.query()` reads more like a plain English/SQL condition (`'score > 90 and age < 18'`) instead of repeating `df[...]` and column brackets for every condition — easier to read, especially with several conditions chained together.
22. `usecols` loads only the specified columns instead of all of them; `nrows` loads only the first N rows. Both are useful for speeding up work with very large files when you don't need the whole thing.
