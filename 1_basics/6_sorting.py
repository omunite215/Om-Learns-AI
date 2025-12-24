"""
================================================================================
PYTHON FUNDAMENTALS: SORTING LISTS, TUPLES, AND OBJECTS
================================================================================
Day: 9

Description:
    Comprehensive guide to sorting in Python covering both built-in methods
    (sort(), sorted()) and manual sorting algorithms. Includes sorting with
    custom keys, lambda functions, and sorting complex objects.

Learning Objectives:
    - Use sort() method and sorted() function
    - Sort in ascending and descending order
    - Use key parameter for custom sorting
    - Sort tuples, dictionaries, and objects
    - Understand manual sorting algorithms
    - Use attrgetter and itemgetter for sorting

Prerequisites:
    - Lists, tuples, and dictionaries
    - Functions and lambda expressions
================================================================================
"""

# =============================================================================
# 1. BASIC SORTING - sort() vs sorted()
# =============================================================================

# --- sort() method - Modifies list IN PLACE ---
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
li.sort()
print(li)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Original list is modified, returns None

# --- sorted() function - Returns NEW sorted list ---
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
sorted_li = sorted(li)
print(f"Original: {li}")
print(f"Sorted: {sorted_li}")
# Output: 
# Original: [9, 1, 8, 2, 7, 3, 6, 4, 5] (unchanged)
# Sorted: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Key difference ---
# sort() - Only for lists, modifies in place, returns None
# sorted() - Works on any iterable, returns new list, original unchanged


# =============================================================================
# 2. SORTING IN REVERSE ORDER
# =============================================================================

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# --- Descending with sort() ---
li.sort(reverse=True)
print(li)
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# --- Descending with sorted() ---
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
sorted_desc = sorted(li, reverse=True)
print(sorted_desc)
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1]


# =============================================================================
# 3. SORTING WITH KEY PARAMETER
# =============================================================================

# key parameter specifies a function to be called on each element before comparing

# --- Sort by absolute value ---
li = [-6, -5, -4, 1, 2, 3]
sorted_abs = sorted(li, key=abs)
print(sorted_abs)
# Output: [1, 2, 3, -4, -5, -6]
# Sorted by: 1, 2, 3, 4, 5, 6 (absolute values)

# --- Sort strings by length ---
words = ['banana', 'pie', 'Washington', 'book']
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)
# Output: ['pie', 'book', 'banana', 'Washington']

# --- Sort strings case-insensitive ---
words = ['Banana', 'pie', 'Apple', 'cherry']
sorted_lower = sorted(words, key=str.lower)
print(sorted_lower)
# Output: ['Apple', 'Banana', 'cherry', 'pie']


# =============================================================================
# 4. SORTING WITH LAMBDA FUNCTIONS
# =============================================================================

# Lambda allows custom sorting logic

# --- Sort tuples by second element ---
tuples = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)
# Output: [(3, 'a'), (1, 'b'), (2, 'c')]

# --- Sort by last character of string ---
words = ['banana', 'apple', 'cherry', 'date']
sorted_by_last = sorted(words, key=lambda x: x[-1])
print(sorted_by_last)
# Output: ['banana', 'apple', 'date', 'cherry']

# --- Sort by multiple criteria ---
students = [('John', 85), ('Jane', 90), ('Bob', 85), ('Alice', 90)]
# Sort by grade (desc), then by name (asc)
sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
print(sorted_students)
# Output: [('Alice', 90), ('Jane', 90), ('Bob', 85), ('John', 85)]


# =============================================================================
# 5. SORTING DICTIONARIES
# =============================================================================

# --- Sort list of dictionaries by key ---
students = [
    {'name': 'John', 'grade': 85, 'age': 20},
    {'name': 'Jane', 'grade': 90, 'age': 19},
    {'name': 'Bob', 'grade': 78, 'age': 21},
    {'name': 'Alice', 'grade': 92, 'age': 20}
]

# Sort by grade
by_grade = sorted(students, key=lambda x: x['grade'])
print("By grade:")
for s in by_grade:
    print(f"  {s['name']}: {s['grade']}")
# Output: Bob: 78, John: 85, Jane: 90, Alice: 92

# Sort by grade descending
by_grade_desc = sorted(students, key=lambda x: x['grade'], reverse=True)
print("\nBy grade (desc):")
for s in by_grade_desc:
    print(f"  {s['name']}: {s['grade']}")
# Output: Alice: 92, Jane: 90, John: 85, Bob: 78

