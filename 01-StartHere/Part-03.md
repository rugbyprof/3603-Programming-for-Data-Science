# CMPS 3603 Student Setup

## Part 3 — Create and Connect Your Course Repository

In this part, you will create a public GitHub repository, clone the instructor’s course repository to your computer, and connect your local copy to both repositories.

When finished, your computer will know about two GitHub repositories:

```text
upstream: instructor course repository
             ↓ course updates
        your local repository
             ↓ your pushes
origin:   your GitHub repository
```

You will download course material from `upstream` and publish your own commits to `origin`.

---

## What You Will Accomplish

By the end of this part, you should have:

- a public GitHub repository named `3603-data-science-[yourlastname]`;
- a local copy of the CMPS 3603 course repository;
- the course repository configured as `upstream`;
- your repository configured as `origin`;
- the initial course files published to your GitHub repository; and
- the exact repository URL needed for the class registration form.

---

## Before You Begin

Confirm that you completed Parts 1 and 2.

You should have:

- a verified GitHub account;
- Git installed;
- Git Bash on Windows;
- Visual Studio Code installed;
- your Git author name and email configured; and
- an internet connection.

Check your Git identity before continuing:

```bash
git config --global user.name
git config --global user.email
```

If either command produces no output, configure it now:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Use your actual name and your chosen verified or GitHub `noreply` email address.

---

### 1. Choose the Repository Name

Your repository must use this pattern:

```text
3603-data-science-[yourlastname]
```

Replace `[yourlastname]` with your actual last name. Do not include the square brackets.

Examples:

```text
3603-data-science-smith
3603-data-science-smith-jones
3603-data-science-delacruz
```

Use lowercase letters. Replace spaces with nothing or with a hyphen. Avoid apostrophes and other punctuation.

Because the repository is stored under your GitHub username, two students may use the same repository name without a conflict:

```text
https://github.com/alex-smith/3603-data-science-smith
https://github.com/jordan-smith/3603-data-science-smith
```

Write your selected name here before continuing:

```text
My repository name: __________________________________________
```

---

### 2. Create an Empty Public Repository on GitHub

The repository must be **empty** because it will receive the existing files and history from the course repository.

