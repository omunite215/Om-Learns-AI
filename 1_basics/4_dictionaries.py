"""
================================================================================
PYTHON FUNDAMENTALS: DICTIONARIES
================================================================================
File: 1_basics/4_dictionaries.py
Author: Om
Date: 2024-12-17
Source: Corey Schafer - Python Tutorial for Beginners
Status: ✅ Completed

Description:
    Comprehensive guide to Python dictionaries - key-value pair data structures.
    Covers creation, accessing, modifying, iterating, and common dictionary
    methods and operations.

Learning Objectives:
    - Create and work with dictionaries
    - Access values using keys safely
    - Add, update, and remove key-value pairs
    - Iterate over dictionaries (keys, values, items)
    - Use dictionary methods effectively
    - Understand nested dictionaries

Prerequisites:
    - Basic Python syntax
    - Lists, tuples, and sets
================================================================================
"""

# =============================================================================
# 1. CREATING DICTIONARIES
# =============================================================================

# Basic dictionary creation
student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}
print(student)
# Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(type(student))
# Output: <class 'dict'>

# Empty dictionary
empty_dict = {}
another_empty = dict()

# Using dict() constructor
student_2 = dict(name='Jane', age=22, major='Physics')
print(student_2)
# Output: {'name': 'Jane', 'age': 22, 'major': 'Physics'}

# Dictionary from list of tuples
pairs = [('a', 1), ('b', 2), ('c', 3)]
dict_from_pairs = dict(pairs)
print(dict_from_pairs)
# Output: {'a': 1, 'b': 2, 'c': 3}


# =============================================================================
# 2. ACCESSING DICTIONARY VALUES
# =============================================================================

student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# --- Method 1: Square bracket notation ---
print(student['name'])
# Output: 'John'

print(student['courses'])
# Output: ['Math', 'CompSci']

# Accessing nested values
print(student['courses'][0])
# Output: 'Math'

# WARNING: KeyError if key doesn't exist!
# print(student['phone'])
# KeyError: 'phone'

# --- Method 2: get() method (SAFER) ---
print(student.get('name'))
# Output: 'John'

print(student.get('phone'))
# Output: None (no error!)

# Provide default value if key not found
print(student.get('phone', 'Not Found'))
# Output: 'Not Found'

print(student.get('age', 0))
# Output: 25 (key exists, so returns actual value)


# =============================================================================
# 3. ADDING AND UPDATING VALUES
# =============================================================================

student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# --- Add new key-value pair ---
student['phone'] = '555-1234'
print(student)
# Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-1234'}

# --- Update existing value ---
student['age'] = 26
print(student['age'])
# Output: 26

# --- update() method - Update multiple values at once ---
student.update({'name': 'Jane', 'age': 27, 'email': 'jane@email.com'})
print(student)
# Output: {'name': 'Jane', 'age': 27, 'courses': ['Math', 'CompSci'], 'phone': '555-1234', 'email': 'jane@email.com'}

# update() with keyword arguments
student.update(city='New York', country='USA')
print(student)


# =============================================================================
# 4. REMOVING VALUES
# =============================================================================

student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci'],
    'phone': '555-1234'
}

# --- del statement ---
del student['phone']
print(student)
# Output: {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# --- pop() - Remove and return value ---
age = student.pop('age')
print(age)      # Output: 25
print(student)  # Output: {'name': 'John', 'courses': ['Math', 'CompSci']}

# pop() with default value (no error if key missing)
phone = student.pop('phone', 'Not Found')
print(phone)
# Output: 'Not Found'

# --- popitem() - Remove and return last inserted item (Python 3.7+) ---
student = {'name': 'John', 'age': 25, 'city': 'NYC'}
last_item = student.popitem()
print(last_item)  # Output: ('city', 'NYC')
print(student)    # Output: {'name': 'John', 'age': 25}

# --- clear() - Remove all items ---
student.clear()
print(student)
# Output: {}


# =============================================================================
# 5. CHECKING KEYS AND VALUES
# =============================================================================

student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# --- Check if KEY exists ---
print('name' in student)
# Output: True

print('phone' in student)
# Output: False

print('phone' not in student)
# Output: True

# --- Check if VALUE exists ---
print('John' in student.values())
# Output: True

print(25 in student.values())
# Output: True


# =============================================================================
# 6. DICTIONARY LENGTH AND KEYS/VALUES
# =============================================================================

student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# --- Length ---
print(len(student))
# Output: 3

# --- keys() - Get all keys ---
print(student.keys())
# Output: dict_keys(['name', 'age', 'courses'])

# Convert to list
keys_list = list(student.keys())
print(keys_list)
# Output: ['name', 'age', 'courses']

# --- values() - Get all values ---
print(student.values())
# Output: dict_values(['John', 25, ['Math', 'CompSci']])

# --- items() - Get all key-value pairs as tuples ---
print(student.items())
# Output: dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])


