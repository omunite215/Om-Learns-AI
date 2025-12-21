"""
================================================================================
PYTHON FUNDAMENTALS: VARIABLE SCOPE - THE LEGB RULE
================================================================================
Day: 6

Description:
    Comprehensive guide to Python variable scope and the LEGB rule. Covers
    local, enclosing, global, and built-in scopes, along with the global
    and nonlocal keywords for modifying variables in different scopes.

Learning Objectives:
    - Understand the LEGB rule (Local, Enclosing, Global, Built-in)
    - Know how Python searches for variable names
    - Use the 'global' keyword to modify global variables
    - Use the 'nonlocal' keyword to modify enclosing variables
    - Avoid common scope-related errors
    - Write cleaner code with proper scope management

Prerequisites:
    - Basic Python syntax
    - Functions (defining and calling)
================================================================================
"""

# =============================================================================
# 1. WHAT IS SCOPE?
# =============================================================================

"""
SCOPE determines where a variable is accessible in your code.

Python uses the LEGB rule to find variables:
    L - Local: Inside the current function
    E - Enclosing: Inside enclosing (outer) functions
    G - Global: At the top level of the module
    B - Built-in: Python's built-in names (print, len, etc.)

Python searches in this order: Local → Enclosing → Global → Built-in
It stops as soon as it finds the variable name.
"""


# =============================================================================
# 2. LOCAL SCOPE
# =============================================================================

# Variables created inside a function are LOCAL to that function

def local_example():
    local_var = "I'm local"  # Local variable
    print(local_var)

local_example()
# Output: I'm local

# print(local_var)  # NameError: 'local_var' is not defined
# Local variables don't exist outside the function!

# --- Each function has its own local scope ---
def func_a():
    x = 10  # Local to func_a
    print(f"func_a: x = {x}")

def func_b():
    x = 20  # Local to func_b (different variable!)
    print(f"func_b: x = {x}")

func_a()  # Output: func_a: x = 10
func_b()  # Output: func_b: x = 20


# =============================================================================
# 3. GLOBAL SCOPE
# =============================================================================

# Variables created outside any function are GLOBAL

x = 'global x'  # Global variable

def read_global():
    print(x)  # Can READ global variable

read_global()
# Output: global x

print(x)
# Output: global x

# --- Local shadows global ---
x = 'global x'

def shadow_example():
    x = 'local x'  # Creates NEW local variable, doesn't modify global
    print(f"Inside function: {x}")

shadow_example()
# Output: Inside function: local x

print(f"Outside function: {x}")
# Output: Outside function: global x (unchanged!)


# =============================================================================
# 4. THE GLOBAL KEYWORD
# =============================================================================

# Use 'global' to MODIFY a global variable inside a function

x = 'global x'

def modify_global():
    global x  # Declare we want to use the global x
    x = 'modified global x'
    print(f"Inside function: {x}")

print(f"Before function: {x}")
# Output: Before function: global x

modify_global()
# Output: Inside function: modified global x

print(f"After function: {x}")
# Output: After function: modified global x (changed!)

# --- Without global keyword ---
counter = 0

def increment_wrong():
    # counter += 1  # UnboundLocalError!
    # Python sees assignment and thinks counter is local
    # But local counter doesn't exist yet
    pass

def increment_correct():
    global counter
    counter += 1

increment_correct()
increment_correct()
increment_correct()
print(f"Counter: {counter}")
# Output: Counter: 3

# --- Creating new global from function (not recommended) ---
def create_global():
    global new_var
    new_var = "I was created inside a function"

create_global()
print(new_var)
# Output: I was created inside a function


# =============================================================================
# 5. ENCLOSING SCOPE (Nested Functions)
# =============================================================================

# Enclosing scope is for nested (inner) functions
# Inner function can access variables from outer (enclosing) function

def outer():
    x = 'outer x'  # Enclosing scope for inner()
    
    def inner():
        print(x)  # Accesses enclosing variable
    
    inner()

outer()
# Output: outer x

# --- Each level has its own scope ---
x = 'global x'

def outer():
    x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(f"inner: {x}")
    
    inner()
    print(f"outer: {x}")

outer()
print(f"global: {x}")
# Output:
# inner: inner x
# outer: outer x
# global: global x

