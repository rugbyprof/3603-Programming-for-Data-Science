# 📝 Quiz: 03 - Strings and Text

20 questions covering string basics, string methods, formatted strings (f-strings), and the "going further" topics from the Challenge sections. Mix of multiple choice, true/false, code-tracing, and short answer.

Try every question on your own first — the Answer Key is at the bottom, no peeking. If you're using an AI tutor, paste in *your answer* and ask it to check your reasoning rather than asking it to solve the question first.

---

## Section A — String Basics

**1.** (Multiple Choice) Which of these lets you write a string that spans multiple lines without using `\n`?
A) `'...'`  B) `"..."`  C) `'''...'''`  D) `f'...'`

**2.** (Code Tracing) What prints?
```python
word = 'Python'
print(word[-1])
```

**3.** (Code Tracing) What prints?
```python
word = 'Python'
print(word[::-1])
```

**4.** (True/False) Writing `'It's a test'` (an unescaped apostrophe inside single quotes) causes an error.

**5.** (Short Answer) Why can't you run `word[0] = 'J'` if `word` is a string?

**6.** (Code Tracing) What does this print (describe the spacing)?
```python
print('Hi\tThere')
```

---

## Section B — String Methods

**7.** (Code Tracing) What prints?
```python
print('  Ada  '.strip())
```

**8.** (Code Tracing) What prints?
```python
print('the quick brown fox'.split())
```

**9.** (Short Answer) What's the difference between using `.find()` and using the `in` keyword to check whether a substring is present?

**10.** (Multiple Choice) Which method checks whether a string contains only digit characters?
A) `.isdigit()`  B) `.isalpha()`  C) `.find()`  D) `.strip()`

**11.** (Code Tracing) What prints?
```python
print('hello.py'.endswith('.py'))
```

**12.** (Short Answer) What does `'a,b,c'.split(',')` return?

---

## Section C — Formatted Strings

**13.** (Code Tracing) What prints?
```python
price = 9.5
print(f'{price:.2f}')
```

**14.** (Code Tracing) What prints?
```python
print(f'{1234567:,}')
```

**15.** (Short Answer) What does the `f` at the front of an f-string actually do?

**16.** (Multiple Choice) Which format spec right-aligns a value in a 10-character field?
A) `:<10`  B) `:>10`  C) `:^10`  D) `:10>`

**17.** (Code Tracing) What prints?
```python
x = 5
print(f'{x * 2}')
```

**18.** (Short Answer) Name the two older string-formatting styles that predate f-strings (still seen in older code).

---

## Section D — Going Further (Bonus)

**19.** (Short Answer) What does prefixing a string with `r` (a raw string) do, and why is it especially useful for Windows file paths?

**20.** (Code Tracing) What prints?
```python
x = 7
print(f'{x=}')
```

---

## ✅ Answer Key

1. **C** — triple-quoted strings.
2. `n`
3. `nohtyP`
4. **True** — Python sees the apostrophe as closing the string early, leaving invalid syntax after it.
5. Strings are immutable — once created, individual characters can't be reassigned. You have to build a new string instead (e.g. `'J' + word[1:]`).
6. `Hi`, then a tab, then `There` — the `\t` inserts a tab character, not the literal text `\t`.
7. `Ada` — leading and trailing spaces are removed.
8. `['the', 'quick', 'brown', 'fox']`
9. `.find()` returns the *index* where the substring starts (or `-1` if missing); `in` just gives you `True`/`False`.
10. **A** — `.isdigit()`.
11. `True`.
12. `['a', 'b', 'c']`
13. `9.50`
14. `1,234,567`
15. It marks the string as an f-string, meaning anything inside `{}` is evaluated as a Python expression and inserted into the string.
16. **B** — `:>10`.
17. `10`
18. `.format()` and `%`-style formatting (the `%` operator).
19. It disables escape-character processing, so backslashes are treated as literal characters instead of the start of an escape sequence — e.g. `r'C:\Users\name'` doesn't need `\\` for every backslash, and you don't risk accidentally typing a real escape sequence like `\n`.
20. `x=7` — the `=` debug spec prints both the expression text and its value.
