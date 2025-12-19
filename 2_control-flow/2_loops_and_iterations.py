"""
================================================================================
PYTHON FUNDAMENTALS: LOOPS AND ITERATIONS
================================================================================

Day: 3

Description:
    Comprehensive guide to Python loops and iteration techniques. Covers for
    loops, while loops, loop control statements (break, continue, pass),
    range(), enumerate(), zip(), and nested loops.

Learning Objectives:
    - Master for loops for iterating over sequences
    - Use while loops for conditional iteration
    - Control loop flow with break, continue, and pass
    - Work with range() for numeric iterations
    - Use enumerate() for index-value pairs
    - Combine iterables with zip()
    - Understand nested loops and their applications

Prerequisites:
    - Basic Python syntax
    - Data types (lists, strings, dicts)
    - Conditional statements
================================================================================
"""

# =============================================================================
# 1. BASIC FOR LOOP
# =============================================================================

# For loops iterate over sequences (lists, strings, tuples, etc.)

nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5

# Iterating over a string
for char in "Python":
    print(char)
# Output: P, y, t, h, o, n (each on new line)

# Iterating over a tuple
colors = ('red', 'green', 'blue')
for color in colors:
    print(color)


# =============================================================================
# 2. BREAK STATEMENT
# =============================================================================

# 'break' exits the loop immediately

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found 3! Exiting loop.')
        break
    print(num)
# Output:
# 1
# 2
# Found 3! Exiting loop.

# Practical use: Search and stop when found
names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie']
search_name = 'Bob'

for name in names:
    if name == search_name:
        print(f"Found {search_name}!")
        break
    print(f"Checking {name}...")
# Output:
# Checking John...
# Checking Jane...
# Found Bob!


# =============================================================================
# 3. CONTINUE STATEMENT
# =============================================================================

# 'continue' skips the rest of current iteration and moves to next

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Skipping 3')
        continue
    print(num)
# Output:
# 1
# 2
# Skipping 3
# 4
# 5

# Practical use: Skip invalid data
scores = [85, -1, 90, 75, -1, 88]  # -1 represents missing data

total = 0
count = 0

for score in scores:
    if score < 0:
        continue  # Skip invalid scores
    total += score
    count += 1

print(f"Average: {total / count}")
# Output: Average: 84.5


# =============================================================================
# 4. PASS STATEMENT
# =============================================================================

# 'pass' does nothing - placeholder for future code

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        pass  # TODO: Handle special case later
    print(num)
# Output: 1, 2, 3, 4, 5 (all numbers printed)

# Common use: Empty function or class definition
def future_function():
    pass  # Will implement later

class FutureClass:
    pass  # Will implement later


# =============================================================================
# 5. NESTED LOOPS
# =============================================================================

# Loop inside another loop

nums = [1, 2, 3]
letters = ['a', 'b', 'c']

for num in nums:
    for letter in letters:
        print(num, letter)
# Output:
# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c

# Practical use: Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")  # Separator between tables

# Practical use: 2D list (matrix) iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row
# Output:
# 1 2 3
# 4 5 6
# 7 8 9


# =============================================================================
# 6. RANGE() FUNCTION
# =============================================================================

# range() generates a sequence of numbers

# --- range(stop) - 0 to stop-1 ---
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# --- range(start, stop) - start to stop-1 ---
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# --- range(start, stop, step) - with custom step ---
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8 (even numbers)

for i in range(1, 10, 2):
    print(i)
# Output: 1, 3, 5, 7, 9 (odd numbers)

# --- Counting backwards ---
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# --- Convert to list ---
numbers = list(range(1, 6))
print(numbers)
# Output: [1, 2, 3, 4, 5]


# =============================================================================
# 7. ENUMERATE() FUNCTION
# =============================================================================

# enumerate() returns both index and value

courses = ['History', 'Math', 'Physics', 'CompSci']

# --- Basic enumerate ---
for index, course in enumerate(courses):
    print(index, course)
# Output:
# 0 History
# 1 Math
# 2 Physics
# 3 CompSci

# --- Start counting from 1 ---
for index, course in enumerate(courses, start=1):
    print(f"{index}. {course}")
# Output:
# 1. History
# 2. Math
# 3. Physics
# 4. CompSci

# --- What enumerate actually returns ---
print(list(enumerate(courses)))
# Output: [(0, 'History'), (1, 'Math'), (2, 'Physics'), (3, 'CompSci')]

# --- Without enumerate (less Pythonic) ---
for i in range(len(courses)):
    print(i, courses[i])
# Same output but enumerate is cleaner!


# =============================================================================
# 8. ZIP() FUNCTION
# =============================================================================

# zip() combines multiple iterables into tuples

