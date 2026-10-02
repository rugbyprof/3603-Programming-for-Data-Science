# 📚 Glossary: 06 - Working with Data (Advanced)

**Series**  
A one-dimensional labeled array from Pandas — like a list, but every value has an index label.

**DataFrame**  
A two-dimensional, tabular Pandas structure with labeled rows (the index) and labeled columns.

**Default Index**  
The row labels `0, 1, 2, ...` that pandas uses when you don't give it any.

**List of Dictionaries**  
One dictionary per row, the way Modules 03/03b stored records (and the shape most JSON and APIs use). `pd.DataFrame(list_of_dicts)` turns each dictionary into a row.

**Index Alignment**  
When you do math between two `Series`, Pandas matches values by their index *label*, not their position — mismatched labels produce `NaN`.

**`read_csv()`**  
Loads a CSV file into a DataFrame.

**`.head()` / `.tail()`**  
Shows the first / last 5 rows of a DataFrame (or `n` rows if you pass a number).

**`.info()`**  
Prints a summary of a DataFrame: column names, dtypes, and non-null counts.

**`.describe()`**  
Summary statistics (mean, std, min/max, quartiles) for numeric columns — pass `include='all'` to include non-numeric ones too.

**`.dtypes`**  
The data type of every column: `int64`, `float64`, `object`/`str` (text), `bool`, `datetime64`. A column of whole numbers with missing values becomes `float64`.

**`.duplicated()` / `.drop_duplicates()`**  
Flag (or remove) rows that repeat an earlier row. `subset=[...]` compares only some columns; `keep='last'` keeps the last copy instead of the first; `keep=False` (with `.duplicated()`) marks **every** copy, so you can inspect them side by side.

**`.unique()` / `.nunique()`**  
The distinct values in a column / how many distinct values there are.

**`.loc[]`**  
Label-based selection — row/column labels, inclusive on both ends of a slice.

**`.iloc[]`**  
Position-based selection — integer positions, stop-exclusive like a normal Python slice.

**`.set_index()`**  
Turns a column into the row labels (e.g. `df.set_index('PassengerId')`), so `.loc[]` can look rows up by something meaningful. Returns a new DataFrame.

**`.at[]` / `.iat[]`**  
Fast access to **one** value — by label (`df.at[1, 'Fare']`) or by position (`df.iat[1, 9]`).

**Boolean Mask**  
A Series of `True`/`False` values (from a condition like `df['age'] < 10`) used to filter rows: `df[mask]`.

**`.isin()`**  
True where a value is in a list: `df['Embarked'].isin(['C', 'Q'])` replaces a chain of `|` conditions.

**`.between()`**  
True where a value is in a range, **including** both ends: `df['Age'].between(13, 19)`.

**`~` (Not)**  
Flips a boolean mask: every `True` becomes `False` and vice versa. `df[~df['Embarked'].isin(['S'])]` keeps everyone who did **not** board at Southampton.

**`.isna()` / `.notna()`**  
Boolean masks for missing / present values. `.isna()` is the same as `.isnull()`, and `.notna()` the same as `.notnull()`.

**`.nlargest()` / `.nsmallest()`**  
The N rows with the largest / smallest values in a column, e.g. `df.nlargest(5, 'Fare')`. A shortcut for sorting and then taking `.head()`.

**Chained Assignment**  
Selecting and then assigning in two bracket steps, like `df[mask]['col'] = value`. The first step makes a copy, so the original never changes (pandas only warns). Use one step instead: `df.loc[mask, 'col'] = value`.

**`.query()`**  
Filters rows using a readable, SQL-like string, e.g. `df.query('score > 90')`.

**Named Mask**  
A boolean mask saved in a descriptively named variable (`is_affordable = df['price'] < 30`), so a long filter reads like a sentence: `df[is_office & is_affordable & has_stock]`.

**`@` in `.query()`**  
Uses a Python variable's value inside a query: `df.query('score >= @minimum')`. Without `@`, pandas looks for a column with that name. Wrap column names with spaces in backticks: ``df.query('`Unit Price` < 5')``.

**Regular Expression (Pattern)**  
A text pattern where some characters have special meanings, e.g. `|` means "or" in `.str.contains('son|ez')`. Characters like `+`, `.`, and `(` are special too, so use `regex=False` to search for literal text like `'C++'`.

**`.str` Accessor**  
Applies string methods to every value in a text column: `.str.contains()`, `.str.startswith()`, `.str.endswith()`, `.str.upper()`, `.str.strip()`. Use `case=False` to ignore capitalization and `na=False` so missing values count as "no match".

**Missing Value (`NaN`)**  
A placeholder for missing or null data in a numeric column. Text/object columns can also hold `None`.

**`.isnull()` / `.notnull()`**  
Boolean mask of missing (or present) values, cell by cell.

**`.fillna()`**  
Fills missing values with a specified constant, or a computed value like a column's mean/median.

**`.dropna()`**  
Drops rows (or columns) that contain missing values.

**Hidden Missing Values**  
Values that *mean* "missing" but that `.isna()` can't see: empty strings (`""`), text placeholders (`'N/A'`, `'Unknown'`), and number codes (`-1`, `999`). Turn them into real missing values with `.replace()` before counting or averaging.

**`pd.NA`**  
Pandas' own missing-value marker, used by nullable types like `Int64` (shown as `<NA>`).

**`ffill()` / `bfill()`**  
Fill a gap with the value from the row before (forward fill) or after (backward fill). Only sensible when row order means something, like time series.

**Missing-Value Flag**  
A True/False column recording which values were missing, made **before** filling: `df['x_was_missing'] = df['x'].isna()`.

**Type Mismatch**  
A value stored as the wrong type for its meaning: numbers as text, dates as text, `'yes'`/`'Y'` for True, `'IL'`/`'il'` as two categories.

