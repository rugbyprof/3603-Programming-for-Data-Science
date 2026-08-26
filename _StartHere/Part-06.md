# CMPS 3603 Student Setup

## Part 6 — Complete, Organize, Commit, and Submit Notebook Work

This part combines the complete course workflow: obtain an instructor notebook, preserve the original, work from a copy, validate it, move it into `Completed`, record the work with Git, and push it to your registered public repository when instructed.

The normal notebook path is:

```text
Instructor-provided notebook
          ↓ copy
        Work/
          ↓ complete and validate
      Completed/
          ↓ commit locally
       Git history
          ↓ push when instructed
Your public GitHub repository
```

---

## What You Will Accomplish

By the end of this part, you should be able to:

- preserve instructor-provided notebooks;
- organize notebooks under `Work` and `Completed`;
- make local Git checkpoint commits;
- validate a notebook from its final location;
- review and stage only intended files;
- create useful commit messages;
- distinguish committing from pushing;
- inspect everything that a push will publish;
- push completed work to your `origin` repository;
- verify the submission on GitHub; and
- recover safely from common Git mistakes.

---

## 1. Understand the Four States of Your Work

Git work moves through four useful states.

| State             | Meaning                                         |
| ----------------- | ----------------------------------------------- |
| **Working file**  | A file on your computer that you are editing    |
| **Staged change** | A change selected for the next commit           |
| **Commit**        | A recorded checkpoint in your local Git history |
| **Pushed commit** | A local commit uploaded to GitHub               |

These operations are not interchangeable:

```text
Save → Stage → Commit → Push
```

- **Save** writes notebook changes to the local file.
- **Stage** selects particular changes for the next checkpoint.
- **Commit** records those staged changes locally.
- **Push** publishes commits to GitHub.

A commit does not require an internet connection and does not make work public. A push does.

