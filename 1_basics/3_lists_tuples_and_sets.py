"""
================================================================================
PYTHON FUNDAMENTALS: LISTS, TUPLES, AND SETS
================================================================================
File: 1_basics/3_lists_tuples_sets.py
Author: Om
Date: 2024-12-17
Source: Corey Schafer - Python Tutorial for Beginners
Status: ✅ Completed

Description:
    Comprehensive guide to Python's core collection data types: lists, tuples,
    and sets. Covers creation, manipulation, common methods, and when to use
    each data structure.

Learning Objectives:
    - Create and manipulate lists
    - Understand list methods (append, insert, remove, pop, sort, etc.)
    - Work with tuples and understand immutability
    - Use sets for unique collections and set operations
    - Choose the right data structure for different scenarios

Prerequisites:
    - Basic Python syntax
    - Strings and numeric operations
================================================================================
"""

# =============================================================================
# PART 1: LISTS
# =============================================================================
# Lists are ordered, mutable (changeable) collections that allow duplicates
# Syntax: square brackets []

# =============================================================================
# 1.1 CREATING LISTS
# =============================================================================

# Basic list creation
courses = ['History', 'Math', 'Physics', 'ComSci']
print(courses)
# Output: ['History', 'Math', 'Physics', 'ComSci']

# Check type
print(type(courses))
# Output: <class 'list'>

# List length
print(len(courses))
# Output: 4

# Empty list
empty_list = []
another_empty = list()


# =============================================================================
# 1.2 ACCESSING LIST ELEMENTS
# =============================================================================

courses = ['History', 'Math', 'Physics', 'ComSci']

# Access by index (starts at 0)
print(courses[0])    # Output: 'History'
print(courses[1])    # Output: 'Math'
print(courses[-1])   # Output: 'ComSci' (last element)
print(courses[-2])   # Output: 'Physics' (second from last)

# Slicing (same as strings)
print(courses[0:2])  # Output: ['History', 'Math']
print(courses[:3])   # Output: ['History', 'Math', 'Physics']
print(courses[2:])   # Output: ['Physics', 'ComSci']


# =============================================================================
# 1.3 ADDING ELEMENTS TO LISTS
# =============================================================================

courses = ['History', 'Math', 'Physics', 'ComSci']

# --- append() - Add to END of list ---
courses.append('Art')
print(courses)
# Output: ['History', 'Math', 'Physics', 'ComSci', 'Art']

# --- insert() - Add at SPECIFIC position ---
courses.insert(0, 'Music')
print(courses)
# Output: ['Music', 'History', 'Math', 'Physics', 'ComSci', 'Art']
# Note: All other elements shift right

courses.insert(2, 'Biology')
print(courses)
# Output: ['Music', 'History', 'Biology', 'Math', 'Physics', 'ComSci', 'Art']

# --- extend() - Add MULTIPLE elements (merge lists) ---
courses = ['History', 'Math', 'Physics', 'ComSci']
courses_2 = ['Art', 'Education']

courses.extend(courses_2)
print(courses)
# Output: ['History', 'Math', 'Physics', 'ComSci', 'Art', 'Education']

# Difference between append and extend
courses = ['History', 'Math']
courses.append(['Art', 'Music'])  # Adds list as single element
print(courses)
# Output: ['History', 'Math', ['Art', 'Music']]

courses = ['History', 'Math']
courses.extend(['Art', 'Music'])  # Adds each element individually
print(courses)
# Output: ['History', 'Math', 'Art', 'Music']


# =============================================================================
# 1.4 REMOVING ELEMENTS FROM LISTS
# =============================================================================

courses = ['History', 'Math', 'Physics', 'ComSci', 'Art']

# --- remove() - Remove by VALUE ---
courses.remove('Math')
print(courses)
# Output: ['History', 'Physics', 'ComSci', 'Art']
# Note: Raises ValueError if element not found

# --- pop() - Remove by INDEX (default: last element) ---
courses = ['History', 'Math', 'Physics', 'ComSci', 'Art']

popped = courses.pop()  # Removes and returns last element
print(popped)           # Output: 'Art'
print(courses)          # Output: ['History', 'Math', 'Physics', 'ComSci']

popped = courses.pop(1)  # Remove element at index 1
print(popped)            # Output: 'Math'
print(courses)           # Output: ['History', 'Physics', 'ComSci']

# --- del statement - Remove by INDEX ---
courses = ['History', 'Math', 'Physics', 'ComSci']
del courses[0]
print(courses)
# Output: ['Math', 'Physics', 'ComSci']

