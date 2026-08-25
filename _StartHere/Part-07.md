# CMPS 3603 Student Setup

## Part 7 — Maintain the Repository and Troubleshoot Git

Your course repository connects three locations:

```text
upstream/main
Instructor repository on GitHub
          ↓ fetch and merge

main
Your working repository on this computer
          ↓ push when instructed

origin/main
Your public repository on GitHub
```

This part explains how to maintain those connections, receive instructor updates safely, work from more than one computer when necessary, understand repository status, and respond to Git problems without destroying work.

---

## What You Will Accomplish

By the end of this part, you should be able to:

- verify the repository, branch, and remotes;
- distinguish `main`, `origin/main`, and `upstream/main`;
- fetch and inspect changes without modifying working files;
- merge instructor updates deliberately;
- recognize ahead, behind, and diverged branches;
- avoid accidental publication through VS Code Sync;
- move safely between computers;
- recognize and resolve simple text conflicts;
- know when a notebook conflict requires assistance;
- inspect Git’s diagnostic output; and
- avoid destructive recovery commands.

---

# 1. Understand the Three Versions of `main`

Your repository normally contains three related branch references.

| Reference       | Location                                                    | Meaning                               |
| --------------- | ----------------------------------------------------------- | ------------------------------------- |
| `main`          | Your computer                                               | The branch containing your local work |
| `origin/main`   | Your computer’s last knowledge of your GitHub repository    | The public student branch             |
| `upstream/main` | Your computer’s last knowledge of the instructor repository | The instructor course branch          |

`origin/main` and `upstream/main` are **remote-tracking references**. They are local records of remote branches. Fetching updates those records.

Fetching does not edit notebooks or merge changes into `main`.

---

# 2. Begin with a Repository Health Check

Open the complete repository folder and its VS Code terminal:

```bash
cd ~/Projects/3603-data-science-YOURLASTNAME
code .
```

Run:

```bash
git status
git branch --show-current
git branch -vv
git remote -v
```

Confirm:

- the current folder is your course repository;
- the current branch is `main`;
- `main` tracks `origin/main`;
- `origin` points to your GitHub repository; and
- `upstream` points to the instructor repository.

Expected remote ownership:

```text
origin    https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
upstream  https://github.com/rugbyprof/3603-Programming-for-Data-Science.git
```

Do not pull, merge, or push until these relationships are correct.

---

# 3. Keep the Working Tree Clean Before Updates

Run:

```bash
git status
```

A clean result includes:

```text
nothing to commit, working tree clean
```

If modified or untracked student work appears:

1. save all open notebooks;
2. review the changes;
3. stage only intended files; and
4. commit a meaningful checkpoint.

Do not pull instructor updates over unexplained changes.

Do not use a stash merely to hide work you do not understand. A normal checkpoint commit is easier for beginners to locate and recover.

---

# 4. Fetch Instructor Updates Without Changing Files

Fetch from the instructor repository:

```bash
git fetch upstream
```

Fetching downloads new commits and updates `upstream/main`. It does not change your current `main` files.

This makes fetching a safe first step when you want to see whether the instructor published anything.

