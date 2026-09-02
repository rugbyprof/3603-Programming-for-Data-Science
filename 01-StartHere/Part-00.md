# CMPS 3603 Student Setup

## Part 0 — Check What Is Already Installed

Some students arrive with Git, Python, or Visual Studio Code already installed from a previous course, a bootcamp, or personal projects. Others have none of it. Both situations are normal.

This part is a short inventory, not an installation. You will open a terminal and run a few commands to find out what is already on your computer, so the instructions in Part 1 and Part 2 make sense the first time you read them. You will not install, fix, or configure anything yet.

---

## What You Will Accomplish

By the end of this part, you should know:

- how to open a terminal on your computer;
- whether Git is already installed, and which version;
- whether Python is already installed, and which version;
- whether Visual Studio Code is already installed;
- whether Conda or Anaconda is present; and
- a short list of what you already have versus what Part 2 still needs to install.

---

# 1. Open a Terminal

You do not need Git Bash for this part. Git Bash is installed in Part 2, and if it is not on your computer yet, that is expected.

## Windows

Use the terminal that already ships with Windows:

1. Open the **Start Menu**.
2. Type `Terminal` (or `PowerShell` or `Command Prompt` if `Terminal` does not appear).
3. Open it.

While you are here, also type `Git Bash` into the Start Menu search. If a **Git Bash** application appears, Git is already installed on this computer — remember that for the next section.

## macOS

1. Open **Spotlight** with `Cmd+Space`.
2. Type `Terminal`.
3. Open it.

---

# 2. Check for Git

Run:

```bash
git --version
```

- If this prints something like `git version 2.x.x`, Git is already installed. Write down the version number.
- If the terminal reports that `git` is not recognized or not found, Git is not installed. That is fine — Part 2 installs it.

---

# 3. Check for Python

## Windows

```bash
py --version
```

If that fails, also try:

```bash
python --version
```

If a window opens advertising the Microsoft Store instead of printing a version number, treat that as **not installed** — that is a Store shortcut, not a real Python installation.

## macOS

```bash
python3 --version
```

macOS ships a limited system Python at `/usr/bin/python3` used by the operating system itself. If this command succeeds, note the version, but do not assume it is suitable for the course — Part 2 explains why a dedicated Python 3.13 install is still required.

For this course you need **Python 3.13** specifically. If a version prints but it isn't 3.13, that's still useful to know — Part 2 will install 3.13 alongside it.

---

# 4. Check for Visual Studio Code

```bash
code --version
```

- If this prints a version number, VS Code is already installed and its `code` command already works from a terminal.
- If the command is not recognized, that does not necessarily mean VS Code isn't installed — it may just mean the `code` command was never added to your terminal's PATH. Either way, Part 2 covers installing it and enabling this command, so no action is needed here.

---

# 5. Check for Conda or Anaconda

```bash
conda --version
```

If this prints a version number, or if your terminal prompt begins with `(base)`, Conda is present on this computer. That is not an emergency, but it matters: this course does not use Conda, and Part 2 includes a section on keeping Conda from interfering with the course environment. Just note that it's present for now.

---

# 6. Record Your Inventory

Fill in what you found. You will use this in Part 1 and Part 2 to know which steps apply to you.

```text
Git installed?            yes / no    version: ______
Python installed?         yes / no    version: ______   is it 3.13? ______
VS Code installed?        yes / no    version: ______
Git Bash available?       yes / no  (Windows only)
Conda / Anaconda present? yes / no
```

Nothing here is graded, and there is no wrong answer — this is only to save you from following installation steps you don't need, or skipping ones you do.

---

# What This Part Does Not Cover

- Installing anything — that is Part 2.
- Configuring Git's name and email — that is Part 1, Section 6.
- Creating the course repository or Python environment — those come later.

If you found that Git, Python 3.13, and VS Code are **all** already installed and working, you can move quickly through Part 2 — but still skim it, since it also covers configuration steps (Git Bash as the default VS Code terminal, the required VS Code extensions) that a prior install may not already have.

---

# Completion Checklist

Before continuing to Part 1, confirm each item:

- [ ] I can open a terminal on my computer.
- [ ] I know whether Git is installed, and its version if so.
- [ ] I know whether Python is installed, and whether it is 3.13.
- [ ] I know whether VS Code and its `code` command are installed.
- [ ] I know whether Conda or Anaconda is present.
- [ ] I saved my inventory somewhere I can refer back to.

Next: [**Part 1 — Create a GitHub Account and Configure Your Git Identity**](./Part-01.md)
