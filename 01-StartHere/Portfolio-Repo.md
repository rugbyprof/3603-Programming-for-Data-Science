# 📁 Your Repository Is a Graded Portfolio — 10% of Your Course Grade

Everything in [Part 3](./Part-03.md) through [Part 8](./Part-08.md) gets you to one place: **your own public copy of this course repository** (`origin`), kept in sync with the instructor copy (`upstream`), with all of your coursework committed and pushed.

That repository is not just where you turn work in. By the end of the semester it is a **portfolio** — something you can hand to an employer, link on a résumé, or walk through in an interview. **10% of your final grade** is based on how well it reads as one.

The code you write is graded elsewhere, notebook by notebook. This 10% is about the **repository around the code**: is it organized, is it complete, and does it show that *you* understood what you were doing?

---

## 🎯 What You Are Building

A repo that a stranger can open on GitHub and, within a minute, understand:

- who you are and what the course was,
- what each module covered,
- where to find your finished work for any module,
- and — in your own words — what you got out of each module.

You already have good models to copy: every module folder in `02-Assignments/` ships with a `README.md` that has a notebook table and a "Learning Goals" section. Your job is to make the equivalent pages in *your* repo reflect *your* work.

---

## ✅ What's Expected

### 1. Keep the repository current

- Your `Completed/` folder contains every assigned notebook, organized by module folder, each one restarted and run top-to-bottom before its final commit (see [Part 6](./Part-06.md)).
- Commits happen **throughout the semester**, with descriptive messages — not one giant "added everything" push the night before grading.
- No clutter: no `.venv/`, no large stray data files, no `final2.ipynb` / `asdf.ipynb`. Your `.gitignore` is doing its job.
- `origin` is your public repo, `upstream` is the instructor repo, the branch is `main`.

### 2. Write a README for every module

For each module you complete, your repo should have a `README.md` in that module's folder (create one, or adapt the instructor's) that includes:

- **A table linking to each notebook** you completed for that module, with a one-line description of what it covers. Links must actually work on GitHub.
- **Your own commentary** — a short paragraph or bullet list in your own words:
  - what the module was about,
  - what you learned or what finally "clicked,"
  - what was hard, confusing, or worth revisiting,
  - anything you'd do differently.

Per-notebook notes (a sentence or two under each row about what that specific notebook taught you) are encouraged and count in your favor.

This must be **your writing**, not the instructor's text left in place. Copy the *structure* of the provided READMEs; replace the *content* with your experience.

### 3. Write a top-level README that ties it together

Your repository's front-page `README.md` should be personalized:

- your name and a short line about you (student at MSU Texas, what you're studying, interests),
- one sentence on what the course covered,
- **an index table linking to each module folder** so a reader can jump straight to any module's work,
- a note on how the repo is organized (`Completed/`, module folders, etc.).

Keep the tone professional. Assume a recruiter is reading it.

---

## 📊 How the 10% Breaks Down

| Component | Weight | What earns full marks |
|---|---|---|
| **Repo setup & hygiene** | 20% | Correct `origin`/`upstream`/`main`; public; `.gitignore` working; no `.venv`, junk, or misnamed files; `Work/` and `Completed/` used as described in Part 6. |
| **Coursework completeness** | 25% | Every assigned notebook present in `Completed/`, in the right module folder, runs top-to-bottom without errors. |
| **Module READMEs** | 30% | Each completed module has a README with a working notebook table **and** your own commentary on the module and what you learned. |
| **Top-level README / polish** | 15% | Personalized landing page with an index/table to every module; professional tone; renders cleanly on GitHub. |
| **Commit history** | 10% | Regular, descriptive commits spread across the semester — not one end-of-term dump. |

Scored out of 100, then worth 10 points of your final course grade.

---

## 🗓️ When It's Graded

- **Mid-semester check** — a quick pass for progress: repo set up correctly, early modules complete, at least one real module README written. Low-stakes, mostly feedback.
- **End of semester** — the full rubric above, on the state of your repository at the deadline.

Both grades read your **public GitHub repo**, not your local machine. Work that was committed but never pushed does not count.

---

## 📋 Quick Checklist

- [ ] My repo is public, on `main`, with `origin` = me and `upstream` = instructor.
- [ ] `.gitignore` keeps `.venv/` and junk out; `git status` is clean of clutter.
- [ ] Every assigned notebook is in `Completed/`, in its module folder, and runs top-to-bottom.
- [ ] Each completed module folder has a `README.md` with a working notebook table.
- [ ] Each module README has **my own** notes on what the module covered and what I learned.
- [ ] My top-level `README.md` has my name, a short bio, and an index linking to every module.
- [ ] My commit history shows steady work across the semester with clear messages.
- [ ] I viewed my repo on GitHub (incognito) and it looks like something I'd show an employer.

---

Next: [**Part 7 — Maintain the Repository, Receive Updates, and Troubleshoot Git**](./Part-07.md)