1. Sign in to [GitHub](https://github.com/).
2. Open [Create a New Repository](https://github.com/new), or select the **+** menu and then **New repository**.
3. Under **Owner**, select your personal GitHub account.
4. Enter your required repository name:

   ```text
   3603-data-science-[yourlastname]
   ```

5. Enter a description such as:

   ```text
   Coursework for CMPS 3603 Programming for Data Science
   ```

6. Select **Public**.
7. Leave **Add a README file** unselected.
8. Leave **Add .gitignore** set to **None**.
9. Leave **Choose a license** set to **None**.
10. Select **Create repository**.

GitHub should display a **Quick setup** page for an empty repository.

> Do not add a README, `.gitignore`, license, or any other file on GitHub. The course repository already contains the files and history that will be pushed here.

GitHub’s own instructions recommend leaving these initialization options empty when pushing an existing local repository, because creating unrelated starter files can cause errors. See [Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).

## Copy Your Repository URL

On the Quick setup page, copy the **HTTPS** URL. It should resemble:

```text
https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
```

Keep this browser tab open. You will use the URL shortly.

---

### 3. Open the Correct Terminal

## Windows

Open Visual Studio Code and create a new **Git Bash** terminal:

1. Select **Terminal → New Terminal**.
2. Confirm that the terminal profile says **Git Bash**.

If VS Code opens PowerShell, open the terminal profile menu, choose **Select Default Profile**, select **Git Bash**, close the old terminal, and open a new one.

## macOS

Open either:

- the regular macOS Terminal; or
- **Terminal → New Terminal** inside Visual Studio Code.

The following Git commands are the same on both systems.

---

### 4. Choose a Parent Folder

Create a general folder for programming projects:

```bash
mkdir -p ~/Projects
```

Move into that folder:

```bash
cd ~/Projects
```

Display the current location:

```bash
pwd
```

Do not create the repository folder yourself. The `git clone` command will create it.

Do not clone the course repository inside another Git repository.

---

### 5. Clone the Instructor’s Course Repository

The instructor repository is:

[rugbyprof/3603-Programming-for-Data-Science](https://github.com/rugbyprof/3603-Programming-for-Data-Science)

Use the following command, replacing the final folder name with your required repository name:

```bash
git clone https://github.com/rugbyprof/3603-Programming-for-Data-Science.git 3603-data-science-smith
```

For example, a student named Jordan De La Cruz would use:

```bash
git clone https://github.com/rugbyprof/3603-Programming-for-Data-Science.git 3603-data-science-delacruz
```

The first URL identifies what to clone. The final argument chooses the name of the new folder on your computer.

Cloning downloads the files, branches, commits, and project history—not merely the visible files. See [GitHub’s cloning documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Do Not Download a ZIP File

A ZIP download contains files but does not contain the useful local Git configuration and complete repository workflow needed for this course. Use `git clone`.

---

### 6. Enter the Repository Folder

Change into the folder created by `git clone`. Use your own repository name:

```bash
cd 3603-data-science-smith
```

Verify the location:

```bash
pwd
```

List the course files:

```bash
ls
```

Check the repository status:

```bash
git status
```

The current branch should be `main`, and the working tree should be clean.

Verify the branch explicitly:

```bash
git branch --show-current
```

Expected output:

```text
main
```

Do not run `git init`. The cloned folder is already a Git repository.

---

### 7. Examine the Initial Remote

Run:

```bash
git remote -v
```

Immediately after cloning, the result should resemble:

```text
origin  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git (fetch)
origin  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git (push)
```

Git automatically calls the repository used for cloning `origin`. However, the instructor’s repository should not remain your `origin`, because you do not own it and cannot push to it.

We will rename it.

---

### 8. Rename the Instructor Remote to `upstream`

Run:

```bash
git remote rename origin upstream
```

Verify the result:

```bash
git remote -v
```

Expected result:

```text
upstream  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git (fetch)
upstream  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git (push)
```

The `upstream` name now means **the instructor’s course repository**.

You will eventually pull new course material from `upstream`. You will not push student work there.

---

### 9. Add Your Repository as `origin`

Return to the GitHub browser tab containing your empty repository. Copy its HTTPS URL.

Add it as `origin`:

```bash
git remote add origin https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
```

Replace the example URL with your exact URL.

For example:

```bash
git remote add origin https://github.com/jordan-delacruz/3603-data-science-delacruz.git
```

Do not use the instructor’s username in this command.

The official Git remote command uses the same `git remote add NAME URL` structure. See the [Git remote documentation](https://git-scm.com/docs/git-remote).

---

### 10. Verify Both Remotes Before Pushing

Run:

```bash
git remote -v
```

You should see four lines resembling:

```text
origin    https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git (fetch)
origin    https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git (push)
upstream  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git (fetch)
upstream  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git (push)
```

Check these carefully:

| Remote     | GitHub owner         | Purpose                             |
| ---------- | -------------------- | ----------------------------------- |
| `origin`   | Your GitHub username | Your public course repository       |
| `upstream` | `rugbyprof`          | Instructor-provided course material |

If `origin` contains `rugbyprof`, stop and correct the configuration before pushing.

You can inspect one URL at a time:

```bash
git remote get-url origin
git remote get-url upstream
```

---

### 11. Push the Initial Repository to GitHub

Push the existing `main` branch to your public repository:

```bash
git push -u origin main
```

This first push copies the already-public course files and their history to your repository. It does not publish any new completed student work.

## Authentication

GitHub may ask you to sign in through Visual Studio Code or a web browser.

1. Select **Allow** or **Sign in with your browser** when prompted.
2. Sign in to the same GitHub account that owns the student repository.
3. Approve the requested GitHub authorization.
4. Return to Visual Studio Code or the terminal.

VS Code includes basic GitHub authentication for clone, fetch, pull, and push operations. See [Working with GitHub in VS Code](https://code.visualstudio.com/docs/sourcecontrol/github).

GitHub does not accept a normal account password for Git operations over HTTPS. If the terminal asks directly for a GitHub password instead of opening a browser sign-in, cancel with `Ctrl+C`, sign in to GitHub through VS Code, and run the push command again.

Do not send anyone a password, authentication token, two-factor code, or recovery code.

#### What `-u` Means

The `-u` option makes `origin/main` the default destination for later pushes from your local `main` branch.

Git unfortunately uses the word “upstream” in more than one context. In this course:

- the remote explicitly named `upstream` is the instructor repository; and
- `git push -u origin main` configures your local branch to track `origin/main`.

The `-u` command does **not** give you permission to push to the instructor repository.

---

### 12. Verify the Repository on GitHub

Return to your repository page in the browser and refresh it.

The page should now display the course files rather than the empty Quick setup page.

Confirm all of the following:

- the repository name follows `3603-data-science-[yourlastname]`;
- the owner is your GitHub account;
- the repository is marked **Public**;
- the default branch is `main`;
- the course folders and Jupyter notebooks are visible; and
- the URL is your student repository, not the instructor repository.

Your URL should resemble:

```text
https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME
```

Open the URL in a private/incognito browser window. If it opens while you are signed out, the repository is public.

---

### 13. Open the Local Repository in Visual Studio Code

From inside the local repository folder, run:

```bash
code .
```

The period means “open the current folder.”

If VS Code displays a **Workspace Trust** prompt, confirm that you trust the repository. You cloned this repository from the instructor-provided course URL.

In VS Code, verify that:

- the Explorer displays the course files;
- the folder name matches your repository name;
- the Source Control view recognizes the repository; and
- the integrated terminal opens inside the repository folder.

Run one final status check in the VS Code terminal:

```bash
git status
```

The working tree should be clean.

---

### 14. Understand the Normal Direction of Work

Your two remotes have different roles:

```text
git pull upstream main
```

will eventually download new course material from the instructor.

```text
git push
```

will publish your committed work to your repository after the first `-u` push establishes the default destination.

Do not pull course updates yet. That workflow will be introduced later.

Do not push completed notebook work until instructed. You may still make local commits regularly; commits remain on your computer until pushed.

---

## Troubleshooting

### `destination path ... already exists and is not an empty directory`

Git will not clone into a nonempty folder with the requested name.

- Run `pwd` to confirm your current location.
- Run `ls` to inspect the parent folder.
- Do not overwrite or delete a folder containing work.
- If you previously attempted this setup, ask the instructor to inspect the existing folder before trying again.

### `fatal: not a git repository`

You are not currently inside the cloned repository folder.

Run:

```bash
pwd
ls
```

Then move into your course folder:

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
```

Replace `YOURLASTNAME` with your own folder name.

### `error: remote origin already exists`

Inspect the current configuration:

```bash
git remote -v
```

If `origin` still points to the instructor repository, you probably skipped the rename step. Run:

```bash
git remote rename origin upstream
```

Then add your repository as `origin`.

Do not repeatedly add or remove remotes without first reading `git remote -v`.

### `error: remote upstream already exists`

The rename may already have succeeded. Run:

```bash
git remote -v
```

If `upstream` points to the instructor repository, continue with the next unfinished step.

### `Repository not found`

Check the student URL:

```bash
git remote get-url origin
```

Confirm:

- the GitHub username is spelled correctly;
- the repository name is spelled correctly;
- the repository exists under your account; and
- you authenticated using the account that owns it.

### `Permission denied` or `403`

First inspect the destination:

```bash
git remote get-url origin
```

If it points to `rugbyprof`, the remotes are configured incorrectly. Your `origin` must point to your account.

If the URL is correct, sign out and back into GitHub through VS Code, then retry the push.

### Push Is Rejected Because the Remote Contains Work

This commonly occurs when the GitHub repository was initialized with a README, `.gitignore`, or license.

Do not force-push and do not use commands copied from an unrelated troubleshooting page.

If the GitHub repository contains only automatically generated starter files and no student work, ask the instructor to help you recreate it as an empty repository. If it contains actual work, it must be examined before anything is replaced.

### `src refspec main does not match any`

Confirm that you are in the cloned course repository and check the current branch:

```bash
git status
git branch --show-current
```

The instructor repository should place you on `main`. If it does not, show the instructor the output rather than guessing at a branch name.

### Authentication Never Opens a Browser

In VS Code:

1. Open the Accounts menu.
2. Choose **Sign in with GitHub** if available.
3. Complete the browser authorization.
4. Return to the terminal.
5. Retry:

   ```bash
   git push -u origin main
   ```

Do not enter your normal GitHub password into a Git password prompt.

### `Could not resolve host: github.com`

This is normally a network or DNS problem rather than a Git configuration problem.

- Confirm that GitHub opens in a web browser.
- Check the internet connection.
- Disconnect from a malfunctioning VPN if applicable.
- Retry when GitHub and the network are available.

---

## Final Verification Commands

Run these commands inside the repository:

```bash
pwd
git status
git branch --show-current
git remote -v
git config user.name
git config user.email
```

Your results should show:

- a folder named `3603-data-science-[yourlastname]`;
- a clean working tree;
- the `main` branch;
- `origin` pointing to your GitHub repository;
- `upstream` pointing to `rugbyprof/3603-Programming-for-Data-Science`; and
- your intended Git author name and email.

---

## Completion Checklist

- [ ] My repository name follows `3603-data-science-[yourlastname]`.
- [ ] My GitHub repository is public.
- [ ] I created the GitHub repository without a README, `.gitignore`, or license.
- [ ] I cloned the instructor repository with `git clone`.
- [ ] My local folder uses my required repository name.
- [ ] My current branch is `main`.
- [ ] `origin` points to my GitHub repository.
- [ ] `upstream` points to the instructor repository.
- [ ] The initial push completed successfully.
- [ ] My course files are visible on my GitHub repository page.
- [ ] My repository opens while I am signed out of GitHub.
- [ ] I recorded my exact repository URL for the class registration form.
- [ ] I can open the local repository with `code .`.

Next: **Part 4 — Create the Python Virtual Environment and Install Course Packages**
