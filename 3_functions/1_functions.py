"""
================================================================================
PYTHON FUNDAMENTALS: FUNCTIONS
================================================================================
Day: 4

Description:
    Comprehensive guide to Python functions including definition, parameters,
    return values, *args, **kwargs, scope, lambda functions, and best practices.

Learning Objectives:
    - Define and call functions
    - Work with parameters and arguments
    - Understand default parameters and keyword arguments
    - Use *args and **kwargs for flexible functions
    - Understand variable scope (local, global)
    - Write lambda (anonymous) functions
    - Apply best practices for clean, reusable code

Prerequisites:
    - Basic Python syntax
    - Data types and control flow
================================================================================
"""

# =============================================================================
# 1. BASIC FUNCTION DEFINITION
# =============================================================================

# Functions are defined with 'def' keyword
# They allow code reuse and better organization

# --- Simple function (no parameters, no return) ---
def hello_func():
    print("Hello Function!")

hello_func()
# Output: Hello Function!

# Calling multiple times
hello_func()
hello_func()
# Functions can be called as many times as needed


# =============================================================================
# 2. RETURN VALUES
# =============================================================================

# Functions can return values using 'return' keyword

# --- Function with return ---
def get_greeting():
    return "Hello!"

message = get_greeting()
print(message)
# Output: Hello!

# --- Return vs Print ---
def print_greeting():
    print("Hello!")  # Prints but returns None

def return_greeting():
    return "Hello!"  # Returns value, doesn't print

result1 = print_greeting()  # Prints "Hello!", result1 is None
result2 = return_greeting()  # Nothing printed, result2 is "Hello!"

print(result1)  # Output: None
print(result2)  # Output: Hello!

# --- Multiple return values (as tuple) ---
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")
# Output: Min: 1, Max: 9

# --- Early return ---
def check_positive(num):
    if num <= 0:
        return "Not positive"
    return "Positive"

print(check_positive(-5))  # Output: Not positive
print(check_positive(10))  # Output: Positive


# =============================================================================
# 3. PARAMETERS AND ARGUMENTS
# =============================================================================

# Parameters: Variables in function definition
# Arguments: Actual values passed when calling

# --- Required parameters ---
def greet(name):
    return f"Hello, {name}!"

print(greet("Om"))
# Output: Hello, Om!

# print(greet())  # TypeError: missing required argument

# --- Multiple parameters ---
def add(a, b):
    return a + b

print(add(3, 5))
# Output: 8


# =============================================================================
# 4. DEFAULT PARAMETERS
# =============================================================================

# Default values are used when argument is not provided

def hello_func(greeting, name="You"):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi'))
# Output: Hi, You

print(hello_func('Hello', 'Om'))
# Output: Hello, Om

# --- Multiple default parameters ---
def create_user(name, age=18, country="India"):
    return f"{name}, {age} years old, from {country}"

print(create_user("Om"))
# Output: Om, 18 years old, from India

print(create_user("John", 25))
# Output: John, 25 years old, from India

print(create_user("Jane", 30, "USA"))
# Output: Jane, 30 years old, from USA

# IMPORTANT: Default parameters must come AFTER non-default parameters
# def wrong(name="default", age):  # SyntaxError!


# =============================================================================
# 5. KEYWORD ARGUMENTS
# =============================================================================

# Arguments can be passed by name (order doesn't matter)

def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

# Positional arguments (order matters)
print(describe_person("Om", 25, "Mumbai"))

# Keyword arguments (order doesn't matter)
print(describe_person(city="Delhi", name="John", age=30))
# Output: John is 30 years old and lives in Delhi

# Mix of positional and keyword (positional must come first)
print(describe_person("Jane", city="NYC", age=28))
# Output: Jane is 28 years old and lives in NYC


# =============================================================================
# 6. *ARGS (Arbitrary Positional Arguments)
# =============================================================================

# *args collects extra positional arguments into a tuple

def add_all(*args):
    print(f"args = {args}")
    print(f"type = {type(args)}")
    return sum(args)

