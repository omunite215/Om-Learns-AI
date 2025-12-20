"""
================================================================================
PYTHON FUNDAMENTALS: IMPORTS AND MODULES
================================================================================
Day: 5

Description:
    Comprehensive guide to Python modules and imports. Covers importing modules,
    creating custom modules, understanding sys.path, exploring the standard
    library, and best practices for organizing code.

Learning Objectives:
    - Understand what modules are and why they're useful
    - Import modules using different techniques
    - Create and use custom modules
    - Understand how Python finds modules (sys.path)
    - Explore commonly used standard library modules
    - Follow best practices for imports

Prerequisites:
    - Basic Python syntax
    - Functions
================================================================================
"""

# =============================================================================
# 1. WHAT ARE MODULES?
# =============================================================================

"""
MODULES are Python files (.py) containing code (functions, classes, variables)
that can be reused in other Python files.

Why use modules?
- Code reusability: Write once, use everywhere
- Organization: Break large programs into smaller files
- Namespace: Avoid naming conflicts
- Maintainability: Easier to update and debug

Types of modules:
1. Built-in modules: Come with Python (math, os, sys, datetime)
2. Third-party modules: Installed via pip (numpy, pandas, sklearn)
3. Custom modules: Created by you
"""


# =============================================================================
# 2. IMPORTING ENTIRE MODULE
# =============================================================================

# --- Basic import ---
import math

# Access using module.function syntax
result = math.sqrt(16)
print(result)
# Output: 4.0

print(math.pi)
# Output: 3.141592653589793

print(math.floor(3.7))
# Output: 3

print(math.ceil(3.2))
# Output: 4

# Convert degrees to radians
radians = math.radians(90)
print(radians)
# Output: 1.5707963267948966 (π/2)

# --- Import with alias ---
import math as m

print(m.sqrt(25))
# Output: 5.0

# Alias is useful for long module names
# Common aliases: numpy as np, pandas as pd, matplotlib.pyplot as plt


# =============================================================================
# 3. IMPORTING SPECIFIC ITEMS
# =============================================================================

# --- Import specific function ---
from math import sqrt

# Now use directly without module prefix
print(sqrt(36))
# Output: 6.0

# --- Import multiple items ---
from math import sqrt, pi, floor, ceil

print(pi)
# Output: 3.141592653589793

print(floor(4.9))
# Output: 4

# --- Import with alias ---
from math import sqrt as square_root
from math import pi as PI

print(square_root(49))
# Output: 7.0

print(PI)
# Output: 3.141592653589793

# --- Import everything (NOT RECOMMENDED) ---
# from math import *
# This imports all public names from the module
# Problems:
# - Pollutes namespace
# - Can cause naming conflicts
# - Hard to track where functions come from


# =============================================================================
# 4. CUSTOM MODULES
# =============================================================================

"""
Create a file named 'sample_module.py' in the same directory:

-------- sample_module.py --------
print("Welcome to module")  # Runs when module is imported!

test = "Test string"

def find_index(to_search, target):
    '''Find the index of target in a list'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
----------------------------------
"""

# --- Importing custom module ---
# import sample_module

# Note: "Welcome to module" prints when imported!
# This is why we use if __name__ == "__main__" (covered later)

# --- Using custom module ---
# courses = ['History', 'Math', 'Physics', 'ComSci']
# index = sample_module.find_index(courses, 'Math')
# print(index)  # Output: 1
# print(sample_module.test)  # Output: Test string

# --- Import specific items from custom module ---
# from sample_module import find_index, test
# index = find_index(courses, 'Math')
# print(index)  # Output: 1

# --- Import with alias ---
# from sample_module import find_index as fi
# index = fi(courses, 'Math')


# =============================================================================
# 5. HOW PYTHON FINDS MODULES (sys.path)
# =============================================================================

import sys

# sys.path is a list of directories Python searches for modules
print("Python module search paths:")
for path in sys.path:
    print(f"  {path}")

