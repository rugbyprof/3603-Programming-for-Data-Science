# CMPS 3603 Student Setup

## Part 5 — Use Jupyter Notebooks in Visual Studio Code

Jupyter notebooks combine executable Python code, formatted explanations, results, tables, and visualizations in one document. In this part, you will learn how to open, edit, run, inspect, validate, and save notebooks in Visual Studio Code.

The file extension for a Jupyter notebook is:

```text
.ipynb
```

---

## What You Will Accomplish

By the end of this part, you should be able to:

- open a notebook in the VS Code Notebook Editor;
- select the course `.venv` kernel;
- create, edit, move, and delete cells;
- distinguish code cells from Markdown cells;
- run individual cells and an entire notebook;
- inspect variables and data frames;
- interrupt and restart the kernel;
- recognize problems caused by running cells out of order;
- validate a notebook from a clean kernel; and
- save a notebook with useful output.

---

## 1. Open the Entire Course Repository

Always open the repository folder in Visual Studio Code—not merely one notebook file.

From a terminal:

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
code .
```

Or use **File → Open Folder** and select your `3603-data-science-[lastname]` folder.

Opening the entire repository allows VS Code to find:

- `.venv`;
- `requirements.txt`;
- course data files;
- notebook dependencies;
- Git configuration; and
- the complete project structure.

### Workspace Trust

Visual Studio Code may ask whether you trust the repository.

You may trust the course repository that you cloned from the instructor’s official URL. VS Code uses Workspace Trust to restrict code execution in unfamiliar folders. Do not automatically trust unrelated repositories downloaded from unknown sources. See [VS Code Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust).

A notebook contains executable code. Never select **Run All** in an unfamiliar notebook before reviewing what it does.

---

## 2. Confirm the Course Environment

Open a VS Code terminal.

Windows students should use Git Bash. Activate `.venv` if VS Code has not activated it automatically.

### Windows — Git Bash

```bash
source .venv/Scripts/activate
```

### macOS

```bash
source .venv/bin/activate
```

Verify the interpreter:

```bash
python -c "import sys; print(sys.executable)"
```

The path must contain the course repository’s `.venv` folder.

If `.venv` is missing or cannot be activated, return to Part 4 before opening course notebooks.

---

## 3. Open a Jupyter Notebook

In the VS Code Explorer:

1. Expand a course folder containing notebooks.
2. Select a file ending in `.ipynb`.
3. Wait for the Notebook Editor to load.

The notebook should appear as a sequence of cells rather than as raw JSON text.

VS Code provides notebook support through Microsoft’s Jupyter extension. The official [Jupyter Notebooks in VS Code guide](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) describes the editor, cells, variable viewer, plots, and related tools.

### If the Notebook Opens as JSON

1. Right-click the editor tab or notebook file.
2. Select **Reopen Editor With...** or **Open With...**.
3. Choose **Jupyter Notebook**.
4. If that option is absent, confirm that the Microsoft Jupyter extension is installed:

   ```text
   ms-toolsai.jupyter
   ```

5. Run **Developer: Reload Window** from the Command Palette and try again.

Do not edit the raw JSON representation of a notebook.

---

## 4. Select the `.venv` Kernel

The **kernel** is the Python process that executes notebook code.

1. Find the kernel selector in the upper-right corner of the notebook.
2. Select **Select Kernel** or the currently displayed kernel name.
3. Select `.venv` if it appears.
4. Otherwise, select **Select Another Kernel**.
5. Select **Python Environments**.
6. Choose the Python 3.13 interpreter inside the current repository’s `.venv`.

The correct path ends with:

### Windows

```text
.venv\Scripts\python.exe
```

### macOS

```text
.venv/bin/python
```

VS Code remembers recently selected kernels, but always verify the selection when changing computers, recreating `.venv`, or opening a notebook for the first time. See [VS Code’s kernel-selection guide](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).

### Verify from Inside the Notebook

Run this in a code cell:

```python
import sys
print(sys.executable)
```

The path must contain `.venv`.

The terminal environment and notebook kernel are related but separate selections. Activating `.venv` in a terminal does not guarantee that an already-open notebook changed kernels.

---

## 5. Understand Notebook Cells

A notebook is organized into cells.

The two cell types used most often in this course are:

| Cell type    | Purpose                                                           |
| ------------ | ----------------------------------------------------------------- |
| **Code**     | Python statements that the kernel executes                        |
| **Markdown** | Headings, explanations, lists, formulas, links, and documentation |

Code cells may produce output such as:

- text;
- numbers;
- tables;
- data frames;
- plots;
- images;
- warnings; and
- error messages.

Markdown cells do not execute Python. They render formatted text.

---

## 6. Create a Practice Notebook

Do not practice editing commands in a graded notebook.

1. Open the Command Palette.
2. Run **Create: New Jupyter Notebook**.
3. Save it in the repository root as:

   ```text
   notebook-practice.ipynb
   ```

4. Select `.venv` as its kernel.

This file is temporary and will be removed at the end of the tutorial.

---

## 7. Work with Code Cells

Enter this code in the first cell:

```python
import sys