# --- clear() - Remove ALL elements ---
courses = ['History', 'Math', 'Physics', 'ComSci']
courses.clear()
print(courses)
# Output: []


# =============================================================================
# 1.5 MODIFYING LIST ELEMENTS
# =============================================================================

courses = ['History', 'Math', 'Physics', 'ComSci']

# Change single element
courses[0] = 'Art'
print(courses)
# Output: ['Art', 'Math', 'Physics', 'ComSci']

# Change multiple elements using slicing
courses[1:3] = ['Biology', 'Chemistry']
print(courses)
# Output: ['Art', 'Biology', 'Chemistry', 'ComSci']


# =============================================================================
# 1.6 SORTING AND REVERSING LISTS
# =============================================================================

# --- reverse() - Reverse in place ---
courses = ['History', 'Math', 'Physics', 'ComSci']
courses.reverse()
print(courses)
# Output: ['ComSci', 'Physics', 'Math', 'History']

# --- sort() - Sort in place (ascending by default) ---
courses = ['History', 'Math', 'Physics', 'ComSci']
courses.sort()
print(courses)
# Output: ['ComSci', 'History', 'Math', 'Physics']

# Sort descending
courses.sort(reverse=True)
print(courses)
# Output: ['Physics', 'Math', 'History', 'ComSci']

# Sorting numbers
nums = [2, 1, 3, 4, 6, 5]
nums.sort()
print(nums)
# Output: [1, 2, 3, 4, 5, 6]

nums.sort(reverse=True)
print(nums)
# Output: [6, 5, 4, 3, 2, 1]

# --- sorted() - Returns NEW sorted list (original unchanged) ---
courses = ['History', 'Math', 'Physics', 'ComSci']
sorted_courses = sorted(courses)
print(sorted_courses)  # Output: ['ComSci', 'History', 'Math', 'Physics']
print(courses)         # Output: ['History', 'Math', 'Physics', 'ComSci'] (unchanged)


# =============================================================================
# 1.7 USEFUL LIST FUNCTIONS
# =============================================================================

nums = [2, 1, 3, 4, 6, 5]

# --- min() and max() ---
print(min(nums))  # Output: 1
print(max(nums))  # Output: 6

# --- sum() ---
print(sum(nums))  # Output: 21

# --- index() - Find index of element ---
courses = ['History', 'Math', 'Physics', 'ComSci']
print(courses.index('Physics'))
# Output: 2
# Note: Raises ValueError if not found

# --- count() - Count occurrences ---
nums = [1, 2, 2, 3, 3, 3, 4]
print(nums.count(3))
# Output: 3


# =============================================================================
# 1.8 CHECKING MEMBERSHIP
# =============================================================================

courses = ['History', 'Math', 'Physics', 'ComSci']

# --- in operator ---
print('Math' in courses)
# Output: True

print('Art' in courses)
# Output: False

print('Art' not in courses)
# Output: True


# =============================================================================
# 1.9 ITERATING OVER LISTS
# =============================================================================

courses = ['History', 'Math', 'Physics', 'ComSci']

# --- Basic for loop ---
for course in courses:
    print(course)
# Output:
# History
# Math
# Physics
# ComSci

# --- enumerate() - Get index and value ---
for index, course in enumerate(courses):
    print(f'{index}: {course}')
# Output:
# 0: History
# 1: Math
# 2: Physics
# 3: ComSci

# Start counting from 1 instead of 0
for index, course in enumerate(courses, start=1):
    print(f'{index}. {course}')
# Output:
# 1. History
# 2. Math
# 3. Physics
# 4. ComSci


# =============================================================================
# 1.10 JOINING AND SPLITTING
# =============================================================================

courses = ['History', 'Math', 'Physics', 'ComSci']

# --- join() - Convert list to string ---
course_str = ' - '.join(courses)
print(course_str)
# Output: 'History - Math - Physics - ComSci'

course_str = ', '.join(courses)
print(course_str)
# Output: 'History, Math, Physics, ComSci'

# --- split() - Convert string to list ---
course_str = 'History - Math - Physics - ComSci'
new_list = course_str.split(' - ')
print(new_list)
# Output: ['History', 'Math', 'Physics', 'ComSci']


# =============================================================================
# 1.11 COPYING LISTS
# =============================================================================

# --- Wrong way (creates reference, not copy) ---
original = ['History', 'Math', 'Physics']
reference = original  # Both point to same list!

reference.append('Art')
print(original)  # Output: ['History', 'Math', 'Physics', 'Art']
# Original is modified too!

# --- Correct ways to copy ---
original = ['History', 'Math', 'Physics']

# Method 1: copy()
copy_1 = original.copy()

