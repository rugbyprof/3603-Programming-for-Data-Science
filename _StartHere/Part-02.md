# CMPS 3603 Student Setup

## Part 2 — Install or Repair Git, Python, and Visual Studio Code

This course uses Git, Python, Visual Studio Code, and Jupyter notebooks. This guide provides separate setup instructions for Windows and macOS, followed by repair procedures for computers that already contain older or conflicting installations.

Use the instructions for your operating system. Do not complete both paths.

---

## What You Will Accomplish

By the end of this part, you should have:

- Git installed and working;
- Git Bash available on Windows;
- Python 3.13 installed;
- Visual Studio Code installed;
- the Microsoft Python and Jupyter extensions installed;
- Git Bash configured as the VS Code terminal on Windows;
- Git author information configured; and
- a verified set of tools ready for the course repository.

You will create a project-specific Python virtual environment after cloning the course repository in a later part.

---

# Before You Begin

## Use Python 3.13 for This Course

Install a current **Python 3.13** release. Do not install a prerelease, beta, release candidate, experimental free-threaded build, or Python 2.

Python 3.13 is identified by a version resembling:

```text
Python 3.13.x
```

The final number may be different from examples in this guide. That is normal.

Do not choose a version with a `t`, `a`, `b`, or `rc` suffix, such as:

```text
3.13t
3.15.0a1
3.15.0b2
3.15.0rc1
```

Those builds are not the standard course environment.

## Do Not Install Conda or Anaconda

This course does not use Conda, Anaconda, or Miniconda.

Conda attempts to manage Python versions, packages, virtual environments, and shell configuration through its own parallel system. Those are all problems already handled adequately for this course by a standard Python installation, `pip`, and Python’s built-in `venv` module.

Adding a second package and environment manager makes error messages less predictable and makes it harder to determine which Python is actually running. We will use one small project-local environment named `.venv` instead.

If Conda is already installed, do not panic and do not start deleting files. Follow the repair section near the end of this guide.

---

# Windows Clean Installation

Windows students will use **Git Bash**, including Git Bash inside Visual Studio Code. PowerShell can run Git, but using Git Bash keeps course commands consistent with macOS and other Unix-like environments.

## 1. Check the Windows System Type

Most Windows computers use an x64 processor. Some newer computers use ARM64.

1. Open **Settings**.
2. Select **System**.
3. Select **About**.
4. Find **System type**.
5. Remember whether it reports **x64** or **ARM64**.

Download installers matching that system type whenever a site offers both versions.

## 2. Install Visual Studio Code

