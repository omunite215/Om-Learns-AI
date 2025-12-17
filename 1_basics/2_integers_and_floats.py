"""
================================================================================
PYTHON FUNDAMENTALS: INTEGERS AND FLOATS
================================================================================
File: basics/2_integers_and_floats.py
Author: Om
Date: 2024-12-16
Source: Corey Schafer - Python Tutorial for Beginners
Status: ✅ Completed

Description:
    Comprehensive guide to numeric data types in Python including integers
    and floats, arithmetic operators, comparison operators, and built-in
    numeric functions.

Learning Objectives:
    - Understand integers and floating-point numbers
    - Master arithmetic operators
    - Use comparison and assignment operators
    - Work with built-in numeric functions
    - Handle type conversion between int and float

Prerequisites:
    - Basic Python syntax
    - Understanding of variables
================================================================================
"""

# =============================================================================
# 1. BASIC ARITHMETIC OPERATORS
# =============================================================================

# --- Addition ---
print(3 + 2)
# Output: 5

# --- Subtraction ---
print(3 - 2)
# Output: 1

# --- Multiplication ---
print(3 * 2)
# Output: 6

# --- Division (always returns float) ---
print(3 / 2)
# Output: 1.5
# Note: Division ALWAYS returns a float, even if dividing evenly

print(4 / 2)
# Output: 2.0 (still a float, not an integer)

