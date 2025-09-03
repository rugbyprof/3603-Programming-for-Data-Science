# 3603-Programming-for-Data-Science

## 🧱 Phase 1: Foundation Planning

### 🎯 Course Goals

<!-- - **Audience**: Non-CS majors, low programming experience
- **Approach**: Project-based with a final exam and study guide
- **Tools**: Jupyter Notebooks (lecture + assignments)
- **Content split**: ~30–40% textbook, ~60–70% your custom materials -->

### Books Source

<a href="https://github.com/jakevdp"><img src="https://images2.imgbox.com/a5/09/MlsXoTxv_o.png" width="120"></a>

|                                  |                                   |
| :------------------------------: | :-------------------------------: |
| <img src="pdsh.png" width="100"> | <img src="awtop.png" width="100"> |

Using Jake VanderPlas’ Jupyter notebooks, I've developed a **14-week data science course** that is:

- beginner-friendly,
- steadily paced,
- and project-focused.

It integrates hands-on coding with conceptual understanding and light math intuition, ideal for young programmers or non-CS majors.

---

### 🗓️ **14-Week Data Science Course (VanderPlas-based)**

| **Week** | **Theme**                                       | **Topics**                                                                                                                                                        |
| -------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**    | **Getting Started with Data Science**           | - What is data science?<br>- Setting up Jupyter & IPython basics<br>- Python review: variables, data types, loops<br>- Help, magic commands, input/output history |
| **2**    | **Working with Arrays (NumPy)**                 | - NumPy arrays: creation & indexing<br>- Universal functions (ufuncs)<br>- Aggregation and broadcasting<br>- Fancy indexing, masks, filtering                     |
| **3**    | **Manipulating DataFrames (Pandas 1)**          | - Series & DataFrames<br>- Indexing & selection<br>- Operations & filtering<br>- Handling missing data                                                            |
| **4**    | **DataFrames Continued (Pandas 2)**             | - Combining datasets (merge, join, concat)<br>- GroupBy and aggregation<br>- Time series basics<br>- String operations                                            |
| **5**    | **Exploratory Data Analysis**                   | - Project: “Your First Dataset”<br>- Read CSV, clean, summarize<br>- Ask questions, answer with Pandas<br>- Light intro to `.query()` / `.eval()`                 |
| **6**    | **Plotting with Matplotlib**                    | - Line, scatter, bar, hist<br>- Subplots, colors, annotations<br>- Styles and config<br>- Errors, ticks, and legends                                              |
| **7**    | **Better Visuals with Seaborn**                 | - Categorical plots<br>- Pairplots, heatmaps<br>- Styling and palettes<br>- Multivariate plotting                                                                 |
| **8**    | **Project: Visual Storytelling**                | - Project: Tell a story with data<br>- Pick a topic (sports, music, etc.)<br>- Visual narrative using Matplotlib/Seaborn<br>- Present findings                    |
| **9**    | **Modeling: Regression**                        | - What is modeling?<br>- Correlation vs. causation<br>- Linear regression (scikit-learn)<br>- Train/test split, metrics                                           |
| **10**   | **Classification: Naive Bayes, Decision Trees** | - Supervised learning basics<br>- Naive Bayes intuition<br>- Decision Trees + feature importance<br>- Accuracy, confusion matrix                                  |
| **11**   | **Beyond Basics: SVMs and k-NN**                | - SVM intuition<br>- k-Nearest Neighbors<br>- Hyperparameters & validation<br>- Project: Classify your dataset                                                    |
| **12**   | **Unsupervised Learning**                       | - K-means clustering<br>- Principal Component Analysis (PCA)<br>- DBSCAN or Gaussian Mixture Models                                                               |
| **13**   | **Putting It Together**                         | - Face detection walkthrough OR mini project<br>- Model pipelines<br>- Final project planning<br>- Optional: Kernel Density Estimation                            |
| **14**   | **Final Project + Review**                      | - Final project presentations<br>- Study guide & course wrap-up<br>- Concept review & practice exam                                                               |

## 🗂️ **Proposed Repo Structure (Clean & Scalable)**

```
📁 Assignments/
├── 01-Getting_Started/
│   ├── 01-Colab_GettingStarted/
│   │   └── README.md (instructions)
│   ├── 02-GitHub_Colab_Workflow/
│   │   └── README.md
│   └── 03-Colab_Badge_Template/
│       └── README.md
├── 02-Intro_to_Python/
│   ├── 01-Variables_and_Types/
│   ├── 02-Lists_and_Strings/
│   └── 03-Dictionaries/
├── 03-Working_with_Data/
├── 04-Visualization/
├── 05-Modeling/
└── 06-Final_Project/
```

```
📁 Exams/
├── 01-Intro_to_Python/
│   └── (instructions or question bank)
├── 02-Data_Types/
├── 03-Midterm/
└── 04-Final/
```

---

## 🗓️ Step 1: **High-Level Schedule Framework**

We'll base this on a 14-week semester:

| Week | Focus Area                 | Assignment Folder             | Exam?     |
| ---- | -------------------------- | ----------------------------- | --------- |
| 1    | Getting Started            | 01-Getting_Started            | ❌        |
| 2    | Variables & Data Types     | 02-Intro_to_Python/01-...     | ❌        |
| 3    | Lists and Strings          | 02-Intro_to_Python/02-...     | ❌        |
| 4    | Dictionaries               | 02-Intro_to_Python/03-...     | ✅ Exam 1 |
| 5    | NumPy Basics               | 03-Working_with_Data/01-...   | ❌        |
| 6    | Pandas + DataFrames        | 03-Working_with_Data/02-...   | ❌        |
| 7    | Data Cleaning              | 03-Working_with_Data/03-...   | ✅ Exam 2 |
| 8    | Matplotlib + Seaborn       | 04-Visualization/             | ❌        |
| 9    | Storytelling with Data     | 04-Visualization/Project      | ❌        |
| 10   | Modeling Basics            | 05-Modeling/01-Regression     | ❌        |
| 11   | Classification Models      | 05-Modeling/02-Classification | ✅ Exam 3 |
| 12   | Clustering + PCA           | 05-Modeling/03-Unsupervised   | ❌        |
| 13   | Project Work               | 06-Final_Project              | ❌        |
| 14   | Final Presentations + Exam | 06-Final_Project              | ✅ Final  |

---

### 🧠 Course Notes

- **3 Mini-Projects**:

  - Week 5: First data analysis
  - Week 8: Visual narrative
  - Week 11: Classifier on student-chosen dataset

- **Final Project Ideas**:

  - Sports predictions
  - Spotify data trends
  - COVID or flu pattern analysis
  - Campus-related mini-research (cafeteria hours vs. attendance?)

- **Light Math Approach**: Focus on **intuition over derivation**, especially in modeling weeks.

- **Optional Deeper Topics**:
  - Kernel density estimation (Week 13)
  - 3D plotting and mapping (as bonus content)