# Sort by name
by_name = sorted(students, key=lambda x: x['name'])
print("\nBy name:")
for s in by_name:
    print(f"  {s['name']}")
# Output: Alice, Bob, Jane, John


# =============================================================================
# 6. USING ATTRGETTER AND ITEMGETTER
# =============================================================================

from operator import itemgetter, attrgetter

# --- itemgetter for dictionaries/tuples ---
students = [
    {'name': 'John', 'grade': 85},
    {'name': 'Jane', 'grade': 90},
    {'name': 'Bob', 'grade': 78}
]

# Same as: key=lambda x: x['grade']
by_grade = sorted(students, key=itemgetter('grade'))
print([s['name'] for s in by_grade])
# Output: ['Bob', 'John', 'Jane']

# Sort by multiple keys
students = [
    {'name': 'John', 'grade': 85, 'age': 20},
    {'name': 'Jane', 'grade': 90, 'age': 19},
    {'name': 'Bob', 'grade': 85, 'age': 21}
]
by_grade_age = sorted(students, key=itemgetter('grade', 'age'))
print([(s['name'], s['grade'], s['age']) for s in by_grade_age])
# Output: [('John', 85, 20), ('Bob', 85, 21), ('Jane', 90, 19)]

# --- attrgetter for objects ---
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

students = [Student('John', 85), Student('Jane', 90), Student('Bob', 78)]

# Same as: key=lambda x: x.grade
by_grade = sorted(students, key=attrgetter('grade'))
print(by_grade)
# Output: [Student(Bob, 78), Student(John, 85), Student(Jane, 90)]


# =============================================================================
# 7. SORTING TUPLES
# =============================================================================

# Tuples are immutable, so use sorted() (returns new list)

my_tuple = (9, 1, 8, 2, 7, 3)

# sorted() returns a list!
sorted_list = sorted(my_tuple)
print(sorted_list)
# Output: [1, 2, 3, 7, 8, 9]

# Convert back to tuple if needed
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)
# Output: (1, 2, 3, 7, 8, 9)


# =============================================================================
# 8. SORTING STRINGS
# =============================================================================

# Strings are also iterable - sorted() returns list of characters

my_string = "python"
sorted_chars = sorted(my_string)
print(sorted_chars)
# Output: ['h', 'n', 'o', 'p', 't', 'y']

# Convert back to string
sorted_string = ''.join(sorted(my_string))
print(sorted_string)
# Output: 'hnopty'

# Sort list of strings
words = ['Banana', 'apple', 'Cherry', 'date']

# Default: case-sensitive (uppercase first)
print(sorted(words))
# Output: ['Banana', 'Cherry', 'apple', 'date']

# Case-insensitive
print(sorted(words, key=str.lower))
# Output: ['apple', 'Banana', 'Cherry', 'date']


# =============================================================================
# 9. MANUAL SORTING ALGORITHMS
# =============================================================================

# Understanding how sorting works under the hood

# --- Bubble Sort ---
def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly swap adjacent elements if in wrong order.
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

nums = [64, 34, 25, 12, 22, 11, 90]
print(f"Bubble Sort: {bubble_sort(nums)}")
# Output: [11, 12, 22, 25, 34, 64, 90]


# --- Selection Sort ---
def selection_sort(arr):
    """
    Selection Sort: Find minimum and place at beginning.
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

print(f"Selection Sort: {selection_sort(nums)}")
# Output: [11, 12, 22, 25, 34, 64, 90]


# --- Insertion Sort ---
def insertion_sort(arr):
    """
    Insertion Sort: Build sorted array one item at a time.
    Time: O(n²), Space: O(1)
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

print(f"Insertion Sort: {insertion_sort(nums)}")
# Output: [11, 12, 22, 25, 34, 64, 90]


# --- Quick Sort ---
def quick_sort(arr):
    """
    Quick Sort: Divide and conquer using pivot.
    Time: O(n log n) average, O(n²) worst, Space: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

print(f"Quick Sort: {quick_sort(nums)}")
# Output: [11, 12, 22, 25, 34, 64, 90]


# --- Merge Sort ---
def merge_sort(arr):
    """
    Merge Sort: Divide, sort, and merge.
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(f"Merge Sort: {merge_sort(nums)}")
# Output: [11, 12, 22, 25, 34, 64, 90]


# =============================================================================
# 10. SORTING ALGORITHM COMPARISON
# =============================================================================

