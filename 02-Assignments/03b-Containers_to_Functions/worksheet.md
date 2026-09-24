# 📝 Worksheet: 03b - Containers → Functions

Do this worksheet **on paper, without a computer**. The point is to practice being the computer. Each section ends with an **🤖 Explain It** prompt: write your explanation in your own words, then (optionally) paste it into an AI tutor and ask it to point out anything you got wrong or left out.

---

## 🧠 Section 1: Trace a Loop

Fill in the table for this code:

```python
temps = [31, 45, 28, 52]
total = 0
count = 0
for t in temps:
    total += t
    if t <= 32:
        count += 1
```

| pass | `t` | `total` | `count` |
|------|-----|---------|---------|
| start | — | 0 | 0 |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

Which **two** patterns are mixed together in this loop?  
`Answer:` ____________________________

> 🤖 **Explain It:** Explain the difference between Accumulate, Count, and Filter as if you were talking to someone who has never programmed.

---

## 🧠 Section 2: Pick Your Weapon

| Scenario | Container | Why? |
|----------|-----------|------|
| Daily step counts for a month | | |
| A playing card (rank, suit) | | |
| Username → password hash | | |
| Every distinct IP address in a log file | | |
| Your class schedule, in order | | |

> 🤖 **Explain It:** Pick the scenario you were *least* sure about and argue for a different container than the one you chose.

---

## 🧠 Section 3: Take It Apart

```python
course = {
    "title": "CMPS 3603",
    "students": [
        {"name": "Ana", "scores": [88, 92]},
        {"name": "Ben", "scores": [75, 81]}
    ]
}
```

Write the value after **each** step:

1. `course["students"]` → ____________________________
2. `course["students"][1]` → ____________________________
3. `course["students"][1]["scores"]` → ____________________________
4. `course["students"][1]["scores"][0]` → ____________________________

Write the expression that gets Ana's second score:  
`Answer:` ____________________________

---

## 🧠 Section 4: Functions

1. What prints?

```python
def f(x):
    return x + 1

print(f(f(f(0))))
```

   `Answer:` ____________________________

2. What prints? Explain why.

```python
def shout(word):
    print(word.upper())

x = shout("hi")
print(x)
```

   `Answer:` ____________________________

3. Circle the **parameters** and underline the **arguments**:

```python
def greet(name, greeting):
    return greeting + ", " + name

greet("Ada", "Hello")
```

> 🤖 **Explain It:** In your own words, explain `print()` vs. `return`. Then explain why getting it wrong breaks a pipeline.

---

## 🧠 Section 5: Contracts and Tests

Write a contract for a function `longest_word(words)`:

```text
IN:
OUT:
DOES:
```

Write one test of each kind:

- Normal: ____________________________
- Boundary: ____________________________
- Weird: ____________________________

---

## 🧠 Section 6: Draw the Pipeline

> "Given a list of prices, drop any that are `0` or less, add 8.25% tax to each, then find the total."

1. Name each function you'd need.
2. For each one, write what goes **in** and what comes **out** (shape, not just "data").
3. Draw the pipeline with arrows, labeling each arrow with the data's shape.

> 🤖 **Explain It:** Why is a pipeline of small functions easier to fix than one big block of code?
