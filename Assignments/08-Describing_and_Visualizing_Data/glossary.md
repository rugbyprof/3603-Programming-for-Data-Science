# 📘 Glossary: 08 - Describing and Visualizing Data

## 1️⃣ Types of Data
- **Quantitative Data**: Numeric values that can be measured (e.g. height, income).
- **Qualitative (Categorical) Data**: Non-numeric categories or labels (e.g. color, eye color).
- **Discrete Data**: Countable values (e.g. number of students).
- **Continuous Data**: Measurable values within a range (e.g. weight, time).
- **Nominal Data**: Categories without order (e.g. eye color).
- **Ordinal Data**: Ordered categories, but not evenly spaced (e.g. small, medium, large).
- **Interval Data**: Numeric, equal intervals, no true zero (e.g. temperature in °C).
- **Ratio Data**: Numeric, equal intervals, and a meaningful zero (e.g. height, weight).

## 2️⃣ Summary Statistics
- **Mean**: The arithmetic average of a dataset.
- **Median**: The middle value when data are ordered.
- **Mode**: The most frequent value in a dataset.
- **Range**: Difference between the maximum and minimum values.
- **Variance**: Measure of data spread around the mean.
- **Standard Deviation (σ)**: The square root of variance, in the original units.
- **`ddof`**: "Delta degrees of freedom" — `ddof=1` for a sample, `ddof=0` (the default) for a full population.
- **Quartiles & IQR**: Divide sorted data into quarters; IQR = Q3 − Q1.
- **Outlier**: A value significantly higher or lower than most of the data.
- **Skewness**: Measures asymmetry — which tail of the distribution is longer.
- **Kurtosis**: Measures "peakedness" and how heavy the tails are.

## 3️⃣ Matplotlib Basics
- **Matplotlib**: The core Python library for creating static plots.
- **Figure**: The overall window or page everything is drawn on.
- **Axes**: The individual plot area (contains x/y labels, ticks, etc.) within a figure.
- **`plot()`**: Draws line plots.
- **`bar()`**: Creates a bar chart.
- **`hist()`**: Displays a histogram of numeric data.
- **`scatter()`**: Creates a scatter plot for relationships between two variables.
- **`xlabel()`, `ylabel()`, `title()`, `legend()`**: Label and annotate a plot.

## 4️⃣ Seaborn Basics
- **Seaborn**: A visualization library built on Matplotlib, for attractive statistical graphics with less code.
- **`sns.barplot()`**: Displays a summary value (mean, by default) per category, with an error bar.
- **`sns.histplot()`**: Shows a distribution, with flexible bin control and an optional KDE overlay.
- **`sns.scatterplot()`**: Scatter plots with `hue`/style options for coloring by category.
- **`sns.boxplot()`**: Shows a distribution through quartiles and outliers.
- **`sns.heatmap()`**: Visualizes a matrix (often a correlation matrix) with color.
- **`errorbar`**: The current Seaborn argument for what kind of error bar to draw (e.g. `errorbar='sd'`). Older code/tutorials may show `ci=`, which was renamed.

## 5️⃣ Visualization and EDA
- **Trend**: A general direction or pattern visible in a chart.
- **Correlation**: A statistical relationship between two variables (positive, negative, or none) — not the same as causation.
- **Distribution**: The pattern of frequency of data points across their possible values.
- **Exploratory Data Analysis (EDA)**: The process of visually exploring a dataset to understand its main characteristics before formal analysis or modeling.
- **Visualization Best Practice**: Always label axes, include units, and give plots a readable title.
