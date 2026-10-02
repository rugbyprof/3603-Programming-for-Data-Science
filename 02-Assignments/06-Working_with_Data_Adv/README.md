# 🧰 Module 06: Working with Data (Advanced)

This module introduces Pandas — the core tool for manipulating, cleaning, and inspecting real datasets. It's the messy middle of any data science project, and now you're equipped to handle it.

All notebooks use **local data files in this folder** (`titanic.csv`, `pokemon.csv`, `ufo.csv`, `students.csv`, `state_abbr.json`, and the lab's `messy_purchases.csv`) — nothing downloads over the network, so everything here works offline and keeps working even after you copy a notebook into your `Completed` folder.

---

## 🗂 Notebook Overview

| Notebook | Description |
|----------|-------------|
| [01-Pandas_Series_and_DataFrames.ipynb](01-Pandas_Series_and_DataFrames.ipynb) | Core Pandas data structures: `Series` (math and filtering on every value at once) and `DataFrame`, built from a dictionary of columns or a list of dictionaries (rows). |
| [02-Loading_and_Exploring_Data.ipynb](02-Loading_and_Exploring_Data.ipynb) | Reading CSVs, dtypes, `.head()`/`.info()`/`.describe()`, duplicates and distinct values, and a first-look checklist ("what does one row represent?"). |
| [03-Indexing_and_Selection.ipynb](03-Indexing_and_Selection.ipynb) | `.loc[]` vs. `.iloc[]` (labels vs. positions), `.set_index()`, `.at[]`/`.iat[]`, boolean masks with `&`/`\|`/`~`, `.isin()`, `.between()`, `.isna()`, rows **and** columns in one `.loc[]`, `.nlargest()`, avoiding chained assignment, and `reset_index()`. |
| [04-Basic_Cleaning.ipynb](04-Basic_Cleaning.ipynb) | What counts as missing, inspecting before cleaning, fill vs. drop (`subset=`, `thresh=`, `ffill`), safe conversions (`format='mixed'` dates, nullable `Int64`), placeholders, text categories, duplicates, and a full cleaning pipeline with validation. |
| [05-Column_Operations.ipynb](05-Column_Operations.ipynb) | Creating columns (arithmetic, True/False, `pd.cut()` bands, `.str`/`.dt`), conditional updates with `.loc[]` (rule order matters), renaming and tidying names, dropping safely, `.apply()` and `apply(axis=1)`, and choosing between vectorized operations, `.apply()`, and loops. |
| [06-Sorting_and_Filtering.ipynb](06-Sorting_and_Filtering.ipynb) | `.sort_values()` (multi-column, returns a copy), named masks for long filters, `.query()` with `in`/`@variables`/backticks, text search with `.str.contains()` (patterns and `regex=False`)/`.startswith()`/`.endswith()`, and filter-then-sort reports. |
| [07-Grouping_and_Combining.ipynb](07-Grouping_and_Combining.ipynb) | `value_counts()` (with percentages), `groupby()` (`.size()` vs. `.count()`, `as_index=False`), named `.agg()`, filtering groups, `pd.concat()` vs. `.merge()`, join types, `suffixes=`, `left_on`/`right_on`, checking joins with `validate=`, and UFO sightings per million people. |
| [08-Pandas_Wrangle_Lab.ipynb](08-Pandas_Wrangle_Lab.ipynb) | Capstone lab: take `messy_purchases.csv` (prices like `$1,249.99`, placeholders, mixed date formats, duplicates, messy names) from raw file to a validated revenue report by state and department — everything above, combined. Saves its results to `08-OutputFiles`. |

Each notebook ends with a **🏋️ Practice** section and an optional **🔥 Challenge**.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- Create and inspect Pandas `Series` and `DataFrame` objects, including from a list of dictionaries
- Load tabular data from `.csv`, explore its structure, and say what one row represents
- Select data with `.loc[]`, `.iloc[]`, `.at[]`, boolean masks, `.isin()`, and `.between()`, and change it in one `.loc[]` step (no chained assignment)
- Handle missing values, duplicate rows, placeholder values, messy text categories, and mismatched data types, then validate the result
- Add, rename, and drop columns, update rows conditionally (in the right order), band numbers with `pd.cut()`, and use `.apply()`
- Choose whole-column (vectorized) operations over row-by-row loops
- Filter, sort, and search text data using multiple strategies, keeping long filters readable with named masks and `.query()`
- Summarize and filter groups with `groupby()` and `.agg()`, and combine tables with `pd.concat()` and `.merge()`, checking every join with its row count and `validate=`
- Prepare a dataset for visualization or modeling

---

## 🎯 Key Takeaways

> **The core habit:** inspect first, select carefully, and prefer whole-column operations over row-by-row loops.

- **Know what one row represents** before you analyze anything. It decides what every count, average, and group actually means.
- **Missing values** are common and must be handled early to avoid broken logic later — and not every kind of "missing" looks like `NaN` (a text value like `'ninety'` in a numeric column hides from `.isnull()` until you try to convert it).
- **Data types** matter: just because it looks like a number doesn't mean Python — or Pandas — agrees.
- **Column operations** let you build new insights and features from existing ones.
- **Filtering and sorting** are the core tools of exploratory data analysis (EDA).
- **Grouping** answers the questions people actually ask (*per class*, *per state*), and **joins** only work when the keys match exactly.
- Pandas is powerful, but *you* are the one asking the questions and defining the structure.

---

## 🛠️ Tips

- Try chaining methods (`df[df.col > 5].sort_values('col2')`) but don't be afraid to split steps for clarity while you're learning.
- Use `.copy()` when slicing if you plan to modify the result, to avoid a `SettingWithCopyWarning`.
- Use `%timeit` (from Foundations) to compare loops vs. vectorized operations. Notebook 05 shows a vectorized calculation running thousands of times faster than `.iterrows()`.

---

## 📚 Also in this module

- [glossary.md](glossary.md) — key terms
- [quiz.md](quiz.md) — 47-question self-check with an answer key
- [worksheet.md](worksheet.md) — practice problems and reflection prompts

## 🧪 Up Next: Analyzing & Visualizing Data

Now that you've got your data in shape, it's time to ask questions of it — aggregation, summary statistics, and visualizing data with Matplotlib and Seaborn.
