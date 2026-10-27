<div align="center">

# 🐍 Python Assignments — Week 1

### Strings • Lists • Tuples • Sets • Dictionaries • Problem Solving

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-2E8B57?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Python%20Fundamentals-orange?style=for-the-badge)

**A collection of Week 1 Python practice assignments focused on core language fundamentals, string operations, and built-in data structures.**

</div>

---

## 📚 Table of Contents

- [Project Overview](#-project-overview)
- [Learning Objectives](#-learning-objectives)
- [Assignment Files](#-assignment-files)
- [Topics Covered](#-topics-covered)
- [How the Code Works](#-how-the-code-works)
- [Requirements](#-requirements)
- [Run the Assignments](#-run-the-assignments)
- [Practice and Validation](#-practice-and-validation)
- [Suggested Improvements](#-suggested-improvements)
- [Learning Outcomes](#-learning-outcomes)
- [Author](#-author)

## 🔎 Project Overview

This folder contains Python assignments completed as part of Week 1 practice. The exercises build a foundation in writing Python statements, working with text, storing collections of values, and solving small programming problems.

The assignments use short, focused examples that print results to the terminal. They are intended for learning and practice rather than as a packaged application. Running the scripts and changing the example values is a useful way to understand how Python behaves.

## 🎯 Learning Objectives

- Understand basic Python syntax and expressions.
- Work with strings and common string methods.
- Use indexing and slicing to access values.
- Create and manipulate lists and tuples.
- Understand sets and dictionaries.
- Use loops and conditional statements.
- Apply list comprehensions to concise transformations.
- Sort collections and remove duplicate values.
- Practice membership checks, counting, and unpacking.
- Read output, identify mistakes, and improve code readability.

## 🗂️ Assignment Files

| File | Description |
|---|---|
| `20-Assignment-Question-For-PythonStringOperation-Beginner-and-Intermediate-Level.py` | String fundamentals and intermediate exercises, including case conversion, counting, indexing, substring checks, slicing, replacing, splitting, joining, and other text operations. |
| `40-Assignment-Question-For-PythonDataStructure-List-Tuples-Set-Dictionary-BeginerLevel.py` | Beginner exercises for Python lists, tuples, sets, and dictionaries, covering common operations and collection behavior. |
| `3Assiment.py` | Additional practice problems, including list comprehensions, sorting without changing the original list, and removing duplicates while preserving order. |

## 🧠 Topics Covered

### 1. String operations

Strings represent text in Python. The exercises practice methods and operations such as:

- `upper()` and `lower()` — change letter case.
- `count()` — count occurrences of a substring.
- Indexing such as `text[0]` and `text[-1]` — access characters.
- Slicing such as `text[0:5]` — select part of a string.
- `replace()` — replace one substring with another.
- `split()` and `join()` — divide text into parts and combine strings.
- `strip()` — remove leading and trailing whitespace.
- Membership checks using `in` — check whether a substring exists.

### 2. Lists

Lists are ordered, mutable collections. The assignments practise:

- Accessing items by index.
- Finding the number of items with `len()`.
- Adding values with `append()` and `insert()`.
- Removing values with `remove()` and `pop()`.
- Checking membership with `in`.
- Slicing, counting, and updating elements.
- Sorting values and creating new lists.

### 3. Tuples

Tuples are ordered collections that cannot be changed after creation. Exercises cover:

- Indexing and length.
- Tuple unpacking.
- Membership checks.
- Concatenation and repetition.
- Finding an item's index and counting occurrences.
- Creating an empty tuple and checking its type.

### 4. Sets

Sets store unique elements. They are useful when duplicate values should be removed and for operations such as union, intersection, and difference. Review the set exercises to understand uniqueness and the fact that sets do not guarantee a display order.

### 5. Dictionaries

Dictionaries store key-value pairs. Typical beginner operations include creating a dictionary, reading or updating a value by key, checking whether a key exists, and inspecting keys, values, and items.

### 6. List comprehensions and problem solving

List comprehensions provide a concise way to build a list from an iterable, optionally applying a condition. For example:

```python
# Squares of even numbers from 0 through 20
squares = [number ** 2 for number in range(21) if number % 2 == 0]
print(squares)
```

The additional exercises also demonstrate how `sorted()` returns a new sorted list and how `dict.fromkeys()` can remove duplicates while retaining first-occurrence order for hashable values.

## 🔄 Recommended Learning Workflow

1. Open one assignment file in VS Code.
2. Read the question or comment above each code block.
3. Predict the output before running the code.
4. Run the script and compare the actual output with your prediction.
5. Change the sample values and run it again.
6. Try solving the same problem with a different method.
7. Add clear variable names and comments where they improve understanding.
8. Test edge cases, such as an empty string, an empty list, repeated values, or a missing dictionary key.

## ⚙️ Requirements

- Python 3.10 or later recommended.
- VS Code or another Python editor.
- A terminal or command prompt.

These assignments primarily use Python's built-in features, so external packages are not normally required.

## ▶️ Run the Assignments

### 1. Clone the repository

```bash
git clone https://github.com/azhar-data/Nexskill_project.git
cd Nexskill_project
```

### 2. Run a script from the repository root

Windows, macOS, or Linux terminal:

```bash
python "1. Assigment week 1/3Assiment.py"
python "1. Assigment week 1/20-Assignment-Question-For-PythonStringOperation-Beginner-and-Intermediate-Level.py"
python "1. Assigment week 1/40-Assignment-Question-For-PythonDataStructure-List-Tuples-Set-Dictionary-BeginerLevel.py"
```

If your system uses `python3` to launch Python, replace `python` with `python3`. In VS Code, you can also open a file and select **Run Python File** after choosing the correct Python interpreter.

## 🧪 Practice and Validation

Use these questions to check your understanding:

- What is the difference between `append()` and `insert()`?
- How does `sorted(my_list)` differ from `my_list.sort()`?
- Why does `text[-1]` access the last character?
- What is the difference between a list and a tuple?
- Why does a set remove duplicate values?
- How can a dictionary value be accessed safely when a key might not exist?
- What does the condition `number % 2 == 0` check?
- How does `dict.fromkeys()` help preserve the order of unique values?

**Tip:** Try answering these without looking at the code first, then verify by running small experiments.

## ⚠️ Coding Notes

- Python is case-sensitive: `Name` and `name` are different identifiers.
- Indentation is important, especially inside loops and conditional blocks.
- String indexes start at zero; negative indexes count from the end.
- `remove(value)` removes a matching value, while `pop(index)` removes and returns an item.
- `sorted()` creates a new sorted list; `.sort()` modifies a list in place.
- A string's `join()` method uses the string before the dot as the separator.
- Sets are unordered; do not rely on their printed order.
- Variable names such as `list`, `str`, and `dict` should generally be avoided because they shadow Python's built-in types.
- In exercises involving vowels and consonants, check alphabetic characters with `isalpha()` before classifying them; spaces and punctuation are not consonants.

## 🚀 Suggested Improvements

- [ ] Add sample expected output for each exercise.
- [ ] Organize the assignments into separate topic sections.
- [ ] Correct spelling and improve consistency in file names over time.
- [ ] Add functions for exercises that are repeated or complex.
- [ ] Add input-based versions so users can test their own values.
- [ ] Add simple unit tests for important edge cases.
- [ ] Include a progress checklist for each topic.
- [ ] Add a Week 1 summary notebook with explanations and examples.

## 🎓 Learning Outcomes

By completing these exercises, learners gain practice with Python strings, built-in collections, indexing, slicing, iteration, conditions, list comprehensions, and basic algorithmic thinking. These skills form a foundation for later study of NumPy, Pandas, data analysis, web scraping, and machine learning.

## 👨‍💻 Author

**Muhammad Azhar**  
Python • Data Analysis • Data Science • Machine Learning

- GitHub: [@azhar-data](https://github.com/azhar-data)
- Repository: [Nexskill_project](https://github.com/azhar-data/Nexskill_project)

---

<div align="center">Practice consistently. Understand the logic. Build stronger Python foundations.</div>
