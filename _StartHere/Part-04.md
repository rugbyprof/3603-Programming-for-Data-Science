# CMPS 3603 Student Setup

## Part 4 — Create the Python Environment and Install Course Packages

In this part, you will create a project-specific Python virtual environment named `.venv`, install the packages listed by the course repository, and configure Visual Studio Code to use that environment for Python and Jupyter notebooks.

The environment belongs to this project and stays on your computer. It will not be uploaded to GitHub.

---

## What You Will Accomplish

By the end of this part, you should have:

- a `.venv` environment inside the course repository;
- Python 3.13 running inside that environment;
- the course packages from `requirements.txt` installed;
- `ipykernel` available for Jupyter notebooks;
- `.venv` excluded from Git tracking;
- `.venv` selected as the VS Code Python interpreter; and
- `.venv` selected as the VS Code notebook kernel.

---

# 1. Understand the Purpose of `.venv`

A Python virtual environment is an isolated Python installation for one project.

Your course environment will be stored here:

```text
3603-data-science-yourlastname/
├── .venv/
├── requirements.txt
├── Assignments/
├── Completed/
└── other course files
```

The `.venv` folder contains:

- a Python interpreter;
- `pip`;
- the packages needed by the course; and
- scripts used to activate the environment.

It does **not** contain your notebooks or other course work.