names = ['Peter', 'Bruce', 'Clark']
heroes = ['Spiderman', 'Batman', 'Superman']

for name, hero in zip(names, heroes):
    print(f"{name} is {hero}")
# Output:
# Peter is Spiderman
# Bruce is Batman
# Clark is Superman

# --- Zip with three lists ---
names = ['Peter', 'Bruce', 'Clark']
heroes = ['Spiderman', 'Batman', 'Superman']
universes = ['Marvel', 'DC', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is {hero} from {universe}")
# Output:
# Peter is Spiderman from Marvel
# Bruce is Batman from DC
# Clark is Superman from DC

# --- Zip stops at shortest iterable ---
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

for num, letter in zip(list1, list2):
    print(num, letter)
# Output: 1 a, 2 b, 3 c (stops at 3, ignores 4 and 5)

# --- Convert to list of tuples ---
print(list(zip(names, heroes)))
# Output: [('Peter', 'Spiderman'), ('Bruce', 'Batman'), ('Clark', 'Superman')]

# --- Create dict from two lists ---
hero_dict = dict(zip(names, heroes))
print(hero_dict)
# Output: {'Peter': 'Spiderman', 'Bruce': 'Batman', 'Clark': 'Superman'}


# =============================================================================
# 9. WHILE LOOPS
# =============================================================================

# While loops run as long as condition is True

# --- Basic while loop ---
x = 0
while x < 5:
    print(x)
    x += 1
# Output: 0, 1, 2, 3, 4

# --- While with break ---
x = 0
while True:  # Infinite loop
    if x == 5:
        break
    print(x)
    x += 1
# Output: 0, 1, 2, 3, 4

# --- While with continue ---
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue  # Skip even numbers
    print(x)
# Output: 1, 3, 5, 7, 9

# --- Practical use: User input validation ---
# password = ""
# while password != "secret":
#     password = input("Enter password: ")
# print("Access granted!")


# =============================================================================
# 10. ELSE CLAUSE WITH LOOPS
# =============================================================================

# 'else' runs if loop completes WITHOUT break

# --- For loop with else ---
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 10:
        print("Found 10!")
        break
else:
    print("10 not found in list")
# Output: 10 not found in list (else executed because no break)

# --- When break is triggered ---
nums = [1, 2, 3, 10, 5]

for num in nums:
    if num == 10:
        print("Found 10!")
        break
else:
    print("10 not found in list")
# Output: Found 10! (else NOT executed because break was triggered)

# --- While loop with else ---
x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("Loop completed normally")
# Output: 0, 1, 2, 3, 4, Loop completed normally


# =============================================================================
# 11. LOOPING THROUGH DICTIONARIES
# =============================================================================

student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# --- Loop through keys (default) ---
for key in student:
    print(key)
# Output: name, age, courses

# --- Loop through keys explicitly ---
for key in student.keys():
    print(key)

# --- Loop through values ---
for value in student.values():
    print(value)
# Output: John, 25, ['Math', 'CompSci']

# --- Loop through key-value pairs ---
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 25
# courses: ['Math', 'CompSci']


# =============================================================================
# 12. USEFUL ITERATION PATTERNS
# =============================================================================

# --- Sum of numbers ---
nums = [1, 2, 3, 4, 5]
total = 0
for num in nums:
    total += num
print(f"Sum: {total}")
# Output: Sum: 15

# --- Find maximum ---
nums = [3, 1, 4, 1, 5, 9, 2, 6]
max_val = nums[0]
for num in nums:
    if num > max_val:
        max_val = num
print(f"Max: {max_val}")
# Output: Max: 9

# --- Filter items ---
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
print(f"Evens: {evens}")
# Output: Evens: [2, 4, 6, 8, 10]

# --- Transform items ---
nums = [1, 2, 3, 4, 5]
squares = []
for num in nums:
    squares.append(num ** 2)
print(f"Squares: {squares}")
# Output: Squares: [1, 4, 9, 16, 25]

# --- Count occurrences ---
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. For Loops
   - Iterate over sequences (lists, strings, tuples, dicts)
   - Syntax: for item in sequence:
   - Use when you know what to iterate over

2. While Loops
   - Run while condition is True
   - Syntax: while condition:
   - Use when you don't know iterations in advance
   - Be careful of infinite loops!

3. Loop Control
   - break: Exit loop immediately
   - continue: Skip to next iteration
   - pass: Do nothing (placeholder)

4. Useful Functions
   - range(start, stop, step): Generate number sequence
   - enumerate(iterable, start): Get index and value
   - zip(iter1, iter2, ...): Combine iterables

5. Loop Else Clause
   - Runs if loop completes without break
   - Useful for search patterns

6. Dictionary Iteration
   - dict.keys(): Iterate keys
   - dict.values(): Iterate values
   - dict.items(): Iterate key-value pairs

7. Best Practices
   - Prefer for loops over while when possible
   - Use enumerate() instead of range(len())
   - Use zip() to iterate multiple lists together
   - Keep loops simple and readable
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Sum of Evens [EASY]
# Calculate the sum of all even numbers from 1 to 100
# TODO: Write your code here

# Solution:
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(f"Sum of evens: {total}")  # Output: 2550


# Exercise 2: FizzBuzz [EASY]
# Print numbers 1-20, but:
# - Print "Fizz" for multiples of 3
# - Print "Buzz" for multiples of 5
# - Print "FizzBuzz" for multiples of both
# TODO: Write your code here

# Solution:
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# Exercise 3: Find First Vowel [MEDIUM]
# Find the index of the first vowel in a word
word = "python"
vowels = "aeiou"
# TODO: Write your code here

# Solution:
# for index, char in enumerate(word):
#     if char.lower() in vowels:
#         print(f"First vowel '{char}' at index {index}")
#         break
# else:
#     print("No vowel found")


# Exercise 4: Multiplication Table [MEDIUM]
# Print multiplication table for numbers 1-5
# Format: "2 x 3 = 6"
# TODO: Write your code here

# Solution:
# for i in range(1, 6):
#     print(f"\n--- Table of {i} ---")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")


# Exercise 5: Password Retry [MEDIUM]
# Allow user 3 attempts to enter correct password "secret"
# Print "Access granted" or "Account locked"
correct_password = "secret"
max_attempts = 3
# TODO: Write your code here (comment out input for testing)

# Solution:
# attempts = 0
# while attempts < max_attempts:
#     password = input("Enter password: ")
#     attempts += 1
#     if password == correct_password:
#         print("Access granted!")
#         break
#     print(f"Wrong password. {max_attempts - attempts} attempts remaining.")
# else:
#     print("Account locked!")


# Exercise 6: Prime Numbers [MEDIUM]
# Print all prime numbers between 1 and 50
# TODO: Write your code here

# Solution:
# for num in range(2, 51):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')


# Exercise 7: Pattern Printing [CHALLENGE]
# Print this pattern:
# *
# **
# ***
# ****
# *****
rows = 5
# TODO: Write your code here

# Solution:
# for i in range(1, rows + 1):
#     print('*' * i)


# Exercise 8: Flatten Nested List [CHALLENGE]
# Convert [[1, 2], [3, 4], [5, 6]] to [1, 2, 3, 4, 5, 6]
nested = [[1, 2], [3, 4], [5, 6]]
# TODO: Write your code here

# Solution:
# flat = []
# for sublist in nested:
#     for item in sublist:
#         flat.append(item)
# print(flat)


# Exercise 9: Common Elements [CHALLENGE]
# Find common elements in two lists using loops (not sets)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
# TODO: Write your code here

# Solution:
# common = []
# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)
# print(f"Common elements: {common}")


# Exercise 10: Number Guessing Game [CHALLENGE]
# Computer picks random number 1-100
# User guesses, getting "Too high" or "Too low" hints
# Count number of attempts
import random
secret_number = random.randint(1, 100)
# TODO: Write your code here (comment out for testing)

# Solution:
# attempts = 0
# while True:
#     guess = int(input("Guess the number (1-100): "))
#     attempts += 1
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print(f"Correct! You got it in {attempts} attempts!")
#         break


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Infinite while loops
   ❌ while True:
          print("Forever!")  # No break condition!
   ✅ while True:
          if condition:
              break
          # or
   ✅ while x < 10:
          x += 1

2. Modifying list while iterating
   ❌ for item in my_list:
          if condition:
              my_list.remove(item)  # Skips items!
   ✅ for item in my_list.copy():
          if condition:
              my_list.remove(item)
   ✅ my_list = [item for item in my_list if not condition]

3. Using range(len()) instead of enumerate
   ❌ for i in range(len(items)):
          print(i, items[i])
   ✅ for i, item in enumerate(items):
          print(i, item)

4. Forgetting to increment in while loop
   ❌ x = 0
      while x < 5:
          print(x)  # x never changes - infinite loop!
   ✅ x = 0
      while x < 5:
          print(x)
          x += 1

5. Off-by-one errors with range
   range(5) gives 0,1,2,3,4 (not 1,2,3,4,5)
   range(1, 5) gives 1,2,3,4 (not 1,2,3,4,5)
   range(1, 6) gives 1,2,3,4,5 ✅

6. Confusing break and continue
   break: EXIT the loop completely
   continue: SKIP to next iteration

7. Not using else with for loops
   for item in items:
       if found:
           break
   else:
       print("Not found")  # Only runs if no break
"""