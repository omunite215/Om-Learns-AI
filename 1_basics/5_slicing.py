"""
================================================================================
PYTHON FUNDAMENTALS: SLICING LISTS AND STRINGS
================================================================================
Day: 7

Description:
    Comprehensive guide to Python slicing techniques for lists and strings.
    Covers basic slicing, step parameter, negative indices, reversing
    sequences, slice assignment, and slice objects.

Learning Objectives:
    - Master slicing syntax [start:stop:step]
    - Use negative indices for slicing from the end
    - Reverse sequences using slicing
    - Modify lists using slice assignment
    - Create and use slice objects
    - Apply slicing to strings, lists, and tuples

Prerequisites:
    - Basic Python syntax
    - Lists and strings fundamentals
================================================================================
"""

# =============================================================================
# 1. BASIC SLICING SYNTAX
# =============================================================================

"""
SLICING SYNTAX: sequence[start:stop:step]

- start: Index to begin (inclusive, default 0)
- stop: Index to end (exclusive, default len(sequence))
- step: Increment between indices (default 1)

All three are optional!
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Basic slicing [start:stop] ---
print(my_list[0:5])
# Output: [0, 1, 2, 3, 4]
# Gets indices 0, 1, 2, 3, 4 (stop index NOT included)

print(my_list[2:7])
# Output: [2, 3, 4, 5, 6]

print(my_list[5:10])
# Output: [5, 6, 7, 8, 9]


# =============================================================================
# 2. OMITTING START AND STOP
# =============================================================================

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Omit start (defaults to 0) ---
print(my_list[:5])
# Output: [0, 1, 2, 3, 4]
# Same as my_list[0:5]

# --- Omit stop (defaults to end) ---
print(my_list[5:])
# Output: [5, 6, 7, 8, 9]
# Same as my_list[5:10]

# --- Omit both (copies entire list) ---
print(my_list[:])
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Creates a shallow copy of the list


# =============================================================================
# 3. NEGATIVE INDICES
# =============================================================================

"""
NEGATIVE INDEXING:
- -1 is the last element
- -2 is second from last
- And so on...

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Positive:  0  1  2  3  4  5  6  7  8  9
Negative:-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Access single element with negative index ---
print(my_list[-1])
# Output: 9 (last element)

print(my_list[-2])
# Output: 8 (second from last)

print(my_list[-10])
# Output: 0 (first element, same as my_list[0])

# --- Slicing with negative indices ---
print(my_list[-5:])
# Output: [5, 6, 7, 8, 9]
# Last 5 elements

print(my_list[:-2])
# Output: [0, 1, 2, 3, 4, 5, 6, 7]
# Everything except last 2 elements

print(my_list[-7:-2])
# Output: [3, 4, 5, 6, 7]
# From index -7 to -2 (exclusive)

print(my_list[-5:-1])
# Output: [5, 6, 7, 8]
# From 5th last to 2nd last


# =============================================================================
# 4. STEP PARAMETER
# =============================================================================

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Basic step ---
print(my_list[0:10:2])
# Output: [0, 2, 4, 6, 8]
# Every 2nd element from index 0 to 9

print(my_list[0:3:2])
# Output: [0, 2]
# From index 0 to 2, step by 2

print(my_list[1:10:2])
# Output: [1, 3, 5, 7, 9]
# Every 2nd element starting from index 1 (odd indices)

# --- Step with omitted start/stop ---
print(my_list[::2])
# Output: [0, 2, 4, 6, 8]
# Every 2nd element from entire list

print(my_list[::3])
# Output: [0, 3, 6, 9]
# Every 3rd element

print(my_list[1::2])
# Output: [1, 3, 5, 7, 9]
# Every 2nd element starting from index 1


# =============================================================================
# 5. NEGATIVE STEP (REVERSING)
# =============================================================================

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Reverse entire list ---
print(my_list[::-1])
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Most Pythonic way to reverse!

# --- Reverse with step ---
print(my_list[::-2])
# Output: [9, 7, 5, 3, 1]
# Every 2nd element in reverse

# --- Reverse a portion ---
print(my_list[5:0:-1])
# Output: [5, 4, 3, 2, 1]
# From index 5 down to 1 (0 not included)

print(my_list[8:3:-1])
# Output: [8, 7, 6, 5, 4]
# From index 8 down to 4