print(sys.version)
print(sys.executable)
```

Run the cell using its triangular **Run Cell** button.

You may also use:

- `Shift+Enter` — run the cell and move to the next cell;
- `Ctrl+Enter` — run the cell and remain on it; or
- the notebook toolbar’s **Run All** command — run every code cell in order.

On macOS, VS Code may display platform-specific key symbols in menus and tooltips. The cell’s Run button works on every platform.

### Add a Code Cell

Use the **+ Code** control between cells or in the notebook toolbar.

Enter:

```python
numbers = [2, 4, 6, 8, 10]
sum(numbers)
```

Run the cell. The final expression is displayed as output.

### Edit and Rerun a Cell

Change the list and run the cell again:

```python
numbers = [1, 3, 5, 7, 9]
sum(numbers)
```

The displayed output is replaced by the new result.

Editing a cell does not automatically execute it. The kernel still remembers the result of the previous execution until the edited cell is run again.

---

# 8. Work with Markdown Cells

Add a Markdown cell using **+ Markdown**.

Enter:

```markdown
## CMPS 3603 Notebook Practice

This notebook demonstrates:

- Python code cells;
- Markdown documentation;
- NumPy arrays;
- Pandas data frames; and
- Matplotlib visualizations.

### Author

Your Name
```

Run or render the Markdown cell.

Useful Markdown syntax includes:

```markdown
# Main heading

## Section heading

### Subsection heading

**bold text**
_italic text_
`inline code`

- bulleted item
- another item

1. numbered item
2. another item