# All three 'x' variables are DIFFERENT!


# =============================================================================
# 6. THE NONLOCAL KEYWORD
# =============================================================================

# Use 'nonlocal' to MODIFY an enclosing variable from inner function

def outer_nonlocal():
    x = 'outer x'
    
    def inner():
        nonlocal x  # Refer to enclosing x, not create new local
        x = 'inner modified x'
        print(f"inner: {x}")
    
    print(f"Before inner: {x}")
    inner()
    print(f"After inner: {x}")

outer_nonlocal()
# Output:
# Before inner: outer x
# inner: inner modified x
# After inner: inner modified x (changed!)

# --- Practical use: Counter with closure ---
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

my_counter = make_counter()
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3

# Each call to make_counter() creates a new independent counter
another_counter = make_counter()
print(another_counter())  # Output: 1 (starts fresh!)


# =============================================================================
# 7. BUILT-IN SCOPE
# =============================================================================

# Built-in scope contains Python's built-in functions and names
# Examples: print, len, min, max, list, dict, etc.

import builtins

# See all built-in names
print("Some built-in names:")
builtin_names = [name for name in dir(builtins) if not name.startswith('_')]
print(builtin_names[:10])  # First 10

# --- Built-ins can be shadowed (BAD PRACTICE!) ---
# DON'T DO THIS:
# def min():
#     pass
# 
# m = min([5, 1, 4, 2, 3])  # TypeError! min is now your function

# --- Safe example ---
print(f"\nBuilt-in min: {min([5, 1, 4, 2, 3])}")
# Output: Built-in min: 1

print(f"Built-in max: {max([5, 1, 4, 2, 3])}")
# Output: Built-in max: 5

# --- Checking if name is built-in ---
print(f"\n'print' is built-in: {hasattr(builtins, 'print')}")
print(f"'my_func' is built-in: {hasattr(builtins, 'my_func')}")


# =============================================================================
# 8. LEGB RULE IN ACTION
# =============================================================================

# Let's trace how Python finds variable 'x' at each level

x = 'global x'  # Global scope

def outer():
    x = 'enclosing x'  # Enclosing scope
    
    def inner():
        x = 'local x'  # Local scope
        print(f"1. Local found: {x}")
    
    def inner_no_local():
        # No local x, searches enclosing
        print(f"2. Enclosing found: {x}")
    
    inner()
    inner_no_local()

outer()
# Output:
# 1. Local found: local x
# 2. Enclosing found: enclosing x

def outer_no_enclosing():
    # No enclosing x, searches global
    print(f"3. Global found: {x}")

outer_no_enclosing()
# Output: 3. Global found: global x

# Built-in example
def show_builtin():
    # No local/enclosing/global 'len', finds built-in
    print(f"4. Built-in found: len = {len}")

show_builtin()
# Output: 4. Built-in found: len = <built-in function len>


# =============================================================================
# 9. LEGB VISUAL DIAGRAM
# =============================================================================

"""
┌─────────────────────────────────────────────────────────────────┐
│                        BUILT-IN SCOPE                           │
│   print, len, min, max, list, dict, True, False, None, etc.    │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                     GLOBAL SCOPE                          │  │
│  │   Variables defined at module level                       │  │
│  │   x = 'global x'                                          │  │
│  │                                                           │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │                ENCLOSING SCOPE                      │  │  │
│  │  │   Variables in outer function                       │  │  │
│  │  │   def outer():                                      │  │  │
│  │  │       x = 'enclosing x'                            │  │  │
│  │  │                                                     │  │  │
│  │  │  ┌───────────────────────────────────────────────┐  │  │  │
│  │  │  │              LOCAL SCOPE                      │  │  │  │
│  │  │  │   Variables in current function               │  │  │  │
│  │  │  │   def inner():                                │  │  │  │
│  │  │  │       x = 'local x'                          │  │  │  │
│  │  │  │       print(x)  ← Python searches from here  │  │  │  │
│  │  │  └───────────────────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘

Search order: Local → Enclosing → Global → Built-in
"""


# =============================================================================
# 10. COMMON SCOPE ERRORS
# =============================================================================

# --- UnboundLocalError ---
x = 10

