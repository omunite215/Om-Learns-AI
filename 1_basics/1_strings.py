"""
================================================================================
PYTHON FUNDAMENTALS: STRING OPERATIONS
================================================================================
File: basics/1_strings.py
Date: 2024-12-16

Description:
    Comprehensive guide to Python string operations including creation,
    manipulation, formatting, and common methods.

Learning Objectives:
    - Create and work with strings
    - Master string indexing and slicing
    - Use built-in string methods effectively
    - Format strings using multiple techniques
    - Understand string immutability

Prerequisites:
    - Basic Python syntax
================================================================================
"""

# =============================================================================
# 1. BASIC STRING CREATION AND OUTPUT
# =============================================================================

# Simple print statement
print("Hello World!!")
# Output: Hello World!!

# Storing strings in variables
message = "hello world"
print(message)
# Output: hello world


# =============================================================================
# 2. MULTI-LINE STRINGS
# =============================================================================

# Using triple quotes (""" or ''') preserves formatting including newlines
message = """This is a first line.
This is another line.
This is another line.
Okay!! This is last line.
"""
print(message)
# Output: (displays across multiple lines as written)

# Note: Triple quotes are useful for docstrings and long text blocks


# =============================================================================
# 3. STRING LENGTH
# =============================================================================

message = "Hello World"
print(len(message))
# Output: 11
# Returns: int (counts all characters including spaces)


# =============================================================================
# 4. STRING INDEXING AND SLICING
# =============================================================================

message = "Hello World"

# --- Single Character Access (Indexing) ---
print(message[1])
# Output: 'e'
# Note: Indexing starts at 0, so [1] returns the 2nd character

print(message[0])    # Output: 'H' (first character)
print(message[-1])   # Output: 'd' (last character, negative indexing from end)
print(message[-2])   # Output: 'l' (second from end)

# --- Range of Characters (Slicing) ---
print(message[0:2])
# Output: 'He'
# Syntax: [start:end] where end index is NOT included

print(message[0:5])   # Output: 'Hello'
print(message[6:])    # Output: 'World' (omitting end = slice to end)
print(message[:5])    # Output: 'Hello' (omitting start = slice from beginning)
print(message[6:11])  # Output: 'World'
print(message[-5:])   # Output: 'World' (last 5 characters)

# Note: Slicing creates a new string, doesn't modify the original


# =============================================================================
# 5. STRING METHODS - CASE CONVERSION
# =============================================================================

message = "Hello World"

# Convert to lowercase
print(message.lower())
# Output: 'hello world'

# Convert to uppercase
print(message.upper())
# Output: 'HELLO WORLD'

# Capitalize first character only
print(message.capitalize())
# Output: 'Hello world'

# Title case (capitalize first letter of each word)
print(message.title())
# Output: 'Hello World'


# =============================================================================
# 6. STRING METHODS - SEARCHING AND COUNTING
# =============================================================================

message = "Hello World"

# Count occurrences of a substring
print(message.count("l"))
# Output: 3
# Counts how many times 'l' appears in the string

print(message.count("Hello"))  # Output: 1
print(message.count("o"))      # Output: 2

# Find position of substring
print(message.find("Universe"))
# Output: -1
# Returns -1 when substring is NOT found

print(message.find("World"))
# Output: 6
# Returns the starting index where substring is found

print(message.find("o"))  # Output: 4 (finds first occurrence)


# =============================================================================
# 7. STRING METHODS - REPLACEMENT
# =============================================================================

message = "Hello World"

# Replace substring with another string
new_message = message.replace("World", "Universe")
print(message)
# Output: 'Hello World'
# IMPORTANT: Original string is UNCHANGED (strings are immutable)

print(new_message)
# Output: 'Hello Universe'
# A new string is created with the replacement

# Replace ALL occurrences
message = message.replace("l", "a")
print(message)
# Output: 'Heaao Worad'
# Replaces every 'l' with 'a'

# Note: Strings are immutable - methods return new strings, don't modify originals


# =============================================================================
# 8. STRING CONCATENATION AND FORMATTING
# =============================================================================

greeting = "Hello"
name = "Om"

# --- Method 1: Standard Concatenation ---
message = greeting + ", " + name + ". Welcome!"
print(message)
# Output: Hello, Om. Welcome!
# Uses + operator to join strings

# --- Method 2: .format() Method ---
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
# Output: Hello, Om. Welcome!
# Placeholders {} are filled with arguments in order

message = '{1}, {0}. Welcome!'.format(greeting, name)
# Output: Om, Hello. Welcome! (can specify order with indices)

