"""
================================================================================
PYTHON FUNDAMENTALS: STRING FORMATTING - ADVANCED OPERATIONS
================================================================================
Day: 10

Description:
    Comprehensive guide to Python string formatting techniques including
    old-style % formatting, .format() method, and modern f-strings. Covers
    formatting numbers, dates, alignment, and working with dictionaries,
    lists, and objects.

Learning Objectives:
    - Understand different string formatting methods
    - Use .format() with positional and keyword arguments
    - Format numbers (decimals, padding, separators)
    - Format dates and times
    - Align and pad strings
    - Access object attributes and dictionary values in formatting
    - Choose the right formatting method for each situation

Prerequisites:
    - Basic string operations
    - Dictionaries and objects
================================================================================
"""

# =============================================================================
# 1. STRING CONCATENATION (Old Way - Avoid!)
# =============================================================================

person = {'name': 'Jenn', 'age': 23}

# --- String concatenation (not recommended) ---
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)
# Output: My name is Jenn and I am 23 years old.

# Problems with concatenation:
# - Need to convert non-strings with str()
# - Hard to read with many variables
# - Easy to make mistakes with spaces


# =============================================================================
# 2. OLD STYLE % FORMATTING (Legacy)
# =============================================================================

# Still seen in older code, but not recommended for new code

name = 'Jenn'
age = 23

# --- Basic % formatting ---
sentence = 'My name is %s and I am %d years old.' % (name, age)
print(sentence)
# Output: My name is Jenn and I am 23 years old.

# Format specifiers:
# %s - String
# %d - Integer
# %f - Float
# %x - Hexadecimal

# --- Float formatting with % ---
pi = 3.14159265
sentence = 'Pi is approximately %.2f' % pi
print(sentence)
# Output: Pi is approximately 3.14

# --- Multiple values ---
sentence = '%s is %d years old and %.1f feet tall' % ('John', 25, 5.9)
print(sentence)
# Output: John is 25 years old and 5.9 feet tall


# =============================================================================
# 3. .format() METHOD - BASIC USAGE
# =============================================================================

person = {'name': 'Jenn', 'age': 23}

# --- Basic .format() ---
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)
# Output: My name is Jenn and I am 23 years old.

# --- Positional arguments ---
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)
# Output: My name is Jenn and I am 23 years old.

# --- Reusing arguments with index ---
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
# Output: <h1>This is a headline</h1>

# --- Keyword arguments ---
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age=30)
print(sentence)
# Output: My name is Jenn and I am 30 years old.


# =============================================================================
# 4. .format() WITH DICTIONARIES
# =============================================================================

person = {'name': 'Jenn', 'age': 23}

# --- Unpacking dictionary with ** ---
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)
# Output: My name is Jenn and I am 23 years old.

# --- Accessing dict values directly ---
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)
# Output: My name is Jenn and I am 23 years old.

# --- Multiple dictionaries ---
person = {'name': 'Jenn'}
details = {'age': 23, 'city': 'NYC'}
sentence = '{0[name]} is {1[age]} years old from {1[city]}.'.format(person, details)
print(sentence)
# Output: Jenn is 23 years old from NYC.


# =============================================================================
# 5. .format() WITH OBJECTS
# =============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', 33)

# --- Accessing object attributes ---
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)
# Output: My name is Jack and I am 33 years old.

# --- Multiple objects ---
p2 = Person('Jill', 28)
sentence = '{0.name} is {0.age}, {1.name} is {1.age}.'.format(p1, p2)
print(sentence)
# Output: Jack is 33, Jill is 28.


# =============================================================================
# 6. .format() WITH LISTS
# =============================================================================

# --- Accessing list elements ---
data = ['John', 25, 'Developer']
sentence = '{0[0]} is {0[1]} years old and works as a {0[2]}.'.format(data)
print(sentence)
# Output: John is 25 years old and works as a Developer.

# --- Multiple lists ---
names = ['Alice', 'Bob']
ages = [30, 25]
sentence = '{0[0]} is {1[0]}, {0[1]} is {1[1]}.'.format(names, ages)
print(sentence)
# Output: Alice is 30, Bob is 25.


# =============================================================================
# 7. NUMBER FORMATTING
# =============================================================================

# --- Large numbers with comma separator ---
sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)
# Output: 1 MB is equal to 1,000,000 bytes

sentence = 'Population: {:,}'.format(7900000000)
print(sentence)
# Output: Population: 7,900,000,000

# --- Decimal places ---
pi = 3.14159265

sentence = 'Pi is equal to {}'.format(pi)
print(sentence)
# Output: Pi is equal to 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)
# Output: Pi is equal to 3.14

sentence = 'Pi is equal to {:.4f}'.format(pi)
print(sentence)
# Output: Pi is equal to 3.1416

