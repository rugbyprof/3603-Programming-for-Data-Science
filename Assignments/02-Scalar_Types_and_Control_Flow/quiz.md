# 📝 Quiz: 02 - Scalar Types and Control Flow

22 questions covering scalar types, arithmetic/casting, control flow, and the "going further" topics from the Challenge sections. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — Scalar Types

**1.** (Multiple Choice) What does `type(True)` return?
A) `bool`  B) `int`  C) `str`  D) `NoneType`

**2.** (Code Tracing) What prints?
```python
x = 10
print(type(x))
```

**3.** (Short Answer) What scalar type would best represent: a person's name, their age, and whether they passed a test?

**4.** (Code Tracing) What prints?
```python
print(int('21') + 1)
```

**5.** (True/False) `input()` always returns a string, even if the user types a number.

---

## Section B — Arithmetic and Casting

**6.** (Code Tracing) What prints?
```python
print(17 // 5)
```

**7.** (Code Tracing) What prints?
```python
print(17 % 5)
```

**8.** (Multiple Choice) Which operator raises a number to a power?
A) `^`  B) `**`  C) `//`  D) `%%`

**9.** (Short Answer) `'5' + '5'` does **not** produce `10`. What does it produce, and why?

---

## Section C — Control Flow

**10.** (Code Tracing) What prints?
```python
x = 7
print(x >= 7 and x < 10)
```

**11.** (Short Answer) What does the `not` operator do to a boolean expression?

**12.** (Fill in the Blank) What operator belongs in the blank to check for equality?
```python
if score ___ 100:
    print("Perfect score!")
```

**13.** (Multiple Choice) Which keyword adds an additional condition after an initial `if`?
A) `else`  B) `elseif`  C) `elif`  D) `when`

**14.** (Code Tracing) What prints?
```python
score = 85
print(0 <= score <= 100)
```

**15.** (True/False) Python uses indentation (whitespace) to define code blocks — it's not just a style choice.

**16.** (Short Answer) `and` requires every condition to be True to return True. What does `or` require?

---

## Section D — Going Further (Bonus)

**17.** (Short Answer) Rewrite this as a one-line conditional expression:
```python
if age >= 18:
    status = 'adult'
else:
    status = 'minor'
```

**18.** (Short Answer) Why is comparing two floats with `==` risky? Give an example.

**19.** (Short Answer) What two keywords did Python 3.10 add for structural pattern matching?

**20.** (Code Tracing) What prints?
```python
print('A' <= 'B' <= 'C')
```

**21.** (Code Tracing) What prints (both words, on one line)?
```python
balance = 500
if balance >= 1000:
    tier = 'Gold'
    perk = 'Free shipping'
else:
    tier = 'Standard'
    perk = 'No perks yet'

print(tier, perk)
```

**22.** (Short Answer, C++ Comparison) In C++, `0 <= score <= 100` compiles without any error, but doesn't check what you'd think. If `score = 150`, what does this condition actually evaluate to, and why?

---

## ✅ Answer Key

1. **A** — `bool`.
2. `<class 'int'>`
3. `str` for name, `int` for age, `bool` for whether they passed.
4. `22` — `int('21')` converts the string to `21`, then `+ 1` makes `22`.
5. **True**.
6. `3` — floor division drops the remainder (`17 / 5 = 3.4`, floored to `3`).
7. `2` — the remainder of `17 / 5`.
8. **B** — `**`.
9. `'55'` — with two strings, `+` concatenates them instead of adding numbers.
10. `True`.
11. It flips the value: `not True` is `False`, and `not False` is `True`.
12. `==`
13. **C** — `elif`.
14. `True` — chained comparisons check both sides at once.
15. **True**.
16. `or` requires at least one condition to be True.
17. `status = 'adult' if age >= 18 else 'minor'`
18. Floats are stored in binary, so most decimal fractions (like `0.1` or `0.2`) can't be represented exactly — e.g. `0.1 + 0.2 == 0.3` is `False` in Python, even though it looks like it should be `True`.
19. `match` and `case`.
20. `True`.
21. `Standard No perks yet` — `balance` is only `500`, so the `else` branch runs, setting both `tier` and `perk` before the `print()` after the block.
22. It always evaluates to `true`, regardless of `score`. C++ evaluates left to right: `(0 <= score)` produces a `bool`, which gets silently converted to `0` or `1` (an `int`). That `0`/`1` is then compared with `<= 100`, which is always true. The condition never actually checks the upper bound — the correct C++ requires `0 <= score && score <= 100`.