# =============================================================================
# 7. ITERATING OVER DICTIONARIES
# =============================================================================

student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# --- Iterate over keys (default) ---
for key in student:
    print(key)
# Output:
# name
# age
# courses

# --- Iterate over values ---
for value in student.values():
    print(value)
# Output:
# John
# 25
# ['Math', 'CompSci']

# --- Iterate over key-value pairs ---
for key, value in student.items():
    print(f'{key}: {value}')
# Output:
# name: John
# age: 25
# courses: ['Math', 'CompSci']


# =============================================================================
# 8. COPYING DICTIONARIES
# =============================================================================

# --- Wrong way (creates reference) ---
original = {'a': 1, 'b': 2}
reference = original  # Both point to same dict!

reference['c'] = 3
print(original)  # Output: {'a': 1, 'b': 2, 'c': 3} - Modified!

# --- Correct ways to copy ---
original = {'a': 1, 'b': 2}

# Method 1: copy()
copy_1 = original.copy()

# Method 2: dict()
copy_2 = dict(original)

# Method 3: dict comprehension
copy_3 = {k: v for k, v in original.items()}

copy_1['c'] = 3
print(original)  # Output: {'a': 1, 'b': 2} - Unchanged
print(copy_1)    # Output: {'a': 1, 'b': 2, 'c': 3}

# NOTE: These are SHALLOW copies. For nested dicts, use copy.deepcopy()


# =============================================================================
# 9. NESTED DICTIONARIES
# =============================================================================

# Dictionary containing dictionaries
students = {
    'student1': {
        'name': 'John',
        'age': 25,
        'grades': {'math': 90, 'science': 85}
    },
    'student2': {
        'name': 'Jane',
        'age': 22,
        'grades': {'math': 95, 'science': 92}
    }
}

# Accessing nested values
print(students['student1']['name'])
# Output: 'John'

print(students['student2']['grades']['math'])
# Output: 95

# Safe access with get()
print(students.get('student3', {}).get('name', 'Unknown'))
# Output: 'Unknown'

# Iterating nested dicts
for student_id, student_info in students.items():
    print(f"\n{student_id}:")
    for key, value in student_info.items():
        print(f"  {key}: {value}")


# =============================================================================
# 10. DICTIONARY METHODS REFERENCE
# =============================================================================

sample = {'a': 1, 'b': 2, 'c': 3}

# --- setdefault() - Get value, set if not exists ---
value = sample.setdefault('d', 4)  # 'd' doesn't exist, so sets it to 4
print(value)   # Output: 4
print(sample)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

value = sample.setdefault('a', 100)  # 'a' exists, returns existing value
print(value)   # Output: 1 (not 100)

# --- fromkeys() - Create dict with keys from sequence ---
keys = ['name', 'age', 'city']
default_dict = dict.fromkeys(keys, 'Unknown')
print(default_dict)
# Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}


# =============================================================================
# 11. DICTIONARY COMPREHENSIONS
# =============================================================================

# Basic comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transform existing dict
prices = {'apple': 1.50, 'banana': 0.75, 'orange': 2.00}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)
# Output: {'apple': 1.35, 'banana': 0.675, 'orange': 1.8}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(swapped)
# Output: {1: 'a', 2: 'b', 3: 'c'}


# =============================================================================
# 12. MERGING DICTIONARIES
# =============================================================================

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}

# --- Method 1: update() (modifies original) ---
dict_1_copy = dict_1.copy()
dict_1_copy.update(dict_2)
print(dict_1_copy)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# --- Method 2: ** unpacking (Python 3.5+) ---
merged = {**dict_1, **dict_2}
print(merged)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# --- Method 3: | operator (Python 3.9+) ---
merged = dict_1 | dict_2
print(merged)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Note: If keys overlap, later dict values override earlier ones


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Dictionary Basics
   - Key-value pairs: {key: value}
   - Keys must be immutable (strings, numbers, tuples)
   - Values can be any type
   - Keys are unique (duplicates overwrite)
   - Ordered (Python 3.7+)

2. Accessing Values
   - dict[key] - Raises KeyError if not found
   - dict.get(key) - Returns None if not found (safer!)
   - dict.get(key, default) - Returns default if not found

3. Modifying Dictionaries
   - Add/Update: dict[key] = value
   - Update multiple: dict.update({...})
   - Remove: del dict[key], dict.pop(key), dict.popitem()

4. Iteration
   - for key in dict - iterate keys
   - for value in dict.values() - iterate values
   - for key, value in dict.items() - iterate both

5. Useful Methods
   - keys(), values(), items()
   - get(), setdefault()
   - pop(), popitem(), clear()
   - copy(), update()

6. Best Practices
   - Use get() to avoid KeyError
   - Use 'in' to check key existence
   - Use dict comprehensions for transformations
   - Remember shallow vs deep copy for nested dicts
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Create and Access [EASY]
# Create a dictionary for a book with: title, author, year, pages
# Print each value using both [] and get() methods
# TODO: Write your code here