**`pd.to_numeric()`**  
Converts a Series to a numeric type; `errors='coerce'` turns anything that can't convert into `NaN` instead of raising an error.

**`pd.to_datetime()`**  
Converts a Series of date-like strings into actual datetime values; `errors='coerce'` turns invalid entries into `NaT` (missing datetime).

**`format='mixed'`**  
Tells `pd.to_datetime` that a column mixes date formats. Without it, pandas 2+ guesses the format from the first value and **silently** turns other formats into `NaT`.

**Nullable Integer (`Int64`)**  
Pandas' integer type that can hold missing values (note the capital **I**). Regular `int64` can't, so `.astype('int64')` fails if anything is missing.

**`.map()` with a Dictionary**  
Replaces each value using a lookup dictionary. Values not in the dictionary become `NaN`, so unexpected values show up instead of slipping through, which is safer than `.replace()` for standardizing categories.

**`.replace()`**  
Swaps one value for another — often used to turn placeholder codes like `-1`, `999`, or `'N/A'` into real missing values (`np.nan`).

**`.rename()`**  
Renames column(s) using a `{old: new}` dictionary.

**Standardizing Column Names**  
Cleaning every column name at once: `df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')` turns `' First Name'` into `'first_name'`.

**`.drop(columns=...)`**  
Removes column(s) from a DataFrame.

**`errors='ignore'`**  
Tells `.drop()` to skip columns that don't exist instead of raising a `KeyError`. Useful, but it can also hide a typo. `.drop(index=[...])` removes rows instead of columns.

**`.apply()`**  
Runs a function across every value in a column (or, with `axis=1`, across every row). It's still a loop under the hood, so prefer a whole-column operation when one exists.

**`lambda`**  
A small, unnamed one-line function, handy inside `.apply()`: `df['score'].apply(lambda s: s >= 88)`. Use a named `def` function when the rule has several steps.

**`pd.cut()`**  
Sorts numbers into labeled bands (bins): `pd.cut(df['score'], bins=[0, 80, 90, float('inf')], labels=['C', 'B', 'A'], right=False)`. A vectorized alternative to an `if`/`elif` function.

**`.dt` Accessor**  
Date parts for a whole datetime column: `.dt.year`, `.dt.month`, `.dt.day_name()`.

**Conditional Update**  
Changing a column only where a condition is true: `df.loc[condition, 'col'] = value`. Rows that don't match keep their old value (or get `NaN` if the column is new). With several rules, the **last** one wins, so put the most specific rule last. `df.loc[condition, ['a', 'b']] = [x, y]` updates several columns at once.

**`.itertuples()` / `.iterrows()`**  
Ways to loop over a DataFrame one row at a time. Prefer `.itertuples()`: it's faster and keeps data types. Use either only when the logic truly needs one row at a time.

**Vectorized Operation**  
A calculation on a whole column at once (`df['price'] * df['qty']`) instead of a row-by-row loop. Shorter, clearer, and often thousands of times faster.

**`.sort_values()`**  
Sorts rows by one or more columns: `by=['a', 'b']` sorts by `a`, then uses `b` to break ties, with `ascending=[True, False]` setting each direction. Returns a **new** DataFrame.

**`.groupby()`**  
Groups rows by a shared column value so you can run aggregations (`.mean()`, `.sum()`, etc.) per group.

**`.size()` vs. `.count()`**  
After `groupby`, `.size()` counts the **rows** in each group; `.count()` counts the **non-missing values** in a column, so it's smaller wherever that column has gaps.

**`as_index=False`**  
`df.groupby('col', as_index=False)` keeps the group labels as ordinary columns instead of the index, the same as adding `.reset_index()`.

**Filtering Groups (HAVING)**  
Keeping only the groups that meet a condition: summarize first, then filter the summary, e.g. `summary[summary['passengers'] >= 20]`.

**`.agg()`**  
Computes several summaries per group at once, with named output columns: `.agg(total='sum', average='mean')` on one column, or `.agg(total=('amount', 'sum'), riders=('id', 'count'))` with `(column, function)` pairs to summarize **different** columns.

**`.reset_index()`**  
Turns the index (for example, the group labels from a `groupby`) back into ordinary columns. `reset_index(drop=True)` throws the old labels away and renumbers the rows `0, 1, 2, ...`, which is handy after filtering.

**`.value_counts()`**  
Counts how many times each unique value appears in a Series. `normalize=True` gives proportions; `dropna=False` also counts missing values.

**`pd.concat()`**  
Stacks DataFrames with the same columns on top of each other. `ignore_index=True` renumbers the rows.

**`.merge()` / Join**  
Combines two tables side by side by matching a shared **key** column (like a SQL `JOIN`). `how='left'` keeps every row of the left table (unmatched columns become `NaN`); `how='inner'` keeps only keys found in both. Keys must match exactly — `'tx'` ≠ `'TX'`.

**`suffixes=`**  
When both tables in a merge have a column with the same name, pandas renames them `_x` and `_y` by default. `suffixes=('_shipped', '_home')` picks meaningful names instead.

**`left_on` / `right_on`**  
Merge on key columns with **different** names: `orders.merge(buyers, left_on='customer_number', right_on='buyer_id')`.

**`validate=`**  
States the relationship a merge should have, e.g. `validate='many_to_one'` (many purchases per buyer, one row per buyer). If a key is unexpectedly duplicated, pandas raises a `MergeError` instead of silently copying rows. Also compare row counts before and after merging.

**`.to_csv()`**  
Writes a DataFrame out to a CSV file.

**`usecols` / `nrows`** *(Challenge)*  
Optional `pd.read_csv()` arguments to load only specific columns, or only the first N rows — useful for large files.
