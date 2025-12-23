"""
================================================================================
PYTHON FUNDAMENTALS: COMPREHENSIONS
================================================================================
Day: 8

Description:
    Comprehensive guide to Python comprehensions - a concise and powerful way
    to create lists, dictionaries, and sets. Covers list comprehensions,
    dictionary comprehensions, set comprehensions, conditional logic, nested
    comprehensions, and comparison with map/filter.

Learning Objectives:
    - Write list comprehensions to replace loops
    - Add conditional logic to comprehensions
    - Create dictionary and set comprehensions
    - Use nested comprehensions for complex data
    - Understand when to use comprehensions vs loops
    - Compare comprehensions with map() and filter()

Prerequisites:
    - Loops and iterations
    - Conditional statements
    - Lists, dictionaries, and sets
================================================================================
"""

# =============================================================================
# 1. WHY COMPREHENSIONS?
# =============================================================================

"""
COMPREHENSIONS are a concise, readable way to create collections.

Benefits:
- More readable and Pythonic
- Usually faster than loops
- Single line instead of multiple
- Widely used in data science and ML

Types:
- List comprehensions: [expression for item in iterable]
- Dict comprehensions: {key: value for item in iterable}
- Set comprehensions: {expression for item in iterable}
- Generator expressions: (expression for item in iterable)
"""


# =============================================================================
# 2. BASIC LIST COMPREHENSION
# =============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Traditional loop approach ---
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# --- List comprehension (same result) ---
my_list = [n * n for n in nums]
print(my_list)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Syntax: [expression for item in iterable]

# --- More examples ---
# Double each number
doubled = [n * 2 for n in nums]
print(doubled)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18]

# Convert to strings
str_nums = [str(n) for n in nums]
print(str_nums)
# Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Using range()
squares = [x ** 2 for x in range(1, 6)]
print(squares)
# Output: [1, 4, 9, 16, 25]

# With strings
letters = [char.upper() for char in 'hello']
print(letters)
# Output: ['H', 'E', 'L', 'L', 'O']


# =============================================================================
# 3. COMPREHENSION WITH CONDITIONAL (IF)
# =============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Traditional loop with condition ---
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)
# Output: [2, 4, 6, 8]

# --- Comprehension with if (filter) ---
my_list = [n for n in nums if n % 2 == 0]
print(my_list)
# Output: [2, 4, 6, 8]

# Syntax: [expression for item in iterable if condition]

# --- More filtering examples ---
# Odd numbers only
odds = [n for n in nums if n % 2 != 0]
print(odds)
# Output: [1, 3, 5, 7, 9]

# Numbers greater than 5
greater_than_5 = [n for n in nums if n > 5]
print(greater_than_5)
# Output: [6, 7, 8, 9]

# Numbers divisible by 3
div_by_3 = [n for n in nums if n % 3 == 0]
print(div_by_3)
# Output: [3, 6, 9]

# Filter strings by length
words = ['apple', 'be', 'cat', 'door', 'elephant']
long_words = [word for word in words if len(word) > 3]
print(long_words)
# Output: ['apple', 'door', 'elephant']


# =============================================================================
# 4. COMPREHENSION WITH IF-ELSE
# =============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- If-else in comprehension ---
# Note: if-else goes BEFORE the for (different position!)
result = ['even' if n % 2 == 0 else 'odd' for n in nums]
print(result)
# Output: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

# Syntax: [value_if_true if condition else value_if_false for item in iterable]

# --- More if-else examples ---
# Replace negatives with 0
numbers = [-5, 3, -2, 8, -1, 7]
non_negative = [n if n >= 0 else 0 for n in numbers]
print(non_negative)
# Output: [0, 3, 0, 8, 0, 7]

# Categorize numbers
categories = ['big' if n > 5 else 'small' for n in nums]
print(categories)
# Output: ['small', 'small', 'small', 'small', 'small', 'big', 'big', 'big', 'big']

# Pass/Fail based on score
scores = [85, 42, 91, 55, 73, 38]
results = ['Pass' if score >= 60 else 'Fail' for score in scores]
print(results)
# Output: ['Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Fail']


# =============================================================================
# 5. COMBINING IF-ELSE WITH FILTER
# =============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transform AND filter in one comprehension
# Square only even numbers
squared_evens = [n ** 2 for n in nums if n % 2 == 0]
print(squared_evens)
# Output: [4, 16, 36, 64]

