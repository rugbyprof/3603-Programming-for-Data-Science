# 🧩 Module 07: Working with Data

Welcome to the data-wrangling dojo. You've mastered the environment (Jupyter, files, Markdown, plotting, timing)... now it's time to bend raw data to your will. This module introduces you to Python's and Pandas' core data structures, and teaches you how to load, explore, filter, and clean real-world datasets.

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

---

## 📚 Notebooks

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

## 🧠 Assessment

- `Working_with_Data_Quiz.ipynb` – Short quiz to reinforce key concepts
- `glossary.md` – Terms, functions, and expressions used in this module

---

## 🗂️ Suggested Datasets

- Titanic Dataset (`seaborn.load_dataset("titanic")`)
- Pokémon Stats (`pokemon.csv`)
- UFO Sightings (`ufo.csv`)
- Iris Dataset (`seaborn.load_dataset("iris")`)

---

## 🛠️ Tips

- Try chaining methods (`df[df.col > 5].sort_values("col2")`) but don’t be afraid to split steps for clarity.
- Use `.copy()` when slicing to avoid `SettingWithCopyWarning`.
- Use `%timeit` to compare loops vs. vectorized filters.

---

Rubber chickens optional. Pandas mandatory.