Python’s documentation describes virtual environments as isolated, disposable, and unsuitable for committing to source control. If an environment breaks, it should be recreated from `requirements.txt` rather than repaired package by package. See the official [`venv` documentation](https://docs.python.org/3/library/venv.html).

## One Repository, One Environment

For this course:

```text
Environment name: .venv
Package manager:  pip
Package list:     requirements.txt
```

Do not create several environments with names such as:

```text
venv
env
test-env
myenv
base
```

Do not use Conda for this repository.

---

# 2. Open the Course Repository

Open Visual Studio Code and open your local course folder.

If you are starting from a terminal, move into the repository using your actual folder name:

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
```

Then open it in VS Code:

```bash
code .
```

Open a new terminal in VS Code with **Terminal → New Terminal**.

Windows students must confirm that this is a **Git Bash** terminal rather than PowerShell.

Verify that the terminal is inside the repository:

```bash
pwd
git status
```

Check that the requirements file exists:

```bash
ls requirements.txt
```

Expected output:

```text
requirements.txt
```

If the file is not found, stop. You are probably in the wrong folder.

---

# 3. Confirm That Conda Is Not Active

Look at the beginning of the terminal prompt.

This indicates that Conda is active:

```text
(base) student@computer ...
```

If `(base)` or another Conda environment appears, deactivate it:

```bash
conda deactivate
```

Disable automatic base activation:

```bash
conda config --set auto_activate_base false
```

Close the terminal and open a new one. The `(base)` prefix should be gone before continuing.

Do not create `.venv` while a Conda environment is active. That produces an unnecessarily confusing environment whose base interpreter may not be the course Python installation.

---

# 4. Create `.venv`

Use the command for your operating system.

## Windows — Git Bash

```bash
py -V:3.13 -m venv .venv
```

This explicitly creates the environment with standard Python 3.13, even if other Python versions are installed.

## macOS

```bash
python3.13 -m venv .venv
```

The command may take a few seconds and may produce no output when successful.

## Confirm That the Folder Exists

Run:

```bash
ls -a
```

You should see `.venv` in the listing.

Do not manually place notebooks or other files inside `.venv`.

---

# 5. Activate `.venv`

Activation changes the terminal so that `python` and `pip` refer to the project environment.

Use the command for your operating system.

## Windows — Git Bash

```bash
source .venv/Scripts/activate
```

## macOS

```bash
source .venv/bin/activate
```

The prompt should now begin with:

```text
(.venv)
```

For example:

```text
(.venv) student@computer ...
```

If the prompt begins with both `(base)` and `(.venv)`, stop and deactivate both environments. Then close the terminal, open a new terminal, and activate only `.venv`.

---

# 6. Verify the Active Python Interpreter

After activation, the same verification commands work on Windows and macOS.

Check the version:

```bash
python --version
```

Expected output resembles:

```text
Python 3.13.x
```

Display the exact interpreter location:

```bash
python -c "import sys; print(sys.executable)"
```

The result must contain your repository’s `.venv` folder.

Windows output will resemble:

```text
C:\Users\student\Projects\3603-data-science-smith\.venv\Scripts\python.exe
```

macOS output will resemble:

```text
/Users/student/Projects/3603-data-science-smith/.venv/bin/python
```

If the path does not contain `.venv`, the environment is not active. Do not install packages until this check succeeds.

Verify `pip`:

```bash
python -m pip --version
```

Its displayed location must also be inside `.venv`.

---

# 7. Upgrade `pip` Inside `.venv`

Run:

```bash
python -m pip install --upgrade pip
```

This upgrades `pip` only inside the project environment.

Do not use:

```bash
sudo pip install ...
```

Do not install the course packages globally.

---

# 8. Install the Course Requirements

The repository contains `requirements.txt`, which lists packages needed for the course.

Install the complete list:

```bash
python -m pip install -r requirements.txt
```

Package installation may take several minutes. Lines of output will appear as packages are downloaded and installed.

Successful installation normally ends with a message beginning with:

```text
Successfully installed ...
```

Some packages may report:

```text
Requirement already satisfied
```

That is not an error. It means the required package is already present in `.venv`.

The `-r` option tells `pip` to install the package specifications from a requirements file. See the official [pip requirements instructions](https://pip.pypa.io/en/stable/getting-started/#install-multiple-packages-using-a-requirements-file).

## Do Not Overwrite `requirements.txt`

Do not run:

```bash
pip freeze > requirements.txt
```

The instructor’s requirements file defines the course environment. Students should not replace it with a list generated from one computer.

---

# 9. Ensure That `ipykernel` Is Installed

VS Code requires `ipykernel` to run the selected Python environment as a Jupyter notebook kernel.

Run:

```bash
python -m pip install ipykernel
```

If `ipykernel` was already included in `requirements.txt`, `pip` will report that the requirement is already satisfied.

The full Jupyter application does not need to be installed globally. VS Code’s Jupyter extension can use a Python environment when `ipykernel` is available. See [VS Code’s Jupyter kernel documentation](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).

---

# 10. Check the Installed Packages

Check for incompatible installed dependencies:

```bash
python -m pip check
```

Expected output:

```text
No broken requirements found.
```

Display the installed packages if you need to inspect them:

```bash
python -m pip list
```

Verify several packages commonly used in the course:

```bash
python -c "import numpy, pandas, matplotlib, seaborn, sklearn, ipykernel; print('Course packages imported successfully.')"
```

Expected output:

```text
Course packages imported successfully.
```

If this command reports a missing package, use the troubleshooting section before installing random packages individually.

---

# 11. Confirm That `.venv` Is Ignored by Git

The virtual environment contains many generated files and must not be uploaded to GitHub.

Ask Git whether a file inside `.venv` is ignored:

```bash
git check-ignore -v .venv/pyvenv.cfg
```

If the command prints an ignore rule and a path, `.venv` is ignored.

Also check repository status:

```bash
git status --short
```

The output should not list thousands of `.venv` files.

## If `.venv` Is Not Ignored

Open the repository’s root `.gitignore` file in VS Code and add:

```gitignore
# Local Python virtual environment
.venv/
```

Save `.gitignore`, then verify again:

```bash
git check-ignore -v .venv/pyvenv.cfg
git status --short
```

Only `.gitignore` should appear as a changed file. The `.venv` contents should not appear.

Do not use `git add -f` to force `.venv` into the repository.

---

# 12. Select `.venv` as the VS Code Python Interpreter

Visual Studio Code needs to know which Python interpreter belongs to the project.

1. Open the Command Palette:
   - Windows: `Ctrl+Shift+P`
   - macOS: `Cmd+Shift+P`
2. Run **Python: Select Interpreter**.
3. Choose the interpreter whose path contains the current repository and `.venv`.

The choice may be labeled:

```text
Python 3.13.x ('.venv': venv)
```

or may display a path ending in:

### Windows

```text
.venv\Scripts\python.exe
```

### macOS

```text
.venv/bin/python
```

The selected environment appears in the VS Code status bar. VS Code uses it for running Python, IntelliSense, debugging, and related language features. See [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments).

## If `.venv` Does Not Appear

1. Confirm that the repository folder—not merely one notebook—is open in VS Code.
2. Confirm that `.venv` exists in the repository root.
3. Open the Command Palette and run **Developer: Reload Window**.
4. Run **Python: Select Interpreter** again.
5. Choose **Enter interpreter path** if necessary and browse to the interpreter inside `.venv`.

---

# 13. Select `.venv` as the Jupyter Kernel

Open one of the course `.ipynb` files in Visual Studio Code.

1. Select **Select Kernel** in the upper-right corner of the notebook.
2. If `.venv` appears immediately, select it.
3. Otherwise, select **Select Another Kernel**.
4. Select **Python Environments**.
5. Choose the Python 3.13 environment whose path contains `.venv`.

VS Code remembers the selected kernel for the notebook.

Do not select:

- a global Python installation;
- Apple’s system Python;
- a Conda `base` environment;
- an environment from another course; or
- an interpreter whose path does not contain this repository’s `.venv`.

---

# 14. Test the Kernel Without Changing a Course Notebook

Create a temporary unsaved notebook:

1. Open the Command Palette.
2. Run **Create: New Jupyter Notebook**.
3. Select `.venv` as the kernel if it is not already selected.
4. Enter the following code in the first cell:

```python
import sys

import matplotlib
import numpy
import pandas
import seaborn
import sklearn

print(sys.version)
print(sys.executable)
print("Jupyter environment is ready.")
```

5. Run the cell.

The interpreter path printed by the notebook must contain `.venv`, and the final line should be:

```text
Jupyter environment is ready.
```

Close this temporary notebook without saving it. Do not use a graded course notebook as an environment test.

---

# 15. Deactivate and Reactivate the Environment

Deactivate the terminal environment:

```bash
deactivate
```

The `(.venv)` prefix should disappear.

Reactivate it when returning to the project.

## Windows — Git Bash

```bash
source .venv/Scripts/activate
```

## macOS

```bash
source .venv/bin/activate
```

VS Code may automatically activate the selected environment when it creates a new terminal. Even so, always confirm that the terminal prompt begins with `(.venv)` or verify `sys.executable` before installing packages.

---

# Normal Environment Workflow

Each time you work on the course:

1. Open the repository folder in VS Code.
2. Open a terminal.
3. Activate `.venv` if VS Code did not activate it automatically.
4. Confirm the notebook kernel is `.venv`.
5. Work on the notebook.
6. Deactivate the environment when finished if desired.

The environment does not need to be recreated each day.

---

# Repair a Broken Environment

The `.venv` directory is generated from Python and `requirements.txt`. It is disposable.

Recreate it when:

- it was created with the wrong Python version;
- it was copied or moved from another computer;
- the repository folder was moved and the environment stopped working;
- package installation was interrupted and left inconsistent results;
- VS Code persistently selects an interpreter that no longer exists; or
- the environment contains unexplained dependency conflicts.

## Safe Recreation Procedure

1. Save all notebooks and source files.
2. Close running notebook kernels.
3. Deactivate the environment:

   ```bash
   deactivate
   ```

4. Verify that the folder you intend to remove is exactly `.venv` inside the course repository.
5. Delete only the `.venv` folder using the VS Code Explorer or your operating system’s file manager.
6. Recreate it with the correct command.

### Windows — Git Bash

```bash
py -V:3.13 -m venv .venv
source .venv/Scripts/activate
```

### macOS

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

7. Reinstall packages:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   python -m pip install ipykernel
   python -m pip check
   ```

8. Select the recreated `.venv` interpreter and kernel in VS Code.

Deleting `.venv` does not delete notebooks or Git history, provided you delete only that exact generated folder.

---

# Troubleshooting

## `requirements.txt` Is Not Found

You are probably in the wrong folder.

Run:

```bash
pwd
ls
git status
```

Move to the repository root before installing:

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
```

## `No module named venv`

Confirm that you are using the course’s standard Python 3.13 installation.

### Windows

```bash
py -V:3.13 --version
```

### macOS

```bash
python3.13 --version
```

If the command fails, return to Part 2 and repair the base Python installation.

## Windows: `source .venv/Scripts/activate` Fails

Confirm all of the following:

- the terminal profile is Git Bash;
- the current folder is the repository root;
- `.venv` was created successfully; and
- the activation path uses `Scripts` with a capital `S`.

Inspect the folder:

```bash
ls .venv/Scripts
```

If you are in PowerShell, close that terminal and open Git Bash. Do not change PowerShell execution policy for this course workflow.

## macOS: `source .venv/bin/activate` Fails

Confirm the folder exists:

```bash
ls .venv/bin
```

If it does not, recreate `.venv` using `python3.13 -m venv .venv`.

## The Prompt Does Not Show `(.venv)`

Run:

```bash
python -c "import sys; print(sys.executable)"
```

The interpreter path is more reliable than the appearance of the prompt. If the path does not contain `.venv`, activate the environment again.

## Package Installation Reports `Permission denied`

Check the active interpreter:

```bash
python -c "import sys; print(sys.executable)"
```

If the path does not contain `.venv`, activate the environment before installing.

Do not solve the problem with `sudo`, administrator mode, or a global package installation.

## `No matching distribution found`

First verify the interpreter:

```bash
python --version
python -c "import sys; print(sys.executable)"
```

Confirm that it is standard Python 3.13 inside `.venv`, not a prerelease or free-threaded build.

Then upgrade `pip` and retry the requirements installation:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If the same package fails again, record the complete error and show it to the instructor. Do not substitute an arbitrary package version.

## macOS Reports an SSL Certificate Error

Open:

```text
/Applications/Python 3.13/
```

Run:

```text
Install Certificates.command
```

Then close and reopen the terminal, reactivate `.venv`, and retry.

## VS Code Shows the Wrong Kernel

1. Select the kernel name in the notebook’s upper-right corner.
2. Select **Select Another Kernel**.
3. Select **Python Environments**.
4. Choose the interpreter inside the repository’s `.venv`.

Verify from a notebook cell:

```python
import sys
print(sys.executable)
```

## VS Code Says `ipykernel` Is Missing

Activate `.venv` and run:

```bash
python -m pip install ipykernel
```

Reload VS Code and select the `.venv` kernel again.

## A Package Imports in the Terminal but Not the Notebook

The terminal and notebook are using different interpreters.

Compare:

### Terminal

```bash
python -c "import sys; print(sys.executable)"
```

### Notebook cell

```python
import sys
print(sys.executable)
```

Both paths must point into the same `.venv` folder.

## `git status` Lists Thousands of `.venv` Files

Do not stage or commit them.

Add this line to the repository’s root `.gitignore`:

```gitignore
.venv/
```

Then run:

```bash
git status --short
```

If `.venv` files were already staged, ask the instructor for help before continuing. Do not use a force-add command.

## The Terminal Shows `(base)` and `(.venv)`

Deactivate environments until both labels disappear:

```bash
deactivate
conda deactivate
```

Close the terminal, open a new terminal, verify that `(base)` is absent, and activate only `.venv`.

---

# Final Verification

With `.venv` activated, run:

```bash
python --version
python -c "import sys; print(sys.executable)"
python -m pip --version
python -m pip check
python -c "import numpy, pandas, matplotlib, seaborn, sklearn, ipykernel; print('Course environment is ready.')"
git check-ignore -v .venv/pyvenv.cfg
git status --short
```

Confirm that:

- Python reports version 3.13;
- the interpreter path contains `.venv`;
- `pip` is inside `.venv`;
- no broken requirements are reported;
- the import test succeeds;
- Git ignores `.venv`; and
- Git does not list `.venv` contents as changes.

---

# Completion Checklist

- [ ] I created `.venv` inside the course repository.
- [ ] I created it with standard Python 3.13.
- [ ] My terminal can activate `.venv`.
- [ ] `python` points inside `.venv` after activation.
- [ ] I upgraded `pip` inside `.venv`.
- [ ] I installed `requirements.txt` successfully.
- [ ] I installed or verified `ipykernel`.
- [ ] `python -m pip check` reports no broken requirements.
- [ ] The course-package import test succeeds.
- [ ] Git ignores `.venv`.
- [ ] VS Code uses `.venv` as its Python interpreter.
- [ ] VS Code uses `.venv` as its notebook kernel.
- [ ] A temporary notebook cell ran successfully.
- [ ] Conda is not active.

Next: [**Part 5 — Use Jupyter Notebooks in Visual Studio Code**](./Part-05.md)