# Note: With negative step, start should be > stop


# =============================================================================
# 6. SLICING STRINGS
# =============================================================================

# Slicing works the same way on strings!

sample_string = "Good morning!!"

# --- Basic string slicing ---
print(sample_string[0:4])
# Output: 'Good'

print(sample_string[5:12])
# Output: 'morning'

print(sample_string[:4])
# Output: 'Good'

print(sample_string[5:])
# Output: 'morning!!'

# --- Negative indices ---
print(sample_string[-2:])
# Output: '!!'

print(sample_string[:-2])
# Output: 'Good morning'

# --- Reverse string ---
print(sample_string[::-1])
# Output: '!!gninrom dooG'

# --- Every nth character ---
print(sample_string[::2])
# Output: 'Go onng!'

# --- Practical: Get file extension ---
filename = "document.pdf"
print(filename[-3:])
# Output: 'pdf'

# --- Practical: Remove extension ---
print(filename[:-4])
# Output: 'document'


# =============================================================================
# 7. SLICING TUPLES
# =============================================================================

# Slicing also works on tuples

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(my_tuple[2:7])
# Output: (2, 3, 4, 5, 6)

print(my_tuple[::-1])
# Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

print(my_tuple[::2])
# Output: (0, 2, 4, 6, 8)

# Note: Result is also a tuple


# =============================================================================
# 8. SLICE ASSIGNMENT (Lists Only)
# =============================================================================

# You can modify lists using slice assignment

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Replace a portion ---
my_list[2:5] = ['a', 'b', 'c']
print(my_list)
# Output: [0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9]

# --- Replace with different length ---
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list[2:5] = ['a', 'b']  # Fewer elements
print(my_list)
# Output: [0, 1, 'a', 'b', 5, 6, 7, 8, 9]

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list[2:5] = ['a', 'b', 'c', 'd', 'e']  # More elements
print(my_list)
# Output: [0, 1, 'a', 'b', 'c', 'd', 'e', 5, 6, 7, 8, 9]

# --- Insert without removing ---
my_list = [0, 1, 2, 3, 4]
my_list[2:2] = ['a', 'b', 'c']  # Insert at index 2
print(my_list)
# Output: [0, 1, 'a', 'b', 'c', 2, 3, 4]

# --- Delete using slice assignment ---
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list[2:5] = []  # Remove indices 2, 3, 4
print(my_list)
# Output: [0, 1, 5, 6, 7, 8, 9]

# Note: Strings are immutable, can't use slice assignment!
# sample_string[0:4] = "Bad"  # TypeError!


# =============================================================================
# 9. SLICE OBJECTS
# =============================================================================

# Create reusable slice objects with slice()

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Creating slice objects ---
first_five = slice(0, 5)
print(my_list[first_five])
# Output: [0, 1, 2, 3, 4]

# Same as my_list[0:5]

last_three = slice(-3, None)  # None = to the end
print(my_list[last_three])
# Output: [7, 8, 9]

# --- Slice with step ---
every_other = slice(None, None, 2)  # [::2]
print(my_list[every_other])
# Output: [0, 2, 4, 6, 8]

reverse_slice = slice(None, None, -1)  # [::-1]
print(my_list[reverse_slice])
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# --- Reusing slices on different sequences ---
s = slice(1, 5)

print(my_list[s])
# Output: [1, 2, 3, 4]

print("Hello World"[s])
# Output: 'ello'

print((10, 20, 30, 40, 50, 60)[s])
# Output: (20, 30, 40, 50)

# --- Slice object attributes ---
my_slice = slice(1, 10, 2)
print(f"start: {my_slice.start}")   # Output: 1
print(f"stop: {my_slice.stop}")     # Output: 10
print(f"step: {my_slice.step}")     # Output: 2


# =============================================================================
# 10. PRACTICAL EXAMPLES
# =============================================================================

# --- Palindrome check ---
word = "racecar"
is_palindrome = word == word[::-1]
print(f"'{word}' is palindrome: {is_palindrome}")
# Output: 'racecar' is palindrome: True

# --- Get first and last n elements ---
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_3 = data[:3]
last_3 = data[-3:]
print(f"First 3: {first_3}, Last 3: {last_3}")
# Output: First 3: [10, 20, 30], Last 3: [80, 90, 100]