def unbound_error():
    # print(x)  # Would work if no assignment below
    # x = 20   # This makes Python think x is local
    # print(x)  # UnboundLocalError: x referenced before assignment
    pass

# Fix with global:
def fixed_with_global():
    global x
    print(x)  # Works! x is global
    x = 20    # Modifies global x

# --- Variable not defined in enclosing ---
def outer_error():
    def inner():
        # nonlocal y  # SyntaxError: no binding for nonlocal 'y'
        pass
    inner()

# nonlocal requires variable to exist in enclosing scope!


# =============================================================================
# 11. BEST PRACTICES
# =============================================================================

"""
1. MINIMIZE USE OF GLOBAL VARIABLES
   - Global state makes code hard to debug
   - Pass values as function arguments instead
   - Return values instead of modifying globals

2. AVOID SHADOWING BUILT-INS
   - Don't name variables: list, dict, str, int, len, min, max, etc.
   - Use descriptive names: my_list, user_dict, name_str

3. PREFER RETURNING VALUES OVER MODIFYING STATE
   ❌ Bad:
      total = 0
      def add(x):
          global total
          total += x
   
   ✅ Good:
      def add(total, x):
          return total + x

4. USE CLOSURES FOR ENCAPSULATION
   - Closures can maintain state without globals
   - Great for creating factory functions

5. KEEP FUNCTIONS PURE WHEN POSSIBLE
   - Pure functions don't modify external state
   - Same input always produces same output
   - Easier to test and debug
"""

# --- Good practice: Return instead of modify ---
def bad_append(item):
    global my_list
    my_list.append(item)

def good_append(lst, item):
    return lst + [item]  # Returns new list

my_list = [1, 2, 3]
new_list = good_append(my_list, 4)
print(f"Original: {my_list}")  # [1, 2, 3] (unchanged)
print(f"New: {new_list}")      # [1, 2, 3, 4]


# =============================================================================
# 12. CLOSURES
# =============================================================================

# A closure is a function that remembers variables from its enclosing scope

def make_multiplier(n):
    """Factory function that creates multiplier functions"""
    def multiplier(x):
        return x * n  # 'n' is remembered from enclosing scope
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")  # Output: 10
print(f"triple(5) = {triple(5)}")  # Output: 15

# --- Checking closure variables ---
print(f"double's closure: {double.__closure__}")
print(f"Enclosed value: {double.__closure__[0].cell_contents}")
# Output: Enclosed value: 2

# --- Practical closure: Logger ---
def make_logger(prefix):
    def logger(message):
        print(f"[{prefix}] {message}")
    return logger

info_log = make_logger("INFO")
error_log = make_logger("ERROR")

info_log("Application started")   # Output: [INFO] Application started
error_log("Something went wrong") # Output: [ERROR] Something went wrong


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. LEGB Rule (Search Order)
   - Local: Variables inside current function
   - Enclosing: Variables in outer function (for nested functions)
   - Global: Variables at module level
   - Built-in: Python's built-in names

2. Reading vs Modifying
   - Can READ variables from any outer scope
   - To MODIFY, need 'global' or 'nonlocal' keyword

3. Keywords
   - global: Modify global variable from inside function
   - nonlocal: Modify enclosing variable from inner function

4. Variable Shadowing
   - Inner scope variable hides outer scope variable with same name
   - Each is independent - modifying one doesn't affect others

5. Common Errors
   - UnboundLocalError: Assignment makes Python think variable is local
   - Fix: Use 'global' or 'nonlocal', or restructure code

6. Best Practices
   - Minimize global variables
   - Don't shadow built-ins
   - Return values instead of modifying state
   - Use closures for encapsulation
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Predict the Output [EASY]
# What will this print? (Don't run it first!)
x = 50

def func():
    x = 100
    print(x)

func()
print(x)
# TODO: Predict the output, then run to verify

# Answer: 100, then 50 (local x doesn't affect global)


# Exercise 2: Fix the Error [EASY]
# This code has an error. Fix it.
count = 0

def increment():
    # count += 1  # UnboundLocalError!
    pass

# TODO: Fix the increment function

# Solution:
# def increment():
#     global count
#     count += 1


# Exercise 3: LEGB Tracing [MEDIUM]
# Predict output for each print statement
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"A: {x}")  # What prints?
    
    inner()
    print(f"B: {x}")  # What prints?