# --- Floor Division (returns integer, rounds down) ---
print(3 // 2)
# Output: 1
# Discards decimal part, rounds toward negative infinity

print(7 // 2)   # Output: 3
print(-7 // 2)  # Output: -4 (rounds down, not toward zero)

# --- Exponentiation (power) ---
print(3 ** 2)
# Output: 9
# 3 raised to the power of 2 (3²)

print(2 ** 3)   # Output: 8 (2³)
print(5 ** 0)   # Output: 1 (anything to power 0 is 1)

# --- Modulus (remainder after division) ---
print(2 % 2)
# Output: 0
# Remainder when 2 is divided by 2

print(3 % 2)
# Output: 1
# Remainder when 3 is divided by 2

print(4 % 2)
# Output: 0

print(5 % 2)
# Output: 1

# Practical use: Check if number is even or odd
print(10 % 2 == 0)  # Output: True (10 is even)
print(11 % 2 == 0)  # Output: False (11 is odd)


# =============================================================================
# 2. ORDER OF OPERATIONS (PEMDAS)
# =============================================================================

# Python follows mathematical order of operations:
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

print(3 * 2 + 1)
# Output: 7
# Multiplication first (3 * 2 = 6), then addition (6 + 1 = 7)

print(3 * (2 + 1))
# Output: 9
# Parentheses first (2 + 1 = 3), then multiplication (3 * 3 = 9)

print(2 + 3 * 4)   # Output: 14 (not 20)
print((2 + 3) * 4) # Output: 20

print(10 / 2 * 3)  # Output: 15.0 (left to right: 10/2=5, 5*3=15)


# =============================================================================
# 3. INTEGERS VS FLOATS
# =============================================================================

# --- Integers (whole numbers) ---
num = 3
print(type(num))
# Output: <class 'int'>

# --- Floats (decimal numbers) ---
num = 3.14
print(type(num))
# Output: <class 'float'>

# Operations mixing int and float return float
print(3 + 2.5)    # Output: 5.5 (float)
print(type(3 + 2.5))  # Output: <class 'float'>

# Division always returns float
print(type(4 / 2))    # Output: <class 'float'>


# =============================================================================
# 4. INCREMENTING AND ASSIGNMENT OPERATORS
# =============================================================================

num = 1

# --- Long form ---
num = num + 1
print(num)
# Output: 2

# --- Shorthand (increment) ---
num += 1
print(num)
# Output: 3

# Other compound assignment operators
num *= 10
print(num)
# Output: 30

num -= 5
print(num)
# Output: 25

num /= 5
print(num)
# Output: 5.0

num **= 2
print(num)
# Output: 25.0

num %= 3
print(num)
# Output: 1.0


# =============================================================================
# 5. BUILT-IN NUMERIC FUNCTIONS
# =============================================================================

# --- abs() - Absolute value ---
print(abs(-3))
# Output: 3
# Returns the absolute (positive) value

print(abs(3))     # Output: 3
print(abs(-5.5))  # Output: 5.5

# --- round() - Round to nearest integer ---
print(round(3.75))
# Output: 4

print(round(3.25))  # Output: 3
print(round(3.5))   # Output: 4

# Specify decimal places
print(round(3.14159, 2))  # Output: 3.14
print(round(3.14159, 3))  # Output: 3.142


# =============================================================================
# 6. COMPARISON OPERATORS
# =============================================================================

num_1 = 3
num_2 = 2

# --- Equal to ---
print(num_1 == num_2)
# Output: False

# --- Not equal to ---
print(num_1 != num_2)
# Output: True

# --- Greater than ---
print(num_1 > num_2)
# Output: True

# --- Less than ---
print(num_1 < num_2)
# Output: False

# --- Greater than or equal to ---
print(num_1 >= num_2)
# Output: True

# --- Less than or equal to ---
print(num_1 <= num_2)
# Output: False


# =============================================================================
# 7. TYPE CONVERSION (CASTING)
# =============================================================================

# --- String to Integer ---
num_str = "100"
print(type(num_str))  # Output: <class 'str'>

num_int = int(num_str)
print(type(num_int))  # Output: <class 'int'>
print(num_int)        # Output: 100

# --- String to Float ---
num_str = "3.14"
num_float = float(num_str)
print(type(num_float))  # Output: <class 'float'>
print(num_float)        # Output: 3.14

# --- Float to Integer (truncates decimal) ---
num_float = 3.9
num_int = int(num_float)
print(num_int)  # Output: 3 (not 4, just removes decimal)

# --- Integer to String ---
num = 100
num_str = str(num)
print(type(num_str))  # Output: <class 'str'>
print(num_str)        # Output: '100'


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Arithmetic Operators
   - Basic: +, -, *, / (division always returns float)
   - Advanced: // (floor division), ** (exponent), % (modulus)
   - Order of operations: PEMDAS (use parentheses for clarity)

2. Integer vs Float
   - int: Whole numbers (1, 42, -7)
   - float: Decimal numbers (3.14, -0.5, 2.0)
   - Mixed operations return float
   - Division (/) ALWAYS returns float

3. Compound Assignment
   - Shorthand: +=, -=, *=, /=, //=, **=, %=
   - num += 1 is same as num = num + 1

4. Built-in Functions
   - abs() - absolute value
   - round() - round to nearest integer or decimal places
   - type() - check data type

5. Comparison Operators
   - Return True or False (boolean values)
   - ==, !=, >, <, >=, <=

6. Type Conversion
   - int() - convert to integer
   - float() - convert to float
   - str() - convert to string
   - Be careful: int(3.9) gives 3, not 4 (truncates, doesn't round)
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Temperature Converter [EASY]
# Convert 75 degrees Fahrenheit to Celsius
# Formula: C = (F - 32) * 5/9
fahrenheit = 75
# TODO: Calculate celsius and print the result

# Solution:
# celsius = (fahrenheit - 32) * 5/9
# print(f"{fahrenheit}°F is {round(celsius, 2)}°C")


# Exercise 2: Even or Odd Checker [EASY]
# Use modulus operator to check if a number is even or odd
number = 17
# TODO: Print whether the number is even or odd

# Solution:
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


# Exercise 3: Circle Calculations [MEDIUM]
# Given radius = 5, calculate:
# a) Area of circle (π * r²)
# b) Circumference (2 * π * r)
# Use 3.14159 for π
radius = 5
pi = 3.14159
# TODO: Calculate area and circumference

# Solution:
# area = pi * radius ** 2
# circumference = 2 * pi * radius
# print(f"Area: {round(area, 2)}")
# print(f"Circumference: {round(circumference, 2)}")


# Exercise 4: Compound Interest Calculator [MEDIUM]
# Calculate final amount with compound interest
# Formula: A = P(1 + r/n)^(nt)
# P = 1000 (principal), r = 0.05 (5% annual rate)
# n = 12 (monthly), t = 10 (years)
principal = 1000
rate = 0.05
compounds_per_year = 12
years = 10
# TODO: Calculate final amount

# Solution:
# amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * years)
# print(f"Final amount: ${round(amount, 2)}")


# Exercise 5: Time Converter [MEDIUM]
# Convert 5000 seconds into hours, minutes, and remaining seconds
total_seconds = 5000
# TODO: Calculate hours, minutes, and seconds

# Solution:
# hours = total_seconds // 3600
# remaining = total_seconds % 3600
# minutes = remaining // 60
# seconds = remaining % 60
# print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")


# Exercise 6: BMI Calculator [CHALLENGE]
# Calculate Body Mass Index (BMI) = weight(kg) / height(m)²
# Then categorize:
# - Below 18.5: Underweight
# - 18.5-24.9: Normal
# - 25-29.9: Overweight
# - 30+: Obese
weight = 70  # kg
height = 1.75  # meters
# TODO: Calculate BMI and print category

# Solution:
# bmi = weight / (height ** 2)
# print(f"BMI: {round(bmi, 2)}")
# if bmi < 18.5:
#     print("Category: Underweight")
# elif bmi < 25:
#     print("Category: Normal")
# elif bmi < 30:
#     print("Category: Overweight")
# else:
#     print("Category: Obese")


# Exercise 7: Tip Calculator [CHALLENGE]
# Calculate tip and total bill
# Bill: $85.50, tip percentage: 18%
# Also split between 4 people
bill = 85.50
tip_percentage = 18
people = 4
# TODO: Calculate tip, total, and amount per person

# Solution:
# tip = bill * (tip_percentage / 100)
# total = bill + tip
# per_person = total / people
# print(f"Tip: ${round(tip, 2)}")
# print(f"Total: ${round(total, 2)}")
# print(f"Per person: ${round(per_person, 2)}")


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Integer division when you need float result
   ❌ result = 5 // 2  # Gives 2 (floor division)
   ✅ result = 5 / 2   # Gives 2.5 (regular division)

2. Forgetting operator precedence
   ❌ result = 2 + 3 * 4  # Equals 14, not 20
   ✅ result = (2 + 3) * 4  # Use parentheses for clarity

3. Confusing = (assignment) with == (comparison)
   ❌ if num = 5:  # SyntaxError
   ✅ if num == 5:  # Correct comparison

4. Type conversion errors
   ❌ int("3.14")  # ValueError (can't convert float string directly)
   ✅ int(float("3.14"))  # First to float, then to int

5. Rounding vs truncating
   int(3.9) gives 3 (truncates)
   round(3.9) gives 4 (rounds)
   
6. Modulus with negative numbers
   -7 % 3 gives 2 (not -1)
   Python's modulus always returns positive with positive divisor

7. Float precision issues
   0.1 + 0.2 gives 0.30000000000000004 (not exactly 0.3)
   Use round() when displaying or comparing floats
"""