# 🧰 Module 07: Working with Data (Advanced)

This module introduces Pandas — the core tool for manipulating, cleaning, and inspecting real datasets. It's the messy middle of any data science project, and now you're equipped to handle it.

All notebooks use **local data files in this folder** (`titanic.csv`, `pokemon.csv`, `ufo.csv`, `students.csv`, `students_messy.csv`, `state_abbr.json`) — nothing downloads over the network, so everything here works offline and keeps working even after you copy a notebook into your `Completed` folder.

---

## 🗂 Notebook Overview

| Notebook | Description |
|----------|-------------|
| [01-Sets_and_a_Quick_Recap.ipynb](01-Sets_and_a_Quick_Recap.ipynb) | A quick recap of lists/tuples/dicts, plus `set` — the one container Module 01 didn't cover. |
| [02-Pandas_Series_and_DataFrames.ipynb](02-Pandas_Series_and_DataFrames.ipynb) | Core Pandas data structures: `Series` and `DataFrame`. |
| [03-Loading_and_Exploring_Data.ipynb](03-Loading_and_Exploring_Data.ipynb) | Reading CSVs, inspecting structure with `.head()`/`.info()`/`.describe()`. |
| [04-Indexing_and_Selection.ipynb](04-Indexing_and_Selection.ipynb) | `.loc[]`, `.iloc[]`, boolean masks, and compound filters. |
| [05-Basic_Cleaning.ipynb](05-Basic_Cleaning.ipynb) | Handling missing values and fixing data types. |
| [06-Column_Operations.ipynb](06-Column_Operations.ipynb) | Creating, renaming, dropping columns; `.apply()`. |
| [07-Sorting_and_Filtering.ipynb](07-Sorting_and_Filtering.ipynb) | `.sort_values()`, conditional filters, `.query()`. |
| [08-Pandas_Wrangle_Lab.ipynb](08-Pandas_Wrangle_Lab.ipynb) | Clean and explore a dataset with real, deliberately-planted messiness — everything above, combined. |

Each notebook ends with a **🏋️ Practice** section and an optional **🔥 Challenge**.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- Use `set` alongside the containers from Module 01, and know when to reach for one
- Create and inspect Pandas `Series` and `DataFrame` objects
- Load tabular data from `.csv` and explore its structure
- Select data with `.loc[]`, `.iloc[]`, and boolean masks
- Handle missing values and fix mismatched data types
- Add, rename, and drop columns, including with `.apply()`
- Filter and sort data using multiple strategies
- Prepare a dataset for visualization or modeling

---

## 🎯 Key Takeaways

- **Missing values** are common and must be handled early to avoid broken logic later — and not every kind of "missing" looks like `NaN` (a text value like `'ninety'` in a numeric column hides from `.isnull()` until you try to convert it).
- **Data types** matter: just because it looks like a number doesn't mean Python — or Pandas — agrees.
- **Column operations** let you build new insights and features from existing ones.
- **Filtering and sorting** are the core tools of exploratory data analysis (EDA).
- Pandas is powerful, but *you* are the one asking the questions and defining the structure.

---

## 🛠️ Tips

- Try chaining methods (`df[df.col > 5].sort_values('col2')`) but don't be afraid to split steps for clarity while you're learning.
- Use `.copy()` when slicing if you plan to modify the result, to avoid a `SettingWithCopyWarning`.
- Use `%timeit` (from Foundations) to compare loops vs. vectorized filters.

---

## 📚 Also in this module

- [glossary.md](glossary.md) — key terms
- [quiz.md](quiz.md) — 22-question self-check with an answer key
- [worksheet.md](worksheet.md) — practice problems and reflection prompts

## 🧪 Up Next: Analyzing & Visualizing Data

Now that you've got your data in shape, it's time to ask questions of it — aggregation, summary statistics, and visualizing data with Matplotlib and Seaborn.
