# CMPS 3603 Student Setup

## Part 8 — Setup and Submission Quick Reference

Use this page after completing Parts 1–7. It is a compact reminder, not a replacement for the detailed instructions and troubleshooting guides.

> **Course:** CMPS 3603 Programming for Data Science  
> **Instructor repository:** <https://github.com/rugbyprof/3603-Programming-for-Data-Science>  
> **Student repository:** `3603-data-science-YOURLASTNAME`  
> **Student repository visibility:** Public  
> **Course environment:** Python 3.13 in `.venv`  
> **Windows terminal:** Git Bash

---

## The Complete Workflow

```text
Instructor repository (upstream)
              ↓ fetch and merge
       Your local repository
              ↓ work in a copy
      Work → Completed
              ↓ save and commit
        Local Git history
              ↓ push when instructed
Your public repository (origin)
              ↓ report its URL
     Course registration form
```

---

## 1. Accounts and Required Software

### GitHub Account

- Create a personal account at <https://github.com/signup>.
- Verify the email address.
- Enable two-factor authentication.
- Save the recovery codes somewhere safe.
- Record the exact GitHub username.

### Required Software

- [Git](https://git-scm.com/downloads)
- [Python 3.13](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/Download)
- VS Code **Python** extension from Microsoft
- VS Code **Jupyter** extension from Microsoft

Do not install Anaconda or Miniconda for this course. If Conda is already installed, make sure `(base)` is not active while working in the course repository.

### Terminal

| System  | Use                                 |
| ------- | ----------------------------------- |
| Windows | Git Bash inside VS Code             |
| macOS   | The regular terminal inside VS Code |

---

## 2. Configure Git Identity Once

Replace the sample values with your real name and the email associated with GitHub:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify them:

```bash
git config --global --get user.name
git config --global --get user.email
```

These values become the author information recorded in your commits. They are separate from your GitHub username and password.

---

## 3. Verify the Installation

## Windows — Git Bash

```bash
git --version
py -3.13 --version
code --version
```

### macOS

```bash
git --version
python3.13 --version
code --version
```

Each command should display a version. Fix missing commands before continuing.

---

## 4. Create the Student Repository on GitHub

Create one **empty public repository** named:

```text
3603-data-science-YOURLASTNAME
```

Example:

```text
3603-data-science-smith
```

When creating it, do **not** add a README, `.gitignore`, or license. The course repository already supplies the starting files.

Your repository URL will resemble:

```text
https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
```

---

## 5. Clone and Connect the Course Repository

Choose a location such as `Projects`, and then run these commands in Git Bash on Windows or Terminal on macOS:

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/rugbyprof/3603-Programming-for-Data-Science.git 3603-data-science-YOURLASTNAME
cd 3603-data-science-YOURLASTNAME
git remote rename origin upstream
git remote add origin https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
git remote -v
```

Replace both placeholders:

- `YOURLASTNAME` with your last name;
- `YOUR-USERNAME` with your GitHub username.

The final remote list should show:

```text
origin    https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
upstream  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git
```

The names have specific meanings:

| Remote     | Repository                         |
| ---------- | ---------------------------------- |
| `origin`   | Your public student repository     |
| `upstream` | The instructor's course repository |

Push the initial course files when instructed:

```bash
git push -u origin main
```

Open the complete folder in VS Code:

```bash
code .
```

---

## 6. Create the Python Environment Once

Run these commands from the repository root.

### Windows — Git Bash

```bash
py -3.13 -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install ipykernel
```

### macOS

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install ipykernel
```

When activated, the terminal prompt normally begins with:

```text
(.venv)
```

Verify the environment:

```bash
python --version
python -m pip --version
```

The Python and `pip` locations should be inside `.venv`.

Never commit `.venv`. If it is missing or broken, recreate it from `requirements.txt`.

---

## 7. Select the VS Code Interpreter and Kernel

### Python Interpreter

1. Open the Command Palette with `Ctrl+Shift+P` on Windows or `Cmd+Shift+P` on macOS.
2. run **Python: Select Interpreter**;
3. select the interpreter inside `.venv`.

### Notebook Kernel

1. open a course `.ipynb` file;
2. select **Select Kernel** in the upper-right corner;
3. choose **Python Environments**; and
4. select the `.venv` interpreter.

Typical paths are:

```text
Windows: .venv\Scripts\python.exe
macOS:   .venv/bin/python
```

---

## 8. Start a Normal Work Session

Open the repository, activate `.venv`, and inspect Git before editing.

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
code .
git status
git branch --show-current
git remote -v
```

### Windows — Activate `.venv`

```bash
source .venv/Scripts/activate
```

### macOS — Activate `.venv`

```bash
source .venv/bin/activate
```

Confirm all of the following:

- the branch is `main`;
- `origin` points to your GitHub account;
- `upstream` points to `rugbyprof`;
- you understand every change reported by `git status`; and
- the notebook kernel is `.venv`.

---

## 9. Receive Instructor Updates

First save and commit your current work. Begin the update only when `git status` reports a clean working tree.

Fetch without changing your files:

```bash
git fetch upstream
```

Inspect incoming commits:

```bash
git log --oneline HEAD..upstream/main
git diff --stat HEAD..upstream/main
```

Merge the update:

```bash
git merge upstream/main
```

The shorter alternative is:

```bash
git pull upstream main
```

Use the explicit fetch-and-merge sequence when you want to inspect an update before applying it.

Do not use VS Code **Sync Changes** for instructor updates. This course repository has two remotes, so explicit commands make the direction clear.

---

## 10. Complete an Assigned Notebook

Do not edit the only instructor-provided copy.

1. Copy the assigned `.ipynb` file into `Work`.
2. Keep its original filename unless instructed otherwise.
3. Open the copy from `Work`.
4. confirm that the selected kernel is `.venv`;
5. complete every requested code and Markdown cell;
6. save frequently; and
7. use relative paths for data files.

When the notebook is finished:

1. restart the kernel;
2. run every cell from top to bottom;
3. confirm that no cell reports an error;
4. confirm that plots, tables, and answers appear;
5. save the final outputs; and
6. move the finished notebook from `Work` to `Completed`.

Run the notebook again from its final location when relative file paths may be affected by the move.

```text
Instructor copy → Work → Completed
```

---

## 11. Commit a Local Checkpoint

You may commit locally throughout the assignment even when you have not been told to push.

Review the work:

```bash
git status
git diff --stat
```

Stage only the intended notebook or folder:

```bash
git add Completed/path/to/notebook.ipynb
```

Review the staged files:

```bash
git diff --cached --stat
git status
```

Commit them with a meaningful message:

```bash
git commit -m "Complete data-cleaning notebook"
```

Good messages describe the work. Avoid messages such as `stuff`, `update`, or `final final`.

Remember:

```text
Save → Stage → Commit → Push
```

A commit stays on your computer. A push publishes it to your public GitHub repository.

---

## 12. Push When Instructed

Before pushing, remember that the student repository is public. Do not publish passwords, access tokens, private data, answer keys, or work that the instructor has told you to keep local.

Inspect the unpublished commits and files:

```bash
git fetch origin
git log --oneline origin/main..HEAD
git diff --stat origin/main..HEAD
git status
git remote -v
```

Confirm that `origin` belongs to you. Then push:

```bash
git push origin main
```

Afterward, open your repository on GitHub and verify that:

- the newest commit appears;
- the completed notebook is inside `Completed`;
- the notebook opens and displays its final outputs; and
- no unintended files were published.

Do not assume that a successful local commit is a submitted assignment.

---

## 13. Register the Repository

Complete the course registration form provided by the instructor. Enter the exact requested information, including:

- your name;
- GitHub username;
- full public repository URL;
- repository name; and
- other requested course usernames, such as Discord.

Copy the repository URL from the browser instead of typing it from memory. Test it in a private or signed-out browser window to confirm that the public repository is visible.

---

## 14. End a Normal Work Session

Before closing VS Code:

```bash
git status
git log -1 --oneline
```

Confirm that:

- every notebook is saved;
- intended progress has been committed;
- no unexpected files are staged;
- `.venv` is not listed by Git; and
- you know whether the latest commits are local only or already pushed.

Deactivate the environment if desired:

```bash
deactivate
```

---

## 15. Work from Another Computer

On the first computer, save, commit, and push all permitted work before switching.

On the other computer:

```bash
git pull origin main
```

Never copy `.venv` between computers. Recreate it from `requirements.txt`.

If your unpushed work remains on the first computer, it will not appear on the second computer.

---

## Fast Troubleshooting

### `python`, `git`, or `code` Is Not Found

- Close and reopen the terminal after installation.
- On Windows, use Git Bash and try `py -3.13 --version`.
- On macOS, try `python3.13 --version`.
- Revisit Part 2 if the command still fails.

### The Notebook Has No Kernel

Activate `.venv`, install `ipykernel`, and select `.venv` again:

```bash
python -m pip install ipykernel
```

### `ModuleNotFoundError`

Make sure the notebook uses `.venv`, then install the course requirements:

```bash
python -m pip install -r requirements.txt
```

### `fatal: not a git repository`

You are in the wrong folder. Move into the repository:

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
git status
```

### A Push Is Rejected

Do not force-push. Fetch the student repository and inspect the situation:

```bash
git fetch origin
git status
git log --oneline --graph --decorate --all -15
```

If you used another computer or edited on GitHub, you may need:

```bash
git pull origin main
git push origin main
```

If Git reports a conflict, stop and resolve it carefully before pushing.

### An Instructor Update Causes a Conflict

- Do not delete files merely to silence Git.
- Do not force-push.
- For a text file, use VS Code's Merge Editor and review the final result.
- For a notebook conflict, preserve copies of both versions and ask for help.
- If the merge has not been committed and you need to return to the pre-merge state, the instructor may direct you to use `git merge --abort`.

### `.venv` Files Appear in `git status`

Do not commit them. Confirm that `.gitignore` contains:

```gitignore
.venv/
```

Ask for help if `.venv` has already been committed.

### GitHub Authentication Fails

- Confirm that `origin` contains your username.
- Complete the browser sign-in prompt if it appears.
- GitHub account passwords are not accepted as Git passwords.
- In VS Code, open **View → Output**, then choose **Git** for the detailed error.

### Collect Safe Diagnostic Information

When asking for help, copy the output of:

```bash
git status
git branch --show-current
git remote -v
git log --oneline --graph --decorate --all -15
python --version
python -m pip --version
```

Do not share passwords, tokens, recovery codes, or private keys.

---

## Commands to Avoid Without Instructor Guidance

Do not try random destructive commands from search results. In particular, pause before using:

```bash
git push --force
git reset --hard
git clean -fd
git rebase
```

An error message is useful evidence. Preserve it and ask for help before destroying the state that produced it.

---

## Submission Checklist

- [ ] I worked in a copy of the instructor notebook.
- [ ] The finished notebook is inside `Completed`.
- [ ] The `.venv` kernel is selected.
- [ ] I restarted the kernel and ran every cell from top to bottom.
- [ ] Every required answer, plot, table, and final output is visible.
- [ ] The notebook runs without errors from its final location.
- [ ] I saved the notebook after the final run.
- [ ] I reviewed `git status` and the staged files.
- [ ] I committed the intended work with a meaningful message.
- [ ] I checked the unpublished commits before pushing.
- [ ] I confirmed that `origin` is my repository.
- [ ] I pushed only when instructed.
- [ ] I opened the notebook on GitHub and verified the result.
- [ ] I submitted the exact repository URL through the course form.

---

## Detailed Guides

Use the full guide when this reference does not provide enough detail:

1. [Create a GitHub Account and Configure Your Git Identity](./Part-01.md)
2. [Install or Repair Git, Python, and Visual Studio Code](./Part-02.md)
3. [Create and Connect Your Course Repository](./Part-03.md)
4. [Create the Python Environment and Install Course Packages](./Part-04.md)
5. [Use Jupyter Notebooks in Visual Studio Code](./Part-05.md)
6. [Complete, Organize, Commit, and Submit Notebook Work](./Part-06.md)
7. [Maintain the Repository and Troubleshoot Git](./Part-07.md)

---

## The Five Commands Worth Remembering

```bash
git status
git fetch upstream
git merge upstream/main
git add Completed/path/to/notebook.ipynb
git commit -m "Describe the completed work"
```

And, only when it is time to publish:

```bash
git push origin main
```
