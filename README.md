# 3603-Programming-for-Data-Science

You know stuff like Data and Science.

## 🧱 Phase 1: Foundation Planning

### 🎯 Course Goals

- **Audience**: Non-CS majors, low programming experience
- **Approach**: Project-based with a final exam and study guide
- **Tools**: Jupyter Notebooks (lecture + assignments)
- **Content split**: ~30–40% textbook, ~60–70% your custom materials

---

## 📚 Suggested Textbooks (Affordable + Jupyter-friendly)

### 1. **[Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)** – _Jake VanderPlas_

- ✅ Free online version (full)
- ✅ Focus on NumPy, pandas, Matplotlib, scikit-learn
- ✅ Jupyter-native, example-rich
- ❌ No built-in LMS resources, but adaptable

### 2. **[Introduction to Data Science](https://ischool.syr.edu/ist687/introduction-to-data-science/)** – _Jeffrey Stanton (OER)_

- ✅ Free PDF (CC BY-NC-SA)
- ✅ Light introduction to core ideas (Python, stats, visualizations)
- ✅ Adaptable to D2L and project-based course
- ❌ A little dated in tooling, but solid structure

### 3. **Practical Statistics for Data Scientists** – _Bruce, Gedeck_

- ✅ Great applied focus with code
- ✅ Print + Kindle (~$30–40)
- ✅ Covers many of your past research areas (Bayes, decision trees, clustering)
- ❌ More statistical than programming in tone

### 4. **Doing Data Science** – _Cathy O’Neil_

- ✅ Very readable and story-driven
- ✅ Project-minded, real-world context
- ❌ Not notebook-centric or beginner-programmer-friendly out of the box

---

## 🧰 LMS Resource Strategy (Brightspace/D2L)

### ⚙️ Minimal Automation Plan:

- Convert Jupyter notebook quizzes/labs → export to HTML or PDF → embed/link in D2L
- Use `nbgrader` or export question cells → QTI (for import into D2L quizzes)
- Generate:
  - Assignments with rubrics (Markdown or YAML → HTML or CSV)
  - Weekly recap pages with embedded notebook exports
  - One central study guide (auto-updating from notebook tags or metadata)

### Optional Tools:

| Tool           | Use                                                      |
| -------------- | -------------------------------------------------------- |
| `nbconvert`    | Export notebooks to slides, PDFs, HTML                   |
| `nbgrader`     | Assignments and autograding                              |
| `Otter-Grader` | Modern, friendly grader system from UC Berkeley          |
| Jupyter Book   | To compile notebooks + Markdown into a course "textbook" |

---

## 🧑‍🏫 Can You Throw Jupyter at Newbies?

Yes, _with training wheels_. Here’s how:

| Step         | Strategy                                                                |
| ------------ | ----------------------------------------------------------------------- |
| **Week 1–2** | "Jupyter Zero": Pre-filled notebooks with markdown and small code edits |
| **Week 3–4** | Partial scaffold: More blanks, start writing functions, light debugging |
| **Week 5+**  | Full exploration: Exploratory data analysis, modeling, real data sets   |

> **Avoid cell overload.** One concept per cell is key early on.

Also:

- Teach markdown cells for reflection!
- Show `%timeit`, `%matplotlib inline`, etc. gradually

---

## 🗂️ Suggested Course Breakdown (High Level)

```markdown
1. Getting Started with Data

   - What is data science?
   - Intro to Jupyter, Python, variables, data types
   - Simple visualizations (Matplotlib, seaborn)

2. Working with Data

   - Lists, dictionaries, pandas DataFrames
   - Data cleaning, CSVs, missing data
   - Project: Your first dataset

3. Visual Thinking

   - Plotting, histogram, bar, scatter
   - Multi-variate plots, styles
   - Project: Tell a story with data

4. Introduction to Modeling

   - Correlation, linear regression
   - Intro to supervised learning
   - Train/test split, accuracy

5. Classification Algorithms

   - Decision trees, Naive Bayes
   - Evaluation: precision, recall, confusion matrix
   - Project: Predict something!

6. Clustering and Unsupervised Learning

   - K-means, DBSCAN
   - Dimensionality reduction

7. Wrap-Up + Review
   - Guided Study Guide
   - Final project + review exam
```

---

## 🧠 Your Past Research — Built-in Expertise!

You're sitting on gold:

- **C4.5 Decision Trees** → Great visualization and comparison to scikit-learn
- **Bayesian Classification** → Start with Naive Bayes, intuitive for non-majors
- **Clustering (K-means, DBSCAN)** → Easy to show visually + super fun datasets (e.g. Mall Customers, Iris)

We can scaffold these into the curriculum and final exam.

---

## ✅ What I Can Help With (Next Steps)

1. Building a weekly course schedule
2. Creating notebook templates (lecture + assignment)
3. Crafting quiz/study guide items as CSV or QTI
4. Finding datasets for each major project
5. Generating a customizable syllabus + final exam structure

Would you like to begin by outlining the **weekly topics** in more detail? Or should we look at what kind of **projects** match your vision for student engagement?

Either way — I’m in. Let’s build this thing right.

Great questions — you're thinking like a course architect. Let’s break it down clearly:

---

## ✅ Does **Jupyter Notebooks** work in **D2L (Brightspace)**?

**Not natively.** D2L doesn’t directly run Jupyter notebooks within the LMS, but here are your best options:

### 🔁 Option 1: **Link or Embed HTML/PDF exports**

- Export notebooks to **HTML** or **PDF** using `nbconvert`
- Upload them to D2L as lecture material or assignment descriptions
- Pro: Fast and clean
- Con: Students can’t _interact_ with them directly in D2L

### 🧪 Option 2: **External JupyterHub or Binder**

