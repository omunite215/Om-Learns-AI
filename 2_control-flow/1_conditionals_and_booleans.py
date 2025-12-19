"""
================================================================================
PYTHON FUNDAMENTALS: CONDITIONALS AND BOOLEANS
================================================================================
Day: 3

Description:
    Comprehensive guide to Python conditional statements and boolean logic.
    Covers if/elif/else, comparison operators, logical operators, truthy/falsy
    values, and identity vs equality.

Learning Objectives:
    - Write conditional statements (if, elif, else)
    - Use comparison operators effectively
    - Combine conditions with logical operators (and, or, not)
    - Understand truthy and falsy values
    - Differentiate between == (equality) and is (identity)
    - Write clean, readable conditional code

Prerequisites:
    - Basic Python syntax
    - Data types (strings, numbers, lists, dicts)
================================================================================
"""

# =============================================================================
# 1. BOOLEAN VALUES
# =============================================================================

# Booleans represent True or False
is_active = True
is_deleted = False

print(type(is_active))
# Output: <class 'bool'>

# Booleans from comparisons
print(5 > 3)   # Output: True
print(5 < 3)   # Output: False
print(5 == 5)  # Output: True


# =============================================================================
# 2. COMPARISON OPERATORS
# =============================================================================

x = 10
y = 5

# --- Equal to ---
print(x == y)
# Output: False

# --- Not equal to ---
print(x != y)
# Output: True

# --- Greater than ---
print(x > y)
# Output: True

# --- Less than ---
print(x < y)
# Output: False

# --- Greater than or equal to ---
print(x >= y)
# Output: True

# --- Less than or equal to ---
print(x <= y)
# Output: False

# Chained comparisons (Pythonic!)
age = 25
print(18 <= age <= 65)
# Output: True
# Same as: age >= 18 and age <= 65


# =============================================================================
# 3. BASIC IF STATEMENTS
# =============================================================================

language = "Java"

if language == 'Python':
    print("Language is Python.")
elif language == "Java":
    print("Language is Java.")
else:
    print("No match!!")
# Output: Language is Java.

# --- Simple if ---
age = 20
if age >= 18:
    print("You are an adult")
# Output: You are an adult

# --- if-else ---
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
# Output: You are a minor

# --- if-elif-else (multiple conditions) ---
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")
# Output: Your grade is: B


# =============================================================================
# 4. LOGICAL OPERATORS (and, or, not)
# =============================================================================

# --- and - Both conditions must be True ---
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
# Output: Admin Page

# --- or - At least one condition must be True ---
day = 'Saturday'

if day == 'Saturday' or day == 'Sunday':
    print("It's the weekend!")
else:
    print("It's a weekday.")
# Output: It's the weekend!

# --- not - Reverses the boolean value ---
is_logged_in = False

if not is_logged_in:
    print("Please log in")
else:
    print("Welcome back!")
# Output: Please log in

# --- Combining multiple operators ---
age = 25
has_license = True
is_insured = True

if age >= 18 and has_license and is_insured:
    print("You can rent a car")
else:
    print("Sorry, you cannot rent a car")
# Output: You can rent a car

# --- Complex conditions with parentheses ---
is_weekend = True
is_holiday = False
has_work = False

if (is_weekend or is_holiday) and not has_work:
    print("You can relax!")
else:
    print("Time to work!")
# Output: You can relax!


# =============================================================================
# 5. TRUTHY AND FALSY VALUES
# =============================================================================

"""
FALSY VALUES (evaluate to False):
- False
- None
- 0 (zero of any numeric type: 0, 0.0, 0j)
- Empty sequences: '', [], (), {}
- Empty set: set()

TRUTHY VALUES (evaluate to True):
- Everything else!
- Non-zero numbers
- Non-empty sequences
- True
"""

# --- Falsy examples ---
falsy_values = [False, None, 0, 0.0, '', [], (), {}, set()]

for value in falsy_values:
    if value:
        print(f"{repr(value)} is Truthy")
    else:
        print(f"{repr(value)} is Falsy")
# All will print as Falsy

# --- Truthy examples ---
truthy_values = [True, 1, -1, 3.14, 'hello', [1, 2], {'a': 1}, {1, 2}]

for value in truthy_values:
    if value:
        print(f"{repr(value)} is Truthy")
    else:
        print(f"{repr(value)} is Falsy")
# All will print as Truthy

# --- Practical use: Check if list is empty ---
my_list = []

if my_list:
    print("List has items")
else:
    print("List is empty")
# Output: List is empty

# --- Practical use: Check if string is empty ---
name = ""

if name:
    print(f"Hello, {name}")
else:
    print("Name is required")
# Output: Name is required

# --- Practical use: Check if dict is empty ---
condition = {}

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")
# Output: Evaluated to False


# =============================================================================
# 6. IDENTITY VS EQUALITY (is vs ==)
# =============================================================================

"""
== (Equality): Checks if VALUES are equal
is (Identity): Checks if they are the SAME OBJECT in memory
"""

# --- Equality (==) ---
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# Output: True (same values)

# --- Identity (is) ---
print(a is b)
# Output: False (different objects in memory)