1. Visit [Download Visual Studio Code](https://code.visualstudio.com/download).
2. Download the Windows **User Installer** matching your system type.
3. Run the downloaded installer.
4. Accept the license agreement.
5. Keep the default installation location.
6. If offered, enable these options:
   - **Add “Open with Code” action to Windows Explorer file context menu**;
   - **Add “Open with Code” action to Windows Explorer directory context menu**; and
   - **Add to PATH**.
7. Complete the installation.

The User Installer is appropriate for most students and normally does not require administrator access. See the official [VS Code Windows installation guide](https://code.visualstudio.com/docs/setup/windows).

Close any terminals that were open before installing VS Code. PATH changes are recognized by newly opened terminals.

## 3. Install Git for Windows and Git Bash

1. Visit [Git for Windows](https://git-scm.com/install/windows).
2. Download the installer matching your system type.
3. Run the installer.
4. Accept the default components, including **Git Bash Here**.
5. If asked to choose Git’s default editor, select **Visual Studio Code**.
6. If asked about Git’s default branch name, choose the option that allows new repositories to use `main`.
7. Accept the remaining recommended defaults.
8. Complete the installation.

Open **Git Bash** from the Windows Start menu and verify Git:

```bash
git --version
```

Expected output resembles:

```text
git version 2.x.x.windows.x
```

The exact numbers will change over time.

## 4. Configure Git

Set the name that should appear on your commits:

```bash
git config --global user.name "Your Name"
```

Set the email address that should appear on your commits:

```bash
git config --global user.email "your.email@example.com"
```

Replace both examples with your own information. If you selected GitHub’s private `noreply` address in Part 1, use that exact address here.

Configure `main` as the default name for new branches:

```bash
git config --global init.defaultBranch main
```

Configure Visual Studio Code as Git’s editor:

```bash
git config --global core.editor "code --wait"
```

Verify the identity settings:

```bash
git config --global user.name
git config --global user.email
```

Git permanently includes the configured name and email in new commits. The official Git documentation identifies this as part of the [first-time Git setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

## 5. Install Python 3.13

Python now provides a Windows install manager that installs and selects Python runtimes.

1. Visit [Python Releases for Windows](https://www.python.org/downloads/windows/).
2. Download the current **Python install manager**.
3. Open the downloaded installer.
4. Select **Install** and allow the installation to finish.
5. Close and reopen Git Bash.

Install the current standard Python 3.13 runtime:

```bash
py install 3.13
```

Do not add `t` to the version. `3.13t` is the experimental free-threaded build and is not used in this course.

Verify the installed runtime:

```bash
py -V:3.13 --version
```

Expected output resembles:

```text
Python 3.13.x
```

Verify that `pip` is available through this exact Python installation:

```bash
py -V:3.13 -m pip --version
```

Using `python -m pip` or `py -V:3.13 -m pip` is safer than using a bare `pip` command because it identifies which Python installation will receive the package.

For current details, see the official [Python-on-Windows documentation](https://docs.python.org/3/using/windows.html).

## 6. Install the VS Code Extensions

Open Visual Studio Code.

1. Select the **Extensions** icon on the left side of the window.
2. Search for `Python`.
3. Install **Python**, published by **Microsoft**.
4. Search for `Jupyter`.
5. Install **Jupyter**, published by **Microsoft**.

Verify the publisher before installing. Extensions with similar names are not necessarily the same products.

The required extension identifiers are:

```text
ms-python.python
ms-toolsai.jupyter
```

You do not need to install every extension suggested by VS Code.

## 7. Make Git Bash the Default VS Code Terminal

1. Open Visual Studio Code.
2. Open the Command Palette with `Ctrl+Shift+P`.
3. Search for **Terminal: Select Default Profile**.
4. Select **Git Bash**.
5. Close existing VS Code terminal panels.
6. Open a new terminal with **Terminal → New Terminal**.

The terminal prompt should resemble Git Bash rather than PowerShell:

```text
student@computer MINGW64 ~
$
```

In the VS Code terminal, repeat these checks:

```bash
git --version
py -V:3.13 --version
code --version
```

If all three commands work, continue to **Cross-Platform Final Verification**.

---

# macOS Clean Installation

macOS students may use the regular Terminal application or the terminal built into Visual Studio Code. The default macOS shell is normally `zsh`, and the course commands will work there.

## 1. Install or Verify Git

Open **Terminal** and run:

```bash
git --version
```

If Git is already installed, the command displays a version number and you may continue.

If macOS asks to install the Xcode Command Line Tools, accept the installation and allow it to finish. You can also start that installer with:

```bash
xcode-select --install
```

After installation, close and reopen Terminal, then verify Git again:

```bash
git --version
```

The Apple-provided Git from the Command Line Tools is sufficient for this course. Git also documents this installation method on its official [macOS installation page](https://git-scm.com/install/mac).

## 2. Install Visual Studio Code

1. Visit [Download Visual Studio Code](https://code.visualstudio.com/download).
2. Download the macOS build appropriate for your Mac. The Universal build supports both Apple silicon and Intel Macs.
3. Open the downloaded `.dmg` file.
4. Drag **Visual Studio Code.app** into the **Applications** folder.
5. Open Visual Studio Code from Applications or Spotlight.

See the official [VS Code macOS installation guide](https://code.visualstudio.com/docs/setup/mac) if macOS blocks or cannot locate the application.

## 3. Add the `code` Command to the Terminal

1. Open Visual Studio Code.
2. Open the Command Palette with `Cmd+Shift+P`.
3. Search for **Shell Command: Install 'code' command in PATH**.
4. Run that command.
5. Close and reopen Terminal.

Verify the command:

```bash
code --version
```

The `code` command will later let you open the current project folder with:

```bash
code .
```

## 4. Configure Git

Set the name that should appear on your commits:

```bash
git config --global user.name "Your Name"
```

Set the email address that should appear on your commits:

```bash
git config --global user.email "your.email@example.com"
```

Replace both examples with your own information. If you selected GitHub’s private `noreply` address in Part 1, use that exact address here.

Configure `main` as the default name for new branches:

```bash
git config --global init.defaultBranch main
```

Configure Visual Studio Code as Git’s editor:

```bash
git config --global core.editor "code --wait"
```

Verify the identity settings:

```bash
git config --global user.name
git config --global user.email
```

## 5. Install Python 3.13

Do not rely on Apple’s system Python. That copy belongs to macOS and its development tools.

1. Visit [Python Releases for macOS](https://www.python.org/downloads/macos/).
2. Locate the latest stable Python **3.13** release.
3. Download its macOS installer.
4. Open the downloaded `.pkg` file.
5. Accept the standard installation options.
6. Do not enable an experimental free-threaded build.
7. Complete the installation.

After installation, open the newly created `/Applications/Python 3.13/` folder and double-click:

```text
Install Certificates.command
```

A temporary terminal window should report that certificate installation completed successfully. This step allows the Python installation to establish secure connections when downloading packages. It is part of the official [Python macOS installation procedure](https://docs.python.org/3/using/mac.html).

Close and reopen Terminal, then verify Python:

```bash
python3.13 --version
```

Expected output resembles:

```text
Python 3.13.x
```

Verify `pip` through this exact Python installation:

```bash
python3.13 -m pip --version
```

Do not delete or modify `/usr/bin/python3`. That installation is controlled by Apple and may be used by macOS or Apple development tools.

## 6. Install the VS Code Extensions

Open Visual Studio Code.

1. Select the **Extensions** icon on the left side of the window.
2. Search for `Python`.
3. Install **Python**, published by **Microsoft**.
4. Search for `Jupyter`.
5. Install **Jupyter**, published by **Microsoft**.

The required extension identifiers are:

```text
ms-python.python
ms-toolsai.jupyter
```

## 7. Verify the VS Code Terminal

1. In VS Code, select **Terminal → New Terminal**.
2. Run:

```bash
git --version
python3.13 --version
code --version
```

If all three commands work, continue to **Cross-Platform Final Verification**.

---

# Repair an Existing Installation

Use this section if tools were already installed, commands produce surprising results, or VS Code cannot locate Git or Python.

Do not randomly delete Python folders or manually remove files from system directories. First determine what the computer is actually running.

## Windows Diagnostic Commands

Open Git Bash and run:

```bash
git --version
where.exe git
where.exe python
where.exe py
py list
py -V:3.13 --version
py -V:3.13 -c "import sys; print(sys.executable)"
```

Not every command must return a result. The output helps identify duplicate installations and incorrect PATH entries.

### Windows: Git Is Not Recognized

1. Close every terminal and VS Code window.
2. Reopen Git Bash from the Start menu.
3. Run `git --version` again.
4. If it still fails, rerun the official Git for Windows installer.
5. Make sure the Git command-line and Git Bash components are enabled.

### Windows: `code` Is Not Recognized

1. Close and reopen Git Bash.
2. Confirm that VS Code was installed using the User or System Installer rather than merely extracted from a ZIP file.
3. If necessary, rerun the VS Code installer and enable **Add to PATH**.

### Windows: Python Opens the Microsoft Store or the Wrong Version

Install the current Python install manager from Python.org, close all terminals, and open a fresh Git Bash window. Then run:

```bash
py install --configure -y
py install 3.13
py -V:3.13 --version
```

For this course, use the explicit `py -V:3.13` command until the project virtual environment has been created. This avoids accidentally using a different global Python installation.

### Windows: Multiple Python Versions Are Listed

Multiple Python installations are not automatically a problem. The important requirement is that this command selects Python 3.13:

```bash
py -V:3.13 -c "import sys; print(sys.version); print(sys.executable)"
```

Do not uninstall other versions if another course or application may require them. Ask the instructor before removing an installation you do not recognize.

### Windows: VS Code Opens PowerShell Instead of Git Bash

1. Open the Command Palette with `Ctrl+Shift+P`.
2. Run **Terminal: Select Default Profile**.
3. Select **Git Bash**.
4. Delete or close the existing terminal session.
5. Open a new terminal.

Changing the default does not transform a terminal that is already open; you must create a new one.

## macOS Diagnostic Commands

Open Terminal and run:

```bash
git --version
which -a git
which -a python3
which -a python3.13
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

### macOS: Git Requests Developer Tools

Run:

```bash
xcode-select --install
```

Complete the Apple installer, close Terminal, reopen it, and run `git --version` again.

### macOS: `python3` Uses `/usr/bin/python3`

Do not delete `/usr/bin/python3`.

Install Python 3.13 from Python.org, run `Install Certificates.command`, and use the explicit course interpreter:

```bash
python3.13 --version
python3.13 -c "import sys; print(sys.executable)"
```

The project virtual environment created later will prevent the system Python from being selected accidentally.

### macOS: `code` Is Not Recognized

Open VS Code and run this command from the Command Palette:

```text
Shell Command: Install 'code' command in PATH
```

Close and reopen Terminal before testing `code --version` again.

## Conda Is Activating Itself

If the terminal prompt begins with `(base)`, Conda has automatically activated its base environment:

```text
(base) student@computer ...
```

Deactivate it:

```bash
conda deactivate
```

Disable automatic base activation:

```bash
conda config --set auto_activate_base false
```

Close and reopen the terminal. The `(base)` prefix should no longer appear.

Conda may remain installed for another course, but do not activate it while working on CMPS 3603. Do not combine a Conda environment with the course `.venv`.

If `(base)` returns after disabling automatic activation, show the instructor the output of these commands before editing shell configuration files:

### Windows Git Bash

```bash
where.exe conda
where.exe python
```

### macOS

```bash
which -a conda
which -a python3
```

## VS Code Cannot Find an Extension

1. Confirm that the computer is connected to the internet.
2. Open the Extensions view.
3. Search for the exact extension identifier:

   ```text
   @id:ms-python.python
   ```

4. Repeat for:

   ```text
   @id:ms-toolsai.jupyter
   ```

5. Confirm that the publisher is Microsoft.
6. Open the Command Palette and run **Developer: Reload Window** after installation.

## VS Code Finds the Wrong Python

Do not spend time repairing the global interpreter selection yet. In a later part, you will create `.venv` inside the course repository and explicitly select it in VS Code.

For now, verify only that the required base interpreter works:

### Windows

```bash
py -V:3.13 --version
```

### macOS

```bash
python3.13 --version
```

---

# Cross-Platform Final Verification

Run the appropriate group of commands in the terminal built into VS Code.

## Windows — VS Code Git Bash Terminal

```bash
git --version
py -V:3.13 --version
py -V:3.13 -m pip --version
code --version
git config --global user.name
git config --global user.email
code --list-extensions
```

## macOS — VS Code Terminal

```bash
git --version
python3.13 --version
python3.13 -m pip --version
code --version
git config --global user.name
git config --global user.email
code --list-extensions
```

The extension list should contain:

```text
ms-python.python
ms-toolsai.jupyter
```

Capitalization in the displayed extension list may vary.

---

# What Not to Do

- Do not install Python 2.
- Do not install a Python alpha, beta, release candidate, or free-threaded build.
- Do not install Anaconda, Miniconda, or another Conda distribution for this course.
- Do not run `sudo pip install ...` on macOS.
- Do not delete Apple’s `/usr/bin/python3`.
- Do not install packages globally merely to make an error disappear.
- Do not randomly edit PATH or shell startup files.
- Do not create the course `.venv` yet; that environment belongs inside the repository you will create in the next part.

When troubleshooting, identify which executable is running before changing the computer.

---

# Completion Checklist

Before continuing, confirm each item:

- [ ] Git reports a version number.
- [ ] Windows users can open Git Bash.
- [ ] Windows users configured Git Bash as the default VS Code terminal.
- [ ] Python 3.13 reports a version number.
- [ ] `pip` is available through the Python 3.13 interpreter.
- [ ] Visual Studio Code is installed.
- [ ] The `code` terminal command works.
- [ ] The Microsoft Python extension is installed.
- [ ] The Microsoft Jupyter extension is installed.
- [ ] Git contains my correct author name.
- [ ] Git contains my intended commit email address.
- [ ] Conda is not active.
- [ ] I did not modify or delete an operating-system Python installation.

Next: [**Part 3 — Create the Public Student Repository and Connect It to the Course Repository**](./Part-03.md)
