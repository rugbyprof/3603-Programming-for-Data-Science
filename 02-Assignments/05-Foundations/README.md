# 🏗️ Module 05: Foundations

This module moves beyond core Python and into the Jupyter/IPython tooling you'll use for the rest of the course. You'll learn how notebooks really work, how to get help on your own, how to document your work, how to load and save data in every common format, how to plot it, and how to measure performance.

Unlike the earlier language modules, this one is mostly about *tools*, not new language concepts. You'll learn by doing: every section has a **✅ Your Turn** prompt to try right away.

---

## 📚 Notebooks

Work through them **in order**. Each one builds on the ones before it.

1. [01-magic_commands.ipynb](01-magic_commands.ipynb) — IPython magics and shell commands: `%pwd`/`%cd`, `%whos`/`%reset`, `%debug`, `%%writefile`/`%run`, autoreload, `%pip`, `%%capture`/`%%html`/`%%markdown`, and `%lsmagic`.
2. [02-jupyter_shortcuts_and_workflow.ipynb](02-jupyter_shortcuts_and_workflow.ipynb) — Command vs. Edit mode, keyboard shortcuts, execution order, kernel state vs. notebook contents, **Restart & Run All**, `%history`/`%save`, saving, clearing, exporting, and structuring a notebook.
3. [03-using_help_and_docs.ipynb](03-using_help_and_docs.ipynb) — `?`, `??`, `help()`, tab completion and IntelliSense, `dir()`, reading function signatures and error messages, official docs, and a step-by-step help workflow.
4. [04-markdown_and_formatting.ipynb](04-markdown_and_formatting.ipynb) — Headings, lists, links, images, tables, line breaks, LaTeX math, escaping `$`, and generating Markdown from code.
5. [05-working_with_files_and_paths.ipynb](05-working_with_files_and_paths.ipynb) — Relative vs. absolute paths, `pathlib`, file modes and encoding, text/JSON/CSV files, and finding and managing files with `glob`.
6. [06-data_input_output.ipynb](06-data_input_output.ipynb) — Pandas: reading CSVs (including from a URL), exploring DataFrames, writing CSV/JSON/Excel, nested JSON, and **converting between formats**.
7. [07-plotting_basics.ipynb](07-plotting_basics.ipynb) — NumPy essentials, then Matplotlib: line, bar, scatter, histogram, box, and pie charts, subplots, saving charts, and choosing the right chart.
8. [08-timing_and_performance.ipynb](08-timing_and_performance.ipynb) — `%time`/`%timeit`, fair comparisons, loops vs. NumPy, repeated work, profiling with `%prun`, memory, and loading data efficiently.

Each notebook ends with a **🏋️ Practice** section (easy → harder) and an optional **🔥 Challenge**.

---

## 📦 Submitting Your Work

- **Restart & Run All** before you submit (notebook 02). A notebook that only works when cells are run out of order isn't finished.
- Most notebooks save the files you create into a matching **`NN-OutputFiles`** folder (for example, `05-OutputFiles`). **Upload that folder along with the notebook**, so your saved files, charts, and exports can be graded.
- Notebook 03 doesn't create any files, so it has no output folder.

---

## 🛠️ Setup Notes

- Everything runs in your course `.venv` from `_StartHere`, which includes NumPy, Pandas, and Matplotlib.
- **Notebook 06** reads a sample dataset from the web, so you need an internet connection. Its Excel section needs `openpyxl`, which you install from inside the notebook with `%pip install openpyxl`.
- **Notebook 08**'s optional line-by-line profiling section needs `line_profiler` (`%pip install line_profiler`).

---

## 📝 Assessment

- **[Foundations_Quiz.ipynb](Foundations_Quiz.ipynb)** — a hands-on practical quiz where you write and run real code, covering all 8 notebooks. It saves its files to `Quiz-OutputFiles`.
- **[quiz.md](quiz.md)** — a 45-question conceptual self-check with an answer key.
- **[glossary.md](glossary.md)** — key terms and definitions for quick reference, each tagged with the notebook that introduces it.
- **[worksheet.md](worksheet.md)** — one section per notebook, with practice problems and "Explain It" reflection prompts.

---

## 🚀 Workflow Reminder

This course uses local VS Code, `.venv`, and git/GitHub for everything. See `_StartHere` if you need a refresher on cloning, committing, and pushing your work. There's no Colab or Codespaces step in this course.

**Before this:** [04-More_Functions_and_Loops](../04-More_Functions_and_Loops/README.md)