# --- Padding numbers ---
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)
# Output:
# The value is 01
# The value is 02
# ...
# The value is 10

# --- Percentage ---
ratio = 0.85
sentence = 'Completion: {:.1%}'.format(ratio)
print(sentence)
# Output: Completion: 85.0%

# --- Binary, Octal, Hexadecimal ---
num = 255
print('Binary: {:b}'.format(num))      # Output: 11111111
print('Octal: {:o}'.format(num))       # Output: 377
print('Hex: {:x}'.format(num))         # Output: ff
print('Hex (upper): {:X}'.format(num)) # Output: FF


# =============================================================================
# 8. STRING ALIGNMENT AND PADDING
# =============================================================================

# --- Left align (default for strings) ---
sentence = '{:<10}'.format('test')
print(f"'{sentence}'")
# Output: 'test      '

# --- Right align ---
sentence = '{:>10}'.format('test')
print(f"'{sentence}'")
# Output: '      test'

# --- Center align ---
sentence = '{:^10}'.format('test')
print(f"'{sentence}'")
# Output: '   test   '

# --- Custom fill character ---
sentence = '{:*<10}'.format('test')
print(sentence)
# Output: test******

sentence = '{:*>10}'.format('test')
print(sentence)
# Output: ******test

sentence = '{:-^20}'.format('HEADER')
print(sentence)
# Output: -------HEADER-------

# --- Practical example: Table formatting ---
print('{:<15} {:>10} {:>10}'.format('Item', 'Qty', 'Price'))
print('{:<15} {:>10} {:>10.2f}'.format('Apples', 50, 1.99))
print('{:<15} {:>10} {:>10.2f}'.format('Oranges', 30, 2.49))
print('{:<15} {:>10} {:>10.2f}'.format('Bananas', 100, 0.99))
# Output:
# Item                 Qty      Price
# Apples                50       1.99
# Oranges               30       2.49
# Bananas              100       0.99


# =============================================================================
# 9. DATE AND TIME FORMATTING
# =============================================================================

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)
# Output: 2016-09-24 12:30:45

# --- Basic date formatting ---
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)
# Output: September 24, 2016

# --- Full date with day name ---
sentence = '{:%B %d, %Y} fell on a {:%A} and was the {:%j} day of the year.'.format(
    my_date, my_date, my_date
)
print(sentence)
# Output: September 24, 2016 fell on a Saturday and was the 268 day of the year.

# --- Common date format codes ---
"""
%Y - Year (4 digits): 2016
%y - Year (2 digits): 16
%m - Month (01-12): 09
%B - Month name (full): September
%b - Month name (short): Sep
%d - Day (01-31): 24
%A - Weekday (full): Saturday
%a - Weekday (short): Sat
%j - Day of year (001-366): 268
%H - Hour (00-23): 12
%I - Hour (01-12): 12
%M - Minute (00-59): 30
%S - Second (00-59): 45
%p - AM/PM: PM
"""

# --- More date examples ---
now = datetime.datetime.now()
print('Date: {:%Y-%m-%d}'.format(now))         # 2024-12-17
print('Time: {:%H:%M:%S}'.format(now))         # 14:30:45
print('Full: {:%Y-%m-%d %H:%M:%S}'.format(now)) # 2024-12-17 14:30:45
print('US format: {:%m/%d/%Y}'.format(now))    # 12/17/2024
print('EU format: {:%d/%m/%Y}'.format(now))    # 17/12/2024
print('12-hour: {:%I:%M %p}'.format(now))      # 02:30 PM


# =============================================================================
# 10. F-STRINGS (Python 3.6+) - RECOMMENDED!
# =============================================================================

# F-strings are the most readable and preferred method

person = {'name': 'Jenn', 'age': 23}
name = 'Jenn'
age = 23

# --- Basic f-string ---
sentence = f'My name is {name} and I am {age} years old.'
print(sentence)
# Output: My name is Jenn and I am 23 years old.

# --- Expressions in f-strings ---
a = 5
b = 10
print(f'{a} + {b} = {a + b}')
# Output: 5 + 10 = 15

print(f'{name.upper()} is {age * 2} in dog years.')
# Output: JENN is 46 in dog years.

# --- Dictionary access ---
print(f"My name is {person['name']} and I am {person['age']} years old.")
# Output: My name is Jenn and I am 23 years old.

# --- Object attributes ---
p1 = Person('Jack', 33)
print(f'My name is {p1.name} and I am {p1.age} years old.')
# Output: My name is Jack and I am 33 years old.

# --- Number formatting in f-strings ---
pi = 3.14159265
print(f'Pi is approximately {pi:.2f}')
# Output: Pi is approximately 3.14