# Check memory addresses
print(id(a))  # e.g., 140234567890
print(id(b))  # e.g., 140234567891 (different!)

# --- Same object reference ---
c = a  # c points to same object as a

print(a is c)
# Output: True (same object)

print(id(a) == id(c))
# Output: True

# --- Common use: Check for None ---
value = None

# Correct way
if value is None:
    print("Value is None")

# Also correct, but 'is' is preferred for None
if value == None:
    print("Value is None")

# --- Integer caching (Python optimization) ---
# Small integers (-5 to 256) are cached
x = 256
y = 256
print(x is y)  # Output: True (same cached object)

x = 257
y = 257
print(x is y)  # Output: False (different objects)

# Note: Don't rely on this! Use == for value comparison


# =============================================================================
# 7. NESTED CONDITIONALS
# =============================================================================

age = 25
has_id = True
is_vip = False

if age >= 21:
    if has_id:
        if is_vip:
            print("VIP access granted")
        else:
            print("Regular access granted")
    else:
        print("ID required")
else:
    print("Must be 21 or older")
# Output: Regular access granted

# Better: Flatten with 'and' when possible
if age >= 21 and has_id and is_vip:
    print("VIP access granted")
elif age >= 21 and has_id:
    print("Regular access granted")
elif age >= 21:
    print("ID required")
else:
    print("Must be 21 or older")


# =============================================================================
# 8. TERNARY OPERATOR (One-line if/else)
# =============================================================================

# Syntax: value_if_true if condition else value_if_false

age = 20

# Traditional way
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary way (same result)
status = "adult" if age >= 18 else "minor"
print(status)
# Output: adult

# Practical examples
score = 75
result = "Pass" if score >= 60 else "Fail"
print(result)  # Output: Pass

# With function calls
numbers = [1, 2, 3]
message = "Has items" if len(numbers) > 0 else "Empty"
print(message)  # Output: Has items

# Nested ternary (use sparingly - can be hard to read!)
score = 85
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'
print(grade)  # Output: B


# =============================================================================
# 9. MEMBERSHIP OPERATORS (in, not in)
# =============================================================================

fruits = ['apple', 'banana', 'orange']

# --- in operator ---
if 'apple' in fruits:
    print("Apple is in the list")
# Output: Apple is in the list

# --- not in operator ---
if 'grape' not in fruits:
    print("Grape is not in the list")
# Output: Grape is not in the list

# Works with strings
message = "Hello, World!"
if 'World' in message:
    print("Found 'World' in message")
# Output: Found 'World' in message

# Works with dictionaries (checks keys)
person = {'name': 'John', 'age': 30}
if 'name' in person:
    print("Name key exists")
# Output: Name key exists


# =============================================================================
# 10. SHORT-CIRCUIT EVALUATION
# =============================================================================

"""
Python stops evaluating as soon as the result is determined:
- 'and': Stops at first False (returns it)
- 'or': Stops at first True (returns it)
"""

# --- 'and' short-circuits on False ---
def check_a():
    print("Checking A")
    return False

def check_b():
    print("Checking B")
    return True

# check_b() is never called because check_a() returns False
result = check_a() and check_b()
# Output: Checking A
# (check_b is not executed)

# --- 'or' short-circuits on True ---
def check_c():
    print("Checking C")
    return True

def check_d():
    print("Checking D")
    return False

# check_d() is never called because check_c() returns True
result = check_c() or check_d()
# Output: Checking C
# (check_d is not executed)

# --- Practical use: Default values ---
name = ""
display_name = name or "Guest"
print(display_name)
# Output: Guest

username = "Om"
display_name = username or "Guest"
print(display_name)
# Output: Om


# =============================================================================
# 11. MATCH STATEMENT (Python 3.10+)
# =============================================================================

# Modern alternative to multiple if/elif for pattern matching
# Requires Python 3.10 or later

def get_day_type(day):
    match day.lower():
        case "saturday" | "sunday":
            return "Weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case _:
            return "Invalid day"

# print(get_day_type("Saturday"))  # Output: Weekend
# print(get_day_type("Monday"))    # Output: Weekday

# Note: Uncomment above if using Python 3.10+


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Comparison Operators
   - ==, !=, >, <, >=, <=
   - Can be chained: 18 <= age <= 65

2. Logical Operators
   - and: Both must be True
   - or: At least one must be True
   - not: Reverses boolean value

3. Truthy and Falsy
   - Falsy: False, None, 0, '', [], {}, set()
   - Everything else is Truthy
   - Use this for cleaner code: if my_list: instead of if len(my_list) > 0:

4. Identity vs Equality
   - == checks VALUES
   - is checks if SAME OBJECT
   - Use 'is' for None: if value is None:

5. Ternary Operator
   - value_if_true if condition else value_if_false
   - Great for simple assignments

6. Short-Circuit Evaluation
   - 'and' stops at first False
   - 'or' stops at first True
   - Useful for default values: name or "Guest"