# --- Remove first and last elements ---
trimmed = data[1:-1]
print(f"Trimmed: {trimmed}")
# Output: Trimmed: [20, 30, 40, 50, 60, 70, 80, 90]

# --- Split list into chunks ---
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_half = data[:len(data)//2]
second_half = data[len(data)//2:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")
# Output: First half: [1, 2, 3, 4, 5]
# Output: Second half: [6, 7, 8, 9, 10]

# --- Extract domain from email ---
email = "user@example.com"
at_index = email.index('@')
domain = email[at_index + 1:]
print(f"Domain: {domain}")
# Output: Domain: example.com

# --- Get every nth character ---
text = "abcdefghijklmnop"
every_third = text[::3]
print(f"Every 3rd: {every_third}")
# Output: Every 3rd: adgjmp

# --- Reverse words in sentence ---
sentence = "Hello World Python"
words = sentence.split()
reversed_words = words[::-1]
reversed_sentence = ' '.join(reversed_words)
print(f"Reversed: {reversed_sentence}")
# Output: Reversed: Python World Hello


# =============================================================================
# 11. SLICING VS OTHER METHODS
# =============================================================================

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Copying a list ---
# Method 1: Slicing (most common)
copy1 = my_list[:]

# Method 2: list() constructor
copy2 = list(my_list)

# Method 3: copy() method
copy3 = my_list.copy()

# All create shallow copies

# --- Reversing a list ---
# Method 1: Slicing (creates new list)
reversed1 = my_list[::-1]

# Method 2: reversed() function (returns iterator)
reversed2 = list(reversed(my_list))

# Method 3: reverse() method (modifies in place)
my_list_copy = my_list.copy()
my_list_copy.reverse()

print(f"Original: {my_list}")
print(f"Slice reversed: {reversed1}")
print(f"reversed() reversed: {reversed2}")
print(f"reverse() reversed: {my_list_copy}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Basic Syntax: sequence[start:stop:step]
   - start: Beginning index (inclusive, default 0)
   - stop: Ending index (exclusive, default end)
   - step: Increment (default 1)

2. Omitting Values
   - [:5] - First 5 elements
   - [5:] - From index 5 to end
   - [:] - Copy entire sequence
   - [::2] - Every 2nd element

3. Negative Indices
   - [-1] - Last element
   - [-3:] - Last 3 elements
   - [:-2] - All except last 2
   - [::-1] - Reverse entire sequence

4. Step Parameter
   - [::2] - Every 2nd element
   - [1::2] - Every 2nd starting from index 1
   - [::-1] - Reverse
   - [::-2] - Every 2nd in reverse

5. Slice Assignment (Lists Only)
   - list[2:5] = [a, b, c] - Replace portion
   - list[2:2] = [a, b] - Insert at index 2
   - list[2:5] = [] - Delete portion

6. Slice Objects
   - s = slice(start, stop, step)
   - Reusable across sequences
   - Access attributes: s.start, s.stop, s.step

7. Common Patterns
   - Reverse: [::-1]
   - Copy: [:]
   - First n: [:n]
   - Last n: [-n:]
   - Remove first/last: [1:-1]
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Basic Slicing [EASY]
# Given the list below, use slicing to get:
# a) First 4 elements
# b) Last 3 elements
# c) Elements from index 2 to 6
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# TODO: Write your code here

# Solution:
# print(numbers[:4])      # [10, 20, 30, 40]
# print(numbers[-3:])     # [80, 90, 100]
# print(numbers[2:7])     # [30, 40, 50, 60, 70]


# Exercise 2: Step Slicing [EASY]
# Using the same list:
# a) Get every 2nd element
# b) Get every 3rd element starting from index 1
# c) Get elements at even indices
# TODO: Write your code here

# Solution:
# print(numbers[::2])     # [10, 30, 50, 70, 90]
# print(numbers[1::3])    # [20, 50, 80]
# print(numbers[::2])     # [10, 30, 50, 70, 90] (same as a)


# Exercise 3: Reverse Operations [MEDIUM]
# a) Reverse the list
# b) Get last 5 elements in reverse order
# c) Reverse only the middle portion (indices 3 to 7)
# TODO: Write your code here

# Solution:
# print(numbers[::-1])           # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
# print(numbers[-1:-6:-1])       # [100, 90, 80, 70, 60]
# print(numbers[7:2:-1])         # [80, 70, 60, 50, 40]


# Exercise 4: String Slicing [MEDIUM]
# Given the string:
text = "Python Programming Language"
# a) Extract "Python"
# b) Extract "Language"
# c) Extract "Programming"
# d) Reverse the entire string
# e) Get every other character
# TODO: Write your code here

# Solution:
# print(text[:6])         # Python
# print(text[-8:])        # Language
# print(text[7:18])       # Programming
# print(text[::-1])       # egaugnaL gnimmargorP nohtyP
# print(text[::2])        # Pto rgamn agae


# Exercise 5: Slice Assignment [MEDIUM]
# Start with: my_list = [1, 2, 3, 4, 5]
# a) Replace [2, 3, 4] with [20, 30, 40]
# b) Insert [100, 200] between 1 and 2 (reset list first)
# c) Remove the last 2 elements (reset list first)
# TODO: Write your code here

# Solution:
# my_list = [1, 2, 3, 4, 5]
# my_list[1:4] = [20, 30, 40]
# print(my_list)  # [1, 20, 30, 40, 5]
#
# my_list = [1, 2, 3, 4, 5]
# my_list[1:1] = [100, 200]
# print(my_list)  # [1, 100, 200, 2, 3, 4, 5]
#
# my_list = [1, 2, 3, 4, 5]
# my_list[-2:] = []
# print(my_list)  # [1, 2, 3]


# Exercise 6: Palindrome Checker [MEDIUM]
# Write code to check if these strings are palindromes:
words = ["radar", "hello", "level", "world", "madam"]
# TODO: Write your code here

# Solution:
# for word in words:
#     is_palindrome = word == word[::-1]
#     print(f"'{word}' is palindrome: {is_palindrome}")


# Exercise 7: Extract URL Parts [CHALLENGE]
# Given a URL, extract:
# a) Protocol (http or https)
# b) Domain name
# c) Path
url = "https://www.example.com/path/to/page"
# TODO: Write your code here

# Solution:
# protocol_end = url.index("://")
# protocol = url[:protocol_end]
# 
# domain_start = protocol_end + 3
# domain_end = url.index("/", domain_start)
# domain = url[domain_start:domain_end]
# 
# path = url[domain_end:]
# 
# print(f"Protocol: {protocol}")  # https
# print(f"Domain: {domain}")      # www.example.com
# print(f"Path: {path}")          # /path/to/page


# Exercise 8: Matrix Operations [CHALLENGE]
# Given a 2D list (matrix), use slicing to:
# a) Get the first row
# b) Get the last row
# c) Reverse each row
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# TODO: Write your code here

# Solution:
# print(f"First row: {matrix[0]}")           # [1, 2, 3, 4]
# print(f"Last row: {matrix[-1]}")           # [9, 10, 11, 12]
# reversed_rows = [row[::-1] for row in matrix]
# print(f"Reversed rows: {reversed_rows}")   # [[4,3,2,1], [8,7,6,5], [12,11,10,9]]


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting stop index is exclusive
   ❌ my_list[0:3] gives indices 0, 1, 2 (not 0, 1, 2, 3)
   ✅ my_list[0:4] to get first 4 elements

2. Confusing negative indices
   ❌ my_list[-1:-3] returns [] (empty!)
   ✅ my_list[-3:-1] returns last 3 except last one
   ✅ my_list[-3:] returns last 3

3. Wrong direction with negative step
   ❌ my_list[0:5:-1] returns [] (can't go backwards from 0 to 5)
   ✅ my_list[5:0:-1] returns [5, 4, 3, 2, 1]

4. Slice assignment on immutable types
   ❌ my_string[0:3] = "New"  # TypeError!
   ✅ my_string = "New" + my_string[3:]

5. Out of bounds? No error!
   my_list = [1, 2, 3]
   my_list[0:100]  # Returns [1, 2, 3] (no error)
   my_list[100]    # IndexError! (single index)

6. Modifying while slicing creates new object
   original = [1, 2, 3]
   sliced = original[:]  # Different object
   sliced.append(4)
   print(original)  # Still [1, 2, 3]
"""