print(add_all(1, 2, 3))
# Output:
# args = (1, 2, 3)
# type = <class 'tuple'>
# 6

print(add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# Output: 55

# --- Combining regular parameters with *args ---
def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Hello", "Om", "John", "Jane")
# Output:
# Hello, Om!
# Hello, John!
# Hello, Jane!


# =============================================================================
# 7. **KWARGS (Arbitrary Keyword Arguments)
# =============================================================================

# **kwargs collects extra keyword arguments into a dictionary

def print_info(**kwargs):
    print(f"kwargs = {kwargs}")
    print(f"type = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Om", age=25, city="Mumbai")
# Output:
# kwargs = {'name': 'Om', 'age': 25, 'city': 'Mumbai'}
# type = <class 'dict'>
# name: Om
# age: 25
# city: Mumbai

# --- Practical use: Flexible function ---
def create_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

user = create_profile(name="Om", email="om@email.com", role="Developer")
print(user)
# Output: {'name': 'Om', 'email': 'om@email.com', 'role': 'Developer'}


# =============================================================================
# 8. COMBINING *ARGS AND **KWARGS
# =============================================================================

# Order must be: regular params, *args, default params, **kwargs

def student_info(*args, **kwargs):
    print(f"Courses (args): {args}")
    print(f"Info (kwargs): {kwargs}")

student_info('Math', 'Art', 'Science', name='John', age=22)
# Output:
# Courses (args): ('Math', 'Art', 'Science')
# Info (kwargs): {'name': 'John', 'age': 22}

# --- Complete parameter order ---
def complete_function(required, *args, default="value", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"default: {default}")
    print(f"kwargs: {kwargs}")

complete_function("must have", 1, 2, 3, default="custom", extra="data")
# Output:
# required: must have
# args: (1, 2, 3)
# default: custom
# kwargs: {'extra': 'data'}


# =============================================================================
# 9. UNPACKING ARGUMENTS
# =============================================================================

# Use * to unpack list/tuple into positional arguments
# Use ** to unpack dict into keyword arguments

def add_three(a, b, c):
    return a + b + c

# --- Unpacking a list ---
numbers = [1, 2, 3]
print(add_three(*numbers))
# Output: 6
# Same as: add_three(1, 2, 3)

# --- Unpacking a tuple ---
coords = (10, 20, 30)
print(add_three(*coords))
# Output: 60

# --- Unpacking a dictionary ---
def introduce(name, age, city):
    return f"{name}, {age}, from {city}"

person = {'name': 'Om', 'age': 25, 'city': 'Mumbai'}
print(introduce(**person))
# Output: Om, 25, from Mumbai
# Same as: introduce(name='Om', age=25, city='Mumbai')

# --- Combining both ---
def display(a, b, c, x, y):
    print(a, b, c, x, y)

args = [1, 2, 3]
kwargs = {'x': 4, 'y': 5}
display(*args, **kwargs)
# Output: 1 2 3 4 5


# =============================================================================
# 10. VARIABLE SCOPE
# =============================================================================

# Scope determines where variables are accessible

# --- Global scope ---
global_var = "I'm global"

def show_global():
    print(global_var)  # Can read global variable

show_global()
# Output: I'm global

# --- Local scope ---
def show_local():
    local_var = "I'm local"
    print(local_var)

show_local()
# print(local_var)  # NameError: local_var not defined outside function

# --- Local shadows global ---
x = "global x"

def shadow_example():
    x = "local x"  # Creates new local variable
    print(x)

shadow_example()  # Output: local x
print(x)          # Output: global x (unchanged)

# --- Modifying global variable (use 'global' keyword) ---
counter = 0

def increment():
    global counter  # Declare we want to modify global
    counter += 1

increment()
increment()
print(counter)
# Output: 2

# --- Nested scope (enclosing) ---
def outer():
    outer_var = "outer"
    
    def inner():
        print(outer_var)  # Can access enclosing scope
    
    inner()

outer()
# Output: outer

# --- nonlocal keyword ---
def outer_func():
    count = 0
    
    def inner_func():
        nonlocal count  # Modify enclosing variable
        count += 1
        return count
    
    return inner_func

counter_func = outer_func()
print(counter_func())  # Output: 1
print(counter_func())  # Output: 2
print(counter_func())  # Output: 3


# =============================================================================
# 11. LAMBDA FUNCTIONS (Anonymous Functions)
# =============================================================================

# Lambda: Small, one-line anonymous functions
# Syntax: lambda arguments: expression

# --- Basic lambda ---
square = lambda x: x ** 2
print(square(5))
# Output: 25

# --- Multiple arguments ---
add = lambda a, b: a + b
print(add(3, 5))
# Output: 8

# --- Equivalent regular function ---
def square_func(x):
    return x ** 2

# Lambda is just a shorter way to write simple functions

# --- Lambda with conditionals ---
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd


# =============================================================================
# 12. LAMBDA WITH BUILT-IN FUNCTIONS
# =============================================================================

# Lambdas are commonly used with map(), filter(), sorted()

# --- sorted() with key ---
students = [
    {'name': 'John', 'grade': 85},
    {'name': 'Jane', 'grade': 92},
    {'name': 'Bob', 'grade': 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda x: x['grade'])
print([s['name'] for s in sorted_students])
# Output: ['Bob', 'John', 'Jane']

# Sort by grade descending
sorted_desc = sorted(students, key=lambda x: x['grade'], reverse=True)
print([s['name'] for s in sorted_desc])
# Output: ['Jane', 'John', 'Bob']

# --- map() - Apply function to all items ---
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
# Output: [1, 4, 9, 16, 25]

# --- filter() - Keep items that match condition ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
# Output: [2, 4, 6, 8, 10]

# --- Combining map and filter ---
# Square only even numbers
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)
# Output: [4, 16, 36, 64, 100]


# =============================================================================
# 13. DOCSTRINGS
# =============================================================================

# Document your functions with docstrings

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    -----------
    length : float
        The length of the rectangle
    width : float
        The width of the rectangle
    
    Returns:
    --------
    float
        The area of the rectangle
    
    Examples:
    ---------
    >>> calculate_area(5, 3)
    15
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)