"""
Python searches in this order:
1. Current directory (where script is running)
2. PYTHONPATH environment variable directories
3. Standard library directories
4. Site-packages (where pip installs)
"""

# --- Adding custom path ---
# sys.path.append('/path/to/your/modules')

# --- Check where a module is located ---
print(f"\nmath module location: {math.__file__}")


# =============================================================================
# 6. COMMONLY USED STANDARD LIBRARY MODULES
# =============================================================================

# --- datetime: Working with dates and times ---
import datetime

today = datetime.date.today()
print(f"Today's date: {today}")
# Output: Today's date: 2024-12-17

now = datetime.datetime.now()
print(f"Current datetime: {now}")
# Output: Current datetime: 2024-12-17 14:30:45.123456

# Create specific date
birthday = datetime.date(1995, 5, 15)
print(f"Birthday: {birthday}")

# Date arithmetic
days_until_new_year = datetime.date(2025, 1, 1) - today
print(f"Days until new year: {days_until_new_year.days}")


# --- calendar: Calendar operations ---
import calendar

# Check if year is leap year
print(f"Is 2024 a leap year? {calendar.isleap(2024)}")
# Output: Is 2024 a leap year? True

print(f"Is 2025 a leap year? {calendar.isleap(2025)}")
# Output: Is 2025 a leap year? False

# Print month calendar
print(calendar.month(2024, 12))


# --- os: Operating system interface ---
import os

# Current working directory
print(f"Current directory: {os.getcwd()}")

# List files in directory
print(f"Files: {os.listdir('.')}")

# Check if path exists
print(f"Does 'sample_module.py' exist? {os.path.exists('sample_module.py')}")

# Join paths (cross-platform)
full_path = os.path.join('folder', 'subfolder', 'file.txt')
print(f"Joined path: {full_path}")

# Get environment variables
print(f"Home directory: {os.environ.get('HOME', 'Not found')}")


# --- random: Generate random numbers ---
import random

# Random float between 0 and 1
print(f"Random float: {random.random()}")

# Random integer in range
print(f"Random int (1-10): {random.randint(1, 10)}")

# Random choice from list
colors = ['red', 'green', 'blue']
print(f"Random color: {random.choice(colors)}")

# Shuffle list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled: {numbers}")

# Random sample (without replacement)
print(f"Sample 3: {random.sample([1,2,3,4,5,6,7,8,9,10], 3)}")


# --- sys: System-specific parameters ---
import sys

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")

# Command line arguments
# print(f"Arguments: {sys.argv}")


# =============================================================================
# 7. THE __name__ VARIABLE
# =============================================================================

"""
Every module has a special __name__ variable:
- If module is run directly: __name__ = "__main__"
- If module is imported: __name__ = module's filename

This allows code to run only when file is executed directly.
"""

print(f"\nThis file's __name__: {__name__}")
# Output: __main__ (when run directly)

# --- Common pattern ---
def main():
    """Main function that runs when script is executed directly"""
    print("This runs only when script is executed directly")
    print("Not when imported as a module")

if __name__ == "__main__":
    main()

"""
In sample_module.py, you should add:

if __name__ == "__main__":
    # Test code here
    courses = ['History', 'Math', 'Physics']
    print(find_index(courses, 'Math'))
    
This prevents "Welcome to module" from printing when imported!
"""


# =============================================================================
# 8. PACKAGE STRUCTURE
# =============================================================================

"""
PACKAGES are directories containing multiple modules and a __init__.py file.

my_package/
├── __init__.py          # Makes it a package (can be empty)
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py

Importing from packages:
- import my_package.module1
- from my_package import module1
- from my_package.module1 import function_name
- from my_package.subpackage import module3
"""


# =============================================================================
# 9. RELATIVE VS ABSOLUTE IMPORTS
# =============================================================================

