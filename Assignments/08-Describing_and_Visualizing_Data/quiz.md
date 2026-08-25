# 📝 Quiz: 08 - Describing and Visualizing Data

22 questions covering types of data, summary statistics, Matplotlib, Seaborn, and visualization/EDA concepts. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Types of Data

**1.** (Short Answer) Is eye color qualitative or quantitative? What about age?

**2.** (Multiple Choice) Which scale of measurement has a meaningful, "true" zero?
A) Nominal  B) Ordinal  C) Interval  D) Ratio

**3.** (Short Answer) Why is temperature in Celsius considered **Interval** rather than **Ratio**?

**4.** (True/False) Height is an example of discrete data.

**5.** (Short Answer) Why is shoe size usually treated as **Ordinal** rather than **Ratio**, even though it's numeric?

---

## Section B — Summary Statistics

**6.** (Short Answer) Which is more robust to outliers: the mean or the median? Why?

**7.** (Code Tracing) What prints?
```python
data = [1, 2, 3, 4, 100]
print(sorted(data)[len(data) // 2])  # a quick-and-dirty median for odd-length lists
```

**8.** (Short Answer) What does the IQR measure, and how is it computed?

**9.** (Multiple Choice) `ddof=1` in `np.var()`/`np.std()` is used for:
A) A full population  B) A sample

**10.** (Short Answer) What does a **positive** skew tell you about which tail of a distribution is longer?

**11.** (Short Answer) What do you get back from a single call to `df.describe()`?

---

## Section C — Matplotlib

**12.** (Short Answer) What's the difference between a `Figure` and an `Axes` in Matplotlib?

**13.** (Short Answer) Name the three Matplotlib functions that draw a line plot, a bar chart, and a histogram.

**14.** (Short Answer) What does `plt.legend()` require in order to display meaningful labels?

**15.** (Short Answer) Why might you use `ax.set_title()` instead of `plt.title()` when you're making multiple subplots at once?

---

## Section D — Seaborn

**16.** (Short Answer) What does the `hue` parameter do in a Seaborn plot?

**17.** (Multiple Choice) What's the current Seaborn argument for choosing the type of error bar shown (which replaced the older `ci=`)?
A) `errorbar=`  B) `error_type=`  C) `bars=`  D) `variance=`

**18.** (Short Answer) What does `sns.boxplot()` show you that a bar plot of the same data doesn't?

**19.** (Short Answer) Which Seaborn function overlays a smoothed density curve (KDE) on top of a histogram?

---

## Section E — Visualization and EDA

**20.** (Short Answer) What does a correlation heatmap show you at a glance?

**21.** (True/False) A strong correlation between two variables proves that one causes the other.

**22.** (Short Answer) Name at least two things every plot should include to follow good visualization practice.

---

## ✅ Answer Key

1. Eye color is qualitative (a category/label); age is quantitative (a measurable number).
2. **D** — Ratio.
3. Because 0°C doesn't mean "no temperature" — it's an arbitrary reference point (the freezing point of water), not a true absence of the thing being measured. Doubling from 10°C to 20°C isn't "twice as hot" in any physical sense.
4. **False** — height is continuous; it can take any value within a range, not just countable steps.
5. Shoe sizes are ordered and numeric, but the numbers are a manufacturer's labeling convention, not a direct physical measurement, and the gaps between sizes aren't strictly consistent or meaningful as ratios (a size 12 isn't "twice the shoe" of a size 6).
6. The median — a single extreme outlier can drag the mean far from the "typical" value, while the median only cares about the middle position and barely moves.
7. `3`
8. IQR (interquartile range) measures the spread of the middle 50% of the data: `IQR = Q3 - Q1` (the 75th percentile minus the 25th percentile).
9. **B** — a sample. (`ddof=1` corrects for the fact that a sample tends to slightly underestimate the true population variance; `ddof=0`, the default, assumes you already have the whole population.)
10. A positive skew means the **right** tail (toward larger values) is longer — most values cluster on the lower end, with a few large outliers stretching the tail rightward.
11. Count, mean, standard deviation, min, the 25/50/75th percentiles, and max — for every numeric column, all at once.
12. The `Figure` is the whole canvas/window; the `Axes` is one individual plot area within it (a figure can contain multiple axes/subplots).
13. `plot()` for lines, `bar()` for bar charts, `hist()` for histograms.
14. Every plotted line/series needs a `label=` argument when it's drawn — `plt.legend()` just collects and displays whatever labels were already set.
15. Each subplot has its own `ax` object; `ax.set_title()` sets the title for that *specific* subplot, while a single `plt.title()` call would only affect whichever axes was most recently active — not reliable once you have more than one.
16. It colors data points/bars by a categorical column, automatically assigning a distinct color to each category and adding a legend.
17. **A** — `errorbar=`.
18. The median, quartiles, and individual outlier points (drawn separately beyond the "whiskers") — a bar plot typically only shows one summary value (like the mean) plus a single error bar.
19. `sns.histplot()`, with `kde=True`.
20. The correlation coefficient between every pair of numeric variables at once, usually color-coded so strong positive/negative relationships are easy to spot visually.
21. **False** — correlation only shows a statistical association; it doesn't establish that one variable causes the other (there could be a third cause, coincidence, or reversed causation).
22. Any two of: a descriptive title, labeled axes (with units where relevant), a legend when multiple series/categories are shown, and readable font/size choices.
