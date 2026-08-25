# 📚 Glossary: 07 - Working with Data (Advanced)

**Set**  
An unordered Python collection of unique values. Duplicates are silently dropped. Created with `{}` or `set(...)`.

**Union (`|`)**, **Intersection (`&`)**, **Difference (`-`)**  
Set operations for combining or comparing two sets — "in either," "in both," and "in this one but not the other."

**Series**  
A one-dimensional labeled array from Pandas — like a list, but every value has an index label.

**DataFrame**  
A two-dimensional, tabular Pandas structure with labeled rows (the index) and labeled columns.

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

**`.loc[]`**  
Label-based selection — row/column labels, inclusive on both ends of a slice.

**`.iloc[]`**  
Position-based selection — integer positions, stop-exclusive like a normal Python slice.

**Boolean Mask**  
A Series of `True`/`False` values (from a condition like `df['age'] < 10`) used to filter rows: `df[mask]`.

**`.query()`**  
Filters rows using a readable, SQL-like string, e.g. `df.query('score > 90')`.

**Missing Value (`NaN`)**  
A placeholder for missing or null data in a numeric column. Text/object columns can also hold `None`.

**`.isnull()` / `.notnull()`**  
Boolean mask of missing (or present) values, cell by cell.

**`.fillna()`**  
Fills missing values with a specified constant, or a computed value like a column's mean/median.

**`.dropna()`**  
Drops rows (or columns) that contain missing values.

**`pd.to_numeric()`**  
Converts a Series to a numeric type; `errors='coerce'` turns anything that can't convert into `NaN` instead of raising an error.

**`pd.to_datetime()`**  
Converts a Series of date-like strings into actual datetime values; `errors='coerce'` turns invalid entries into `NaT` (missing datetime).

**`.rename()`**  
Renames column(s) using a `{old: new}` dictionary.

**`.drop(columns=...)`**  
Removes column(s) from a DataFrame.

**`.apply()`**  
Runs a function across every value in a column (or, with `axis=1`, across every row).

**`.sort_values()`**  
Sorts rows by one or more columns.

**`.groupby()`**  
Groups rows by a shared column value so you can run aggregations (`.mean()`, `.sum()`, etc.) per group.

**`.value_counts()`**  
Counts how many times each unique value appears in a Series.

**`.to_csv()`**  
Writes a DataFrame out to a CSV file.

**`usecols` / `nrows`** *(Challenge)*  
Optional `pd.read_csv()` arguments to load only specific columns, or only the first N rows — useful for large files.