# Method 2: slicing
copy_2 = original[:]

# Method 3: list()
copy_3 = list(original)

copy_1.append('Art')
print(original)  # Output: ['History', 'Math', 'Physics'] (unchanged)
print(copy_1)    # Output: ['History', 'Math', 'Physics', 'Art']


# =============================================================================
# PART 2: TUPLES
# =============================================================================
# Tuples are ordered, IMMUTABLE (unchangeable) collections that allow duplicates
# Syntax: parentheses ()

# =============================================================================
# 2.1 CREATING TUPLES
# =============================================================================

# Basic tuple creation
tuple_1 = ('History', 'Math', 'Physics', 'ComSci')
print(tuple_1)
# Output: ('History', 'Math', 'Physics', 'ComSci')

print(type(tuple_1))
# Output: <class 'tuple'>

# Single element tuple (note the comma!)
single = ('History',)  # This is a tuple
not_tuple = ('History')  # This is just a string!

print(type(single))     # Output: <class 'tuple'>
print(type(not_tuple))  # Output: <class 'str'>

# Empty tuple
empty_tuple = ()
another_empty = tuple()


# =============================================================================
# 2.2 ACCESSING TUPLE ELEMENTS
# =============================================================================

tuple_1 = ('History', 'Math', 'Physics', 'ComSci')

# Same indexing and slicing as lists
print(tuple_1[0])     # Output: 'History'
print(tuple_1[-1])    # Output: 'ComSci'
print(tuple_1[1:3])   # Output: ('Math', 'Physics')


# =============================================================================
# 2.3 TUPLE IMMUTABILITY
# =============================================================================

tuple_1 = ('History', 'Math', 'Physics', 'ComSci')

# This will cause an error - tuples cannot be modified!
# tuple_1[0] = 'Art'
# TypeError: 'tuple' object does not support item assignment

# Tuples don't have methods like append, insert, remove, etc.
# Because they cannot be changed!


# =============================================================================
# 2.4 TUPLE OPERATIONS
# =============================================================================

tuple_1 = ('History', 'Math', 'Physics', 'ComSci')

# --- Membership testing ---
print('Math' in tuple_1)
# Output: True

# --- Count and Index ---
print(tuple_1.count('Math'))
# Output: 1

print(tuple_1.index('Physics'))
# Output: 2

# --- Tuple concatenation (creates new tuple) ---
tuple_2 = ('Art', 'Music')
combined = tuple_1 + tuple_2
print(combined)
# Output: ('History', 'Math', 'Physics', 'ComSci', 'Art', 'Music')

# --- Tuple repetition ---
repeated = tuple_2 * 3
print(repeated)
# Output: ('Art', 'Music', 'Art', 'Music', 'Art', 'Music')


# =============================================================================
# 2.5 TUPLE UNPACKING
# =============================================================================

# Assign tuple values to variables
coordinates = (10, 20, 30)
x, y, z = coordinates

print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30

# Swap variables using tuple unpacking
a = 1
b = 2
a, b = b, a
print(a, b)  # Output: 2 1


# =============================================================================
# 2.6 WHEN TO USE TUPLES VS LISTS
# =============================================================================

"""
USE TUPLES WHEN:
- Data should not change (coordinates, RGB colors, dates)
- Returning multiple values from a function
- Dictionary keys (lists can't be keys, tuples can)
- Performance matters (tuples are slightly faster)

USE LISTS WHEN:
- Data needs to be modified
- Order matters and items may be added/removed
- You need methods like append, sort, etc.

EXAMPLES:
- Tuple: coordinates = (10, 20)  # x, y shouldn't change
- Tuple: color = (255, 128, 0)   # RGB value
- List: shopping_cart = ['apple', 'banana']  # Items can be added/removed
"""


# =============================================================================
# PART 3: SETS
# =============================================================================
# Sets are unordered, mutable collections with NO DUPLICATES
# Syntax: curly braces {}

# =============================================================================
# 3.1 CREATING SETS
# =============================================================================

# Basic set creation
cs_courses = {'History', 'Math', 'Physics', 'ComSci'}
print(cs_courses)
# Output: {'Physics', 'ComSci', 'Math', 'History'}
# Note: Order may vary - sets are unordered!

print(type(cs_courses))
# Output: <class 'set'>

# Sets automatically remove duplicates
cs_courses = {'History', 'Math', 'Physics', 'ComSci', 'Math'}
print(cs_courses)
# Output: {'Physics', 'ComSci', 'Math', 'History'}
# 'Math' appears only once

# Empty set (NOT {} - that's an empty dict!)
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>