# Transform with if-else AND filter
# Double evens, triple odds, but only if > 3
result = [n * 2 if n % 2 == 0 else n * 3 for n in nums if n > 3]
print(result)
# Output: [8, 15, 12, 21, 16, 27]
# Explanation: 4*2=8, 5*3=15, 6*2=12, 7*3=21, 8*2=16, 9*3=27


# =============================================================================
# 6. NESTED LOOPS IN COMPREHENSION
# =============================================================================

# --- Traditional nested loop ---
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)
# Output: [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ...]

# --- Nested comprehension (same result) ---
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
# Output: [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ...]

# Reading order: left to right = outer to inner loop

# --- Multiplication table ---
table = [(i, j, i*j) for i in range(1, 4) for j in range(1, 4)]
print(table)
# Output: [(1,1,1), (1,2,2), (1,3,3), (2,1,2), (2,2,4), ...]

# --- Flatten a 2D list ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Nested with condition ---
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(pairs)
# Output: [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]


# =============================================================================
# 7. DICTIONARY COMPREHENSIONS
# =============================================================================

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# --- Using zip() with dict comprehension ---
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)
# Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', ...}

# Syntax: {key_expr: value_expr for item in iterable}

# --- Dict comprehension with condition ---
my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)
# Output: {'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}

# --- More dict comprehension examples ---
# Squares dictionary
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Word lengths
words = ['apple', 'banana', 'cherry']
lengths = {word: len(word) for word in words}
print(lengths)
# Output: {'apple': 5, 'banana': 6, 'cherry': 6}

# Invert a dictionary (swap keys and values)
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)
# Output: {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary
prices = {'apple': 1.50, 'banana': 0.75, 'cherry': 2.00, 'date': 3.00}
expensive = {k: v for k, v in prices.items() if v > 1.00}
print(expensive)
# Output: {'apple': 1.50, 'cherry': 2.00, 'date': 3.00}

# Transform values
discounted = {k: v * 0.9 for k, v in prices.items()}
print(discounted)
# Output: {'apple': 1.35, 'banana': 0.675, 'cherry': 1.8, 'date': 2.7}


# =============================================================================
# 8. SET COMPREHENSIONS
# =============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]  # Note duplicates

# --- Basic set comprehension ---
my_set = {n for n in nums}
print(my_set)
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Duplicates automatically removed!

# Syntax: {expression for item in iterable}

# --- Set comprehension with transformation ---
squared_set = {n ** 2 for n in nums}
print(squared_set)
# Output: {1, 4, 9, 16, 25, 36, 49, 64, 81}

# --- Set comprehension with condition ---
even_set = {n for n in nums if n % 2 == 0}
print(even_set)
# Output: {2, 4, 6, 8}

# --- Practical: Get unique first letters ---
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado']
first_letters = {word[0] for word in words}
print(first_letters)
# Output: {'a', 'b', 'c'}

# --- Practical: Get unique word lengths ---
unique_lengths = {len(word) for word in words}
print(unique_lengths)
# Output: {5, 6, 7, 9}


# =============================================================================
# 9. GENERATOR EXPRESSIONS
# =============================================================================

"""
Generator expressions are like list comprehensions but:
- Use parentheses () instead of brackets []
- Don't create the full list in memory
- Generate values on-the-fly (lazy evaluation)
- More memory efficient for large datasets
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- List comprehension (creates list in memory) ---
list_comp = [n ** 2 for n in nums]
print(list_comp)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(type(list_comp))
# Output: <class 'list'>

# --- Generator expression (lazy evaluation) ---
gen_exp = (n ** 2 for n in nums)
print(gen_exp)
# Output: <generator object <genexpr> at 0x...>
print(type(gen_exp))
# Output: <class 'generator'>

# Convert to list to see values
print(list(gen_exp))
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# --- Use with functions that accept iterables ---
nums = [1, 2, 3, 4, 5]

# Sum of squares (no need to create list)
total = sum(n ** 2 for n in nums)
print(total)
# Output: 55

# Max of transformed values
maximum = max(n * 2 for n in nums)
print(maximum)
# Output: 10

# Any/All with conditions
has_even = any(n % 2 == 0 for n in nums)
all_positive = all(n > 0 for n in nums)
print(f"Has even: {has_even}, All positive: {all_positive}")
# Output: Has even: True, All positive: True


# =============================================================================
# 10. COMPREHENSIONS VS MAP/FILTER
# =============================================================================

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- TRANSFORMATION: Comprehension vs map() ---

# List comprehension
squared_comp = [n ** 2 for n in nums]
print(squared_comp)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# map() with lambda
squared_map = list(map(lambda n: n ** 2, nums))
print(squared_map)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# map() returns iterator, need list() to see values
print(map(lambda n: n ** 2, nums))
# Output: <map object at 0x...>

# --- FILTERING: Comprehension vs filter() ---

# List comprehension
evens_comp = [n for n in nums if n % 2 == 0]
print(evens_comp)
# Output: [2, 4, 6, 8]

# filter() with lambda
evens_filter = list(filter(lambda n: n % 2 == 0, nums))
print(evens_filter)
# Output: [2, 4, 6, 8]

# filter() returns iterator
print(filter(lambda n: n % 2 == 0, nums))
# Output: <filter object at 0x...>

# --- COMPARISON ---
"""
Comprehensions:
✅ More readable and Pythonic
✅ Can transform AND filter in one expression
✅ Easier to understand at a glance
✅ Preferred in most Python code

