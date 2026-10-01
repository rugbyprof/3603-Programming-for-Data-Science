# Timing and Performance in Jupyter Notebooks

## 1. Goals

By the end, students should be able to:

- Measure how long code takes to run.
- Use `%time`, `%%time`, `%timeit`, and `%%timeit`.
- Compare Python loops with NumPy vectorized operations.
- Identify basic data-processing bottlenecks.
- Profile moderately slow code without jumping into advanced optimization.

## 2. Why measure performance?

Performance work should begin with evidence.

```text
Slow feeling → measure → identify bottleneck → improve → measure again
```

Do not optimize based only on what looks slow. A loop may be fine for 100 values and painful for 10 million; a rewrite that looks clever may not improve the real workload.

Useful questions:

- Which cell takes the longest?
- Which function takes the most time?
- Does runtime grow too quickly as data grows?
- Is the code repeatedly doing the same work?
- Can NumPy or pandas perform the operation in bulk?

## 3. Timing one expression with `%time`

Use `%time` for a single Python expression or statement.

```python
numbers = list(range(1_000_000))

%time total = sum(numbers)
```

Typical output includes CPU and wall-clock time:

```text
CPU times: user ..., sys: ...
Wall time: ...
```

Use `%time` when testing one reasonably substantial operation.

Example:

```python
import numpy as np

values = np.random.random(1_000_000)

%time average = np.mean(values)
```

## 4. Timing an entire cell with `%%time`

Use `%%time` on the first line of a cell to time everything in that cell.

```python
%%time

values = np.random.random(5_000_000)
squared = values ** 2
average = np.mean(squared)
```

This is useful for a short workflow containing several lines.

```text
%time     one statement or expression
%%time    every statement in one cell
```

## 5. Repeated timing with `%timeit`

Single timing results can vary because of:

- Other programs running
- Memory caching
- Background system work
- One-time setup costs

`%timeit` runs an expression repeatedly and reports a typical time.

```python
%timeit sum(range(1_000))
```

Compare two ways to create a list:

```python
%timeit [n * 2 for n in range(10_000)]
```

```python
%timeit list(map(lambda n: n * 2, range(10_000)))
```

`%timeit` chooses a repetition count automatically. Its output often looks like:

```text
1000 loops, best of 5: 120 µs per loop
```

Interpretation:

```text
1000 loops        Each trial repeated the code 1,000 times.
best of 5          Jupyter reported the best trial out of 5.
120 µs per loop    One execution took about 120 microseconds.
```

## 6. Timing a complete cell with `%%timeit`

Use `%%timeit` when the code needs multiple lines.

```python
%%timeit

values = list(range(100_000))
squares = [value ** 2 for value in values]
```

For a fair comparison, include equivalent work in both versions.

Poor comparison:

```python
# Setup is included here.
%%timeit
values = np.arange(1_000_000)
result = values ** 2
```

```python
# Setup is not included here.
%timeit values ** 2
```

Better comparison:

```python
values = np.arange(1_000_000)

%timeit values ** 2
```

or include setup consistently in both tests.

## 7. Python loops versus NumPy vectorization

NumPy arrays are designed for bulk numeric operations.

### Python-loop version

```python
numbers = list(range(1_000_000))

def square_with_loop(values):
    result = []
    for value in values:
        result.append(value ** 2)
    return result
```

```python
%timeit square_with_loop(numbers)
```

### NumPy vectorized version

```python
numbers_array = np.arange(1_000_000)

def square_with_numpy(values):
    return values ** 2
```

```python
%timeit square_with_numpy(numbers_array)
```

The NumPy version is often faster because the repeated work occurs in optimized compiled code rather than in a Python-level loop.

```text
Python loop:
    Python performs one iteration at a time.

NumPy vectorization:
    Python asks NumPy to process the full array in bulk.
```

## 8. Example: filtering data

### Python-loop filter

```python
scores = list(range(1_000_000))

def passing_scores_loop(values):
    result = []
    for score in values:
        if score >= 700_000:
            result.append(score)
    return result
```

### NumPy boolean-mask filter

```python
scores_array = np.arange(1_000_000)

def passing_scores_numpy(values):
    return values[values >= 700_000]
```

Time both:

```python
%timeit passing_scores_loop(scores)
```

```python
%timeit passing_scores_numpy(scores_array)
```

NumPy is usually faster for large numeric arrays, but the primary reason to use vectorization is not merely speed. It can also make the intended mathematical operation clearer.

## 9. Example: summary statistics

### Loop-based mean

```python
def mean_with_loop(values):
    total = 0
    for value in values:
        total += value
    return total / len(values)
```

### NumPy mean

```python
def mean_with_numpy(values):
    return np.mean(values)
```

```python
values_list = list(range(1_000_000))
values_array = np.array(values_list)

%timeit mean_with_loop(values_list)
%timeit mean_with_numpy(values_array)
```

## 10. Avoid repeated work

A common performance problem is recalculating the same expensive result.

Less efficient:

