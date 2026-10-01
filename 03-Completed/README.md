# ✅ Completed: How to Turn In Your Work

This folder is where you **turn in** each module when you finish it. Your `03-Completed` folder must end up as an exact **mirror** of `02-Assignments`: same folder names, same file names, same layout.

> ⚠️ **Why this matters:** your work is checked by a script, not by a person clicking around. The script looks for each module folder and each file **by its exact name**. If a folder or file is renamed, moved, or missing, the script can't find it, and that work counts as **not turned in**.

---

## 📋 The Short Version

For each module:

1. **Copy** the whole module folder from `02-Assignments/` into `Work/`.
2. **Complete** everything in the `Work/` copy: every notebook, `quiz.md`, and `worksheet.md`.
3. **Restart & Run All** on each notebook, and save.
4. **Move** the whole finished module folder from `Work/` into `03-Completed/`.
5. **Check** it with the script below, then **commit and push**.

Never edit the original files in `02-Assignments/`. Leaving them unchanged lets you receive instructor updates (`git pull upstream main`) without conflicts. See [Part 6](../01-StartHere/Part-06.md) of the setup guide.

---

## 🗂️ What `03-Completed` Should Look Like

Here's the target, through Module 05. Folder and file names must match **exactly**, including capital letters, underscores, and the number prefixes.

```text
03-Completed/
├── 01-Scalar_Types_and_Control_Flow/
│   ├── 01-Scalar_Types.ipynb
│   ├── 02-Control_Flow.ipynb
│   ├── quiz.md
│   ├── scalar_types_and_control_flow.csv
│   └── worksheet.md
├── 02-Strings_and_Text/
│   ├── 01-String_Basics.ipynb
│   ├── 02-String_Methods.ipynb
│   ├── 03-Formatted_Strings.ipynb
│   ├── quiz.md
│   └── worksheet.md
├── 03-Python_Containers/
│   ├── 01-Lists.ipynb
│   ├── 02-Tuples.ipynb
│   ├── 03-Dictionaries.ipynb
│   ├── quiz.md
│   └── worksheet.md
├── 03b-Containers_to_Functions/
│   ├── 01-Too_Many_Variables.ipynb
│   ├── 02-Pick_Your_Container.ipynb
│   ├── 03-Why_Functions.ipynb
│   ├── 04-Mystery_Functions.ipynb
│   ├── 05-Containers_Meet_Functions.ipynb
│   ├── 06-Pipelines.ipynb
│   ├── quiz.md
│   └── worksheet.md
├── 04-More_Functions_and_Loops/
│   ├── 01-Function_Extras.ipynb
│   ├── 02-While_Loops.ipynb
│   ├── 03-Looping_Over_Files.ipynb
│   ├── quiz.md
│   └── worksheet.md
└── 05-Foundations/
    ├── 01-magic_commands.ipynb
    ├── 02-jupyter_shortcuts_and_workflow.ipynb
    ├── 03-using_help_and_docs.ipynb
    ├── 04-markdown_and_formatting.ipynb
    ├── 05-working_with_files_and_paths.ipynb
    ├── 06-data_input_output.ipynb
    ├── 07-plotting_basics.ipynb
    ├── 08-timing_and_performance.ipynb
    ├── Foundations_Quiz.ipynb
    ├── quiz.md
    ├── worksheet.md
    ├── 01-OutputFiles/          ← created when you run the notebooks;
    ├── 02-OutputFiles/            keep every one of these
    ├── …
    └── Quiz-OutputFiles/
```

### What's required in each module folder

| File                                    | Required?                                                                                      |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Every `.ipynb` notebook from the module | ✅ Required                                                                                     |
| `quiz.md`                               | ✅ Required. Write your answers in the file itself, under each question.                        |
| `worksheet.md`                          | ✅ Required. Fill in each `Answer:` blank, the tasks, and the "Explain It" prompts.             |
| `NN-OutputFiles/` folders (Module 05)   | ✅ Required. The notebooks create these when you run them, and they hold files that get graded. |
| `README.md`, `glossary.md`, data files  | Optional. Keeping them is fine, and so is deleting them.                                       |

---

## 🪜 Step by Step

### 1. Copy the module into `Work/`

In the VS Code Explorer:

1. Create a `Work` folder at the top of your repository if you don't have one yet.
2. Right-click the module folder in `02-Assignments/` (for example, `05-Foundations`) and choose **Copy**.
3. Right-click the `Work` folder and choose **Paste**.

You should now have `Work/05-Foundations/`, with the same files inside as the original.

> Copy the **whole folder**, not the notebooks one by one. That keeps the names and layout right automatically, and it keeps any data files the notebooks need next to them.

### 2. Do the work in `Work/`