# Using help()
help(calculate_area)


# =============================================================================
# 14. FUNCTIONS AS FIRST-CLASS OBJECTS
# =============================================================================

# Functions can be passed as arguments and returned from other functions

# --- Function as argument ---
def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x ** 2

print(apply_operation(double, 5))  # Output: 10
print(apply_operation(square, 5))  # Output: 25

# --- Function returning function ---
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

# --- Storing functions in data structures ---
operations = {
    'add': lambda a, b: a + b,
    'subtract': lambda a, b: a - b,
    'multiply': lambda a, b: a * b,
    'divide': lambda a, b: a / b if b != 0 else "Cannot divide by zero"
}

print(operations['add'](10, 5))       # Output: 15
print(operations['multiply'](10, 5))  # Output: 50


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Function Basics
   - Define with 'def', call with ()
   - Use 'return' to send values back
   - Without return, function returns None

2. Parameters
   - Required: Must be provided
   - Default: Have fallback values (come after required)
   - Keyword: Passed by name (order doesn't matter)

3. *args and **kwargs
   - *args: Collects extra positional args as tuple
   - **kwargs: Collects extra keyword args as dict
   - Order: regular, *args, default, **kwargs

4. Unpacking
   - *list unpacks into positional arguments
   - **dict unpacks into keyword arguments

5. Scope (LEGB Rule)
   - Local: Inside current function
   - Enclosing: Inside enclosing function
   - Global: Module level
   - Built-in: Python built-ins

6. Lambda Functions
   - Syntax: lambda args: expression
   - Use with map(), filter(), sorted()
   - Keep them simple and readable

7. Best Practices
   - Use descriptive function names
   - Add docstrings for documentation
   - Keep functions small and focused
   - Avoid modifying global variables
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Basic Function [EASY]
# Write a function that takes a name and returns "Hello, {name}!"
# If no name provided, default to "World"
# TODO: Write your code here

# Solution:
# def greet(name="World"):
#     return f"Hello, {name}!"
# print(greet())
# print(greet("Om"))


# Exercise 2: Calculator Function [EASY]
# Write a function that takes two numbers and an operation (+, -, *, /)
# Returns the result of the operation
# TODO: Write your code here

# Solution:
# def calculate(a, b, operation='+'):
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         return a / b if b != 0 else "Cannot divide by zero"
#     else:
#         return "Invalid operation"
# print(calculate(10, 5, '*'))


# Exercise 3: Sum All Numbers [MEDIUM]
# Write a function that accepts any number of arguments
# and returns their sum
# TODO: Write your code here

# Solution:
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1, 2, 3, 4, 5))