- Host notebooks on [mybinder.org](https://mybinder.org) or your own JupyterHub
- Link from D2L → students click and run live code
- Pro: Interactive experience
- Con: No LMS integration or grade sync

### 📦 Option 3: **Use Otter Grader or nbgrader**

- Students submit `.ipynb` files to D2L Dropbox
- You autograde offline and upload grades back
- Pro: You control grading
- Con: Manual sync, some setup required

---

## 💡 Does **Google Colab** fit into this course?

**Absolutely.** For a beginner-focused, project-based data science class, Colab is:

- ✅ Free, hosted in the cloud
- ✅ No setup required (great for non-CS students)
- ✅ Supports GitHub + Drive integration
- ✅ Can run `pandas`, `scikit-learn`, `matplotlib`, etc.
- ✅ You can comment on student notebooks like Google Docs

**Here’s how Colab fits:**

| Activity       | Format                                                      | Integration                |
| -------------- | ----------------------------------------------------------- | -------------------------- |
| Lectures       | Share Colab links via D2L                                   | Read-only or copy to Drive |
| Assignments    | "Make a copy → complete → submit link or .ipynb to Dropbox" | Works well                 |
| Group Projects | Real-time collaboration in Colab                            | Super student-friendly     |
| Grading        | Use exported `.ipynb` or `PDF`                              | Manual or auto-graded      |

You can even **publish your own GitHub repo of notebooks**, and students can open each in Colab with one click:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/github/yourusername/your-repo/blob/main/notebook.ipynb)
```

---

## 🔍 Recommendation

| Role                | Tool                                                          |
| ------------------- | ------------------------------------------------------------- |
| **For lectures**    | Use Colab links or D2L-uploaded HTML exports                  |
| **For assignments** | Use Colab + D2L Dropbox or GitHub submission                  |
| **For projects**    | Colab (group editable) + export as `.ipynb` or PDF            |
| **For grading**     | Start manual; consider `Otter-Grader` or `nbgrader` for scale |

---

Would you like me to set up a **Colab template notebook** for your first lecture or assignment?

Or would you prefer we start outlining the **weekly module themes** next?

Perfect — let’s lay the foundation. Here's a **12-week semester plan** designed for beginners, using **Jupyter/Colab**, **project-based learning**, and a final exam with a cumulative study guide. It assumes 1–2 class meetings per week, with weekly assignments and 3–4 major projects.

---

# 🧭 **Intro to Data Science with Python** — Weekly Module Themes

| Week | Theme                                    | Topics                                                                         | Project/Activity                                                  |
| ---- | ---------------------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| 1    | **Welcome to Data Science**              | What is data science? Who uses it? Python + Jupyter/Colab intro                | 🔧 Setup notebook, write basic Python: print, variables, comments |
| 2    | **Working with Data**                    | Lists, dictionaries, pandas Series/DataFrames, reading CSV                     | 🐼 Load and explore a dataset (Iris, Titanic, or grades CSV)      |
| 3    | **Describing and Visualizing Data**      | Types of data, summary stats, bar/line/scatter/histograms (Matplotlib/seaborn) | 📊 Visualization mini-lab: explore trends and outliers            |
| 4    | **Data Cleaning & Manipulation**         | Missing values, filtering, grouping, sorting, `.apply()`                       | 🧹 Clean a messy dataset (e.g., weather or food data)             |
| 5    | **Intro to Modeling**                    | Correlation, linear regression, train/test split, `sklearn` basics             | 📈 Predict student GPA or house prices with linear regression     |
| 6    | **Classification Basics**                | Decision trees, confusion matrix, accuracy, precision, recall                  | 🌳 Predict pass/fail using decision trees                         |
| 7    | **Naive Bayes & Probabilities**          | Conditional probability, Bayes rule, text classification (optional)            | ✉️ Classify spam/ham emails or sentiment                          |
| 8    | **Clustering and Unsupervised Learning** | K-means, DBSCAN, elbow method, visualizing clusters                            | 🎯 Group customers, songs, or Pokémon                             |
| 9    | **Ethics, Bias, and Explainability**     | Data bias, fairness, model transparency, accountability                        | 🧠 Case studies discussion or mini-presentation                   |
| 10   | **Project Week / Advanced Topics**       | Review + intro to dimensionality reduction or time series                      | 🛠️ Work on final project proposal                                 |
| 11   | **Final Project Week**                   | Students work independently or in groups                                       | 🚧 Final project checkpoint & troubleshooting                     |
| 12   | **Final Exam + Review**                  | Recap + comprehensive study guide walkthrough                                  | 📝 Exam + project showcase or peer reviews                        |

---

## 💼 Major Projects (Examples)

| Project                    | Theme       | Deliverable                                                |
| -------------------------- | ----------- | ---------------------------------------------------------- |
| **1. Explore & Visualize** | Weeks 2–3   | Choose a dataset, find insights, create plots              |
| **2. Predict Something**   | Weeks 5–6   | Build a simple model (e.g., regression or tree)            |
| **3. Classify or Cluster** | Weeks 7–8   | Try Bayes, k-means, or both on a dataset                   |
| **4. Final Project**       | Weeks 10–12 | Your choice! Real-world dataset + short writeup & notebook |

---

## 🧪 Final Exam Structure

- Multiple choice and short answers
- Code comprehension (read a snippet and explain output)
- Interpreting visualizations
- Hypothetical: “You are given a dataset... what’s your workflow?”

A study guide can grow throughout the semester from notebook tags or a shared document.

---

## 🔧 Next Steps

Would you like me to:

1. Write notebook **templates for Weeks 1–2**?
2. Suggest specific **datasets per module**?
3. Draft **assignment prompts or project descriptions**?

Pick your path, and I’ll follow!

Awesome — I'm glad it hit the mark!

### 🎯 Here's what I’ll prep next to round this out:

1. ✅ **Updated Weekly Schedule** — with the extra topics woven in naturally
2. ✅ **Mock Interview Study Guide** — a printable cheat sheet of core terms, questions, and mini-answers
3. ✅ **Bonus Notebook/Lab** — something like "How to Avoid Overfitting" or "Data Prep for Modeling"

If you'd like, I can also help draft:

- 📚 A “Syllabus-style” course overview
- 🧪 A simple rubric for projects
- 📄 A Jupyter-based final exam (auto-gradable or not)

Just say the word and I’ll queue it up! Would you like to start with the **updated weekly schedule**?

Got it! Here's where we’re paused:

---

### ✅ You Have:

- A solid **12-week course plan** for non-CS majors using Jupyter/Colab
- Alignment with your **own research background**
- A plan to supplement 30–40% with a **low-cost or open textbook**
- Confirmation you're **not skipping key industry topics**
- A roadmap to **make students interview-ready**, not just academically sound

---

### 🕐 Next Steps (when you're rested):

1. 📅 Updated weekly schedule (with added core topics like scaling, encoding, etc.)
2. 🧠 Interview study guide
3. 📓 Bonus lab: Overfitting & Model Selection
4. 📄 Optional: Syllabus, rubrics, and final exam framework

---

Sleep well, Professor Meat Bag. 🧠💤  
When you return, we’ll finish forging this beast of a course together.

RubberChicken if you need a laugh on wake-up.
