# 3603 — Programming for Data Science

Course materials for MSU Texas CS/DS 3603. Beginner-friendly, project-focused Python and data science, built around Jupyter notebooks and two open-source textbooks by Jake VanderPlas.

## 01 - Start here

New to the course? Work through **[`01-StartHere/`](01-StartHere/)** before touching an assignment — it's an 8-part guide covering everything from creating a GitHub account to submitting finished notebooks:

> **You will notice some OVERLAP between some of the Parts, if you've done it already, just skip it (e.g. git config --global blah blah blah)**

| Part                         | Covers                                                               |
| ---------------------------- | -------------------------------------------------------------------- |
| [0](01-StartHere/Part-00.md) | Checking what's already installed (Git, Python, VS Code, Conda)      |
| [1](01-StartHere/Part-01.md) | GitHub account + git identity                                        |
| [2](01-StartHere/Part-02.md) | Installing/repairing Git, Python 3.13, and VS Code                   |
| [3](01-StartHere/Part-03.md) | Creating and connecting your course repository (`upstream`/`origin`) |
| [4](01-StartHere/Part-04.md) | Python virtual environment + `requirements.txt`                      |
| [5](01-StartHere/Part-05.md) | Using Jupyter notebooks in VS Code                                   |
| [6](01-StartHere/Part-06.md) | Committing and submitting your work                                  |
| [7](01-StartHere/Part-07.md) | Maintaining your repo and troubleshooting git                        |
| [8](01-StartHere/Part-08.md) | Quick reference for the whole workflow                               |

Course dependencies (numpy, pandas, matplotlib, seaborn, scikit-learn, jupyter) live in [`01-StartHere/requirements.txt`](01-StartHere/requirements.txt).

This course runs entirely on a **local VS Code + venv + git** setup — not Colab or Codespaces.

## Repo structure

| Folder          | Subfolder | Description                                          |
| :-------------- | --------- | :--------------------------------------------------- |
| 01-StartHere/   |           | Setup guide (Parts 1–8) + requirements.txt           |
| 02-Assignments/ |           | Numbered course modules, 01–08 (see below)           |
| 03-Completed/   |           | Where your finished notebooks land after each module |
| 04-Resources    |           |                                                      |
|                 | Books/    | Source textbooks (VanderPlas), for reference/reading |
|                 | data/     | Shared datasets used across notebooks                |

## 02 - Assignments

Each module folder follows the same layout: numbered notebooks, a `README.md`, `glossary.md`, `mini_quiz.md`, and `worksheet.md`. Most notebooks end with an optional 🔥 Challenge section for extra practice.

| Module                                                                                   | Topic                                                                                          |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [01-Working_with_Data_Basic](02-Assignments/01-Working_with_Data_Basic/)                 | Lists, tuples, and dictionaries                                                                |
| [02-Scalar_Types_and_Control_Flow](02-Assignments/02-Scalar_Types_and_Control_Flow/)     | Scalar types, arithmetic, `if`/`elif`/`else`                                                   |
| [03-Strings_and_Text](02-Assignments/03-Strings_and_Text/)                               | Strings as a sequence type, string methods, f-strings                                          |
| [04-Functions](02-Assignments/04-Functions/)                                             | `def`, `return`, `*args`/`**kwargs`, type-based behavior                                       |
| [05-Loops_and_Iteration](02-Assignments/05-Loops_and_Iteration/)                         | `for`/`while` loops, `enumerate()`/`zip()`, reading files with `with`                          |
| [06-Foundations](02-Assignments/06-Foundations/)                                         | Jupyter/IPython tooling — magics, Markdown, file I/O, plotting basics, getting help, profiling |
| [07-Working_with_Data_Adv](02-Assignments/07-Working_with_Data_Adv/)                     | Pandas `Series`/`DataFrame`, loading and exploring real datasets                               |
| [08-Describing_and_Visualizing_Data](02-Assignments/08-Describing_and_Visualizing_Data/) | Summary statistics and visualization with Matplotlib/Seaborn                                   |

Modules 07 and 08 work entirely from local data files (in-folder or in [`data/`](data/)) — no network access required.

## 03 - Completed work

Copy your finished notebooks into [`Completed/`](Completed/) as you go — see [Part 6](01-StartHere/Part-06.md) of the setup guide for the commit/submit workflow.

## Books

Two open-source textbooks by [Jake VanderPlas](https://github.com/jakevdp) anchor the course content:

- **[Intro2Python](04-Resources/Books/Intro2Python/)** — _A Whirlwind Tour of Python_
- **[PythonDataScienceHandbook](04-Resources/Books/PythonDataScienceHandbook/)** — _Python Data Science Handbook_