large_num = 1000000
print(f'One million: {large_num:,}')
# Output: One million: 1,000,000

# --- Alignment in f-strings ---
text = 'test'
print(f'{text:<10}')  # Left
print(f'{text:>10}')  # Right
print(f'{text:^10}')  # Center

# --- Date formatting in f-strings ---
now = datetime.datetime.now()
print(f'Today is {now:%B %d, %Y}')
# Output: Today is December 17, 2024


# =============================================================================
# 11. F-STRING ADVANCED FEATURES (Python 3.8+)
# =============================================================================

# --- Self-documenting expressions (Python 3.8+) ---
x = 10
y = 25
print(f'{x=}, {y=}')
# Output: x=10, y=25

print(f'{x=}, {y=}, {x+y=}')
# Output: x=10, y=25, x+y=35

# --- With formatting ---
pi = 3.14159
print(f'{pi=:.2f}')
# Output: pi=3.14

# --- Multiline f-strings ---
name = 'Jenn'
age = 23
city = 'NYC'

message = f"""
User Profile:
-------------
Name: {name}
Age: {age}
City: {city}
"""
print(message)


# =============================================================================
# 12. COMPARISON OF FORMATTING METHODS
# =============================================================================

name = 'Jenn'
age = 23

# --- All methods produce same output ---
# Method 1: Concatenation (avoid)
s1 = 'My name is ' + name + ' and I am ' + str(age) + ' years old.'

# Method 2: % formatting (legacy)
s2 = 'My name is %s and I am %d years old.' % (name, age)

# Method 3: .format() method
s3 = 'My name is {} and I am {} years old.'.format(name, age)

# Method 4: f-strings (recommended!)
s4 = f'My name is {name} and I am {age} years old.'

print(s1 == s2 == s3 == s4)  # True

"""
RECOMMENDATION:
- Use f-strings for most cases (readable, fast)
- Use .format() when string is defined separately from variables
- Avoid % formatting (legacy)
- Never use concatenation for complex strings
"""


# =============================================================================
# 13. PRACTICAL EXAMPLES
# =============================================================================

# --- Generating HTML ---
items = ['Apple', 'Banana', 'Cherry']
html = '<ul>\n'
for item in items:
    html += f'  <li>{item}</li>\n'
html += '</ul>'
print(html)

# --- SQL Query (be careful with SQL injection!) ---
table = 'users'
columns = 'name, age, email'
query = f'SELECT {columns} FROM {table} WHERE age > 18'
print(query)
# Note: Use parameterized queries in real applications!

# --- File paths ---
import os
folder = 'documents'
filename = 'report'
extension = 'pdf'
path = f'{folder}/{filename}.{extension}'
print(path)
# Output: documents/report.pdf

# --- Logging messages ---
import datetime
level = 'INFO'
message = 'User logged in'
timestamp = datetime.datetime.now()
log = f'[{timestamp:%Y-%m-%d %H:%M:%S}] [{level}] {message}'
print(log)
# Output: [2024-12-17 14:30:45] [INFO] User logged in

# --- Progress bar ---
total = 100
completed = 45
percentage = completed / total
bar_length = 20
filled = int(bar_length * percentage)
bar = '█' * filled + '░' * (bar_length - filled)
print(f'Progress: [{bar}] {percentage:.1%}')
# Output: Progress: [█████████░░░░░░░░░░░] 45.0%


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. String Formatting Methods
   - Concatenation: 'Hello ' + name (avoid for complex strings)
   - % formatting: 'Hello %s' % name (legacy, avoid)
   - .format(): 'Hello {}'.format(name) (good)
   - f-strings: f'Hello {name}' (best, Python 3.6+)

2. .format() Features
   - Positional: '{0} {1}'.format(a, b)
   - Keyword: '{name}'.format(name='John')
   - Dict unpacking: '{name}'.format(**dict)
   - Object attributes: '{0.name}'.format(obj)
   - List access: '{0[0]}'.format(list)

3. Number Formatting
   - Decimals: {:.2f} → 3.14
   - Thousands separator: {:,} → 1,000,000
   - Percentage: {:.1%} → 85.0%
   - Padding: {:05d} → 00042
   - Binary/Hex: {:b}, {:x}

4. String Alignment
   - Left: {:<10}
   - Right: {:>10}
   - Center: {:^10}
   - Fill: {:*^10}

5. Date Formatting
   - %Y-%m-%d: 2024-12-17
   - %B %d, %Y: December 17, 2024
   - %H:%M:%S: 14:30:45
   - %A: Saturday

6. Best Practices
   - Use f-strings for readability
   - Use .format() for reusable template strings
   - Format numbers for user-friendly output
   - Use alignment for tables and reports
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Basic Formatting [EASY]
# Create a sentence using f-strings: "Hello, my name is [name] and I'm [age] years old."
name = "Alice"
age = 25
# TODO: Write your code here