# --- Method 3: f-strings (Python 3.6+) ---
message = f'{greeting}, {name.capitalize()}. Welcome!'
print(message)
# Output: Hello, Om. Welcome!
# Most readable and preferred method - can include expressions inside {}

age = 25
message = f'{name} is {age} years old'
# Output: Om is 25 years old

# f-strings can evaluate expressions
message = f'2 + 2 = {2 + 2}'
# Output: 2 + 2 = 4


# =============================================================================
# 9. DISCOVERING STRING METHODS
# =============================================================================

message = "Hello World"

# dir() - Lists all available attributes and methods
print(dir(message))
# Output: ['__add__', 'capitalize', 'count', 'find', 'lower', 'upper', ...]
# Shows all methods you can call on a string

# help() - Detailed documentation about string class
print(help(str))
# Output: Complete documentation with descriptions of all string methods
# Use this to learn about methods you haven't seen before


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Strings are IMMUTABLE
   - String methods return NEW strings, they don't modify the original
   - message.upper() creates a new string, doesn't change message

2. Indexing and Slicing
   - Indexing starts at 0: message[0] is first character
   - Negative indexing from end: message[-1] is last character
   - Slicing syntax [start:end] where end is NOT included
   - Omitting start/end goes to beginning/end: message[:5], message[5:]

3. String Formatting
   - Old way: 'Hello ' + name (concatenation)
   - Better: '{} {}'.format(greeting, name) (.format method)
   - Best: f'{greeting} {name}' (f-strings - Python 3.6+)

4. Common String Methods
   - Case: .lower(), .upper(), .capitalize(), .title()
   - Search: .find(), .count()
   - Modify: .replace() (returns new string)

5. Discovery Tools
   - dir(string) - See all available methods
   - help(str) - Get detailed documentation
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: String Slicing [EASY]
# Given the string below, extract:
# a) The first word
# b) The last word
# c) Every second character
full_sentence = "Python is awesome"
# TODO: Write your code here

# Solution:
# first_word = full_sentence[0:6]  # or full_sentence[:6]
# last_word = full_sentence[10:]   # or use negative indexing
# every_second = full_sentence[::2]


# Exercise 2: String Manipulation [EASY]
# Create a variable with your full name, then:
# a) Convert it to all uppercase
# b) Count how many times the letter 'a' appears (case-insensitive)
# c) Replace your first name with "Python"
your_name = "Om Sharma"
# TODO: Write your code here

# Solution:
# uppercase_name = your_name.upper()
# count_a = your_name.lower().count('a')
# replaced = your_name.replace("Om", "Python")


# Exercise 3: String Formatting [MEDIUM]
# Create variables for: name, age, city
# Then create a formatted sentence using f-strings:
# "My name is [name], I am [age] years old, and I live in [city]."
# TODO: Write your code here

# Solution:
# name = "Om"
# age = 25
# city = "Mumbai"
# sentence = f"My name is {name}, I am {age} years old, and I live in {city}."


# Exercise 4: Email Username Extractor [MEDIUM]
# Given an email address, extract just the username (part before @)
email = "om.sharma@example.com"
# Hint: Use .find() to locate '@', then use slicing
# TODO: Write your code here

# Solution:
# at_position = email.find('@')
# username = email[:at_position]


# Exercise 5: Palindrome Checker [CHALLENGE]
# Check if a word is a palindrome (reads same forwards and backwards)
# Hint: Compare the word with its reverse using slicing
word = "racecar"
# TODO: Write your code here

# Solution:
# is_palindrome = (word == word[::-1])
# print(f"'{word}' is palindrome: {is_palindrome}")


# Exercise 6: Word Counter [CHALLENGE]
# Count the number of words in a sentence
# Hint: Use .split() method (look it up with help(str))
sentence = "Python is an amazing programming language"
# TODO: Write your code here

# Solution:
# words = sentence.split()
# word_count = len(words)
# print(f"Number of words: {word_count}")


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Trying to modify strings directly (they're immutable)
   ❌ message[0] = "h"  # TypeError: 'str' object does not support item assignment
   ✅ message = "h" + message[1:]  # Create new string

2. Confusing find() with index()
   ❌ message.index("X")  # Raises ValueError if not found
   ✅ message.find("X")   # Returns -1 if not found (safer)

3. Forgetting string methods return NEW strings
   ❌ message.upper()  # This doesn't change message
   ✅ message = message.upper()  # Assign to use the result

4. Off-by-one errors in slicing
   message[0:5]  # Gets characters at indices 0,1,2,3,4 (NOT 5)
   
5. Case sensitivity in find() and count()
   "Hello".find("hello")  # Returns -1 (case matters!)
   "Hello".lower().find("hello")  # Returns 0 (works!)
"""