empty_dict = {}
print(type(empty_dict))  # Output: <class 'dict'>


# =============================================================================
# 3.2 MEMBERSHIP TESTING (VERY FAST!)
# =============================================================================

cs_courses = {'History', 'Math', 'Physics', 'ComSci'}

# Sets are optimized for membership testing
print('Math' in cs_courses)
# Output: True

print('Art' in cs_courses)
# Output: False

# This is MUCH faster than lists for large collections


# =============================================================================
# 3.3 ADDING AND REMOVING ELEMENTS
# =============================================================================

cs_courses = {'History', 'Math', 'Physics', 'ComSci'}

# --- add() - Add single element ---
cs_courses.add('Art')
print(cs_courses)
# Output: {'Physics', 'ComSci', 'Math', 'History', 'Art'}

# --- update() - Add multiple elements ---
cs_courses.update(['Biology', 'Chemistry'])
print(cs_courses)
# Output: {'Physics', 'ComSci', 'Biology', 'Math', 'History', 'Art', 'Chemistry'}

# --- remove() - Remove element (raises error if not found) ---
cs_courses.remove('Art')
print(cs_courses)

# --- discard() - Remove element (NO error if not found) ---
cs_courses.discard('NonExistent')  # No error
print(cs_courses)

# --- pop() - Remove and return arbitrary element ---
popped = cs_courses.pop()
print(popped)  # Random element removed

# --- clear() - Remove all elements ---
cs_courses.clear()
print(cs_courses)  # Output: set()


# =============================================================================
# 3.4 SET OPERATIONS
# =============================================================================

cs_courses = {'History', 'Math', 'Physics', 'ComSci'}
art_courses = {'History', 'Math', 'Art', 'Drawing'}

# --- intersection() - Elements in BOTH sets ---
print(cs_courses.intersection(art_courses))
# Output: {'History', 'Math'}
# Shorthand: cs_courses & art_courses

# --- difference() - Elements in first set but NOT in second ---
print(cs_courses.difference(art_courses))
# Output: {'Physics', 'ComSci'}
# Shorthand: cs_courses - art_courses

print(art_courses.difference(cs_courses))
# Output: {'Art', 'Drawing'}

# --- union() - ALL elements from BOTH sets (no duplicates) ---
print(cs_courses.union(art_courses))
# Output: {'History', 'Math', 'Physics', 'ComSci', 'Art', 'Drawing'}
# Shorthand: cs_courses | art_courses

# --- symmetric_difference() - Elements in EITHER set, but not BOTH ---
print(cs_courses.symmetric_difference(art_courses))
# Output: {'Physics', 'ComSci', 'Art', 'Drawing'}
# Shorthand: cs_courses ^ art_courses


# =============================================================================
# 3.5 SET COMPARISONS
# =============================================================================

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 3}

# --- issubset() - Is all of A in B? ---
print(set_a.issubset(set_b))
# Output: True

# --- issuperset() - Does B contain all of A? ---
print(set_b.issuperset(set_a))
# Output: True

# --- isdisjoint() - Do they have NO common elements? ---
print(set_a.isdisjoint({4, 5, 6}))
# Output: True

print(set_a.isdisjoint({3, 4, 5}))
# Output: False (3 is common)


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
LISTS []
- Ordered, mutable, allows duplicates
- Use when: Order matters, need to modify data, allow duplicates
- Methods: append(), insert(), extend(), remove(), pop(), sort(), reverse()
- Access: By index, slicing

TUPLES ()
- Ordered, IMMUTABLE, allows duplicates
- Use when: Data shouldn't change, returning multiple values, dict keys
- Methods: Only count() and index()
- Access: By index, slicing
- Special: Tuple unpacking (x, y = coordinates)

SETS {}
- Unordered, mutable, NO duplicates
- Use when: Need unique values, fast membership testing, set operations
- Methods: add(), remove(), discard(), union(), intersection(), difference()
- Access: Cannot access by index (no order!)
- Special: Set operations (union, intersection, difference)

COMPARISON:
| Feature     | List  | Tuple | Set   |
|-------------|-------|-------|-------|
| Ordered     | Yes   | Yes   | No    |
| Mutable     | Yes   | No    | Yes   |
| Duplicates  | Yes   | Yes   | No    |
| Indexing    | Yes   | Yes   | No    |
| Syntax      | []    | ()    | {}    |
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: List Manipulation [EASY]
# Create a list of 5 fruits, then:
# a) Add 'mango' to the end
# b) Insert 'grape' at position 2
# c) Remove 'apple' (if it exists)
# d) Sort the list alphabetically
fruits = ['apple', 'banana', 'orange', 'kiwi', 'strawberry']
# TODO: Write your code here