# Solution:
# sentence = f"Hello, my name is {name} and I'm {age} years old."
# print(sentence)


# Exercise 2: Number Formatting [EASY]
# Format the following number with commas and 2 decimal places: 1234567.891
number = 1234567.891
# TODO: Write your code here

# Solution:
# print(f'{number:,.2f}')  # Output: 1,234,567.89


# Exercise 3: Alignment Table [MEDIUM]
# Create a formatted table of products
products = [
    ('Laptop', 999.99, 5),
    ('Mouse', 29.99, 50),
    ('Keyboard', 79.99, 25)
]
# Print a table with columns: Product (left, 15), Price (right, 10), Stock (right, 8)
# TODO: Write your code here

# Solution:
# print(f'{"Product":<15} {"Price":>10} {"Stock":>8}')
# print('-' * 35)
# for name, price, stock in products:
#     print(f'{name:<15} ${price:>9.2f} {stock:>8}')


# Exercise 4: Date Formatting [MEDIUM]
# Format current date in three different formats:
# a) December 17, 2024
# b) 17/12/2024
# c) 2024-12-17 14:30:45
import datetime
now = datetime.datetime.now()
# TODO: Write your code here

# Solution:
# print(f'{now:%B %d, %Y}')
# print(f'{now:%d/%m/%Y}')
# print(f'{now:%Y-%m-%d %H:%M:%S}')


# Exercise 5: Dictionary Formatting [MEDIUM]
# Format a user profile from dictionary
user = {'username': 'john_doe', 'email': 'john@example.com', 'posts': 42, 'followers': 1500}
# Create output: "john_doe (john@example.com) - 42 posts, 1,500 followers"
# TODO: Write your code here

# Solution:
# print(f"{user['username']} ({user['email']}) - {user['posts']} posts, {user['followers']:,} followers")


# Exercise 6: Progress Display [CHALLENGE]
# Create a function that displays a progress bar
def show_progress(current, total, width=20):
    # TODO: Create progress bar like: [████████░░░░░░░░░░░░] 40.0%
    pass

# Solution:
# def show_progress(current, total, width=20):
#     percentage = current / total
#     filled = int(width * percentage)
#     bar = '█' * filled + '░' * (width - filled)
#     print(f'[{bar}] {percentage:.1%}')
# 
# show_progress(40, 100)


# Exercise 7: Receipt Generator [CHALLENGE]
# Create a formatted receipt
items = [
    ('Coffee', 2, 4.99),
    ('Sandwich', 1, 8.99),
    ('Cookie', 3, 2.49)
]
tax_rate = 0.08
# Generate a receipt with items, subtotal, tax, and total
# TODO: Write your code here

# Solution:
# print('=' * 35)
# print(f'{"RECEIPT":^35}')
# print('=' * 35)
# print(f'{"Item":<15} {"Qty":>5} {"Price":>10}')
# print('-' * 35)
# subtotal = 0
# for name, qty, price in items:
#     item_total = qty * price
#     subtotal += item_total
#     print(f'{name:<15} {qty:>5} ${item_total:>9.2f}')
# print('-' * 35)
# tax = subtotal * tax_rate
# total = subtotal + tax
# print(f'{"Subtotal:":<20} ${subtotal:>9.2f}')
# print(f'{"Tax (8%):":<20} ${tax:>9.2f}')
# print(f'{"TOTAL:":<20} ${total:>9.2f}')
# print('=' * 35)


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting f before string
   ❌ '{name} is {age}'  # Literal string, not formatted
   ✅ f'{name} is {age}'

2. Using wrong quotes in f-strings with dicts
   ❌ f"Name: {person["name"]}"  # SyntaxError
   ✅ f"Name: {person['name']}"  # Use different quotes

3. Forgetting to convert types with concatenation
   ❌ 'Age: ' + age  # TypeError if age is int
   ✅ 'Age: ' + str(age)
   ✅ f'Age: {age}'  # f-strings handle conversion

4. Wrong format specifier order
   ❌ {:2f.}  # Wrong
   ✅ {:.2f}  # Correct

5. Missing colon in format spec
   ❌ {.2f}  # SyntaxError
   ✅ {:.2f}

6. Escaping braces in f-strings
   ❌ f'Use {variable} in braces'  # Works
   ❌ f'Show literal {}'  # Error - empty placeholder
   ✅ f'Show literal {{}}'  # Double braces for literal

7. Using = for debugging without Python 3.8+
   ❌ f'{x=}'  # SyntaxError in Python < 3.8
   ✅ f'x={x}'  # Compatible alternative
"""