# Exercise 4: Build Profile [MEDIUM]
# Write a function that accepts a name (required)
# and any number of keyword arguments
# Returns a dictionary with all the information
# TODO: Write your code here

# Solution:
# def build_profile(name, **kwargs):
#     profile = {'name': name}
#     profile.update(kwargs)
#     return profile
# print(build_profile("Om", age=25, city="Mumbai", skill="Python"))


# Exercise 5: Apply Function to List [MEDIUM]
# Write a function that takes a list and a function
# Applies the function to each element and returns new list
# TODO: Write your code here

# Solution:
# def apply_to_list(items, func):
#     return [func(item) for item in items]
# numbers = [1, 2, 3, 4, 5]
# print(apply_to_list(numbers, lambda x: x ** 2))


# Exercise 6: Counter Factory [CHALLENGE]
# Write a function that returns a counter function
# Each call to counter should return incrementing numbers
# TODO: Write your code here

# Solution:
# def create_counter(start=0):
#     count = start
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# counter = create_counter()
# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3


# Exercise 7: Decorator Preview [CHALLENGE]
# Write a function 'log_call' that takes a function as argument
# Returns a new function that prints "Calling {func_name}" before calling
# TODO: Write your code here

# Solution:
# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# def say_hello(name):
#     return f"Hello, {name}!"
#
# logged_hello = log_call(say_hello)
# print(logged_hello("Om"))


# Exercise 8: Sort by Multiple Keys [CHALLENGE]
# Sort a list of dictionaries by multiple keys
# Primary: by grade (descending), Secondary: by name (ascending)
students = [
    {'name': 'John', 'grade': 85},
    {'name': 'Jane', 'grade': 92},
    {'name': 'Bob', 'grade': 85},
    {'name': 'Alice', 'grade': 92}
]
# TODO: Write your code here

# Solution:
# sorted_students = sorted(students, key=lambda x: (-x['grade'], x['name']))
# for s in sorted_students:
#     print(f"{s['name']}: {s['grade']}")
# Output: Alice: 92, Jane: 92, Bob: 85, John: 85


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Mutable default arguments
   ❌ def append_to(item, lst=[]):
          lst.append(item)
          return lst
      # The same list is reused across calls!
   
   ✅ def append_to(item, lst=None):
          if lst is None:
              lst = []
          lst.append(item)
          return lst

2. Forgetting return statement
   ❌ def add(a, b):
          result = a + b  # Returns None!
   ✅ def add(a, b):
          return a + b

3. Modifying global variables without 'global'
   ❌ count = 0
      def increment():
          count += 1  # UnboundLocalError
   ✅ def increment():
          global count
          count += 1

4. Wrong parameter order
   ❌ def func(*args, required):  # SyntaxError
   ✅ def func(required, *args):

5. Confusing positional and keyword arguments
   ❌ func(name="Om", 25)  # Positional after keyword
   ✅ func(25, name="Om")  # Positional before keyword

6. Overcomplicating with lambda
   ❌ lambda x: (lambda y: y * 2)(x) + 1  # Hard to read
   ✅ def transform(x):
          return x * 2 + 1

7. Not using docstrings
   Always document what your function does, its parameters,
   and what it returns!
"""