# Solution:
# fruits.append('mango')
# fruits.insert(2, 'grape')
# if 'apple' in fruits:
#     fruits.remove('apple')
# fruits.sort()
# print(fruits)


# Exercise 2: List Statistics [EASY]
# Given a list of numbers, find:
# a) The sum of all numbers
# b) The average (sum / count)
# c) The maximum and minimum values
numbers = [23, 45, 67, 12, 89, 34, 56]
# TODO: Write your code here

# Solution:
# total = sum(numbers)
# average = total / len(numbers)
# max_val = max(numbers)
# min_val = min(numbers)
# print(f"Sum: {total}, Avg: {average:.2f}, Max: {max_val}, Min: {min_val}")


# Exercise 3: Tuple Unpacking [EASY]
# Given a tuple of (name, age, city), unpack it into separate variables
# and print a formatted message
person = ('Om', 25, 'Mumbai')
# TODO: Write your code here

# Solution:
# name, age, city = person
# print(f"{name} is {age} years old and lives in {city}")


# Exercise 4: Remove Duplicates [MEDIUM]
# Given a list with duplicates, create a new list with only unique values
# Preserve the original order
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 2]
# Hint: Use a set to track seen values
# TODO: Write your code here

# Solution:
# seen = set()
# unique = []
# for num in numbers:
#     if num not in seen:
#         seen.add(num)
#         unique.append(num)
# print(unique)  # Output: [1, 2, 3, 4, 5]


# Exercise 5: Common Elements [MEDIUM]
# Find common elements between two lists
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [4, 5, 6, 7, 8, 9]
# Hint: Convert to sets and use intersection
# TODO: Write your code here

# Solution:
# common = list(set(list_1).intersection(set(list_2)))
# print(common)  # Output: [4, 5, 6]


# Exercise 6: Frequency Counter [MEDIUM]
# Count how many times each element appears in a list
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# Hint: Use a dictionary or count() method
# TODO: Write your code here

# Solution:
# frequency = {}
# for item in items:
#     frequency[item] = items.count(item)
# print(frequency)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}


# Exercise 7: Matrix Operations [CHALLENGE]
# Given a 2D list (matrix), find:
# a) Sum of all elements
# b) Largest element
# c) Sum of each row
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# TODO: Write your code here

# Solution:
# total_sum = sum(sum(row) for row in matrix)
# largest = max(max(row) for row in matrix)
# row_sums = [sum(row) for row in matrix]
# print(f"Total: {total_sum}, Largest: {largest}, Row sums: {row_sums}")


# Exercise 8: Set Operations [CHALLENGE]
# Given three sets of students in different clubs:
# a) Find students who are in ALL three clubs
# b) Find students who are in at least one club
# c) Find students who are ONLY in the chess club
chess_club = {'Alice', 'Bob', 'Charlie', 'David'}
math_club = {'Bob', 'Charlie', 'Eve', 'Frank'}
science_club = {'Charlie', 'David', 'Eve', 'Grace'}
# TODO: Write your code here

# Solution:
# all_three = chess_club & math_club & science_club
# at_least_one = chess_club | math_club | science_club
# only_chess = chess_club - math_club - science_club
# print(f"In all three: {all_three}")
# print(f"In at least one: {at_least_one}")
# print(f"Only chess: {only_chess}")


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Modifying list while iterating
   ❌ for item in my_list:
          if condition:
              my_list.remove(item)  # Causes unexpected behavior
   ✅ new_list = [item for item in my_list if not condition]

2. Confusing append() and extend()
   ❌ my_list.append([1, 2, 3])  # Adds list as single element
   ✅ my_list.extend([1, 2, 3])  # Adds each element

3. Creating reference instead of copy
   ❌ copy = original  # Both point to same list
   ✅ copy = original.copy()  # Creates new list

4. Trying to modify tuples
   ❌ my_tuple[0] = 'new'  # TypeError
   ✅ my_tuple = ('new',) + my_tuple[1:]  # Create new tuple

5. Using {} for empty set
   ❌ empty = {}  # This is a dict, not a set!
   ✅ empty = set()  # Correct empty set

6. Assuming set order
   ❌ my_set = {3, 1, 2}
      print(my_set[0])  # TypeError: sets don't support indexing
   ✅ print(list(my_set)[0])  # Convert to list first (but order not guaranteed)

7. Forgetting single-element tuple needs comma
   ❌ single = ('item')  # This is just a string!
   ✅ single = ('item',)  # This is a tuple
"""