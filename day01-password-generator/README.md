# Day 01 — Password Generator 🔐

A command-line tool that generates secure random passwords with customizable length and character options.

---

## 🚀 How to Run

```bash
python password_generator.py
```

No external libraries needed — uses Python standard library only.

---

## ✨ Features

- Custom password length
- Toggle symbols on/off
- Generate multiple passwords at once
- Works entirely from the terminal

---

## 📸 Demo

```
=== Password Generator ===
Password length (default 12): 16
Include symbols? (y/n, default y): y
How many passwords? (default 1): 3

Generated passwords:
  1. tR#8kLm@2Xv!qP9w
  2. Jn$5eWz&7Yd@cF3m
  3. Qb!2sHx#4Rk@nM8p
```

---

## 🧠 Concepts Used

- `random.choice()` — picking random characters
- `string` module — `ascii_letters`, `digits`, `punctuation`
- Functions with default parameters
- `try/except` for input validation
- f-strings for formatted output

---

## 📁 Files

| File | Description |
|------|-------------|
| `password_generator.py` | Main script |
| `README.md` | This file |

---

## 💡 Possible Improvements

- Save generated passwords to a `.txt` file
- Add a strength meter (weak / medium / strong)
- Build a GUI version with Tkinter
- Exclude ambiguous characters like `0`, `O`, `l`, `1`

---

*Part of my [30 Days of Python](https://github.com/nawalnaqvii/30-days-python-projects) challenge.*