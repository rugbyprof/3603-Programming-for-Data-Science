# Pandas Lab: Clean and Explore a Real-World-ish Purchases Dataset

## Lab goals

In this lab, students will practice a complete pandas workflow:

- Load, inspect, clean, and explore a messy dataset.
- Use `.info()`, `.describe()`, `.value_counts()`, and `.query()`.
- Detect and handle missing values, placeholders, duplicates, and type mismatches.
- Create, rename, update, sort, filter, and drop columns.
- Group purchase data and calculate meaningful summaries with `.groupby()`.

## Learning objectives

By the end of the lab, students should be able to:

- Practice loading, cleaning, and exploring real-world-ish data.
- Apply column creation, renaming, sorting, and filtering together.
- Use `.info()`, `.describe()`, and `.query()` fluently.
- Group and summarize with `.groupby()`.

## Scenario

A retail company has provided a file named `messy_purchases.csv`. Each row is intended to represent one purchase, but the file contains realistic data-quality problems:

- Prices stored as text, including dollar signs and commas.
- Missing and placeholder values such as `"N/A"`, `"Unknown"`, and `-1`.
- Inconsistent capitalization and whitespace in state and department names.
- Dates stored as text in mixed formats.
- Possible duplicate purchases.
- Columns that are not needed for analysis.

The goal is to produce a clean dataset and answer business questions about revenue by state and department.

## 1. Setup

```python
import pandas as pd
import numpy as np
```

Load the data:

```python
purchases = pd.read_csv("messy_purchases.csv")
```

The dataset is expected to include columns similar to:

```text
purchase_id
buyer_id
product_name
department
state
purchase_date
unit_price
quantity
supplier_note
```

## 2. Initial inspection

Before cleaning, inspect the data without changing it.

```python
purchases.head()
```

```python
purchases.tail()
```

```python
purchases.shape
```

```python
purchases.columns
```

```python
purchases.info()
```

Questions to consider:

```text
How many rows and columns are present?
Which columns have missing values?
Which numeric-looking columns are stored as object/text?
Are dates stored as datetime values or plain text?
Do the column names need cleanup?
```

### Inspect summary statistics

```python
purchases.describe()
```

Include text columns too:

```python
purchases.describe(include="all")
```

For numeric columns, `.describe()` shows values such as:

```text
count
mean
standard deviation
minimum
maximum
quartiles
```

For text columns, it can show:

```text
count
unique values
most common value
frequency of the most common value
```

## 3. Make a working copy

Preserve the original data.

```python
clean_purchases = purchases.copy()
```

Use `clean_purchases` for the remaining steps.

```text
raw data            → purchases
working clean copy  → clean_purchases
```

## 4. Inspect categorical columns

Categorical columns often hide spelling differences, placeholder values, and formatting problems.

```python
clean_purchases["state"].value_counts(dropna=False)
```

```python
clean_purchases["department"].value_counts(dropna=False)
```

```python
clean_purchases["product_name"].value_counts(dropna=False).head(10)
```

Inspect actual unique values:

```python
clean_purchases["state"].unique()
```

Look for problems such as:

```text
IL
il
IL 
Illinois
Unknown
N/A
```

## 5. Standardize column names

Clean column names before writing many expressions that depend on them.

```python
clean_purchases.columns = (
    clean_purchases.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
```

Example transformations:

```text
"Purchase Date"  → purchase_date
" Unit Price "   → unit_price
"Supplier Note"  → supplier_note
```

Check the result:

```python
clean_purchases.columns.tolist()
```

Rename individual columns when necessary:

```python
clean_purchases = clean_purchases.rename(columns={
    "qty": "quantity",
    "purchase_amt": "unit_price"
})
```

## 6. Standardize text values

Remove extra whitespace and standardize capitalization.

```python
clean_purchases["state"] = (
    clean_purchases["state"]
    .astype("string")
    .str.strip()
    .str.upper()
)
```

```python
clean_purchases["department"] = (
    clean_purchases["department"]
    .astype("string")
    .str.strip()
    .str.title()
)
```

```python
clean_purchases["product_name"] = (
    clean_purchases["product_name"]
    .astype("string")
    .str.strip()
)
```

Map long names or alternate spellings to standard values:

```python
clean_purchases["state"] = clean_purchases["state"].replace({
    "ILLINOIS": "IL",
    "WISCONSIN": "WI",
    "MINNESOTA": "MN"
})
```

Reinspect the categories:

```python
clean_purchases["state"].value_counts(dropna=False)
```

## 7. Replace placeholder values with missing values

The following values may mean “missing,” but pandas does not always recognize them automatically:

```text
"N/A"
"Unknown"
"not recorded"
""
-1
```

Replace placeholders carefully by column.

```python
clean_purchases = clean_purchases.replace({
    "state": {
        "N/A": pd.NA,
        "UNKNOWN": pd.NA,
        "": pd.NA
    },
    "department": {
        "N/A": pd.NA,
        "UNKNOWN": pd.NA,
        "": pd.NA
    },
    "unit_price": {
        "N/A": pd.NA,
        "": pd.NA,
        "-1": pd.NA
    },
    "purchase_date": {
        "N/A": pd.NA,
        "not recorded": pd.NA,
        "": pd.NA
    },
    "quantity": {
        -1: pd.NA
    }
})
```

Now count missing values:

```python
clean_purchases.isna().sum()
```

Count all missing cells:

```python
clean_purchases.isna().sum().sum()
```

Display rows with at least one missing value:

```python
clean_purchases[
    clean_purchases.isna().any(axis=1)
]
```

## 8. Clean and convert numeric data safely

A column such as `unit_price` may contain text like:

```text
"$19.99"
"1,250.00"
"N/A"
" 4.99 "
```

First remove currency symbols, commas, and extra whitespace:

```python
clean_purchases["unit_price"] = (
    clean_purchases["unit_price"]
    .astype("string")
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)
```

Then convert safely:

```python
clean_purchases["unit_price"] = pd.to_numeric(
    clean_purchases["unit_price"],
    errors="coerce"
)
```

`errors="coerce"` changes invalid values into missing values instead of stopping the notebook with an error.

Convert quantity:

```python
clean_purchases["quantity"] = pd.to_numeric(
    clean_purchases["quantity"],
    errors="coerce"
).astype("Int64")
```

Check types:

```python
clean_purchases.dtypes
```

Inspect suspicious values:

```python
clean_purchases[
    clean_purchases["unit_price"].isna()
]
```

## 9. Convert dates safely

Convert the purchase-date column:

```python
clean_purchases["purchase_date"] = pd.to_datetime(
    clean_purchases["purchase_date"],
    errors="coerce"
)
```

Invalid dates become `NaT`, pandas’s missing datetime value.

Check the result:

```python
clean_purchases["purchase_date"].dtype
```

```python
clean_purchases["purchase_date"].isna().sum()
```

```python
clean_purchases["purchase_date"].min()
```

```python
clean_purchases["purchase_date"].max()
```

Create useful date columns:

```python
clean_purchases["purchase_month"] = (
    clean_purchases["purchase_date"]
    .dt.to_period("M")
)
```

```python
clean_purchases["purchase_year"] = (
    clean_purchases["purchase_date"]
    .dt.year
)
```

## 10. Find and remove duplicate rows

Count exact duplicate rows:

```python
clean_purchases.duplicated().sum()
```

Display all members of duplicate groups:

```python
clean_purchases[
    clean_purchases.duplicated(keep=False)
]
```

Check whether purchase IDs are duplicated:

```python
clean_purchases.duplicated(
    subset=["purchase_id"]
).sum()
```

Show all records sharing a purchase ID:

```python
clean_purchases[
    clean_purchases.duplicated(
        subset=["purchase_id"],
        keep=False
    )
].sort_values("purchase_id")
```

After investigating the duplicates, remove exact copies:

```python
clean_purchases = clean_purchases.drop_duplicates()
```

If one purchase ID should appear only once, keep the first record:

```python
clean_purchases = clean_purchases.drop_duplicates(
    subset=["purchase_id"],
    keep="first"
)
```

Do not remove duplicates automatically without considering what a row represents.

## 11. Decide whether to fill or drop missing values

Not all missing values should be treated the same way.

| Column type          | Example decision                                                    |
| -------------------- | ------------------------------------------------------------------- |
| Purchase ID missing  | Drop or investigate; a record may not be traceable                  |
| Product name missing | Usually drop from product analysis                                  |
| State missing        | Keep and label `"Not Provided"` if the purchase is otherwise useful |
| Unit price missing   | Usually drop from revenue analysis                                  |
| Quantity missing     | Do not replace with zero unless missing truly means zero            |