- Open the notebooks from **`Work/`**, not from `02-Assignments/`. Check the tab's path if you're not sure.
- Select your `.venv` kernel.
- Complete every notebook, and write your answers in `quiz.md` and `worksheet.md`.
- Commit checkpoints as you go ([Part 6](../01-StartHere/Part-06.md), step 9).

### 3. Restart & Run All, then save

For **each** notebook:

1. **Restart** the kernel and **Run All**.
2. Make sure every cell runs, top to bottom, with no errors. Run All stops at the first error, so one broken cell hides everything after it.
3. **Save** the notebook **with its outputs**. Don't use *Clear All Outputs* before turning it in.

### 4. Move the finished module into `03-Completed/`

Drag the **whole module folder** from `Work/` into `03-Completed/`. You should end up with `03-Completed/05-Foundations/`, and the folder should be gone from `Work/`.

Then open one notebook from its new location and Restart & Run All again, to make sure it still works there.

### 5. Check your submission

From the top of your repository, run this in the VS Code terminal (`python check_completed.py` after saving it as a file, or paste it into a notebook cell):

```python
from pathlib import Path

for module in sorted(p for p in Path('03-Completed').iterdir() if p.is_dir()):
    original = Path('02-Assignments') / module.name
    if not original.is_dir():
        print(f'❌ {module.name}: no folder with this name in 02-Assignments (check the spelling)')
        continue
    required = sorted(p.name for p in original.iterdir()
                      if p.suffix == '.ipynb' or p.name in ('quiz.md', 'worksheet.md'))
    missing = [name for name in required if not (module / name).exists()]
    extra = sorted(p.name for p in module.iterdir()
                   if p.suffix == '.ipynb' and not (original / p.name).exists())
    if missing or extra:
        print(f'❌ {module.name}')
        for name in missing: print(f'     missing:          {name}')
        for name in extra:   print(f'     unexpected name:  {name}')
    else:
        print(f'✅ {module.name}: all {len(required)} required files present')
```

Every module you've turned in should show ✅. A ❌ tells you exactly which file is missing or misnamed.

> If you paste it into a notebook cell, the notebook must be open from the **top** of your repository, or the paths won't match. Running it as a `.py` file from the repository's top folder is simplest.

### 6. Commit and push

Stage just this module's move, commit, and push when instructed:

```bash
git add -A -- "Work/05-Foundations" "03-Completed/05-Foundations"
git commit -m "Complete Module 05 Foundations"
git push origin main
```

Then open your repository on GitHub and confirm the module folder is under `03-Completed/`. See [Part 6](../01-StartHere/Part-06.md), steps 14–20, for the full review-and-push checklist.

---

## 🚫 Things That Break the Checker

| Don't...                                                                                     | Because...                                                                                                                    |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Rename a file, even a little (`01-Lists_done.ipynb`, `01-lists.ipynb`, `01-Lists (1).ipynb`) | The checker looks for the **exact** original name, including capital letters                                                  |
| Leave a `… copy.ipynb` duplicate                                                             | VS Code names a pasted file `… copy` when the original is in the same folder. Make sure the final file has the original name. |
| Rename the module folder (`05-foundations`, `05-Foundations-Smith`, `Module5`)               | The folder name must match `02-Assignments` exactly                                                                           |
| Nest folders (`03-Completed/05-Foundations/05-Foundations/…`)                                | Happens when you drag a folder *into* a folder that already has its name. There should be exactly one level.                  |
| Move notebooks out of their module folder, or put several modules in one folder              | Each notebook must sit in its own module's folder                                                                             |
| Turn in only an export (`.html`, `.pdf`, `.py`) or a `.zip`                                  | The checker reads the `.ipynb` files themselves                                                                               |
| Clear the outputs before turning in                                                          | The outputs are part of what shows your notebook ran                                                                          |
| Delete `quiz.md`, `worksheet.md`, or an `NN-OutputFiles` folder                              | These are required                                                                                                            |
| Edit the originals in `02-Assignments/`                                                      | It causes merge conflicts when you pull instructor updates                                                                    |

---

## ✅ Turn-In Checklist (per module)

- [ ] The module folder is in `03-Completed/`, with **exactly** the same name as in `02-Assignments/`.
- [ ] Every notebook is there, with its **original name**, and nothing renamed or duplicated.
- [ ] Every notebook was **Restart & Run All**'d without errors, and saved with its outputs.
- [ ] `quiz.md` and `worksheet.md` are there, with my answers written in.
- [ ] (Module 05) Every `NN-OutputFiles` folder and `Quiz-OutputFiles` is there.
- [ ] The check script shows ✅ for this module.
- [ ] I committed, pushed (when instructed), and saw the module under `03-Completed/` on GitHub.