"""
ABSOLUTE IMPORTS: Full path from project root
- import my_package.module1
- from my_package.subpackage import module3

RELATIVE IMPORTS: Relative to current module (use dots)
- from . import module1          # Same directory
- from .. import module2         # Parent directory
- from ..subpackage import module3

Best Practice: Prefer absolute imports for clarity
"""


# =============================================================================
# 10. EXPLORING MODULES
# =============================================================================

import math

# --- dir(): List all attributes and methods ---
print("Math module contents:")
print(dir(math))
# Shows all functions, constants, etc. in the module

# --- Filter out private/dunder attributes ---
public_attrs = [attr for attr in dir(math) if not attr.startswith('_')]
print(f"\nPublic attributes: {public_attrs}")

# --- help(): Get documentation ---
# help(math)  # Full module documentation
# help(math.sqrt)  # Specific function documentation

# --- __doc__: Access docstring ---
print(f"\nmath.sqrt docstring: {math.sqrt.__doc__}")


# =============================================================================
# 11. IMPORTANT MODULES FOR AI/ML
# =============================================================================

"""
ESSENTIAL MODULES FOR YOUR AI/ML JOURNEY:

Standard Library:
- math: Mathematical functions
- random: Random number generation
- datetime: Date and time handling
- os: File system operations
- sys: System operations
- json: JSON parsing (for configs, APIs)
- csv: CSV file handling
- collections: Specialized data structures
- itertools: Efficient iteration

Third-Party (Install with pip):
- numpy: Numerical computing (arrays, linear algebra)
- pandas: Data manipulation and analysis
- matplotlib: Data visualization
- seaborn: Statistical visualization
- scikit-learn: Machine learning algorithms
- tensorflow/pytorch: Deep learning
- jupyter: Interactive notebooks

Installation:
pip install numpy pandas matplotlib seaborn scikit-learn
"""


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Import Styles
   - import module                    # Full module
   - import module as alias           # With alias
   - from module import item          # Specific item
   - from module import item as alias # Item with alias
   - from module import *             # All (avoid!)

2. Module Search Order (sys.path)
   - Current directory
   - PYTHONPATH
   - Standard library
   - Site-packages

3. Custom Modules
   - Any .py file can be a module
   - Use if __name__ == "__main__" for test code
   - Organize related code into packages

4. Standard Library Highlights
   - math: Mathematical operations
   - datetime: Date/time handling
   - os: File system operations
   - random: Random numbers
   - sys: System information

5. Best Practices
   - Use absolute imports
   - Avoid from module import *
   - Group imports: standard, third-party, local
   - Use aliases for long names (np, pd, plt)
   
6. Import Order Convention (PEP 8)
   1. Standard library imports
   2. Third-party imports
   3. Local application imports
   (Blank line between each group)
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Basic Import [EASY]
# Import the math module and calculate:
# a) Square root of 144
# b) 2 raised to power 10
# c) Ceiling of 4.2
# TODO: Write your code here

# Solution:
# import math
# print(math.sqrt(144))    # 12.0
# print(math.pow(2, 10))   # 1024.0
# print(math.ceil(4.2))    # 5


# Exercise 2: DateTime Operations [EASY]
# Using datetime module:
# a) Print current date and time
# b) Calculate your age in days
# c) Find what day of the week you were born
# TODO: Write your code here

# Solution:
# import datetime
# print(datetime.datetime.now())
# birthday = datetime.date(1995, 5, 15)  # Change to your birthday
# age_days = (datetime.date.today() - birthday).days
# print(f"Age in days: {age_days}")
# print(f"Born on: {birthday.strftime('%A')}")  # Day name


# Exercise 3: Create Custom Module [MEDIUM]
# Create a module called 'string_utils.py' with:
# a) Function to reverse a string
# b) Function to count vowels in a string
# c) A constant for vowels
# Then import and use it
# TODO: Write your code here

# Solution (create string_utils.py):
# VOWELS = 'aeiouAEIOU'
#
# def reverse_string(s):
#     return s[::-1]
#
# def count_vowels(s):
#     return sum(1 for char in s if char in VOWELS)
#
# if __name__ == "__main__":
#     print(reverse_string("hello"))
#     print(count_vowels("hello"))


