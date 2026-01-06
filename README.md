# 🐍 Python Foundations

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

**A comprehensive 20-day journey from Python beginner to confident programmer**

*Part of the AI-ML-Journey: Zero to Hero in AI/ML*

[Getting Started](#-getting-started) •
[Roadmap](#-20-day-learning-roadmap) •
[Structure](#-folder-structure) •
[How to Learn](#-how-to-get-the-best-out-of-this-guide)

</div>

---

## 🎯 What is This?

This is **Branch 00: Python Foundations** — the first step in your AI/ML journey. Before diving into Machine Learning, Deep Learning, and AI, you need a solid foundation in Python. This branch covers everything you need to know about Python programming, structured as a **20-day learning path**.

Each day builds upon the previous, taking you from basic syntax to advanced concepts like generators and iterators. By the end, you'll have the Python skills required for data science and machine learning.

---

## ✨ Features

- 📚 **Comprehensive Coverage** — From strings to advanced iterators
- 🎓 **Beginner Friendly** — No prior programming experience required
- 💻 **Hands-On Practice** — Every file includes practice exercises with solutions
- 🧠 **ML/AI Context** — Examples relate to real-world data science applications
- 📝 **Well Documented** — Extensive comments and explanations in every file
- 🔄 **Git-Based Learning** — Follow along commit by commit

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher installed ([Download Python](https://www.python.org/downloads/))
- A code editor (VS Code recommended)
- Basic computer skills
- Git installed (for following the commit history)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-ML-Journey.git

# Navigate to the project
cd AI-ML-Journey

# Switch to Python Foundations branch
git checkout 00-Python-Foundations

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Running the Files

```bash
# Run any Python file
python 1_basics/1_strings.py

# Or navigate to the folder first
cd 1_basics
python 1_strings.py
```

---

## 📅 20-Day Learning Roadmap

Follow the commits in order! Each commit is labeled with the day number for easy navigation.

### Week 1: Python Basics 🌱

| Day | Topic | File | What You'll Learn |
|-----|-------|------|-------------------|
| 1 | Strings | `1_basics/1_strings.py` | String creation, methods, slicing, formatting basics |
| 2 | Numbers | `1_basics/2_integers_and_floats.py` | Integers, floats, arithmetic, type conversion |
| 3 | Collections I | `1_basics/3_lists_tuples_and_sets.py` | Lists, tuples, sets, when to use each |
| 4 | Collections II | `1_basics/4_dictionaries.py` | Dictionaries, key-value pairs, nested dicts |
| 5 | Modules | `7_modules/1_imports_and_modules.py` | Importing, creating modules, packages |
| 6 | Slicing | `1_basics/5_slicing.py` | Advanced slicing, negative indices, step |
| 7 | Sorting | `1_basics/6_sorting.py` | sort(), sorted(), custom key functions |

### Week 2: Control Flow & Functions 🔄

| Day | Topic | File | What You'll Learn |
|-----|-------|------|-------------------|
| 8 | String Formatting | `1_basics/7_string_formatting.py` | f-strings, .format(), % formatting |
| 9 | Conditionals | `2_control-flow/1_conditionals_and_booleans.py` | if/elif/else, boolean logic, comparisons |
| 10 | OS Module | `7_modules/2_os.py` | File system operations, paths, directories |
| 11 | DateTime | `7_modules/3_datetime.py` | Dates, times, timezones, formatting |
| 12 | File Handling | `5_file-handling/1_file_operations.py` | Reading, writing, context managers |
| 13 | Error Handling | `6_error-handling/1_exceptions.py` | try/except, raising exceptions, custom errors |
| 14 | Generators | `8_advanced/1_generators.py` | yield, generator expressions, memory efficiency |

### Week 3: Object-Oriented Programming 🏗️

| Day | Topic | File(s) | What You'll Learn |
|-----|-------|---------|-------------------|
| 15 | Classes & Instances | `4_oop/1_classes_and_instances.py` | Classes, objects, __init__, self |
| 16 | Class Variables & Methods | `4_oop/2_class_variables.py`, `4_oop/3_class_and_static_methods.py` | Class vs instance vars, @classmethod, @staticmethod |
| 17 | Inheritance | `4_oop/4_inheritance.py` | Subclasses, super(), method overriding |
| 18 | Special Methods | `4_oop/5_special_methods.py`, `4_oop/6_property_decorators.py` | Dunder methods, @property, getters/setters |
| 19 | JSON & APIs | `5_file-handling/2_handling_json.py`, `5_file-handling/3_api.py` | JSON parsing, REST APIs, data fetching |
| 20 | Iterators | `8_advanced/2_iterators_and_iterables.py` | Iterator protocol, custom iterators |

---

## 📁 Folder Structure

```
00-Python-Foundations/
│
├── 📂 1_basics/                    # Days 1-4, 6-8
│   ├── 1_strings.py               # String manipulation
│   ├── 2_integers_and_floats.py   # Numeric types
│   ├── 3_lists_tuples_and_sets.py # Collection types
│   ├── 4_dictionaries.py          # Key-value mappings
│   ├── 5_slicing.py               # Sequence slicing
│   ├── 6_sorting.py               # Sorting algorithms
│   └── 7_string_formatting.py     # Output formatting
│
├── 📂 2_control-flow/              # Day 9
│   ├── 1_conditionals_and_booleans.py
│   ├── 2_loops_and_iterations.py
│   └── 3_comprehensions.py
│
├── 📂 3_functions/                 # Covered within other days
│   ├── 1_functions.py
│   └── 2_scope.py
│
├── 📂 4_oop/                       # Days 15-18
│   ├── 1_classes_and_instances.py
│   ├── 2_class_variables.py
│   ├── 3_class_and_static_methods.py
│   ├── 4_inheritance.py
│   ├── 5_special_methods.py
│   └── 6_property_decorators.py
│
├── 📂 5_file-handling/             # Days 12, 19
│   ├── 1_file_operations.py
│   ├── 2_handling_json.py
│   └── 3_api.py
│
├── 📂 6_error-handling/            # Day 13
│   └── 1_exceptions.py
│
├── 📂 7_modules/                   # Days 5, 10-11
│   ├── 1_imports_and_modules.py
│   ├── 2_os.py
│   ├── 3_datetime.py
│   └── sample_module.py
│
├── 📂 8_advanced/                  # Days 14, 20
│   ├── 1_generators.py
│   └── 2_iterators_and_iterables.py
│
└── 📄 README.md                    # You are here!
```

---

## 📖 How to Get the Best Out of This Guide

### 🎯 For Complete Beginners

1. **Follow the day order** — Each day builds on previous concepts
2. **Type the code yourself** — Don't just copy-paste; muscle memory matters!
3. **Run every example** — See what the output looks like
4. **Do ALL exercises** — Check solutions only after attempting
5. **Take notes** — Write down concepts in your own words

### 🔄 Following Git Commits

Each commit represents one day's progress. To follow along:

```bash
# See all commits (days)
git log --oneline

# Output looks like:
# abc1234 Day 20: Iterators & Iterables ✅
# def5678 Day 19: JSON & APIs ✅
# ghi9012 Day 18: Special Methods & Properties ✅
# ...

# Go to a specific day
git checkout <commit-hash>

# Return to latest
git checkout 00-Python-Foundations
```

### 📝 Each File Contains

Every Python file in this repository follows this structure:

```
================================================================================
TOPIC TITLE
================================================================================
Day: X

Description: What this file covers
Learning Objectives: What you'll learn
Prerequisites: What you should know first
================================================================================

1. CONCEPT EXPLANATION
   - Theory with comments
   - Code examples

2. MORE CONCEPTS
   ...

PRACTICE EXERCISES
   - Easy, Medium, and Challenge problems
   - Solutions included (commented out)

COMMON MISTAKES TO AVOID
   - What not to do

KEY TAKEAWAYS
   - Summary of important points
================================================================================
```

### 💡 Tips for Success

| Do ✅ | Don't ❌ |
|------|---------|
| Code along with examples | Just read without coding |
| Experiment and break things | Be afraid to make errors |
| Complete exercises first, then check solutions | Look at solutions immediately |
| Take breaks (Pomodoro technique) | Marathon 8-hour sessions |
| Revisit difficult topics | Skip topics you don't understand |
| Build mini-projects | Only do tutorial exercises |

---

## 🏆 Learning Milestones

Track your progress! Check off each milestone as you complete it:

- [ ] **Week 1 Complete** — You understand Python basics, data types, and can work with collections
- [ ] **Week 2 Complete** — You can write functions, handle files, catch errors, and understand control flow
- [ ] **Week 3 Complete** — You understand OOP, can create classes, work with APIs, and write Pythonic code

---

## 🔗 What's Next?

After completing Python Foundations, you're ready for:

| Branch | Topics |
|--------|--------|
| `01-Data-Wrangling` | NumPy, Pandas, Data Cleaning |
| `02-Data-Visualization` | Matplotlib, Seaborn, Plotly |
| `03-Machine-Learning` | Scikit-learn, Algorithms |
| `04-Deep-Learning` | TensorFlow, PyTorch |

---

## 📚 Additional Resources

### Official Documentation
- [Python Official Docs](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Practice Platforms
- [LeetCode](https://leetcode.com/) — Coding challenges
- [HackerRank](https://www.hackerrank.com/domains/python) — Python practice
- [Codewars](https://www.codewars.com/) — Code katas

### Books (Optional)
- "Automate the Boring Stuff with Python" — Al Sweigart
- "Python Crash Course" — Eric Matthes
- "Fluent Python" — Luciano Ramalho (Advanced)

---

## 🤝 Contributing

Found a bug? Have a suggestion? Feel free to:
1. Open an issue
2. Submit a pull request
3. Star the repository if you find it helpful! ⭐

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Happy Learning! 🚀**

*Remember: The best way to learn programming is by programming.*

Made with ❤️ by Om Patel

</div>
