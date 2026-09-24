# 📂 Module 04: More Functions & Loops

Module 03b covered the core ideas: containers, the loop patterns, `def` / `return`, and pipelines. This module adds the tools that are still missing, and each one comes with the problem it solves:

- **Function extras:** default values, keyword arguments, returning a tuple, and scope
- **`while` loops:** for when you know *when to stop* but not *how many times*
- **Files:** reading real data from disk into the same pipelines you already know how to build

---

## 🔗 Assignments

| Notebook | Description |
|----------|-------------|
| [01-Function_Extras.ipynb](01-Function_Extras.ipynb) | Default parameter values, keyword arguments (like `sorted(..., reverse=True)`, and later Pandas' `ascending=False`), returning several values as a tuple, and local vs. global scope. |
| [02-While_Loops.ipynb](02-While_Loops.ipynb) | `while` loops (start / condition / update), infinite loops and how to stop them, choosing `for` vs. `while`, `break`, `continue`, and sentinel values. |
| [03-Looping_Over_Files.ipynb](03-Looping_Over_Files.ipynb) | `with open(...)`, looping over lines with `.strip()` / `.split()`, skipping messy lines, turning a file into a list of dictionaries, and `try` / `except FileNotFoundError`. |

Each notebook ends with an optional **🔥 Challenge** section. Skipping it won't hurt you later in the course.

---

## 🧠 Learning Goals

- Give parameters default values, and call functions with keyword arguments
- Return multiple values as a tuple and unpack them
- Explain local vs. global scope; pass data in through parameters and out through `return`
- Choose `for` vs. `while`, and write a `while` loop that is guaranteed to stop
- Use `break` and `continue` to control a loop
- Read a text file line by line and turn it into a list of dictionaries
- Handle a missing file with `try` / `except`

---

## 📚 Also in this module

- [glossary.md](glossary.md) — key terms
- [quiz.md](quiz.md) — 16-question self-check with an answer key
- [worksheet.md](worksheet.md) — paper tracing and reflection prompts

**Before this:** [03b-Containers_to_Functions](../03b-Containers_to_Functions/README.md)  
**After this:** [06-Foundations](../06-Foundations/README.md)

> The previous `04-Functions` and `05-Loops_and_Iteration` modules are archived in [04-Resources/Archive](../../04-Resources/Archive/). `*args` / `**kwargs`, type-based behavior, `enumerate()` / `zip()`, and nested loops are all still there if you want extra reading.