"""
| Algorithm      | Best      | Average   | Worst     | Space  | Stable |
|----------------|-----------|-----------|-----------|--------|--------|
| Bubble Sort    | O(n)      | O(n²)     | O(n²)     | O(1)   | Yes    |
| Selection Sort | O(n²)     | O(n²)     | O(n²)     | O(1)   | No     |
| Insertion Sort | O(n)      | O(n²)     | O(n²)     | O(1)   | Yes    |
| Quick Sort     | O(n log n)| O(n log n)| O(n²)     | O(log n)| No    |
| Merge Sort     | O(n log n)| O(n log n)| O(n log n)| O(n)   | Yes    |
| Python's sort  | O(n log n)| O(n log n)| O(n log n)| O(n)   | Yes    |

Python uses Timsort (hybrid of merge sort and insertion sort)
- Best for real-world data
- Always use built-in sort() or sorted() unless learning algorithms!
"""


# =============================================================================
# 11. STABLE VS UNSTABLE SORTING
# =============================================================================

"""
STABLE SORT: Maintains relative order of equal elements
UNSTABLE SORT: May change relative order of equal elements

Python's sort is STABLE - important for sorting by multiple keys!
"""

# Example of stable sort importance
students = [
    ('John', 'A'),
    ('Jane', 'B'),
    ('Bob', 'A'),
    ('Alice', 'B')
]

# First sort by name
by_name = sorted(students, key=lambda x: x[0])
print(f"By name: {by_name}")
# Output: [('Alice', 'B'), ('Bob', 'A'), ('Jane', 'B'), ('John', 'A')]

# Then sort by grade - stable sort keeps name order within same grade
by_grade = sorted(by_name, key=lambda x: x[1])
print(f"By grade (stable): {by_grade}")
# Output: [('Bob', 'A'), ('John', 'A'), ('Alice', 'B'), ('Jane', 'B')]
# Within grade 'A': Bob before John (alphabetical order preserved)


# =============================================================================
# 12. PRACTICAL SORTING EXAMPLES
# =============================================================================

# --- Sort files by extension ---
files = ['doc.pdf', 'image.png', 'data.csv', 'script.py', 'notes.txt']
by_extension = sorted(files, key=lambda x: x.split('.')[-1])
print(f"By extension: {by_extension}")
# Output: ['data.csv', 'doc.pdf', 'image.png', 'script.py', 'notes.txt']

# --- Sort dates ---
dates = ['2024-01-15', '2023-12-01', '2024-03-20', '2023-11-30']
sorted_dates = sorted(dates)  # String comparison works for ISO format!
print(f"Sorted dates: {sorted_dates}")
# Output: ['2023-11-30', '2023-12-01', '2024-01-15', '2024-03-20']

# --- Sort by frequency ---
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
by_frequency = sorted(set(items), key=lambda x: items.count(x), reverse=True)
print(f"By frequency: {by_frequency}")
# Output: ['apple', 'banana', 'cherry']

# --- Sort mixed numbers and strings ---
mixed = ['item10', 'item2', 'item1', 'item20']
# Default string sort
print(f"String sort: {sorted(mixed)}")
# Output: ['item1', 'item10', 'item2', 'item20']

# Natural sort (extract number)
import re
natural_sort = sorted(mixed, key=lambda x: int(re.search(r'\d+', x).group()))
print(f"Natural sort: {natural_sort}")
# Output: ['item1', 'item2', 'item10', 'item20']


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. sort() vs sorted()
   - sort(): Modifies list in place, returns None
   - sorted(): Returns new list, works on any iterable

2. Reverse Sorting
   - sort(reverse=True) or sorted(reverse=True)

3. Custom Sorting with key
   - key=len (by length)
   - key=str.lower (case-insensitive)
   - key=lambda x: x[1] (by specific element)
   - key=lambda x: (x[1], x[0]) (multiple criteria)

4. Sorting Complex Objects
   - Dictionaries: key=lambda x: x['field']
   - Objects: key=attrgetter('attr')
   - Tuples: key=itemgetter(index)

5. Sorting Algorithms
   - Bubble, Selection, Insertion: O(n²) - educational
   - Quick Sort, Merge Sort: O(n log n) - efficient
   - Python's Timsort: Best for real-world use

6. Stable Sorting
   - Python's sort is stable
   - Equal elements maintain relative order
   - Important for multi-key sorting

7. Best Practice
   - Always use built-in sort()/sorted()
   - Use key parameter for custom logic
   - Avoid lambda if function exists (len, abs, str.lower)
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Basic Sorting [EASY]
# Sort the list in ascending and descending order
nums = [45, 22, 78, 12, 56, 89, 33]
# TODO: Write your code here