map()/filter():
✅ Functional programming style
✅ Can be slightly faster for simple operations
✅ Useful when you already have a named function
✅ Returns iterator (memory efficient)

General rule: Prefer comprehensions unless you have a good reason for map/filter
"""


# =============================================================================
# 11. WHEN TO USE COMPREHENSIONS
# =============================================================================

"""
USE COMPREHENSIONS WHEN:
✅ Simple transformation or filtering
✅ One-liner is readable
✅ Creating lists, dicts, or sets
✅ The logic is straightforward

USE REGULAR LOOPS WHEN:
❌ Complex logic requiring multiple statements
❌ Need to break/continue
❌ Side effects (printing, modifying external state)
❌ Comprehension becomes too long/unreadable
❌ More than 2 levels of nesting
"""

# --- Good comprehension (readable) ---
squares = [x ** 2 for x in range(10)]

# --- Bad comprehension (too complex) ---
# result = [func1(x) if cond1(x) else func2(x) for x in data if cond2(x) and cond3(x)]

# Better as a loop:
# result = []
# for x in data:
#     if cond2(x) and cond3(x):
#         if cond1(x):
#             result.append(func1(x))
#         else:
#             result.append(func2(x))


# =============================================================================
# 12. PRACTICAL EXAMPLES FOR AI/ML
# =============================================================================

# --- Normalize data ---
data = [10, 20, 30, 40, 50]
max_val = max(data)
normalized = [x / max_val for x in data]
print(f"Normalized: {normalized}")
# Output: [0.2, 0.4, 0.6, 0.8, 1.0]

# --- One-hot encoding ---
categories = ['cat', 'dog', 'bird', 'cat', 'dog']
unique = list(set(categories))
one_hot = [[1 if cat == u else 0 for u in unique] for cat in categories]
print(f"One-hot: {one_hot}")

# --- Filter valid data ---
measurements = [23.5, -1, 45.2, None, 67.8, -999, 34.1]
valid_data = [x for x in measurements if x is not None and x >= 0]
print(f"Valid data: {valid_data}")
# Output: [23.5, 45.2, 67.8, 34.1]

# --- Create feature dictionary ---
features = ['age', 'height', 'weight']
values = [25, 175, 70]
feature_dict = {f: v for f, v in zip(features, values)}
print(f"Features: {feature_dict}")
# Output: {'age': 25, 'height': 175, 'weight': 70}

# --- Tokenize text ---
sentence = "Hello World This Is Python"
tokens = [word.lower() for word in sentence.split()]
print(f"Tokens: {tokens}")
# Output: ['hello', 'world', 'this', 'is', 'python']

# --- Create word frequency dict ---
text = "the cat sat on the mat the cat"
words = text.split()
word_freq = {word: words.count(word) for word in set(words)}
print(f"Word frequency: {word_freq}")
# Output: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. List Comprehension Syntax
   - Basic: [expr for item in iterable]
   - Filter: [expr for item in iterable if condition]
   - If-else: [expr1 if cond else expr2 for item in iterable]

2. Dictionary Comprehension
   - {key: value for item in iterable}
   - {key: value for item in iterable if condition}

3. Set Comprehension
   - {expr for item in iterable}
   - Automatically removes duplicates

4. Generator Expression
   - (expr for item in iterable)
   - Memory efficient, lazy evaluation
   - Use when you don't need the full list

5. Nested Comprehensions
   - [expr for x in iter1 for y in iter2]
   - Left to right = outer to inner loop

6. Comprehensions vs map/filter
   - Comprehensions: More readable, Pythonic
   - map/filter: Functional style, returns iterator

7. Best Practices
   - Keep comprehensions simple and readable
   - Use loops for complex logic
   - Avoid more than 2 levels of nesting
   - Consider generator expressions for large data
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Basic List Comprehension [EASY]
# Create a list of cubes for numbers 1-10
# TODO: Write your code here

# Solution:
# cubes = [n ** 3 for n in range(1, 11)]
# print(cubes)  # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# Exercise 2: Filtering [EASY]
# From the list below, get only the positive numbers
numbers = [-5, 3, -2, 8, -1, 7, 0, -4, 6]
# TODO: Write your code here

# Solution:
# positives = [n for n in numbers if n > 0]
# print(positives)  # [3, 8, 7, 6]


# Exercise 3: If-Else Comprehension [MEDIUM]
# Convert temperatures: if > 30, label 'Hot', else 'Normal'
temps = [25, 32, 18, 35, 28, 40, 22]
# TODO: Write your code here

# Solution:
# labels = ['Hot' if t > 30 else 'Normal' for t in temps]
# print(labels)  # ['Normal', 'Hot', 'Normal', 'Hot', 'Normal', 'Hot', 'Normal']


# Exercise 4: Dictionary Comprehension [MEDIUM]
# Create a dict mapping numbers 1-5 to their factorials
# TODO: Write your code here

# Solution:
# import math
# factorials = {n: math.factorial(n) for n in range(1, 6)}
# print(factorials)  # {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}


# Exercise 5: Nested Comprehension [MEDIUM]
# Create a 3x3 matrix (list of lists) filled with zeros
# TODO: Write your code here

# Solution:
# matrix = [[0 for _ in range(3)] for _ in range(3)]
# print(matrix)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Exercise 6: Set Comprehension [MEDIUM]
# Get unique vowels from a sentence
sentence = "The quick brown fox jumps over the lazy dog"
# TODO: Write your code here

# Solution:
# vowels = {char.lower() for char in sentence if char.lower() in 'aeiou'}
# print(vowels)  # {'a', 'e', 'i', 'o', 'u'}


# Exercise 7: Transform and Filter [CHALLENGE]
# From a list of words, get lengths of words that start with 'a' (case-insensitive)
words = ['Apple', 'banana', 'Apricot', 'cherry', 'avocado', 'date']
# TODO: Write your code here

# Solution:
# lengths = [len(word) for word in words if word.lower().startswith('a')]
# print(lengths)  # [5, 7, 7]


# Exercise 8: Flatten and Filter [CHALLENGE]
# Flatten the matrix and get only even numbers
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# TODO: Write your code here

# Solution:
# flat_evens = [num for row in matrix for num in row if num % 2 == 0]
# print(flat_evens)  # [2, 4, 6, 8]


# Exercise 9: Word Index Dictionary [CHALLENGE]
# Create a dict mapping each word to its index in the list
words = ['apple', 'banana', 'cherry', 'date']
# TODO: Write your code here

# Solution:
# word_index = {word: idx for idx, word in enumerate(words)}
# print(word_index)  # {'apple': 0, 'banana': 1, 'cherry': 2, 'date': 3}


# Exercise 10: Grade Calculator [CHALLENGE]
# Convert scores to grades: A(>=90), B(>=80), C(>=70), D(>=60), F(<60)
scores = [95, 82, 67, 91, 58, 75, 88]
# TODO: Write your code here

# Solution:
# grades = ['A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'D' if s >= 60 else 'F' for s in scores]
# print(grades)  # ['A', 'B', 'D', 'A', 'F', 'C', 'B']


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Confusing if position
   - Filter (if at end): [x for x in items if condition]
   - Transform (if-else before for): [a if cond else b for x in items]
   
   ❌ [x if x > 0 for x in nums]  # SyntaxError!
   ✅ [x for x in nums if x > 0]  # Filter
   ✅ [x if x > 0 else 0 for x in nums]  # Transform

2. Overcomplicating comprehensions
   ❌ [complex_func(x) if cond1(x) and cond2(x) else other_func(x) for x in data if filter_cond(x)]
   ✅ Use a regular loop for complex logic

3. Modifying external state in comprehension
   ❌ [external_list.append(x) for x in data]  # Creates list of None!
   ✅ Use a regular loop for side effects

4. Forgetting that map/filter return iterators
   ❌ print(map(lambda x: x*2, nums))  # Prints <map object>
   ✅ print(list(map(lambda x: x*2, nums)))

5. Nested comprehension confusion
   - Read left to right: outer loop first, inner loop second
   - [expr for outer in outer_iter for inner in inner_iter]
   
6. Creating list when generator is enough
   ❌ sum([x**2 for x in range(1000000)])  # Creates huge list
   ✅ sum(x**2 for x in range(1000000))    # Generator, memory efficient
"""