[link text](https://example.com)
```

Markdown should explain the reasoning, method, and conclusions—not merely decorate the notebook.

---

## 9. Add, Move, Change, and Delete Cells

When a cell is selected, VS Code displays controls for manipulating it.

Practice the following:

- add a code cell;
- add a Markdown cell;
- move a cell up;
- move a cell down;
- change a cell from Code to Markdown;
- change it back to Code; and
- delete the temporary cell.

The available controls may appear in the cell toolbar, notebook toolbar, or context menu depending on the VS Code version and window width.

Be careful when deleting cells. Undo immediately with `Ctrl+Z` on Windows or `Cmd+Z` on macOS if the wrong cell is removed.

---

## 10. Build a Small Data-Science Example

Add a code cell containing:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

Run it.

### Create an Array

Add and run:

```python
x = np.arange(1, 6)
y = x**2

x, y
```

### Create a Data Frame

Add and run:

```python
results = pd.DataFrame(
    {
        "x": x,
        "x_squared": y,
    }
)

results
```

Pandas data frames are displayed as formatted tables in notebook output.

### Create a Plot

Add and run:

```python
fig, ax = plt.subplots()
ax.plot(results["x"], results["x_squared"], marker="o")
ax.set_title("Squares")
ax.set_xlabel("x")
ax.set_ylabel("x squared")
ax.grid(True)
plt.show()
```

The chart should appear directly beneath the cell.

### Add a Validation Cell

Add and run:

```python
assert len(results) == 5
assert results.loc[4, "x_squared"] == 25

print("Practice notebook completed successfully.")
```

Assertions are useful for checking assumptions. If an assertion is false, Python stops and reports an error rather than silently continuing with an invalid result.

---

## 11. Understand Kernel State

The kernel keeps variables in memory until it is restarted or stopped.

Suppose one cell contains:

```python
course_name = "Programming for Data Science"
```

and a later cell contains:

```python
print(course_name)
```

The second cell works only after the first cell has run in the current kernel session.

### The Hidden-State Problem

Notebooks allow cells to be executed in any order. This can create a notebook that appears to work on one computer only because the kernel remembers earlier experiments.

For example:

1. You run a cell that defines `data`.
2. You delete or change that cell.
3. A later cell continues to use the old `data` variable still stored in memory.
4. You save the notebook.
5. Another person opens it with a fresh kernel, and it fails.

Saved output does not prove that the notebook runs correctly from a clean state.

The cure is simple:

> Restart the kernel and run every cell from top to bottom before considering the notebook complete.

---

## 12. Read Execution Indicators

Code cells display execution status or execution counts.

The indicator may show that a cell:

- has not been run;
- is waiting;
- is currently running;
- completed successfully; or
- ended with an error.

Execution counts can reveal that cells were run out of order. However, the most reliable test is still a clean kernel followed by **Run All**.

Do not assume a cell is running forever simply because a large operation takes time. Check the kernel status before repeatedly selecting Run.

Repeatedly starting the same expensive cell can make the problem worse.

---

## 13. Interrupt, Restart, and Clear Output

These operations solve different problems.

### Interrupt

Use **Interrupt** when a cell is taking too long, contains an infinite loop, or is performing an operation you want to stop.

Interrupting attempts to stop the current calculation while preserving other variables in memory.

### Restart

Use **Restart Kernel** when:

- variables contain confusing values;
- imports or package state changed;
- cells were run badly out of order;
- the kernel becomes unreliable; or
- you are performing final validation.

Restarting removes variables and imports from memory. It does not delete notebook cells or saved output.

### Clear Output

Clearing output removes displayed results from the notebook document. It does not undo computations or erase variables from the active kernel.

Use clear output when a cell accidentally prints thousands of lines or produces an unnecessarily large result.

Do not clear meaningful output immediately before submission unless the assignment says to do so. Tables, plots, and results help demonstrate that the notebook was executed.

VS Code places interrupt, restart, run-all, and output controls in the main Notebook Editor toolbar.

---

## 14. Inspect Variables and Data Frames

After running the practice notebook, select the **Variables** control in the notebook toolbar.

The Variable Explorer can display information such as:

- variable name;
- data type;
- size or shape; and
- current value or a summary.

Locate `results` and open it in the Data Viewer if that option is available.

The Data Viewer allows you to inspect, sort, and filter tabular values without changing the data frame in the notebook. This is a debugging and exploration tool; it does not replace code that performs required analysis.

Your submitted notebook should still contain the Python operations needed to reproduce the result.

---

## 15. Use Relative File Paths

Notebooks may read CSV, JSON, image, or other data files.

Avoid paths tied to one computer, such as:

```python
pd.read_csv("C:/Users/Alex/Desktop/data.csv")
```

or:

```python
pd.read_csv("/Users/alex/Desktop/data.csv")
```

Those paths will fail on another computer.

Use files stored in the repository and relative paths instead:

```python
from pathlib import Path

data_file = Path("data") / "example.csv"
data = pd.read_csv(data_file)
```

To inspect the notebook’s current working directory:

```python
from pathlib import Path

print(Path.cwd())
```

When a completed notebook is moved into the `Completed` folder, run it again from its final location. Moving a notebook can expose incorrect assumptions about file paths.

---

## 16. Save the Notebook

Save regularly with:

- Windows: `Ctrl+S`
- macOS: `Cmd+S`
- Menu: **File → Save**

A notebook saves:

- code cells;
- Markdown cells;
- cell order;
- notebook metadata;
- the selected kernel information; and
- displayed output, unless output has been cleared.

The live contents of kernel memory are not saved. Only code and displayed results are stored in the `.ipynb` file.

If you close a notebook with unsaved changes, VS Code should prompt you. Do not rely on the prompt as a substitute for saving.

---

## 17. Perform a Clean Top-to-Bottom Test

This is the most important notebook habit in the course.

For the practice notebook:

1. Save the notebook.
2. Select **Restart Kernel**.
3. Confirm the restart if prompted.
4. Select **Run All**.
5. Wait for every cell to finish.
6. Scroll from the first cell to the last.
7. Confirm that no cell displays an unhandled error.
8. Confirm that tables and plots appear where expected.
9. Confirm that the final validation message appears.
10. Save the notebook again.

Expected final message:

```text
Practice notebook completed successfully.
```

If the notebook fails after a restart, it was depending on hidden state or an incorrect execution order. Fix the notebook rather than merely rerunning cells until the error disappears.

---

## 18. Review Notebook Changes with Git

Save the practice notebook and open the VS Code Source Control view.

The file should appear as an untracked or changed file:

```text
notebook-practice.ipynb
```

Jupyter notebooks are stored internally as structured JSON. VS Code provides a notebook-aware comparison view that is easier to read than a raw JSON diff.

Select the changed notebook in Source Control to inspect its cells and output changes.

Large outputs can make notebooks and Git history unnecessarily large. Avoid:

- printing entire large datasets;
- displaying thousands of rows;
- embedding unnecessary high-resolution media;
- storing secrets in output; and
- leaving accidental diagnostic dumps in the final notebook.

Display enough output to support the analysis without turning the notebook into a data archive.

---

## 19. Remove the Practice Notebook

After completing the clean top-to-bottom test:

1. Close `notebook-practice.ipynb`.
2. In the VS Code Explorer, right-click only that practice file.
3. Select **Delete** or **Move to Trash**.
4. Confirm the exact filename before approving deletion.
5. Run:

   ```bash
   git status --short
   ```

If the practice notebook was never committed, it should no longer appear.

Do not delete a course notebook or the `Completed` folder.

---

## Notebook Completion Standard

Before a course notebook is considered complete, it should satisfy all of these conditions:

1. The correct `.venv` kernel is selected.
2. All required code and Markdown responses are present.
3. The notebook uses repository-relative paths rather than computer-specific paths.
4. The kernel has been restarted.
5. Every cell runs successfully from top to bottom.
6. Results, tables, and plots appear as expected.
7. No accidental debugging output remains.
8. No passwords, tokens, private keys, or personal secrets appear in code or output.
9. The notebook has been saved after the final run.
10. The notebook still runs after being placed in its final `Completed` location.

---

## Troubleshooting

### No Kernel Is Available

Confirm that `.venv` exists and contains `ipykernel`:

```bash
python -c "import sys; print(sys.executable)"
python -m pip show ipykernel
```

If necessary:

```bash
python -m pip install ipykernel
```

Then run **Developer: Reload Window** and reopen the kernel selector.

### The Wrong Kernel Keeps Returning

1. Select the kernel name in the notebook toolbar.
2. Choose **Select Another Kernel**.
3. Choose **Python Environments**.
4. Select the interpreter inside this repository’s `.venv`.
5. Verify it with:

   ```python
   import sys
   print(sys.executable)
   ```

If `.venv` was recently recreated, VS Code may temporarily display an obsolete interpreter entry. Select the entry whose path currently exists.

### `ModuleNotFoundError`

First check the notebook interpreter:

```python
import sys
print(sys.executable)
```

If it does not point to `.venv`, select the correct kernel.

If it does point to `.venv`, activate that environment in the terminal and reinstall the course requirements:

```bash
python -m pip install -r requirements.txt
python -m pip check
```

Do not install an unrelated package merely because its name resembles the missing import.

### `NameError: name ... is not defined`

The cell that creates the variable may not have run, may have failed, or may appear later in the notebook.

Restart the kernel and run the notebook from the beginning. If the error remains, correct the cell order or missing definition.

### A Cell Never Finishes

1. Wait briefly and check the kernel status.
2. Use **Interrupt** once.
3. Inspect the code for infinite loops, extremely large ranges, network requests, or very large data operations.
4. If interrupt does not recover the kernel, restart it.
5. Run cells individually until the problematic cell is identified.

Do not repeatedly select Run while the same cell is still executing.

### The Kernel Crashes or Restarts

Possible causes include:

- exhausting available memory;
- loading a dataset that is too large;
- incompatible compiled packages;
- a damaged `.venv`; or
- code that causes a native library to fail.

Record the cell and error information. Restart the kernel and run cells individually. If ordinary course code continues to crash, recreate `.venv` using Part 4.

### Output Is Stale or Contradicts the Code

The cell was edited after its output was produced, or cells were run out of order.

Restart the kernel, run all cells, and save again.

### A Plot Does Not Appear

Confirm that:

- the plotting cell completed without an error;
- the correct kernel is selected;
- Matplotlib was imported; and
- the cell ends with `plt.show()` when appropriate.

Example:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### A Data File Cannot Be Found

Inspect the working directory and requested path:

```python
from pathlib import Path

print(Path.cwd())
print(Path("data/example.csv").resolve())
print(Path("data/example.csv").exists())
```

Use repository-relative paths and confirm that the data file exists in the cloned repository.

### The Notebook Became Very Large

Look for cells that displayed:

- entire datasets;
- thousands of log lines;
- large embedded images; or
- repeated plot output.

Clear only the accidental oversized output, rerun the cell with a smaller display such as `data.head()`, and save again.

### VS Code Is in Restricted Mode

If you trust the instructor-provided repository:

1. Select the **Restricted Mode** indicator or banner.
2. Open **Manage Workspace Trust**.
3. Trust the current course folder.

Do not disable Workspace Trust globally.

### Notebook Changes Are Difficult to Read in Git

Open the notebook diff through VS Code’s Source Control view rather than opening the `.ipynb` file as text. Focus on changed cells and outputs.

---

## Final Skills Check

Before continuing, make sure you can perform each action without editing a graded notebook:

- open an `.ipynb` file in the Notebook Editor;
- select the repository’s `.venv` kernel;
- create code and Markdown cells;
- run one cell;
- run all cells;
- move and delete a cell;
- restart and interrupt the kernel;
- inspect a variable or data frame;
- save a notebook;
- inspect notebook changes in Source Control; and
- validate a notebook from a clean kernel.

---

## Completion Checklist

- [ ] I opened the complete repository folder in VS Code.
- [ ] I know how to open `.ipynb` files in the Notebook Editor.
- [ ] I selected the `.venv` kernel.
- [ ] I verified `sys.executable` from a notebook cell.
- [ ] I created and ran code cells.
- [ ] I created and rendered Markdown cells.
- [ ] I created a Pandas data frame and Matplotlib plot.
- [ ] I used the Variable Explorer or Data Viewer.
- [ ] I understand that kernel memory is not the same as saved notebook content.
- [ ] I know the difference between interrupt, restart, and clear output.
- [ ] I restarted the kernel and ran the practice notebook from top to bottom.
- [ ] I understand why absolute paths should not appear in submitted notebooks.
- [ ] I deleted only the temporary practice notebook.
- [ ] I did not modify a graded notebook while practicing.

Next: [**Part 6 — Complete, Organize, Commit, and Submit Notebook Work**](./Part-06.md)