outer()
print(f"C: {x}")  # What prints?

# TODO: Predict A, B, C

# Answer: A: local, B: enclosing, C: global


# Exercise 4: Counter with Closure [MEDIUM]
# Create a counter function that:
# - Starts at a given value
# - Can increment by any amount
# - Can decrement by any amount
# - Can reset to initial value
# TODO: Write your code here

# Solution:
# def make_counter(start=0):
#     count = start
#     initial = start
#     
#     def counter(action="get", amount=1):
#         nonlocal count
#         if action == "increment":
#             count += amount
#         elif action == "decrement":
#             count -= amount
#         elif action == "reset":
#             count = initial
#         return count
#     
#     return counter
#
# c = make_counter(10)
# print(c())                    # 10
# print(c("increment"))         # 11
# print(c("increment", 5))      # 16
# print(c("decrement", 3))      # 13
# print(c("reset"))             # 10


# Exercise 5: Bank Account [MEDIUM]
# Create a make_account function that returns functions to:
# - deposit(amount)
# - withdraw(amount)
# - get_balance()
# Use closures to keep balance private
# TODO: Write your code here

# Solution:
# def make_account(initial_balance=0):
#     balance = initial_balance
#     
#     def deposit(amount):
#         nonlocal balance
#         if amount > 0:
#             balance += amount
#         return balance
#     
#     def withdraw(amount):
#         nonlocal balance
#         if amount > 0 and amount <= balance:
#             balance -= amount
#         return balance
#     
#     def get_balance():
#         return balance
#     
#     return deposit, withdraw, get_balance
#
# deposit, withdraw, balance = make_account(100)
# print(balance())      # 100
# print(deposit(50))    # 150
# print(withdraw(30))   # 120


# Exercise 6: Fix Shadowing [CHALLENGE]
# This code accidentally shadows built-ins. Fix it.
# list = [1, 2, 3]
# str = "hello"
# sum = 100
# print = "output"
# 
# result = sum(list)  # Error!
# print(result)       # Error!
# TODO: Write the fixed version

# Solution:
# my_list = [1, 2, 3]
# my_str = "hello"
# total = 100
# output = "output"
# 
# result = sum(my_list)  # Works!
# print(result)          # Works!


# Exercise 7: Scope Detective [CHALLENGE]
# Determine which scope each variable belongs to
import math

global_var = "I'm global"

def outer_func():
    enclosing_var = "I'm enclosing"
    
    def inner_func():
        local_var = "I'm local"
        
        # For each variable below, identify its scope:
        # print(local_var)      # Scope: ?
        # print(enclosing_var)  # Scope: ?
        # print(global_var)     # Scope: ?
        # print(math.pi)        # Scope: ?
        # print(len)            # Scope: ?
        pass
    
    inner_func()

# TODO: Identify the scope of each variable

# Answers:
# local_var: Local
# enclosing_var: Enclosing
# global_var: Global
# math.pi: Global (math is global, pi is attribute)
# len: Built-in


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting that assignment creates local variable
   ❌ x = 10
      def func():
          print(x)  # Works
          x = 20    # Now Python thinks x is local EVERYWHERE in func
                    # Previous print fails: UnboundLocalError
   
   ✅ x = 10
      def func():
          global x
          print(x)
          x = 20

2. Using global when you should restructure
   ❌ result = None
      def calculate():
          global result
          result = 42
      calculate()
      print(result)
   
   ✅ def calculate():
          return 42
      result = calculate()
      print(result)

3. Shadowing built-in names
   ❌ list = [1, 2, 3]  # Shadows built-in list()
   ✅ my_list = [1, 2, 3]

4. Confusing global and nonlocal
   - global: For module-level variables
   - nonlocal: For enclosing function variables
   
   Using wrong one causes SyntaxError or unexpected behavior

5. Modifying mutable global without 'global' keyword
   my_list = []
   def append_item(item):
       my_list.append(item)  # Works! (modifying, not reassigning)
   
   def replace_list():
       my_list = [1, 2, 3]   # Creates LOCAL my_list!
   
   # For reassignment, you NEED 'global'

6. Over-using closures
   - Closures are powerful but can make code hard to follow
   - Use classes for complex state management
"""