Fill a category:

```python
clean_purchases["state"] = (
    clean_purchases["state"]
    .fillna("NOT PROVIDED")
)
```

Drop rows missing essential revenue fields:

```python
clean_purchases = clean_purchases.dropna(
    subset=[
        "purchase_id",
        "purchase_date",
        "unit_price",
        "quantity"
    ]
)
```

Check the remaining shape:

```python
clean_purchases.shape
```

## 12. Create useful columns

Calculate revenue for each purchase:

```python
clean_purchases["revenue"] = (
    clean_purchases["unit_price"]
    * clean_purchases["quantity"]
)
```

Create a low-quantity flag:

```python
clean_purchases["low_quantity"] = (
    clean_purchases["quantity"] < 2
)
```

Create a revenue category:

```python
clean_purchases["revenue_category"] = pd.cut(
    clean_purchases["revenue"],
    bins=[-1, 20, 100, float("inf")],
    labels=["Small", "Medium", "Large"]
)
```

Inspect the new columns:

```python
clean_purchases[
    [
        "product_name",
        "unit_price",
        "quantity",
        "revenue",
        "revenue_category"
    ]
].head()
```

## 13. Update only matching rows with `.loc[]`

Create a default discount rate:

```python
clean_purchases["discount_rate"] = 0.00
```

Apply a 10% discount to Office purchases:

```python
clean_purchases.loc[
    clean_purchases["department"] == "Office",
    "discount_rate"
] = 0.10
```

Apply a 15% discount to high-value purchases:

```python
clean_purchases.loc[
    clean_purchases["revenue"] >= 100,
    "discount_rate"
] = 0.15
```

Create discounted revenue:

```python
clean_purchases["discounted_revenue"] = (
    clean_purchases["revenue"]
    * (1 - clean_purchases["discount_rate"])
)
```

## 14. Drop unnecessary columns safely

Suppose `supplier_note` is not needed for analysis.

```python
analysis_purchases = clean_purchases.drop(
    columns=["supplier_note"],
    errors="ignore"
)
```

Using a new variable preserves `clean_purchases`.

Check the columns:

```python
analysis_purchases.columns.tolist()
```

## 15. Explore the cleaned dataset

Use `.info()` again after cleaning:

```python
analysis_purchases.info()
```

Use `.describe()` for numeric columns:

```python
analysis_purchases.describe()
```

Include text and categorical columns:

```python
analysis_purchases.describe(include="all")
```

Inspect revenue categories:

```python
analysis_purchases["revenue_category"].value_counts(
    dropna=False
)
```

Inspect revenue by state:

```python
analysis_purchases["state"].value_counts(
    normalize=True
).mul(100).round(1)
```

## 16. Filter with Boolean conditions

Find large purchases:

```python
analysis_purchases[
    analysis_purchases["revenue"] >= 100
]
```

Find Office purchases in Illinois:

```python
analysis_purchases[
    (analysis_purchases["department"] == "Office")
    & (analysis_purchases["state"] == "IL")
]
```

Find purchases that are in Illinois or Wisconsin:

```python
analysis_purchases[
    analysis_purchases["state"].isin(["IL", "WI"])
]
```

Select only useful report columns:

```python
analysis_purchases.loc[
    analysis_purchases["revenue"] >= 100,
    [
        "purchase_id",
        "product_name",
        "state",
        "department",
        "revenue"
    ]
]
```

## 17. Filter readably with `.query()`

Use `.query()` when conditions become long.

Find large Office purchases:

```python
analysis_purchases.query(
    "department == 'Office' and revenue >= 100"
)
```

Find purchases in selected states:

```python
analysis_purchases.query(
    "state in ['IL', 'WI'] and quantity >= 2"
)
```

Use Python variables inside `.query()` with `@`:

```python
target_state = "IL"
minimum_revenue = 50

analysis_purchases.query(
    "state == @target_state and revenue >= @minimum_revenue"
)
```

## 18. Sort results

Sort by revenue from largest to smallest:

```python
analysis_purchases.sort_values(
    "revenue",
    ascending=False
).head(10)
```

Sort by state, then by department, then by revenue:

```python
analysis_purchases.sort_values(
    by=["state", "department", "revenue"],
    ascending=[True, True, False]
)
```