# Solution:
# ascending = sorted(nums)
# descending = sorted(nums, reverse=True)
# print(f"Ascending: {ascending}")
# print(f"Descending: {descending}")


# Exercise 2: Sort by Length [EASY]
# Sort words by their length (shortest to longest)
words = ['elephant', 'cat', 'dog', 'butterfly', 'ant']
# TODO: Write your code here

# Solution:
# by_length = sorted(words, key=len)
# print(by_length)  # ['cat', 'dog', 'ant', 'elephant', 'butterfly']


# Exercise 3: Sort Dictionaries [MEDIUM]
# Sort the products by price (lowest to highest)
products = [
    {'name': 'Laptop', 'price': 999},
    {'name': 'Mouse', 'price': 29},
    {'name': 'Keyboard', 'price': 79},
    {'name': 'Monitor', 'price': 299}
]
# TODO: Write your code here

# Solution:
# by_price = sorted(products, key=lambda x: x['price'])
# for p in by_price:
#     print(f"{p['name']}: ${p['price']}")


# Exercise 4: Sort Tuples [MEDIUM]
# Sort students by grade (highest first), then by name (alphabetical)
students = [('John', 85), ('Alice', 92), ('Bob', 85), ('Jane', 92)]
# TODO: Write your code here

# Solution:
# sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
# print(sorted_students)
# [('Alice', 92), ('Jane', 92), ('Bob', 85), ('John', 85)]


# Exercise 5: Case-Insensitive Sort [MEDIUM]
# Sort names alphabetically, ignoring case
names = ['alice', 'Bob', 'CHARLIE', 'David', 'eve']
# TODO: Write your code here

# Solution:
# sorted_names = sorted(names, key=str.lower)
# print(sorted_names)  # ['alice', 'Bob', 'CHARLIE', 'David', 'eve']


# Exercise 6: Sort by Last Name [CHALLENGE]
# Sort full names by last name
full_names = ['John Smith', 'Alice Johnson', 'Bob Williams', 'Jane Smith']
# TODO: Write your code here

# Solution:
# by_last_name = sorted(full_names, key=lambda x: x.split()[-1])
# print(by_last_name)
# ['Alice Johnson', 'John Smith', 'Jane Smith', 'Bob Williams']


# Exercise 7: Implement Bubble Sort [CHALLENGE]
# Write your own bubble sort function
def my_bubble_sort(arr):
    # TODO: Implement bubble sort
    pass

# Solution:
# def my_bubble_sort(arr):
#     arr = arr.copy()
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr


# Exercise 8: Sort by Multiple Criteria [CHALLENGE]
# Sort employees by department (asc), then by salary (desc), then by name (asc)
employees = [
    {'name': 'John', 'dept': 'Sales', 'salary': 50000},
    {'name': 'Jane', 'dept': 'IT', 'salary': 60000},
    {'name': 'Bob', 'dept': 'Sales', 'salary': 50000},
    {'name': 'Alice', 'dept': 'IT', 'salary': 65000},
    {'name': 'Charlie', 'dept': 'Sales', 'salary': 55000}
]
# TODO: Write your code here

# Solution:
# sorted_emp = sorted(employees, key=lambda x: (x['dept'], -x['salary'], x['name']))
# for e in sorted_emp:
#     print(f"{e['dept']} - {e['name']}: ${e['salary']}")


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting sort() returns None
   ❌ sorted_list = my_list.sort()  # sorted_list is None!
   ✅ my_list.sort()  # Modifies in place
   ✅ sorted_list = sorted(my_list)  # Returns new list

2. Modifying list while using sorted()
   sorted() creates a new list - original is unchanged!

3. Wrong key function
   ❌ sorted(words, key=len())  # len() is called immediately!
   ✅ sorted(words, key=len)    # Pass function itself

4. Case-sensitive string sorting
   ❌ sorted(['Apple', 'banana'])  # ['Apple', 'banana']
   ✅ sorted(['Apple', 'banana'], key=str.lower)  # ['Apple', 'banana']

5. Sorting incompatible types
   ❌ sorted([1, 'two', 3])  # TypeError in Python 3
   ✅ Ensure all elements are comparable

6. Using inefficient sorting algorithms
   ❌ Implementing bubble sort for large data
   ✅ Use built-in sort()/sorted() - they're optimized!

7. Forgetting stable sort for multi-key
   Python's sort is stable - can sort by secondary key first,
   then primary key, and order is preserved
"""