VS Code uses the same stage-and-commit model as command-line Git. See the official [VS Code source-control quickstart](https://code.visualstudio.com/docs/sourcecontrol/quickstart).

---

## 2. Start Every Work Session Safely

Open the complete course repository in VS Code:

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
code .
```

Open a VS Code terminal and activate `.venv` if necessary.

### Windows — Git Bash

```bash
source .venv/Scripts/activate
```

### macOS

```bash
source .venv/bin/activate
```

Before editing anything, run:

```bash
git status
git branch --show-current
git remote -v
```

Confirm that:

- the current branch is `main`;
- `origin` belongs to your GitHub account;
- `upstream` belongs to `rugbyprof`; and
- you understand any changes already listed by `git status`.

Never begin a new assignment by blindly ignoring existing changes.

---

## 3. Receive Instructor Updates When Directed

The instructor may publish new notebooks or corrections to the course repository.

Only pull when your current work has been saved and committed.

First require a clean working tree:

```bash
git status
```

Then receive instructor changes:

```bash
git pull upstream main
```

This downloads and merges updates from:

```text
https://github.com/rugbyprof/3603-Programming-for-Data-Science
```

It does not upload student work.

If Git reports a conflict, stop and use the troubleshooting section. Do not force the pull and do not discard files to make the warning disappear.

### Why Preserving Originals Matters

Instructor updates are easier to receive when instructor-provided notebooks remain unchanged. Your work will happen in a separate `Work` copy.

---

## 4. Treat Instructor-Provided Notebooks as Originals

Do not begin by editing the only instructor-provided copy.

Instead:

1. locate the assigned notebook in the repository;
2. review the assignment instructions;
3. copy the notebook into `Work`;
4. complete the copied notebook; and
5. leave the instructor-provided original unchanged.

This provides:

- a clean reference copy;
- an easy way to restart an assignment;
- fewer conflicts when the instructor publishes corrections; and
- a clear distinction between assigned material and student work.

---

## 5. Create the `Work` Folder

If the repository does not already contain `Work`, create it in the VS Code Explorer:

1. right-click the repository root;
2. select **New Folder**;
3. name it exactly:

   ```text
   Work
   ```

You may also create it in the terminal:

```bash
mkdir -p Work
```

Git does not track an empty folder. The folder will appear in Git after it contains a notebook or another file.

---

## 6. Copy an Assigned Notebook into `Work`

Use the VS Code Explorer:

1. right-click the assigned `.ipynb` file;
2. select **Copy**;
3. right-click the `Work` folder;
4. select **Paste**; and
5. keep the original notebook filename unless the assignment says otherwise.

For courses with several units, mirror the assignment organization inside `Work`:

```text
Work/
├── 01-Getting_Started/
├── 02-Working_with_Data/
├── 03-Visualization/
└── 04-Modeling/
```

Example:

```text
Assignments/02-Working_with_Data/arrays.ipynb
                         ↓ copy
Work/02-Working_with_Data/arrays.ipynb
```

Do not rename the file merely to add words such as `final`, `final2`, `really-final`, or `new`. Git already provides version history.

---

## 7. Confirm That You Copied Rather Than Moved

Check the VS Code Explorer.

Both files should exist:

```text
Assignments/.../arrays.ipynb
Work/.../arrays.ipynb
```

Run:

```bash
git status --short
```

The `Work` copy should appear as untracked, typically with `??`:

```text
?? Work/02-Working_with_Data/arrays.ipynb
```

The instructor original should not appear as deleted or modified.

Common status indicators include:

| Indicator | Meaning               |
| :-------: | --------------------- |
|   `??`    | Untracked new file    |
|    `M`    | Modified file         |
|    `D`    | Deleted file          |
|    `R`    | Renamed or moved file |

If the instructor original appears deleted, undo the move before beginning the assignment or copy it back from a clean source.

---

# 8. Complete the Notebook in `Work`

Open the copy inside `Work`.

1. Select the repository’s `.venv` kernel.
2. Verify the kernel:

   ```python
   import sys
   print(sys.executable)
   ```

3. Read the complete notebook before editing.
4. Complete required code cells.
5. Complete required Markdown explanations.
6. Save frequently.
7. Use repository-relative data paths.
8. Keep output focused and useful.

Do not place passwords, API keys, database credentials, private URLs, access tokens, or personal secrets in a notebook, its output, or its metadata.

---

## 9. Make Local Checkpoint Commits

Git commits provide useful checkpoints even when you are not ready to publish.

A reasonable checkpoint occurs after:

- copying and beginning an assignment;
- completing a meaningful section;
- fixing a difficult problem;
- producing a correct analysis or visualization; or
- ending a work session.

### Inspect the Changes

Run:

```bash
git status
```

Open the VS Code Source Control view and select the notebook to review its notebook-aware diff.

### Stage Only the Intended Notebook

In VS Code:

1. find the notebook under **Changes**;
2. select the **+** beside that exact file; and
3. confirm that it moves to **Staged Changes**.

Or use a quoted path in the terminal:

```bash
git add "Work/02-Working_with_Data/arrays.ipynb"
```

Use the actual path for your assignment.

Avoid staging every file automatically with:

```bash
git add .
```

Staging a specific path reduces the chance of committing unrelated work, `.venv`, large data files, or secrets.

### Review What Is Staged

Run:

```bash
git diff --cached --stat
git diff --cached --name-only
```

Only intended files should appear.

### Commit the Checkpoint

Use a short message that describes the work:

```bash
git commit -m "Complete NumPy indexing exercises"
```

Good messages include:

```text
Start Pandas data cleaning notebook
Complete NumPy indexing exercises
Add missing-data analysis
Finish visualization explanations
Correct train-test split
Move completed arrays notebook
```

Weak messages include:

```text
stuff
changes
work
final
asdf
```

Only staged changes enter the commit. Unstaged changes remain on the computer for later. See [VS Code staging and committing](https://code.visualstudio.com/docs/sourcecontrol/staging-commits).

---

## 10. Understand Local Commits and Public Repositories

After committing, run:

```bash
git status
```

Git may report that your local branch is ahead of `origin/main`.

That is normal. It means local commits exist that have not been pushed.

Do not push notebook work until the instructor permits or requires publication. Your repository is public, so pushed notebooks can be viewed by anyone.

### Important: Pushes Include All Unpushed Commits

A push does not upload only the most recent file. It sends all reachable local commits that `origin/main` does not yet have.

Before pushing, you must inspect the entire unpublished range:

```bash
git log --oneline origin/main..HEAD
git diff --name-only origin/main..HEAD
```

If those commands include work that should not yet be public, do not push. Ask the instructor how to separate the work.

---

## 11. Validate the Finished Notebook in `Work`

Before moving the notebook:

1. save every cell;
2. confirm `.venv` is the selected kernel;
3. restart the kernel;
4. run every cell from top to bottom;
5. confirm that no cell ends with an unhandled error;
6. confirm that required tables and plots appear;
7. remove accidental debugging output;
8. confirm that no secret or private information appears;
9. check that all written responses are complete; and
10. save again.

This test proves that the notebook does not depend on hidden kernel state.

---

## 12. Move the Finished Notebook into `Completed`

When the notebook is finished, move the `Work` copy into `Completed`.

Preserve the unit organization when practical:

```text
Work/02-Working_with_Data/arrays.ipynb
                         ↓ move
Completed/02-Working_with_Data/arrays.ipynb
```

In the VS Code Explorer:

1. create the appropriate unit folder inside `Completed` if needed;
2. drag the completed notebook from `Work` into that folder; and
3. confirm that the notebook no longer appears under `Work`.

The instructor-provided original remains in its original assignment location.

The final structure should resemble:

```text
Assignments/02-Working_with_Data/arrays.ipynb   ← instructor original
Completed/02-Working_with_Data/arrays.ipynb     ← student solution
```

---

## 13. Reopen and Rerun from `Completed`

Moving a notebook can affect relative file paths.

After the move:

1. open the notebook from its new `Completed` location;
2. select `.venv` as the kernel;
3. restart the kernel;
4. run every cell from top to bottom;
5. correct any path problems;
6. confirm all output again; and
7. save the notebook in its final location.

The notebook must work where it will be graded—not merely where it was drafted.

---

## 14. Review the Completed Move with Git

Run:

```bash
git status
```

Git may describe the move as:

- a rename;
- one deleted `Work` path and one new `Completed` path; or
- a modified file combined with a move.

All are normal. Git determines rename similarity from file content rather than storing a special move operation.

Open the Source Control view and inspect every listed file.

Confirm that:

- the completed notebook is under `Completed`;
- the `Work` copy is gone;
- the instructor original is unchanged;
- `.venv` does not appear;
- no unexpected data files appear; and
- no unrelated notebook is included.

---

## 15. Stage the Final Move

The VS Code Source Control view is the clearest way to stage a notebook move.

1. Stage the removed `Work` path if it is listed.
2. Stage the new `Completed` path.
3. Stage any required supporting file that belongs to the same assignment.
4. Leave unrelated files unstaged.

If the assignment is organized within matching unit folders, the terminal equivalent may resemble:

```bash
git add -A -- "Work/02-Working_with_Data" "Completed/02-Working_with_Data"
```

Use the actual unit paths. The `-A` option records additions, modifications, and deletions within only the paths named after `--`.

Review the staged set:

```bash
git diff --cached --stat
git diff --cached --name-only
```

If you staged the wrong file, unstage it without deleting its changes:

```bash
git restore --staged "path/to/file"
```

---

## 16. Commit the Completed Notebook

Create a final assignment commit:

```bash
git commit -m "Complete NumPy arrays notebook"
```

Verify the latest commit:

```bash
git log -1 --oneline
```

Check the working tree:

```bash
git status
```

Ideally, the working tree is clean. If changes remain, understand each one before proceeding.

---

## 17. Inspect Everything That Will Be Published

Before pushing to a public repository, inspect all unpushed commits:

```bash
git log --oneline origin/main..HEAD
```

Inspect all files changed by those commits:

```bash
git diff --name-status origin/main..HEAD
```

Inspect the size summary:

```bash
git diff --stat origin/main..HEAD
```

Confirm that the unpublished history does not contain:

- work that should remain private until a later deadline;
- `.venv`;
- passwords, tokens, or secrets;
- personal data;
- unrelated assignments;
- accidentally deleted instructor files; or
- extremely large generated files.

If anything is questionable, do not push.

---

## 18. Confirm the Push Destination

Before every submission push, run:

```bash
git remote get-url origin
git remote get-url upstream
```

Expected ownership:

| Remote     | Owner                |
| ---------- | -------------------- |
| `origin`   | Your GitHub username |
| `upstream` | `rugbyprof`          |

Student work is pushed to `origin`, never to `upstream`.

---

## 19. Push When Instructed

When publication is permitted and the assignment is ready:

```bash
git push origin main
```

Because Part 3 configured the branch, this shorter command should also work:

```bash
git push
```

The explicit `git push origin main` form makes the destination visible and is preferred while learning.

GitHub may request browser authentication. Sign in using the account that owns `origin`.

Do not wait until the final seconds before a deadline. Allow enough time to push, open GitHub, and verify the uploaded notebook.

GitHub documents the same `git push origin main` pattern in its [pushing commits guide](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository).

---

## 20. Verify the Submission on GitHub

Open your registered repository in a browser:

```text
https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME
```

Do not verify only the local VS Code copy.

On GitHub, confirm that:

1. the repository is public;
2. the owner is your GitHub account;
3. the branch is `main`;
4. the latest commit message appears;
5. the notebook exists under `Completed`;
6. the filename is correct;
7. GitHub renders the notebook;
8. required code, Markdown, tables, and plots are visible; and
9. the commit time is before the deadline.

Open the repository in a private/incognito browser window if you need to confirm public visibility.

Only work visible in the registered GitHub repository can be retrieved from GitHub. A local commit that was never pushed is not an online submission.

---

## 21. Register the Repository with the Course

The instructor will provide a Google Form used to associate course identities and repository information.

Enter information carefully. The form may request:

- your name;
- course section;
- GitHub username;
- exact GitHub repository URL; and
- Discord username.

Submit the repository homepage URL without the terminal-only `.git` suffix:

```text
https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME
```

Do not submit:

- a local file path;
- the instructor repository URL;
- the URL of one notebook file;
- a Git clone command;
- a ZIP download URL; or
- a repository belonging to another student.

The repository URL normally remains the same for the entire course. Completed notebooks accumulate inside its `Completed` folder.

---

## 22. The Repeatable Assignment Routine

For each notebook assignment:

1. Open the correct repository.
2. Check `git status`, branch, and remotes.
3. Pull instructor updates when directed and only from a clean working tree.
4. Copy the assigned notebook into `Work`.
5. Preserve the instructor original.
6. Select `.venv` as the kernel.
7. Complete and save the notebook.
8. Make meaningful local checkpoint commits.
9. Restart the kernel and run all cells.
10. Move the notebook from `Work` to `Completed`.
11. Reopen it from `Completed`.
12. Restart and run all cells again.
13. Review all changes.
14. Stage only the intended files.
15. Commit the completed notebook.
16. Inspect every unpushed commit and file.
17. Push to `origin` only when instructed.
18. Verify the notebook on GitHub.

---

## Troubleshooting and Recovery

### `nothing to commit, working tree clean`

Possible explanations:

- the notebook was not saved;
- you edited a different copy;
- you opened a notebook outside the repository;
- the change was already committed; or
- the file is ignored.

Confirm the notebook path and save it, then run:

```bash
pwd
git status
git log -1 --oneline
```

### The Wrong File Was Staged

Unstage it without deleting the work:

```bash
git restore --staged "path/to/file"
```

Then run `git status` again.

In VS Code, use the **−** control beside a file under **Staged Changes**.

Unstaging is different from discarding. Do not select **Discard Changes** unless you deliberately intend to throw away uncommitted work.

### The Wrong File Was Committed but Not Pushed

Do not panic and do not reset the repository.

The safest beginner response is usually:

1. correct the files;
2. stage the correction; and
3. create a new commit explaining the correction.

If unpublished work must be removed from history before a public push, ask the instructor for help.

### The Push Was Rejected

Do not use `--force`.

Run:

```bash
git status
git remote -v
```

A rejection may mean:

- the remote contains commits not present locally;
- another computer pushed to the same repository;
- the wrong GitHub account is authenticated; or
- `origin` points to the wrong URL.

Preserve the complete error message and ask the instructor before merging unfamiliar remote work.

## Student Work Was Accidentally Pushed to `upstream`

Most students do not have permission to push to the instructor repository, so GitHub should reject the attempt.

Verify remotes:

```bash
git remote -v
```

Push only to your `origin`.

### Work Was Pushed Too Early

Because the repository is public, assume pushed content may already have been seen or copied.

Do not rewrite history or force-push in an attempt to hide it. Contact the instructor and explain exactly what was published.

### A Password, Token, or Secret Was Committed

Treat the secret as compromised even if the commit was not intentionally shared.

1. Revoke or rotate the credential immediately.
2. Do not merely delete the visible line and assume the history is safe.
3. Contact the instructor.
4. Do not force-push or run history-rewriting commands without guidance.

GitHub emphasizes that revoking or rotating an exposed credential is the first response because deleted secrets may remain in history, clones, caches, and forks. See [GitHub’s sensitive-data guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

### `.venv` Appears in Git Changes

Do not stage it.

Add this rule to the root `.gitignore`:

```gitignore
.venv/
```

If `.venv` was staged but not committed:

```bash
git restore --staged .venv
```

If it was committed or pushed, ask the instructor for help. Do not attempt to solve the problem with a force-push.

### The Instructor Original Was Modified

Do not discard it until you confirm that all student work exists safely in `Work` or `Completed`.

1. Save the student work under the correct student path.
2. Confirm the copy opens.
3. Check `git status`.
4. Ask the instructor to help restore the original without losing student changes.

### A Notebook Fails After Moving to `Completed`

The notebook probably relies on a relative path based on its previous location.

Inspect:

```python
from pathlib import Path

print(Path.cwd())
```

Use repository-relative paths, correct the notebook, restart the kernel, run all cells from the final location, and recommit.

### Git Reports a Merge Conflict During an Instructor Update

Stop and run:

```bash
git status
```

Do not:

- force the pull;
- delete conflict markers blindly;
- discard the `Work` or `Completed` copy;
- run `git reset --hard`; or
- reclone over the existing repository.

Preserve the status output and ask the instructor for help. The separate `Work` workflow should make conflicts less common, but it cannot eliminate every possibility.

### The GitHub Notebook Does Not Render

The file may contain extremely large output or embedded data.

Open the local notebook, remove only unnecessary oversized output, rerun the relevant cells with smaller summaries, save, commit, push, and verify again.

Useful reductions include:

```python
data.head()
data.sample(10)
data.describe()
```

Do not remove output required to support the assignment’s conclusions.

### Local and GitHub Files Do Not Match

Check whether commits remain unpublished:

```bash
git status
git log --oneline origin/main..HEAD
```

If commits appear and publication is permitted, push them to `origin` and refresh GitHub.

### You Used Another Computer

Do not copy `.venv` between computers.

On the additional computer:

1. clone your own `origin` repository;
2. recreate `.venv` from `requirements.txt`;
3. verify the `upstream` remote;
4. pull before beginning work; and
5. avoid editing the same notebook independently on two computers.

Push completed work from one computer before continuing on another, when course publication rules permit.

---

## Commands to Avoid

Do not use these commands as generic fixes:

```text
git push --force
git reset --hard
git clean -fd
git add -f .venv
```

They can overwrite history, permanently discard work, delete untracked files, or publish generated environment contents.

Do not paste commands from an unrelated troubleshooting page without understanding which files and history they affect.

---

## Final Submission Checklist

Before considering a notebook submitted:

- [ ] I preserved the instructor-provided original.
- [ ] I completed the student copy rather than the only original.
- [ ] The finished notebook is under `Completed`.
- [ ] The filename and unit folder are correct.
- [ ] `.venv` is the selected kernel.
- [ ] I restarted the kernel and ran every cell from the final location.
- [ ] No cell ends with an unhandled error.
- [ ] Required Markdown explanations are complete.
- [ ] Required tables and plots are visible.
- [ ] The notebook contains no secret or private information.
- [ ] I reviewed the notebook-aware Git diff.
- [ ] I staged only intended files.
- [ ] I created a descriptive commit.
- [ ] I inspected all commits and files that the push would publish.
- [ ] `origin` points to my GitHub repository.
- [ ] I pushed only when instructed.
- [ ] The notebook is visible under `Completed` on GitHub.
- [ ] The public GitHub notebook renders correctly.
- [ ] My repository URL is registered with the course.

Next: [**Part 7 — Maintain the Repository, Receive Updates, and Troubleshoot Git**](./Part-07.md)