Create a report of the highest-revenue purchases:

```python
top_purchases = (
    analysis_purchases
    .query("revenue >= 50")
    .loc[
        :,
        [
            "purchase_id",
            "product_name",
            "state",
            "department",
            "revenue"
        ]
    ]
    .sort_values("revenue", ascending=False)
)

top_purchases.head(10)
```

## 19. Group and summarize with `.groupby()`

Calculate total revenue by state:

```python
revenue_by_state = (
    analysis_purchases
    .groupby("state", as_index=False)
    .agg(
        purchase_count=("purchase_id", "count"),
        total_revenue=("revenue", "sum"),
        average_revenue=("revenue", "mean")
    )
    .sort_values("total_revenue", ascending=False)
)

revenue_by_state
```

Calculate revenue by state and department:

```python
revenue_by_state_department = (
    analysis_purchases
    .groupby(
        ["state", "department"],
        as_index=False
    )
    .agg(
        purchase_count=("purchase_id", "count"),
        total_revenue=("revenue", "sum"),
        average_revenue=("revenue", "mean"),
        largest_purchase=("revenue", "max")
    )
    .sort_values(
        ["state", "total_revenue"],
        ascending=[True, False]
    )
)

revenue_by_state_department
```

Each row now represents:

```text
one (state, department) group
```

## 20. Export the cleaned data

Reset the index if rows were dropped:

```python
analysis_purchases = analysis_purchases.reset_index(
    drop=True
)
```

Export the cleaned file:

```python
analysis_purchases.to_csv(
    "cleaned_purchases.csv",
    index=False
)
```

Export the summary report:

```python
revenue_by_state_department.to_csv(
    "revenue_by_state_department.csv",
    index=False
)
```

## 21. Final validation checklist

Before treating the dataset as clean, check:

```python
analysis_purchases.info()
```

```python
analysis_purchases.isna().sum()
```

```python
analysis_purchases.duplicated().sum()
```

```python
analysis_purchases["state"].value_counts(dropna=False)
```

```python
analysis_purchases["revenue"].describe()
```

Ask:

```text
Are essential columns complete?
Are prices numeric?
Are dates datetime values?
Are placeholder values gone?
Are duplicate rules appropriate?
Do state and department categories look standardized?
Are revenue values reasonable?
```

## 22. Lab questions

1. What were the original dimensions of the dataset according to `.shape`?

2. Which columns had missing values before cleaning?

3. Which placeholder values were replaced with `pd.NA`?

4. Which columns required type conversion? Why?

5. How many exact duplicate rows were found?

6. How many duplicated `purchase_id` values were found?

7. Which rows were dropped, and why were those fields considered essential?

8. Which state had the most purchases?

9. Which state generated the greatest total revenue?

10. Which `(state, department)` group generated the greatest total revenue?

11. What is the average purchase revenue for each department?

12. How many purchases have revenue of at least `$100`?

13. Write a `.query()` expression that finds Travel purchases in Illinois with revenue greater than `$50`.

14. Create a report of the ten highest-revenue purchases.

15. Explain why the following is safer than updating a filtered DataFrame directly:

```python
analysis_purchases.loc[
    analysis_purchases["revenue"] >= 100,
    "discount_rate"
] = 0.15
```

## 23. Optional challenge extensions

1. Create a `purchase_quarter` column from `purchase_date`.

2. Calculate total revenue by month.

3. Find the highest-revenue product in each department.

4. Create a Boolean `needs_review` column for purchases with revenue above the 95th percentile.

   ```python
   threshold = analysis_purchases["revenue"].quantile(0.95)
   ```

5. Make a bar chart of total revenue by department.

6. Compare revenue before and after discounts.

7. Create a compact data-quality report showing:

   - Original row count
   - Final row count
   - Missing values before cleaning
   - Missing values after cleaning
   - Duplicate rows removed

## 24. Core workflow

```text
Load
  ↓
Inspect
  ↓
Standardize text and placeholders
  ↓
Fix data types
  ↓
Handle missing values and duplicates
  ↓
Create useful columns
  ↓
Filter, sort, and summarize
  ↓
Validate and export
```

> Clean data is not just data with fewer rows. It is data whose values, types, categories, and assumptions have been inspected well enough to support trustworthy analysis.