Git’s official [`fetch` documentation](https://git-scm.com/docs/git-fetch.html) describes fetch as updating remote-tracking information without automatically merging it into the current branch.

## Inspect Incoming Commits

List commits available from the instructor that are not yet in your local branch:

```bash
git log --oneline HEAD..upstream/main
```

If the command produces no output, your local branch already contains the fetched instructor commits.

Inspect the affected files:

```bash
git diff --name-status HEAD..upstream/main
```

Inspect the size summary:

```bash
git diff --stat HEAD..upstream/main
```

Review new or changed assignment instructions before merging.

---

# 5. Merge Instructor Updates into `main`

After confirming that the working tree is clean and reviewing incoming changes, merge them:

```bash
git merge upstream/main
```

Common successful results include:

- **Already up to date** — there was nothing new to merge.
- **Fast-forward** — Git moved `main` forward to include instructor commits.
- **Merge made** — Git combined instructor commits with your existing local commits.

Run:

```bash
git status
git log --oneline --decorate -5
```

If a conflict occurs, Git pauses the merge. Do not begin running unrelated Git commands. Follow the merge-conflict section below.

## Fetch-and-Merge Versus Pull

This two-step sequence:

```bash
git fetch upstream
git merge upstream/main
```

is similar to:

```bash
git pull upstream main
```

The two-step form is preferred here because it gives you an opportunity to inspect instructor changes before merging them.

---

# 6. Understand What Instructor Updates Do Not Change

Instructor updates modify instructor-controlled paths in your local `main` after merging.

They do not automatically update a notebook you previously copied into `Work` or `Completed`.

For example:

```text
Assignments/arrays.ipynb   ← instructor publishes a correction here
Work/arrays.ipynb          ← your earlier copy remains unchanged
```

Read the instructor’s correction and apply the relevant change to your `Work` copy. Do not assume that pulling automatically patches every student copy.

This separation is intentional: it protects student work from being overwritten by course-material updates.

---

# 7. Decide Whether Instructor Updates Should Be Pushed

After merging `upstream/main`, your local `main` may be ahead of `origin/main`.

Do not automatically push merely because the status bar shows outgoing commits.

Remember: a push sends **all** unpublished commits reachable from local `main`, including student work.

Inspect the complete unpublished range:

```bash
git log --oneline origin/main..HEAD
git diff --name-status origin/main..HEAD
```

If that range contains student work that should not yet be public, do not push.

Instructor material is already public, but your same branch may also contain unpublished solutions.

---

# 8. Use Explicit Git Commands Instead of VS Code Sync

VS Code’s **Sync Changes** operation normally pulls from the tracked remote and then pushes local commits.

That general workflow is convenient for ordinary repositories, but this course has:

- two remotes;
- a public student repository; and
- restrictions on when student notebook work should be published.

For this course, prefer explicit commands:

```bash
git fetch upstream
git merge upstream/main
git push origin main
```

Use the final push only when publication is permitted.

Do not select **Sync Changes** without understanding both the incoming and outgoing commits. VS Code documents that Sync performs both a pull and a push in its [repositories and remotes guide](https://code.visualstudio.com/docs/sourcecontrol/repos-remotes).

---

# 9. Inspect Your Relationship with `origin`

Fetch the current state of your public repository:

```bash
git fetch origin
```

Show a compact status:

```bash
git status -sb
```

Possible results include:

## Up to Date

```text
## main...origin/main
```

Your local and public branches currently point to the same commit.

## Ahead

```text
## main...origin/main [ahead 3]
```

You have three local commits not yet published.

## Behind

```text
## main...origin/main [behind 2]
```

The public repository contains two commits not present on this computer. This may happen if you used another computer or edited files on GitHub.

## Diverged

```text
## main...origin/main [ahead 2, behind 1]
```

Both locations contain different commits. Do not push forcefully. Inspect the history before combining them.

---

# 10. View the Repository History

Display a useful history graph:

```bash
git log --graph --decorate --oneline --all -20
```

The graph helps show how:

- `main`;
- `origin/main`; and
- `upstream/main`

relate to one another.

VS Code also provides a Source Control Graph. Open the Source Control view and select **Graph** to inspect commits and branch labels visually.

Do not choose reset, rebase, delete, or force-push operations merely because the graph looks unfamiliar.

---

# 11. Maintain a Repository from One Computer

The simplest and safest arrangement is to use one computer for notebook work.

At the beginning of a session:

```bash
git status
git fetch upstream
```

Inspect and merge instructor changes when appropriate.

At the end of a session:

1. save notebooks;
2. restart and run all cells when completing an assignment;
3. inspect changes;
4. create a local commit; and
5. push only when instructed.

Local commits protect against editing mistakes but do not protect against loss of the entire computer. When public pushes are permitted, pushing provides an off-computer copy on GitHub.

---

# 12. Work from More Than One Computer

Using multiple computers introduces the possibility that each computer contains different commits.

The safest sequence is:

## Finish on Computer A

1. Save all files.
2. Commit the work.
3. Confirm that publication is permitted.
4. Push to `origin`.
5. Verify the push on GitHub.

## Begin on Computer B

1. Open the existing clone or clone your own `origin` repository.
2. Fetch `origin`:

   ```bash
   git fetch origin
   ```

3. Require a clean working tree:

   ```bash
   git status
   ```

4. Pull your commits:

   ```bash
   git pull origin main
   ```

5. Recreate `.venv` on Computer B. Never copy `.venv` from Computer A.
6. Verify or add the instructor remote:

   ```bash
   git remote -v
   ```

7. Continue working only after the new computer is current.

## When Student Work Cannot Yet Be Public

If course policy does not permit pushing the current work, avoid editing the same notebook on multiple computers. GitHub cannot transfer unpublished commits between computers without publishing them to the remote repository.

Use one computer until pushing is allowed, or ask the instructor about an approved private transfer method.

Do not place the same active Git repository inside OneDrive, iCloud Drive, Dropbox, or another live synchronization service on two computers at the same time. File synchronization is not a substitute for Git coordination and can produce duplicated or partially synchronized repository files.

---

# 13. Clone Your Student Repository on a Replacement Computer

If the original computer is unavailable, clone your own repository—not the instructor repository—as the starting point:

```bash
cd ~/Projects
git clone https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
cd 3603-data-science-YOURLASTNAME
```

The clone automatically creates `origin` pointing to your repository.

Add the instructor remote:

```bash
git remote add upstream https://github.com/rugbyprof/3603-Programming-for-Data-Science.git
```

Verify:

```bash
git remote -v
```

Recreate `.venv` using Part 4. Virtual environments contain computer-specific paths and are not portable.

Any commits that existed only on the lost computer and were never pushed cannot be recovered from GitHub.

---

# 14. Avoid Editing Course Files Directly on GitHub

GitHub allows files to be edited in a web browser. Avoid editing course notebooks or repository files there while also working locally.

Browser edits create commits on `origin/main`. Your computer then becomes behind or diverged.

If a necessary browser edit was made:

1. save and commit all local work;
2. fetch `origin`;
3. inspect the graph;
4. pull from `origin` only from a clean working tree; and
5. resolve any conflicts before continuing.

Do not make the same notebook changes independently in the browser and on the computer.

---

# 15. Understand Merge Conflicts

A merge conflict occurs when Git cannot determine how to combine competing changes automatically.

Common causes include:

- local and instructor branches modify the same lines;
- one branch deletes a file that the other modifies;
- the same notebook is changed independently on two computers; or
- a browser edit competes with a local edit.

When a conflict occurs, Git pauses the merge. Your existing commits are not automatically erased.

Run:

```bash
git status
```

Git lists the conflicting paths and indicates that a merge is in progress.

---

# 16. Resolve a Simple Text Conflict in VS Code

For a small conflict in Markdown, text, Python, or configuration files:

1. open the Source Control view;
2. locate the file under **Merge Changes**;
3. open it in the VS Code Merge Editor;
4. review **Current**, **Incoming**, and **Result**;
5. construct the correct combined result;
6. remove all conflict markers;
7. save the result;
8. stage the resolved file; and
9. commit the merge.

Conflict markers look like:

```text
<<<<<<< HEAD
your current version
=======
incoming version
>>>>>>> upstream/main
```

In an instructor-update merge:

- **Current** normally means your local `main`; and
- **Incoming** normally means `upstream/main`.

Do not select **Accept Both** without reading the result. Accepting both can duplicate configuration, prose, code, or data.

VS Code’s [merge-conflict guide](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts) explains its inline actions and three-way Merge Editor.

---

# 17. Treat Notebook Conflicts Differently

An `.ipynb` file is structured JSON containing cells, metadata, and output. A notebook conflict can be difficult to resolve safely as raw text.

If a notebook appears under **Merge Changes**:

1. do not edit its raw JSON conflict markers casually;
2. do not accept all current or incoming changes without inspection;
3. preserve any visible student work;
4. run `git status`;
5. identify which two notebook versions are competing; and
6. ask the instructor for help if the correct combination is not obvious.

This is one reason student work belongs under `Work` and `Completed` while instructor originals remain in their original locations.

---

# 18. Abort an Unwanted Merge Carefully

If a merge was started from a clean working tree and you have not created conflict-resolution work that must be kept, you may return to the pre-merge state with:

```bash
git merge --abort
```

VS Code also provides **Git: Abort Merge** in the Command Palette.

Before aborting:

- run `git status`;
- confirm that a merge is actually in progress;
- understand that resolution edits made during the merge will be abandoned; and
- ask the instructor if you are uncertain.

Aborting a merge is not a substitute for understanding why the conflict occurred.

---

# 19. Repair Incorrect Remote URLs

Inspect the current configuration:

```bash
git remote -v
```

## Correct an Existing `origin`

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
```

## Correct an Existing `upstream`

```bash
git remote set-url upstream https://github.com/rugbyprof/3603-Programming-for-Data-Science.git
```

## Add a Missing `origin`

```bash
git remote add origin https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME.git
```

## Add a Missing `upstream`

```bash
git remote add upstream https://github.com/rugbyprof/3603-Programming-for-Data-Science.git
```

Run `git remote -v` after every correction.

Never change a remote URL based only on a guess. Copy the HTTPS URL from the correct GitHub repository page.

---

# 20. Diagnose Authentication Problems

Symptoms may include:

- repeated sign-in prompts;
- `Authentication failed`;
- `Permission denied`;
- a push that never completes; or
- a browser authorization that opens under the wrong account.

First verify the destination:

```bash
git remote get-url origin
```

Then confirm that VS Code is signed in to the GitHub account that owns that repository.

GitHub does not accept a normal account password for HTTPS Git operations. Use the browser or credential-manager flow provided by Git and VS Code.

## Open the Git Output Window

In VS Code:

1. open the Source Control view;
2. select **More Actions (...)**;
3. select **Show Git Output**; or
4. run **Git: Show Git Output** from the Command Palette.

The output identifies commands, timestamps, durations, and errors. The first error is usually more useful than later consequences.

VS Code recommends checking this output when Git appears stuck because an invisible authentication prompt may be waiting. See [VS Code source-control troubleshooting](https://code.visualstudio.com/docs/sourcecontrol/troubleshooting).

Review logs before sharing them. Remove tokens, credentials, or other sensitive values.

---

# 21. Respond to a Non-Fast-Forward Push Rejection

A rejection may resemble:

```text
! [rejected] main -> main (non-fast-forward)
```

This means `origin/main` contains commits that your local `main` does not contain. Git refuses to overwrite them.

Do not use `git push --force`.

Run:

```bash
git fetch origin
git status -sb
git log --graph --decorate --oneline --all -20
```

Determine where the remote commit came from:

- another computer;
- a browser edit;
- an accidental upload; or
- another authorized user.

From a clean working tree, you may merge known origin changes with:

```bash
git pull origin main
```

If you do not recognize the remote commits, stop and ask the instructor before merging.

GitHub explains that non-fast-forward protection prevents a push from losing remote commits. See [Dealing with non-fast-forward errors](https://docs.github.com/en/get-started/using-git/dealing-with-non-fast-forward-errors).

---

# 22. Respond When Pull Refuses Local Changes

Git may refuse a pull because local changes would be overwritten.

Do not discard the files merely to allow the pull.

Run:

```bash
git status
```

Then:

1. save all files;
2. review every local change;
3. move student work into the correct `Work` or `Completed` path if necessary;
4. stage intended changes; and
5. create a checkpoint commit.

Retry the fetch and merge only after the working tree is clean.

---

# 23. Respond When Untracked Files Would Be Overwritten

Git may stop because an incoming file has the same path as an untracked local file.

Do not delete the untracked file until you know what it contains.

1. open and inspect it;
2. determine whether it contains student work;
3. move a student copy to an appropriate safe `Work` path;
4. commit it if it belongs in the repository; and
5. retry only after the path conflict has been resolved.

An untracked file has no Git history. Treat it carefully.

---

# 24. Understand Line-Ending Warnings

Windows students may see warnings mentioning `LF` and `CRLF`.

These refer to different text-file line-ending conventions on Unix-like systems and Windows.

A warning such as this is normally informational:

```text
LF will be replaced by CRLF
```

Do not reinstall Git or rewrite notebooks solely because of a line-ending warning.

If a text file appears to have every line changed unexpectedly, show the diff to the instructor before committing it.

---

# 25. Respond to an Oversized File

GitHub rejects individual files larger than its normal file-size limit, and large notebook output can make repositories difficult to use.

Before committing, inspect large or unexpected files in Source Control.

Do not commit:

- `.venv`;
- downloaded installers;
- large raw datasets unless assigned;
- archives or backups;
- generated caches;
- videos; or
- notebooks containing enormous embedded output.

If a large file exists only as an uncommitted change, unstage it and add an appropriate `.gitignore` rule.

If the file is already present in one or more commits, a later deletion may not remove it from Git history. Do not force-push. Ask the instructor for help before rewriting history.

---

# 26. Recover a Deleted Notebook

First check the Windows Recycle Bin or macOS Trash if the file was deleted through VS Code or the file manager.

If the notebook existed in a previous commit, use VS Code’s file **Timeline** or Source Control history to inspect earlier versions.

Before restoring anything:

1. run `git status`;
2. identify the exact missing path;
3. confirm which committed version is needed; and
4. preserve any newer student work under a different filename.

Do not run a broad reset that affects the entire repository merely to recover one file.

---

# 27. Respond to a Detached HEAD

`git status` may report:

```text
HEAD detached at ...
```

This means you are viewing a commit rather than working normally on `main`.

If the working tree is clean and no work was created while detached, return to `main`:

```bash
git switch main
```

If you edited or committed work while detached, do not switch until that work is preserved. Ask the instructor for help attaching the commit to an appropriate branch.

---

# 28. Respond When VS Code Does Not Detect Git

Confirm Git works in the terminal:

```bash
git --version
```

Confirm the repository:

```bash
git status
```

Then:

1. confirm that the full repository folder is open;
2. reload the VS Code window;
3. reopen the Source Control view; and
4. inspect **Git: Show Git Output**.

VS Code uses the Git installed on the computer. GitHub Desktop does not replace that requirement.

---

# 29. Respond to an `index.lock` Error

Git may report that `.git/index.lock` already exists.

This can mean another Git process is still running or a previous process stopped unexpectedly.

Do not immediately delete files inside `.git`.

1. close commit-message editors;
2. close extra VS Code windows using the repository;
3. close other Git applications;
4. wait briefly;
5. restart VS Code; and
6. retry `git status`.

If the error persists, show the instructor the exact message before altering `.git` internals.

---

# 30. Do Not Rename the Repository Mid-Course

The registered URL is expected to remain stable:

```text
https://github.com/YOUR-USERNAME/3603-data-science-YOURLASTNAME
```

Renaming the GitHub repository requires updating `origin` and may invalidate the URL registered with the course.

Renaming or moving the local folder can also break `.venv`, because virtual environments contain absolute paths.

If a rename is unavoidable:

1. notify the instructor;
2. update the registration information;
3. correct the `origin` URL;
4. delete and recreate only `.venv`; and
5. verify all notebooks again.

Do not rename the repository merely for cosmetic reasons.

---

# 31. Maintain the `Completed` Archive

The `Completed` folder accumulates submitted notebook work throughout the course.

Do not delete earlier completed notebooks after they have been graded unless the instructor specifically directs it.

Periodically verify:

- unit folders are organized consistently;
- notebook filenames remain recognizable;
- notebooks render on GitHub;
- required output remains present;
- no unfinished notebook was placed in `Completed`; and
- no duplicate `final2` or backup files are accumulating.

The repository itself becomes a course portfolio.

---

# 32. Collect a Useful Diagnostic Report

When requesting help, run these commands from the repository and copy their output:

```bash
git --version
git status
git status -sb
git branch -vv
git remote -v
git log --graph --decorate --oneline --all -15
git config user.name
git config user.email
python --version
python -c "import sys; print(sys.executable)"
```

Also provide:

- the exact command that failed;
- the complete error message;
- whether you are using Windows Git Bash or macOS;
- whether the notebook was open and running; and
- what you expected to happen.

Do not provide:

- GitHub passwords;
- personal access tokens;
- two-factor codes;
- recovery codes;
- API keys; or
- other credentials.

A screenshot of only the final error line is often less useful than the complete text beginning with the failed command.

---

# 33. Commands That Require Instructor Guidance

Do not use these commands as generic repairs:

```text
git push --force
git reset --hard
git clean -fd
git rebase --onto ...
git filter-repo ...
```

Do not manually delete files from `.git` unless an instructor has identified the exact problem and recovery procedure.

These operations can overwrite public history, discard commits, delete untracked notebooks, or make recovery substantially harder.

The correct first response to an unfamiliar Git error is:

```bash
git status
```

Then preserve the output and ask for help.

---

# Routine Maintenance Checklist

## Before Starting Work

- [ ] I opened the correct repository folder.
- [ ] I am on `main`.
- [ ] I reviewed `git status`.
- [ ] `origin` and `upstream` point to the correct owners.
- [ ] I fetched and inspected instructor updates when directed.
- [ ] I merged updates only from a clean working tree.
- [ ] `.venv` is the active course environment.

## Before Ending Work

- [ ] I saved every notebook.
- [ ] I reviewed changes in Source Control.
- [ ] I committed a meaningful checkpoint.
- [ ] I understand whether local `main` is ahead of `origin/main`.
- [ ] I did not use Sync or Push unintentionally.

## Before Pushing

- [ ] Publication is permitted.
- [ ] I reviewed every unpushed commit.
- [ ] I reviewed every file included in the unpublished range.
- [ ] No future or private student work will be exposed.
- [ ] No credentials or secrets are present.
- [ ] `origin` belongs to me.
- [ ] I will verify the result on GitHub after pushing.

---

# Completion Checklist

- [ ] I understand `main`, `origin/main`, and `upstream/main`.
- [ ] I can fetch instructor changes without modifying working files.
- [ ] I can inspect incoming commits before merging.
- [ ] I can merge `upstream/main` into local `main`.
- [ ] I understand why VS Code Sync is risky for this two-remote public workflow.
- [ ] I can recognize ahead, behind, and diverged states.
- [ ] I know how to display the repository graph.
- [ ] I know the safe sequence for using another computer.
- [ ] I know that `.venv` must be recreated rather than copied.
- [ ] I can recognize a merge conflict.
- [ ] I know that notebook conflicts require special care.
- [ ] I can inspect and correct remote URLs.
- [ ] I know how to open Git Output in VS Code.
- [ ] I know not to force-push after a rejection.
- [ ] I can collect useful diagnostic information without sharing credentials.
- [ ] I know which destructive commands require instructor guidance.

Next: [**Part 8 — CMPS 3603 Setup and Submission Quick Reference**](./Part-08.md)
