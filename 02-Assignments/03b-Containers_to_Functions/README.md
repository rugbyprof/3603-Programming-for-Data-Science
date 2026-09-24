# 📂 Module 03b: Containers → Functions

This module is a bridge between **Python Containers** and **Functions**. It goes back over lists, tuples, dictionaries, and sets, slowly and one problem at a time. Then it shows why functions exist and has you use them to process those containers.

The goal isn't *"know lists, dictionaries, sets, tuples, and functions."* It's this:

> **Take a problem, decide how to store its data, break the work into functions, and pass data between those functions.**

---

## 🔗 Assignments

| Notebook | Description |
|----------|-------------|
| [01-Too_Many_Variables.ipynb](01-Too_Many_Variables.ipynb) | Why lists exist, indexing and `len()` by prediction, tracing a `for` loop by hand, and the three core patterns: **Accumulate**, **Count**, **Filter**. |
| [02-Pick_Your_Container.ipynb](02-Pick_Your_Container.ipynb) | List, tuple, dictionary, and set, each introduced as the fix for a problem. Includes the *Pick Your Weapon* activity and taking nested expressions like `students[1]["grade"]` apart step by step. |
| [03-Why_Functions.ipynb](03-Why_Functions.ipynb) | From copy/paste to `def`. Defining vs. calling, parameter vs. argument, "a call becomes its return value," and **`print()` vs. `return`**. |
| [04-Mystery_Functions.ipynb](04-Mystery_Functions.ipynb) | Read before you write: Predict → Trace → Run → Explain → Modify. One function turned into many variations, a Broken Function Clinic, and Mutation Detective. |
| [05-Containers_Meet_Functions.ipynb](05-Containers_Meet_Functions.ipynb) | Write the contract first. Rebuild `sum`/`len`/`min`/`max` yourself, then build a toolkit of functions that turn a list into a number, a bool, a list, or a dictionary. Test design. |
| [06-Pipelines.ipynb](06-Pipelines.ipynb) | Refactor a blob into small functions and connect them into a pipeline. Includes a pipeline over a list of dictionaries and a team pipeline activity. |

Each notebook ends with an optional **🔥 Challenge** section. Skipping it won't hurt you later in the course.

---

## 🔁 How These Notebooks Work

Most examples follow the same routine:

```text
Predict → Trace → Run → Explain → Modify → Write
```

When you see **✍️ My prediction**, write your guess **before** running the next cell. A wrong prediction is fine. Skipping the prediction is the only way to get nothing out of it.

---

## 🧭 The Mantra

```text
Where is my data?
What shape is my data?
What needs to happen to it?
Can that operation become a function?
What goes in?
What comes out?
```

---

## 🧠 Learning Goals

- Explain *why* containers and functions exist, not just how to type them
- Choose list / tuple / dictionary / set for a scenario and defend the choice
- Evaluate nested expressions one step at a time
- Recognize and write the Accumulate, Count, Filter, and Best So Far patterns
- Define and call functions; use *parameter*, *argument*, and *return value* correctly
- Explain `print()` vs. `return` and why `None` shows up when you get it wrong
- Write a function's contract (in / out / does) before its code
- Write functions that turn containers into numbers, bools, lists, and dictionaries
- Predict which operations change a list and which build a new one
- Break a long block of code into functions and connect them into a pipeline

---

## 📚 Also in this module

- [glossary.md](glossary.md) — key terms
- [quiz.md](quiz.md) — 24-question self-check with an answer key
- [worksheet.md](worksheet.md) — paper tracing and reflection prompts

**Before this:** [03-Python_Containers](../03-Python_Containers/README.md)  
**After this:** [04-More_Functions_and_Loops](../04-More_Functions_and_Loops/README.md) (default and keyword arguments, scope, `while` loops, reading files)