7. Best Practices
   - Use 'is' for None, True, False
   - Use '==' for value comparisons
   - Leverage truthy/falsy for cleaner code
   - Avoid deeply nested conditionals
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Age Classifier [EASY]
# Write a program that classifies age into categories:
# - 0-12: Child
# - 13-19: Teenager
# - 20-59: Adult
# - 60+: Senior
age = 45
# TODO: Write your code here

# Solution:
# if age <= 12:
#     category = "Child"
# elif age <= 19:
#     category = "Teenager"
# elif age <= 59:
#     category = "Adult"
# else:
#     category = "Senior"
# print(f"Age {age}: {category}")


# Exercise 2: Login Validator [EASY]
# Check if username is "admin" AND password is "secret123"
# Print appropriate message for success or failure
username = "admin"
password = "secret123"
# TODO: Write your code here

# Solution:
# if username == "admin" and password == "secret123":
#     print("Login successful!")
# else:
#     print("Invalid credentials!")


# Exercise 3: Leap Year Checker [MEDIUM]
# A year is a leap year if:
# - Divisible by 4 AND
# - (NOT divisible by 100 OR divisible by 400)
year = 2024
# TODO: Write your code here

# Solution:
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# Exercise 4: Grade Calculator with Ternary [MEDIUM]
# Convert a score to Pass/Fail using ternary operator
# Then convert to letter grade (A/B/C/D/F) using if/elif/else
score = 78
# TODO: Write your code here

# Solution:
# result = "Pass" if score >= 60 else "Fail"
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
# print(f"Score: {score}, Result: {result}, Grade: {grade}")


# Exercise 5: Truthy/Falsy Checker [MEDIUM]
# Write a function that takes any value and returns
# "Truthy" or "Falsy" based on its boolean evaluation
# Test with: 0, 1, "", "hello", [], [1,2], None, True
# TODO: Write your code here

# Solution:
# def check_truthy(value):
#     return "Truthy" if value else "Falsy"
#
# test_values = [0, 1, "", "hello", [], [1,2], None, True]
# for val in test_values:
#     print(f"{repr(val)}: {check_truthy(val)}")


# Exercise 6: Number Classifier [MEDIUM]
# Check if a number is:
# - Positive, Negative, or Zero
# - Even or Odd (only if not zero)
number = -7
# TODO: Write your code here

# Solution:
# if number > 0:
#     sign = "Positive"
# elif number < 0:
#     sign = "Negative"
# else:
#     sign = "Zero"
#
# if number != 0:
#     parity = "Even" if number % 2 == 0 else "Odd"
#     print(f"{number} is {sign} and {parity}")
# else:
#     print(f"{number} is {sign}")


# Exercise 7: Ticket Price Calculator [CHALLENGE]
# Calculate ticket price based on:
# - Age: Child (0-12): $5, Teen (13-17): $8, Adult (18-64): $12, Senior (65+): $8
# - Day: Weekend adds $2
# - Matinee (before 5pm): $3 discount
age = 25
is_weekend = True
is_matinee = False
# TODO: Write your code here

# Solution:
# if age <= 12:
#     base_price = 5
# elif age <= 17:
#     base_price = 8
# elif age <= 64:
#     base_price = 12
# else:
#     base_price = 8
#
# final_price = base_price
# if is_weekend:
#     final_price += 2
# if is_matinee:
#     final_price -= 3
#
# print(f"Ticket price: ${final_price}")


# Exercise 8: Rock Paper Scissors [CHALLENGE]
# Determine the winner between two players
# player1 and player2 can be: 'rock', 'paper', or 'scissors'
player1 = 'rock'
player2 = 'scissors'
# TODO: Write your code here

# Solution:
# if player1 == player2:
#     result = "It's a tie!"
# elif (player1 == 'rock' and player2 == 'scissors') or \
#      (player1 == 'scissors' and player2 == 'paper') or \
#      (player1 == 'paper' and player2 == 'rock'):
#     result = "Player 1 wins!"
# else:
#     result = "Player 2 wins!"
# print(result)


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Using = instead of == in conditions
   ❌ if x = 5:  # SyntaxError (assignment, not comparison)
   ✅ if x == 5:

2. Using 'is' for value comparison
   ❌ if x is 5:  # Works sometimes due to caching, but unreliable
   ✅ if x == 5:
   
   Use 'is' only for: None, True, False

3. Checking empty collections incorrectly
   ❌ if len(my_list) == 0:  # Works but not Pythonic
   ✅ if not my_list:  # Cleaner, uses falsy value

4. Redundant boolean comparisons
   ❌ if is_active == True:
   ✅ if is_active:
   
   ❌ if is_active == False:
   ✅ if not is_active:

5. Forgetting 'elif' and using multiple 'if'
   ❌ if x > 0:
          print("positive")
      if x < 0:  # This runs even if first is True
          print("negative")
   
   ✅ if x > 0:
          print("positive")
      elif x < 0:  # Only runs if first is False
          print("negative")

6. Not using parentheses for complex conditions
   ❌ if a and b or c:  # Confusing precedence
   ✅ if (a and b) or c:  # Clear intent

7. Deeply nested conditionals
   ❌ if a:
          if b:
              if c:
                  do_something()
   
   ✅ if a and b and c:
          do_something()
"""