```python
for department in departments:
    department_sales = sales_data[sales_data["department"] == department]
    print(department, department_sales["amount"].sum())
```

Better: calculate grouped results once.

```python
sales_by_department = sales_data.groupby("department")["amount"].sum()

for department, total in sales_by_department.items():
    print(department, total)
```

The general question is:

```text
Am I recalculating the same filter, conversion, file read, or summary inside a loop?
```

## 11. Measure memory as well as time

Fast code can still be a problem if it creates too much data in memory.

For a NumPy array:

```python
values = np.arange(1_000_000)

values.nbytes
```

For a rough Python-object size:

```python
import sys

sys.getsizeof(values)
```

`sys.getsizeof()` does not always include all nested objects, so treat it as a starting point rather than a complete memory audit.

For pandas DataFrames:

```python
dataframe.info(memory_usage="deep")
```

A useful habit is to check:

```python
array.shape
array.dtype
array.nbytes
```

## 12. Basic profiling with `%prun`

Timing tells you how long a complete block takes. Profiling helps identify where time is spent inside functions.

```python
def calculate_total(values):
    total = 0
    for value in values:
        total += value ** 2
    return total

%prun calculate_total(range(1_000_000))
```

Look for:

- Functions called many times
- Functions with high cumulative time
- Repeated work inside loops

Use `%prun` after confirming that a larger block is actually slow. Profiling every two-line example is like bringing a metal detector to look for a paperclip.

## 13. Line-by-line profiling

For code that is slow inside one function, line profiling can be useful. It is often available through the `line_profiler` extension.

```python
%load_ext line_profiler
```

```python
%lprun -f calculate_total calculate_total(range(1_000_000))
```

If this extension is unavailable, use `%prun`, split the function into meaningful sections, and time those sections separately.

Line profiling is most useful when a function has several steps and `%prun` identifies the function but not the expensive line.

## 14. Monitoring repeated execution and notebook state

Notebook timing can be misleading when cells depend on old variables or cached outputs.

Good workflow:

```text
1. Restart the kernel.
2. Run setup cells.
3. Run the timing cell.
4. Repeat the measurement.
5. Record the typical result.
```

Do not accidentally time file loading in one version but not another unless file-loading performance is the question being studied.

Separate setup from the operation being tested:

```python
values = np.random.random(1_000_000)

%timeit np.sqrt(values)
```

This measures square-root computation, not array generation.

## 15. Reading and processing data efficiently

Useful intermediate-level improvements include:

### Read only needed columns

```python
import pandas as pd

sales = pd.read_csv(
    "sales.csv",
    usecols=["date", "department", "amount"]
)
```

### Specify data types when appropriate

```python
sales = pd.read_csv(
    "sales.csv",
    dtype={"department": "category", "amount": "float64"}
)
```

### Process very large files in chunks

```python
total_revenue = 0

for chunk in pd.read_csv("sales.csv", chunksize=100_000):
    total_revenue += chunk["amount"].sum()

total_revenue
```

### Avoid row-by-row DataFrame processing

Less efficient:

```python
for _, row in sales.iterrows():
    # process one row at a time
    pass
```

Prefer vectorized operations:

```python
sales["discounted_amount"] = sales["amount"] * 0.90
```

## 16. Comparing alternatives fairly

When comparing code versions:

- Use the same input size.
- Confirm both produce the same result.
- Exclude unrelated setup from both measurements.
- Run multiple trials.
- Compare representative data, not only toy examples.

Example:

```python
numbers = np.arange(1_000_000)

loop_result = [number ** 2 for number in numbers]
numpy_result = numbers ** 2

np.array_equal(np.array(loop_result), numpy_result)
```

Only compare performance after confirming that both approaches solve the same problem.

## 17. Practice problems

1. Use `%time` to measure how long it takes to sum one million integers.

2. Use `%timeit` to compare these expressions:

   ```python
   sum(range(10_000))
   ```

   ```python
   np.sum(np.arange(10_000))
   ```

   Explain why the result may differ when array creation is included or excluded.

3. Create a list of one million values. Write a loop that adds 10 to every value. Create an equivalent NumPy version, then time both.

4. Compare a Python loop and NumPy boolean masking to select values greater than 500,000.

5. Write a function with two loops. Use `%prun` to identify which part consumes the most time.

6. Load a CSV file containing several columns. Read it once normally, then again with `usecols`. Compare timing and memory use.

7. Create a NumPy array with one million values. Check its `shape`, `dtype`, and `nbytes`. Convert it to a different numeric type and compare memory use.

8. Given a DataFrame, replace an `iterrows()` calculation with a vectorized column operation.

9. Find a repeated calculation inside a loop and move it outside the loop. Use `%timeit` to compare the two versions.

10. Restart the kernel and rerun a timing comparison. Explain why restarting can make the results more trustworthy.

## 18. Core habit to remember

> Measure first, improve the bottleneck, and measure again.

Use `%time` for a quick one-time measurement, `%timeit` for reliable comparisons, NumPy vectorization for large numeric operations, and `%prun` when you need to identify the slow function inside a larger workflow.