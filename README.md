# 3603 — Programming for Data Science

Course materials for MSU Texas CS/DS 3603. Beginner-friendly, project-focused Python and data science, built around Jupyter notebooks and two open-source textbooks by Jake VanderPlas.

## Start here

New to the course? Work through **[`_StartHere/`](_StartHere/)** before touching an assignment — it's an 8-part guide covering everything from creating a GitHub account to submitting finished notebooks:

| Part | Covers |
|------|--------|
| [1](_StartHere/Part-01.md) | GitHub account + git identity |
| [2](_StartHere/Part-02.md) | Installing/repairing Git, Python 3.13, and VS Code |
| [3](_StartHere/Part-03.md) | Creating and connecting your course repository (`upstream`/`origin`) |
| [4](_StartHere/Part-04.md) | Python virtual environment + `requirements.txt` |
| [5](_StartHere/Part-05.md) | Using Jupyter notebooks in VS Code |
| [6](_StartHere/Part-06.md) | Committing and submitting your work |
| [7](_StartHere/Part-07.md) | Maintaining your repo and troubleshooting git |
| [8](_StartHere/Part-08.md) | Quick reference for the whole workflow |

Course dependencies (numpy, pandas, matplotlib, seaborn, scikit-learn, jupyter) live in [`_StartHere/requirements.txt`](_StartHere/requirements.txt).

This course runs entirely on a **local VS Code + venv + git** setup — not Colab or Codespaces.

## Repo structure

```
_StartHere/       Setup guide (Parts 1–8) + requirements.txt
Assignments/       Numbered course modules, 01–08 (see below)
Books/             Source textbooks (VanderPlas), for reference/reading
data/              Shared datasets used across notebooks
Completed/         Where your finished notebooks land after each module
Exams/             Study guides
```

## Assignments

Each module folder follows the same layout: numbered notebooks, a `README.md`, `glossary.md`, `mini_quiz.md`, and `worksheet.md`. Most notebooks end with an optional 🔥 Challenge section for extra practice.

| Module | Topic |
|--------|-------|
| [01-Working_with_Data_Basic](Assignments/01-Working_with_Data_Basic/) | Lists, tuples, and dictionaries |
| [02-Scalar_Types_and_Control_Flow](Assignments/02-Scalar_Types_and_Control_Flow/) | Scalar types, arithmetic, `if`/`elif`/`else` |
| [03-Strings_and_Text](Assignments/03-Strings_and_Text/) | Strings as a sequence type, string methods, f-strings |
| [04-Functions](Assignments/04-Functions/) | `def`, `return`, `*args`/`**kwargs`, type-based behavior |
| [05-Loops_and_Iteration](Assignments/05-Loops_and_Iteration/) | `for`/`while` loops, `enumerate()`/`zip()`, reading files with `with` |
| [06-Foundations](Assignments/06-Foundations/) | Jupyter/IPython tooling — magics, Markdown, file I/O, plotting basics, getting help, profiling |
| [07-Working_with_Data_Adv](Assignments/07-Working_with_Data_Adv/) | Pandas `Series`/`DataFrame`, loading and exploring real datasets |
| [08-Describing_and_Visualizing_Data](Assignments/08-Describing_and_Visualizing_Data/) | Summary statistics and visualization with Matplotlib/Seaborn |

Modules 07 and 08 work entirely from local data files (in-folder or in [`data/`](data/)) — no network access required.

## Books

Two open-source textbooks by [Jake VanderPlas](https://github.com/jakevdp) anchor the course content:

- **[Intro2Python](Books/Intro2Python/)** — *A Whirlwind Tour of Python*
- **[PythonDataScienceHandbook](Books/PythonDataScienceHandbook/)** — *Python Data Science Handbook*

## Exams

[`Exams/Study_Guide/`](Exams/Study_Guide/) has topic-based study guides for exam prep.

## Completed work

Copy your finished notebooks into [`Completed/`](Completed/) as you go — see [Part 6](_StartHere/Part-06.md) of the setup guide for the commit/submit workflow.