# Exercise 4: Random Operations [MEDIUM]
# Using random module:
# a) Generate a random password of 8 characters (letters + digits)
# b) Simulate rolling two dice 10 times
# c) Pick 5 random lottery numbers (1-50, no repeats)
# TODO: Write your code here

# Solution:
# import random
# import string
#
# # a) Random password
# chars = string.ascii_letters + string.digits
# password = ''.join(random.choice(chars) for _ in range(8))
# print(f"Password: {password}")
#
# # b) Roll dice
# for i in range(10):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     print(f"Roll {i+1}: {dice1} + {dice2} = {dice1 + dice2}")
#
# # c) Lottery numbers
# lottery = random.sample(range(1, 51), 5)
# print(f"Lottery: {sorted(lottery)}")


# Exercise 5: OS Module Exploration [MEDIUM]
# Using os module:
# a) Print current working directory
# b) List all Python files in current directory
# c) Create a new directory called 'test_folder' (if not exists)
# d) Check if a file exists
# TODO: Write your code here

# Solution:
# import os
#
# print(f"CWD: {os.getcwd()}")
#
# py_files = [f for f in os.listdir('.') if f.endswith('.py')]
# print(f"Python files: {py_files}")
#
# if not os.path.exists('test_folder'):
#     os.makedirs('test_folder')
#     print("Created test_folder")
#
# print(f"sample_module.py exists: {os.path.exists('sample_module.py')}")


# Exercise 6: Module Inspector [CHALLENGE]
# Write a function that takes a module name (string)
# and prints all its public functions (not starting with _)
# Test with 'math' and 'random' modules
# TODO: Write your code here

# Solution:
# def inspect_module(module_name):
#     import importlib
#     module = importlib.import_module(module_name)
#     public_funcs = [name for name in dir(module) 
#                     if not name.startswith('_') and callable(getattr(module, name))]
#     print(f"\nPublic functions in {module_name}:")
#     for func in public_funcs:
#         print(f"  - {func}")
#
# inspect_module('math')
# inspect_module('random')


# Exercise 7: Package Creator [CHALLENGE]
# Create a package called 'mymath' with:
# - __init__.py (imports all functions)
# - basic.py (add, subtract, multiply, divide)
# - advanced.py (power, sqrt, factorial)
# Then use: from mymath import add, power
# TODO: Write your code here

# Solution:
# Create directory structure:
# mymath/
# ├── __init__.py
# ├── basic.py
# └── advanced.py
#
# basic.py:
# def add(a, b): return a + b
# def subtract(a, b): return a - b
# def multiply(a, b): return a * b
# def divide(a, b): return a / b if b != 0 else None
#
# advanced.py:
# import math
# def power(a, b): return a ** b
# def sqrt(a): return math.sqrt(a)
# def factorial(n): return math.factorial(n)
#
# __init__.py:
# from .basic import add, subtract, multiply, divide
# from .advanced import power, sqrt, factorial


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Circular imports
   ❌ module_a imports module_b, module_b imports module_a
   ✅ Restructure code or use import inside function

2. Using 'from module import *'
   ❌ from math import *  # Pollutes namespace
   ✅ from math import sqrt, pi  # Explicit imports

3. Forgetting if __name__ == "__main__"
   ❌ Test code runs when module is imported
   ✅ Wrap test code in if __name__ == "__main__":

4. Module naming conflicts
   ❌ Creating 'math.py' (shadows built-in math)
   ✅ Use unique names like 'my_math.py'

5. Not understanding import execution
   - Import statements execute the module code
   - Imports are cached (only run once)
   - Side effects in modules can cause issues

6. Relative import errors
   ❌ from . import module  # Fails in script run directly
   ✅ Use absolute imports or run as package

7. Wrong sys.path manipulation
   ❌ sys.path.append() with hardcoded paths
   ✅ Use proper package structure and installation
"""