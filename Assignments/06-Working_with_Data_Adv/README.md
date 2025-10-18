# 🧰 Module 07 – Working with Data

This module introduces core Python and Pandas tools for manipulating, cleaning, and inspecting datasets. It's the messy middle of any data science project—and now you're equipped to handle it like a pro.

---

## 🎯 Learning Objectives

By the end of this module, you should be able to:

- Describe and use Python’s built-in containers (`list`, `dict`, `tuple`, `set`)
- Load tabular data from `.csv` using Pandas
- Explore, index, and select data using `.loc[]`, `.iloc[]`, and masks
- Handle missing values and perform basic data cleaning
- Add, remove, and modify columns in a DataFrame
- Filter and sort data using multiple strategies
- Prepare a dataset for visualization or modeling


## 🗂 Notebook Overview

| Notebook                                | Description                                        |
| --------------------------------------- | -------------------------------------------------- |
| `01-lists_dicts_and_tuples.ipynb`       | Review of native Python containers and why we care |
| `02-pandas_series_and_dataframes.ipynb` | Core data structures in Pandas                     |
| `03-loading_and_exploring_data.ipynb`   | Reading CSVs, inspecting data                      |
| `04-indexing_and_selection.ipynb`       | Accessing rows/columns, boolean masks              |
| `05-basic_cleaning.ipynb`               | Dealing with missing values and data types         |
| `06-column_operations.ipynb`            | Column creation, renaming, dropping                |
| `07-sorting_and_filtering.ipynb`        | Sorting, conditional filters, `.query()`           |
| `08-pandas_wrangle_lab.ipynb`           | Clean and explore a real dataset (assigned)        |

---

## 📦 Module Recap

Data doesn’t come clean and labeled like a science fair project. This module guided you through the messy, glorious reality of **data wrangling** in Python using native tools and Pandas.

By now, you should feel confident:

- Recognizing Python's core data containers (`list`, `tuple`, `dict`, `set`)
- Working with Pandas `Series` and `DataFrames`
- Loading CSVs, exploring structure, and identifying issues
- Cleaning, transforming, and filtering datasets
- Writing your cleaned data back out for analysis or sharing

---

## 🎯 Key Takeaways

- **Missing values** are common and must be handled early to avoid broken logic later.
- **Data types** matter: just because it looks like a number doesn’t mean Python agrees.
- **Column operations** let you build new insights and features from existing ones.
- **Filtering and sorting** are the core tools of exploratory data analysis (EDA).
- Pandas is powerful, but _you_ are the one asking the questions and defining the structure.

---

## 🗂️ Suggested Datasets

- Titanic Dataset (`seaborn.load_dataset("titanic")`)
- Pokémon Stats (`data/pokemon.csv`)
- UFO Sightings (`data/ufo.csv`)
- Iris Dataset (`seaborn.load_dataset("iris")`)
- Students (`data/students.csv` or `data/students.json`)

---

## 🛠️ Tips

- Try chaining methods (`df[df.col > 5].sort_values("col2")`) but don’t be afraid to split steps for clarity.
- Use `.copy()` when slicing to avoid `SettingWithCopyWarning`.
- Use `%timeit` to compare loops vs. vectorized filters.

## 🧪 Up Next: Analyzing & Visualizing Data

Now that you've got your data in shape, it's time to ask questions of it. Coming up:

- Aggregation and grouping
- Basic statistics
- Visualizing data with Matplotlib and Seaborn
