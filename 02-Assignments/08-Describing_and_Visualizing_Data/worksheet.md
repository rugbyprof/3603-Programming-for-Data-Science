# 📝 Worksheet: 08 - Describing and Visualizing Data

Use this worksheet to reinforce data types, summary statistics, and plotting with Matplotlib and Seaborn. Each section ends with an **🤖 Explain It** prompt — write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 📊 Section 1: Types of Data

1. Classify each as qualitative or quantitative: `movie genre`, `runtime in minutes`, `MPAA rating (G/PG/PG-13/R)`.  
   `Answer:` _______________________

2. Classify `runtime in minutes` further: discrete or continuous? What scale of measurement (Nominal/Ordinal/Interval/Ratio)?  
   `Answer:` _______________________

---

### ✏️ Task: Classify a Real Dataset

```python
# Using titanic.csv (or pokemon.csv) from the previous module:
# Pick 5 columns and classify each one: qualitative/quantitative,
# discrete/continuous (if quantitative), and its scale of measurement.
```

### 🤖 Explain It

In your own words: why does it matter whether a variable is Nominal vs. Ordinal before you compute anything with it? What could go wrong if you treated an Ordinal variable's categories as if they were evenly spaced numbers?

---

## 📈 Section 2: Summary Statistics

3. If a dataset's mean is much higher than its median, what does that suggest about the shape of the distribution?  
   `Answer:` _______________________

4. What's the difference between variance and standard deviation (besides the square root)?  
   `Answer:` _______________________

---

### ✏️ Task: Compare Center and Spread

```python
# Using penguins.csv:
# Compute the mean, median, and standard deviation of body_mass_g
# for each species separately. Which species has the most variation?
```

### 🤖 Explain It

In your own words: if two datasets have the same mean but very different standard deviations, what does that tell you about how they'd look different if you plotted them?

---

## 🎨 Section 3: Matplotlib

5. What's the minimum code needed to add a title and axis labels to a plot?  
   `Answer:` _______________________

6. Why would you use `fig, ax = plt.subplots()` instead of just calling `plt.plot()` directly?  
   `Answer:` _______________________

---

### ✏️ Task: Build a Multi-Line Plot

```python
# Plot y = sin(x), y = sin(2x), and y = sin(3x) on the same axes for
# x = np.linspace(0, 2*np.pi, 200). Give each line a distinct color and
# label, and add a legend, title, and axis labels.
```

### 🤖 Explain It

In your own words: why does a chart with no title, no axis labels, and no legend fail at its job even if the data plotted is correct?

---

## 🐧 Section 4: Seaborn

7. What does passing `hue='species'` to a Seaborn plot do that you'd otherwise have to do manually in Matplotlib?  
   `Answer:` _______________________

8. When would you reach for `sns.boxplot()` instead of `sns.histplot()`?  
   `Answer:` _______________________

---

### ✏️ Task: Compare Groups Visually

```python
# Using penguins.csv:
# Make a boxplot of bill_depth_mm grouped by species.
# In a comment, note which species has the widest spread (tallest box + whiskers).
```

### 🤖 Explain It

In your own words: what's the practical difference between `sns.barplot()` (which shows one summary number per group) and `sns.boxplot()` (which shows the whole distribution per group)? When would the bar plot hide something the box plot reveals?

---

## 🔬 Section 5: Visualization and EDA

9. What does a correlation heatmap help you spot that would be hard to see by reading raw numbers in a table?  
   `Answer:` _______________________

10. Why is "correlation is not causation" an important caveat when reading a heatmap?  
    `Answer:` _______________________

---

### ✏️ Task: Full Mini-Analysis

```python
# Using penguins.csv:
# 1. Make one plot showing a trend (a relationship between two variables).
# 2. Make one plot showing possible outliers.
# 3. Make a correlation heatmap of the numeric columns.
# Write 2-3 sentences summarizing what you found.
```

### 🤖 Explain It

In your own words: what's the difference between Exploratory Data Analysis (EDA) and just "making some charts"? What's the actual goal of the exploring part?

---

## 🧾 Submit Checklist

- [ ] I classified at least 5 real variables by qualitative/quantitative, discrete/continuous, and scale of measurement.
- [ ] I computed mean, median, and standard deviation for a real column, and compared groups.
- [ ] I built a labeled, titled Matplotlib plot with a legend.
- [ ] I built at least 2 different Seaborn plot types (scatter, bar, hist, box) on the same dataset.
- [ ] I built a correlation heatmap and identified the strongest relationship.
- [ ] I completed the "Explain It" prompts in my own words.
