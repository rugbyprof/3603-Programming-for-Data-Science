# 📘 Getting Started: Programming for Data Science

This guide will help you set up everything you need for the course. By the end, you’ll have your own GitHub repo connected to Google Colab so you can easily access, edit, and submit assignments.

---

## 🔄 Workflow Overview

Here’s the “big picture” of how everything fits together:

<img src="https://images2.imgbox.com/0a/d0/Uw5BZWwN_o.png">

Think of it like this:

1. **Instructor Repo** = where you get the assignments.
2. **Student Repo** = your personal course repo.
3. **Assignments → Completed** = how you stay organized.
4. **Google Colab** = where you actually do the work.

---

## 1. Create Your Own GitHub Repository

1. Go to [https://github.com](https://github.com) and sign in (or create a free account).
2. In the top-right corner, click the **“+” → “New repository”**.
3. Name your repository something like:
   ```
   username-DataScience-2025
   ```
   (Replace `username` with your GitHub username.)
4. Make it **public** (unless told otherwise).
5. Check **Initialize with README**.
6. Click **Create repository**.

---

## 2. Get the Course Assignments

All course materials live in the instructor’s repository:  
👉 [Course Repo Link](https://github.com/rugbyprof/3603-Programming-for-Data-Science.git)

You have two options:

### Option A (Easy): Download ZIP

1. Click the green **Code** button → **Download ZIP**.
2. Extract the ZIP.
3. Copy the `Assignments/` folder into your repo.

### Option B (Advanced): Git Clone

```bash
git clone https://github.com/rugbyprof/3603-Programming-for-Data-Science.git
```

Move the `Assignments/` folder into your repo.

---

## 3. Organize Your Repo

Your repo should now look like this:

```
Assignments/
Completed/
README.md
```

- `Assignments/` → instructor’s files.
- `Completed/` → where finished notebooks go.
- `README.md` → this guide.

---

## 4. Connect GitHub to Google Colab

1. Go to [https://colab.research.google.com](https://colab.research.google.com).
2. Click **File → Open Notebook**.
3. Select the **GitHub** tab.
4. Paste your repo URL.
5. Authorize Colab to access GitHub (first time only).
6. Pick a notebook and click **Open**.

---

## 5. Working on Assignments

- Always open notebooks from **your repo**, not the instructor’s.
- When you finish:
  1. Save in Colab.
  2. Check changes are synced to GitHub.
  3. Move the notebook from `Assignments/` → `Completed/`.

---

## 6. Submitting Work

I will tell you how to show completed work on D2L later.

---

## ✅ Quick Recap

- Create your **GitHub repo**.
- Copy over **Assignments/**.
- Use **Colab (GitHub tab)** to edit.
- Move finished work into **Completed/**.
