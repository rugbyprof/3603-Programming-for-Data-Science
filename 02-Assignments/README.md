# 📂 Assignments Overview

The course modules, in the order you should work through them. Each module builds on the ones before it, so go **in order**, and finish a module's notebooks before starting the next.

New to the course? Complete the setup guide in [`01-StartHere/`](../01-StartHere/) first.

---

## 🗺️ Modules

| # | Module | Notebooks | What you'll learn |
|---|--------|:---------:|-------------------|
| 01 | [Scalar Types and Control Flow](01-Scalar_Types_and_Control_Flow/README.md) | 2 | `int`, `float`, `str`, `bool`, arithmetic, type casting, comparisons, and `if`/`elif`/`else` with logical operators |
| 02 | [Strings and Text](02-Strings_and_Text/README.md) | 3 | Strings as a sequence (indexing, slicing, immutability), string methods, and f-strings with format specs |
| 03 | [Python Containers](03-Python_Containers/README.md) | 3 | Lists (including 2D lists), tuples, and dictionaries, lists of dictionaries as table rows, and JSON/GeoJSON |
| 03b | [Containers → Functions](03b-Containers_to_Functions/README.md) | 6 | A slower second pass at containers through problems, the Accumulate/Count/Filter patterns, why functions exist, `print()` vs. `return`, and pipelines |
| 04 | [More Functions & Loops](04-More_Functions_and_Loops/README.md) | 3 | Default and keyword arguments, returning tuples, scope, `while`/`break`/`continue`, and reading files with `with` and `try`/`except` |
| 05 | [Foundations](05-Foundations/README.md) | 8 | The Jupyter/IPython toolkit: magics, notebook workflow, getting help, Markdown, files and paths, Pandas data I/O, NumPy and plotting, and timing |

### How the modules fit together

```text
01 → 02 → 03          Core Python: values, text, and containers
            ↓
           03b         Bridge: choosing containers and breaking problems into functions
            ↓
           04          The rest of functions and loops, plus reading files
            ↓
           05          Tools: Jupyter, help, Markdown, files, Pandas, NumPy, plotting, timing
```

Modules 01–04 teach the Python **language**. Module 05 switches to the **tools** you'll use for the data science work in the rest of the course.

---

## 📁 What's in Each Module Folder

Every module folder has the same layout:

| File | Purpose |
|------|---------|
| `README.md` | The module's notebooks, learning goals, and links to the modules before and after it |
| `01-…ipynb`, `02-…ipynb`, … | The notebooks, numbered in the order to complete them |
| `glossary.md` | Key terms for quick reference |
| `quiz.md` | A conceptual self-check with an answer key at the bottom |
| `worksheet.md` | Practice problems and "Explain It" reflection prompts |

Some modules include extras. 01 has a D2L question bank (`.csv`), and 05 has a hands-on `Foundations_Quiz.ipynb`.

### Inside each notebook

- **✅ Learning Goals** at the top tell you what you'll be able to do by the end.
- **✏️ / ✅ Your Turn** prompts give you something to try right away.
- **🏋️ Practice** problems go from easy to harder.
- An optional **🔥 Challenge** at the end is for when you want to push further. Skipping it won't hurt you later in the course.

---

## 📤 Submitting Your Work

- **Restart & Run All** before you submit a notebook, so you know it works from top to bottom (Module 05, notebook 02 explains why).
- In Module 05, most notebooks save the files you create into a matching `NN-OutputFiles` folder. Submit that folder along with the notebook.
- Copy finished notebooks into [`03-Completed/`](../03-Completed/), then commit and push. See [Part 6](../01-StartHere/Part-06.md) of the setup guide for the full workflow.

---

> Older versions of some modules (`04-Functions`, `05-Loops_and_Iteration`) are archived in [`04-Resources/Archive`](../04-Resources/Archive/) for extra reading.