# Solution:
# book = {
#     'title': 'Python Crash Course',
#     'author': 'Eric Matthes',
#     'year': 2019,
#     'pages': 544
# }
# print(book['title'])
# print(book.get('author'))
# print(book.get('isbn', 'Not available'))


# Exercise 2: Update Dictionary [EASY]
# Given a dictionary, add a new key 'email', update 'age', and remove 'phone'
person = {'name': 'Alice', 'age': 30, 'phone': '555-1234'}
# TODO: Write your code here

# Solution:
# person['email'] = 'alice@email.com'
# person['age'] = 31
# person.pop('phone')
# print(person)


# Exercise 3: Word Frequency Counter [MEDIUM]
# Count how many times each word appears in the sentence
sentence = "the quick brown fox jumps over the lazy dog the fox"
# TODO: Create a dictionary with word counts

# Solution:
# words = sentence.split()
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1
# print(word_count)


# Exercise 4: Invert Dictionary [MEDIUM]
# Swap keys and values in a dictionary
grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A', 'David': 'C'}
# Create: {'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}
# TODO: Write your code here

# Solution:
# inverted = {}
# for name, grade in grades.items():
#     if grade not in inverted:
#         inverted[grade] = []
#     inverted[grade].append(name)
# print(inverted)


# Exercise 5: Nested Dictionary Access [MEDIUM]
# Access and modify nested dictionary values
company = {
    'engineering': {
        'team_lead': 'Alice',
        'members': ['Bob', 'Charlie'],
        'budget': 100000
    },
    'marketing': {
        'team_lead': 'David',
        'members': ['Eve'],
        'budget': 50000
    }
}
# a) Print engineering team lead
# b) Add 'Frank' to marketing members
# c) Increase engineering budget by 20%
# TODO: Write your code here

# Solution:
# print(company['engineering']['team_lead'])
# company['marketing']['members'].append('Frank')
# company['engineering']['budget'] *= 1.2
# print(company)


# Exercise 6: Merge and Compare [MEDIUM]
# Given two dictionaries of student scores, create a merged dict
# where if a student appears in both, take the higher score
scores_1 = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
scores_2 = {'Bob': 88, 'Charlie': 82, 'David': 95}
# TODO: Write your code here

# Solution:
# merged = scores_1.copy()
# for name, score in scores_2.items():
#     if name in merged:
#         merged[name] = max(merged[name], score)
#     else:
#         merged[name] = score
# print(merged)


# Exercise 7: Dictionary Comprehension [CHALLENGE]
# Create a dictionary where:
# - Keys are numbers 1-10
# - Values are 'even' or 'odd' based on the number
# TODO: Write your code here

# Solution:
# number_type = {n: 'even' if n % 2 == 0 else 'odd' for n in range(1, 11)}
# print(number_type)


# Exercise 8: Group by Category [CHALLENGE]
# Group items by their category
items = [
    {'name': 'apple', 'category': 'fruit'},
    {'name': 'carrot', 'category': 'vegetable'},
    {'name': 'banana', 'category': 'fruit'},
    {'name': 'broccoli', 'category': 'vegetable'},
    {'name': 'orange', 'category': 'fruit'}
]
# Create: {'fruit': ['apple', 'banana', 'orange'], 'vegetable': ['carrot', 'broccoli']}
# TODO: Write your code here

# Solution:
# grouped = {}
# for item in items:
#     category = item['category']
#     name = item['name']
#     if category not in grouped:
#         grouped[category] = []
#     grouped[category].append(name)
# print(grouped)


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Using [] instead of get() for uncertain keys
   ❌ value = my_dict['key']  # KeyError if not found
   ✅ value = my_dict.get('key', 'default')

2. Modifying dict while iterating
   ❌ for key in my_dict:
          del my_dict[key]  # RuntimeError
   ✅ for key in list(my_dict.keys()):
          del my_dict[key]

3. Using mutable types as keys
   ❌ my_dict[[1, 2, 3]] = 'value'  # TypeError: unhashable type
   ✅ my_dict[(1, 2, 3)] = 'value'  # Tuples are fine

4. Forgetting about reference vs copy
   ❌ copy = original  # Same dict!
   ✅ copy = original.copy()

5. Overwriting when you meant to update
   ❌ my_dict = {'new': 'data'}  # Replaces entire dict
   ✅ my_dict.update({'new': 'data'})  # Adds to dict

6. Case sensitivity in keys
   my_dict = {'Name': 'John'}
   my_dict.get('name')  # Returns None, not 'John'

7. Shallow copy with nested dicts
   original = {'a': {'b': 1}}
   copy = original.copy()
   copy['a']['b'] = 2  # Also modifies original!
   # Use: import copy; copy.deepcopy(original)
"""