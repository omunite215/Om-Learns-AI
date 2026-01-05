"""
================================================================================
PYTHON ADVANCED: ITERATORS AND ITERABLES
================================================================================
Day: 20

Description:
    Complete guide to Python's iteration protocol. Covers iterables, iterators,
    the __iter__ and __next__ methods, creating custom iterators, and practical
    patterns for memory-efficient data processing in ML/AI applications.

Learning Objectives:
    - Understand the difference between iterables and iterators
    - Know how Python's for loop works under the hood
    - Create custom iterator classes
    - Implement the iterator protocol (__iter__, __next__)
    - Compare iterators vs generators
    - Apply iterators in ML/AI data pipelines

Prerequisites:
    - Classes and OOP (Days 15-18)
    - Generators (Day 14)
    - Special methods (Day 18)
================================================================================
"""

# =============================================================================
# 1. ITERABLES VS ITERATORS
# =============================================================================

"""
ITERABLE:
- Any object you can loop over (for x in iterable)
- Has __iter__() method that returns an iterator
- Examples: list, tuple, str, dict, set, range, file

ITERATOR:
- Object that produces values one at a time
- Has __next__() method that returns next value
- Has __iter__() method that returns itself
- Raises StopIteration when exhausted
- Can only be traversed ONCE

Key difference:
- Iterable: CAN be iterated (like a book)
- Iterator: IS iterating (like a bookmark tracking position)

Remember:
- All iterators are iterables
- Not all iterables are iterators
"""

print("=== ITERABLES VS ITERATORS ===")

# List is an ITERABLE
nums = [1, 2, 3]
print(f"nums is iterable: {hasattr(nums, '__iter__')}")
print(f"nums is iterator: {hasattr(nums, '__next__')}")  # False!

# Get an ITERATOR from the iterable
i_nums = iter(nums)  # Same as nums.__iter__()
print(f"\ni_nums is iterable: {hasattr(i_nums, '__iter__')}")
print(f"i_nums is iterator: {hasattr(i_nums, '__next__')}")  # True!

print(f"\nType of nums: {type(nums)}")
print(f"Type of i_nums: {type(i_nums)}")


# =============================================================================
# 2. THE ITERATION PROTOCOL
# =============================================================================

"""
How Python's for loop works:

for item in iterable:
    do_something(item)

Is equivalent to:

iterator = iter(iterable)  # Call __iter__()
while True:
    try:
        item = next(iterator)  # Call __next__()
        do_something(item)
    except StopIteration:
        break
"""

print("\n=== THE ITERATION PROTOCOL ===")

nums = [1, 2, 3]

# Step 1: Get iterator
i_nums = iter(nums)

# Step 2: Get values with next()
print(f"next(i_nums): {next(i_nums)}")  # 1
print(f"next(i_nums): {next(i_nums)}")  # 2
print(f"next(i_nums): {next(i_nums)}")  # 3

# Step 3: StopIteration when exhausted
try:
    print(next(i_nums))
except StopIteration:
    print("StopIteration raised - iterator exhausted!")

# --- Manual iteration with while loop ---
print("\nManual iteration:")
nums = [10, 20, 30]
i_nums = iter(nums)

while True:
    try:
        item = next(i_nums)
        print(f"  Got: {item}")
    except StopIteration:
        print("  Done!")
        break


# =============================================================================
# 3. EXPLORING ITERATOR METHODS
# =============================================================================

print("\n=== ITERATOR METHODS ===")

nums = [1, 2, 3]
i_nums = iter(nums)

# What methods does an iterator have?
iterator_methods = [m for m in dir(i_nums) if not m.startswith('_')]
print(f"Public methods: {iterator_methods}")

# Key dunder methods
dunder_methods = ['__iter__', '__next__']
for method in dunder_methods:
    print(f"Has {method}: {hasattr(i_nums, method)}")

# iter() on iterator returns itself
print(f"\niter(i_nums) is i_nums: {iter(i_nums) is i_nums}")  # True!


# =============================================================================
# 4. CREATING CUSTOM ITERATORS
# =============================================================================

"""
To create a custom iterator:
1. Define __iter__() - returns the iterator object (usually self)
2. Define __next__() - returns next value or raises StopIteration
"""

class MyRange:
    """Custom range iterator"""
    
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start
    
    def __iter__(self):
        """Return the iterator object"""
        return self
    
    def __next__(self):
        """Return next value or raise StopIteration"""
        if (self.step > 0 and self.current >= self.end) or \
           (self.step < 0 and self.current <= self.end):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value
    
    def __repr__(self):
        return f"MyRange({self.start}, {self.end}, {self.step})"


print("\n=== CUSTOM ITERATOR: MyRange ===")

# Use in for loop
print("MyRange(1, 5):")
for num in MyRange(1, 5):
    print(f"  {num}")

# With step
print("\nMyRange(0, 10, 2):")
for num in MyRange(0, 10, 2):
    print(f"  {num}")

# Negative step
print("\nMyRange(5, 0, -1):")
for num in MyRange(5, 0, -1):
    print(f"  {num}")

# Manual iteration
print("\nManual iteration:")
my_range = MyRange(1, 4)
print(f"next(): {next(my_range)}")
print(f"next(): {next(my_range)}")
print(f"next(): {next(my_range)}")


# =============================================================================
# 5. ITERATOR VS GENERATOR COMPARISON
# =============================================================================

"""
Iterator (class-based):
- More code (need __iter__ and __next__)
- Can have multiple methods and state
- More control over behavior
- Reusable if __iter__ returns new instance

Generator (function-based):
- Less code (just use yield)
- Simpler for basic cases
- Automatically handles StopIteration
- Can only iterate once
"""

# --- Iterator class ---
class CountUp:
    """Iterator that counts from start to end"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# --- Generator function ---
def count_up(start, end):
    """Generator that counts from start to end"""
    current = start
    while current < end:
        yield current
        current += 1


print("\n=== ITERATOR VS GENERATOR ===")

# Both work the same way!
print("Iterator class:")
for n in CountUp(1, 4):
    print(f"  {n}")

print("\nGenerator function:")
for n in count_up(1, 4):
    print(f"  {n}")

# Size comparison
import sys
iter_obj = CountUp(1, 1000)
gen_obj = count_up(1, 1000)
print(f"\nIterator size: {sys.getsizeof(iter_obj)} bytes")
print(f"Generator size: {sys.getsizeof(gen_obj)} bytes")


# =============================================================================
# 6. REUSABLE ITERATORS
# =============================================================================

"""
Problem: Iterators can only be used once!
Solution: Make __iter__() return a NEW iterator each time.
"""

# --- Single-use iterator (problematic) ---
class SingleUseRange:
    def __init__(self, n):
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self  # Returns SAME object!
    
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


print("\n=== REUSABLE VS SINGLE-USE ===")

single = SingleUseRange(3)
print("First loop:")
for n in single:
    print(f"  {n}")

print("Second loop (EMPTY!):")
for n in single:
    print(f"  {n}")  # Nothing prints!


# --- Reusable iterator (correct) ---
class ReusableRange:
    """Iterable that creates fresh iterators"""
    
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        # Return a NEW iterator each time!
        return ReusableRangeIterator(self.n)


class ReusableRangeIterator:
    """The actual iterator"""
    
    def __init__(self, n):
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


print("\nReusable version:")
reusable = ReusableRange(3)

print("First loop:")
for n in reusable:
    print(f"  {n}")

print("Second loop (works!):")
for n in reusable:
    print(f"  {n}")


# =============================================================================
# 7. PRACTICAL ITERATOR EXAMPLES
# =============================================================================

# --- Fibonacci Iterator ---
class Fibonacci:
    """Infinite Fibonacci sequence iterator"""
    
    def __init__(self, max_value=None):
        self.max_value = max_value
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.max_value is not None and self.a > self.max_value:
            raise StopIteration
        
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


print("\n=== FIBONACCI ITERATOR ===")
print("Fibonacci up to 100:")
for num in Fibonacci(max_value=100):
    print(f"  {num}")


# --- Cycle Iterator (like itertools.cycle) ---
class Cycle:
    """Infinitely cycle through an iterable"""
    
    def __init__(self, iterable):
        self.items = list(iterable)
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.items:
            raise StopIteration
        
        value = self.items[self.index]
        self.index = (self.index + 1) % len(self.items)
        return value


print("\n=== CYCLE ITERATOR ===")
colors = Cycle(['red', 'green', 'blue'])
print("Cycling colors (first 7):")
for i, color in enumerate(colors):
    if i >= 7:
        break
    print(f"  {color}")


# --- Enumerate Iterator ---
class MyEnumerate:
    """Custom enumerate implementation"""
    
    def __init__(self, iterable, start=0):
        self.iterable = iter(iterable)
        self.count = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = next(self.iterable)  # Raises StopIteration when done
        index = self.count
        self.count += 1
        return (index, value)


print("\n=== CUSTOM ENUMERATE ===")
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in MyEnumerate(fruits, start=1):
    print(f"  {idx}. {fruit}")


# --- Zip Iterator ---
class MyZip:
    """Custom zip implementation"""
    
    def __init__(self, *iterables):
        self.iterators = [iter(it) for it in iterables]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.iterators:
            raise StopIteration
        
        values = []
        for iterator in self.iterators:
            values.append(next(iterator))  # StopIteration propagates
        return tuple(values)


print("\n=== CUSTOM ZIP ===")
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in MyZip(names, scores):
    print(f"  {name}: {score}")


# =============================================================================
# 8. ML/AI ITERATOR PATTERNS
# =============================================================================

import random

class DataLoader:
    """ML-style data loader with batching and shuffling"""
    
    def __init__(self, data, batch_size=32, shuffle=True):
        self.data = list(data)
        self.batch_size = batch_size
        self.shuffle = shuffle
    
    def __iter__(self):
        """Return new iterator (allows multiple epochs)"""
        return DataLoaderIterator(
            self.data, 
            self.batch_size, 
            self.shuffle
        )
    
    def __len__(self):
        """Number of batches"""
        return (len(self.data) + self.batch_size - 1) // self.batch_size


class DataLoaderIterator:
    """Iterator for DataLoader"""
    
    def __init__(self, data, batch_size, shuffle):
        self.data = data.copy()
        if shuffle:
            random.shuffle(self.data)
        self.batch_size = batch_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        batch = self.data[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return batch


print("\n=== ML DATA LOADER ===")

# Create dataset
dataset = list(range(100))
loader = DataLoader(dataset, batch_size=15, shuffle=True)

print(f"Dataset size: {len(dataset)}")
print(f"Batch size: 15")
print(f"Number of batches: {len(loader)}")

print("\nEpoch 1:")
for i, batch in enumerate(loader):
    print(f"  Batch {i}: {len(batch)} samples, first={batch[0]}")
    if i >= 2:
        print("  ...")
        break

print("\nEpoch 2 (reshuffled!):")
for i, batch in enumerate(loader):
    print(f"  Batch {i}: {len(batch)} samples, first={batch[0]}")
    if i >= 2:
        print("  ...")
        break


# --- Infinite Data Augmentation Iterator ---
class AugmentedDataIterator:
    """Infinite iterator with data augmentation"""
    
    def __init__(self, data, augment_func=None):
        self.data = list(data)
        self.augment_func = augment_func or (lambda x: x)
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            self.index = 0
            random.shuffle(self.data)
        
        item = self.data[self.index]
        self.index += 1
        return self.augment_func(item)


def simple_augment(x):
    """Simple augmentation: add random noise"""
    return x + random.uniform(-0.1, 0.1)


print("\n=== AUGMENTED DATA ITERATOR ===")
data = [1.0, 2.0, 3.0]
augmented = AugmentedDataIterator(data, simple_augment)

print("Infinite augmented samples (first 8):")
for i, sample in enumerate(augmented):
    if i >= 8:
        break
    print(f"  {sample:.4f}")


# --- Sequence Iterator for Time Series ---
class SequenceIterator:
    """Generate sequences for time series prediction"""
    
    def __init__(self, data, seq_length, pred_length=1):
        self.data = list(data)
        self.seq_length = seq_length
        self.pred_length = pred_length
        self.index = 0
        self.max_index = len(data) - seq_length - pred_length + 1
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= self.max_index:
            raise StopIteration
        
        X = self.data[self.index:self.index + self.seq_length]
        y = self.data[self.index + self.seq_length:
                      self.index + self.seq_length + self.pred_length]
        
        self.index += 1
        return X, y
    
    def __len__(self):
        return self.max_index


print("\n=== SEQUENCE ITERATOR ===")
time_series = [10, 20, 30, 40, 50, 60, 70, 80]
seq_iter = SequenceIterator(time_series, seq_length=3, pred_length=1)

print(f"Time series: {time_series}")
print(f"Sequence length: 3, Prediction length: 1")
print(f"Total sequences: {len(seq_iter)}")
print("\nSequences:")
for X, y in seq_iter:
    print(f"  X={X} -> y={y}")


# =============================================================================
# 9. BUILT-IN ITERATION FUNCTIONS
# =============================================================================

print("\n=== BUILT-IN ITERATION FUNCTIONS ===")

# iter() with sentinel value
print("iter() with sentinel:")
# iter(callable, sentinel) - calls until sentinel returned
import random
random.seed(42)
# This would call random.randint(1, 6) until it returns 6
# rolls = iter(lambda: random.randint(1, 6), 6)

# next() with default
nums_iter = iter([1, 2])
print(f"next with default: {next(nums_iter, 'default')}")  # 1
print(f"next with default: {next(nums_iter, 'default')}")  # 2
print(f"next with default: {next(nums_iter, 'default')}")  # 'default' (no error!)

# any() and all() use iteration
print(f"\nany([0, 0, 1]): {any([0, 0, 1])}")  # True
print(f"all([1, 1, 1]): {all([1, 1, 1])}")  # True

# sum(), min(), max() iterate
print(f"sum(range(5)): {sum(range(5))}")
print(f"max(range(5)): {max(range(5))}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Iterable vs Iterator
   - Iterable: Has __iter__(), can be looped over
   - Iterator: Has __iter__() and __next__(), produces values

2. Iterator Protocol
   - __iter__(): Returns iterator (usually self)
   - __next__(): Returns next value or raises StopIteration

3. Creating Custom Iterators
   - Class with __iter__ and __next__ methods
   - For reusability, __iter__ should return NEW iterator

4. Iterator vs Generator
   - Iterator: More code, more control, can have state/methods
   - Generator: Less code, simpler, automatic StopIteration

5. Key Functions
   - iter(obj): Get iterator from iterable
   - next(iterator): Get next value
   - next(iterator, default): Get next with default value

6. ML/AI Patterns
   - DataLoader with batching/shuffling
   - Sequence generators for time series
   - Infinite augmentation iterators
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Countdown Iterator [EASY]
# Create iterator that counts down from n to 1
# TODO: Write your code here

# Solution:
# class Countdown:
#     def __init__(self, start):
#         self.current = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <= 0:
#             raise StopIteration
#         value = self.current
#         self.current -= 1
#         return value


# Exercise 2: Take Iterator [MEDIUM]
# Create iterator that takes first n items from any iterable
# TODO: Write your code here

# Solution:
# class Take:
#     def __init__(self, iterable, n):
#         self.iterator = iter(iterable)
#         self.remaining = n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.remaining <= 0:
#             raise StopIteration
#         self.remaining -= 1
#         return next(self.iterator)


# Exercise 3: Filter Iterator [MEDIUM]
# Create iterator that filters items based on predicate
# TODO: Write your code here

# Solution:
# class Filter:
#     def __init__(self, predicate, iterable):
#         self.predicate = predicate
#         self.iterator = iter(iterable)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while True:
#             item = next(self.iterator)
#             if self.predicate(item):
#                 return item


# Exercise 4: Chain Iterator [MEDIUM]
# Chain multiple iterables together
# TODO: Write your code here

# Solution:
# class Chain:
#     def __init__(self, *iterables):
#         self.iterables = list(iterables)
#         self.current_iter = None
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while True:
#             if self.current_iter is None:
#                 if self.index >= len(self.iterables):
#                     raise StopIteration
#                 self.current_iter = iter(self.iterables[self.index])
#                 self.index += 1
#             try:
#                 return next(self.current_iter)
#             except StopIteration:
#                 self.current_iter = None


# Exercise 5: Sliding Window Iterator [CHALLENGE]
# Yield sliding windows over data
# TODO: Write your code here

# Solution:
# class SlidingWindow:
#     def __init__(self, iterable, size):
#         self.data = list(iterable)
#         self.size = size
#         self.index = 0
#     def __iter__(self):
#         self.index = 0
#         return self
#     def __next__(self):
#         if self.index > len(self.data) - self.size:
#             raise StopIteration
#         window = self.data[self.index:self.index + self.size]
#         self.index += 1
#         return window


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Confusing iterable and iterator
   ❌ Calling next() on a list
   ✅ Call next() on iter(list)

2. Not raising StopIteration
   ❌ Return None at end
   ✅ raise StopIteration

3. Single-use iterator when reusable needed
   ❌ __iter__ returns self for data containers
   ✅ __iter__ returns NEW iterator instance

4. Forgetting __iter__ in iterator class
   ❌ Only implementing __next__
   ✅ Implement both __iter__ (return self) and __next__

5. Modifying collection while iterating
   ❌ for item in list: list.remove(item)
   ✅ Iterate over copy or use list comprehension

6. Not handling StopIteration in custom iterators
   ❌ Calling next() without try/except
   ✅ Let StopIteration propagate or handle it
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("ITERATORS AND ITERABLES DEMONSTRATION")
    print("="*60)
    
    # Basic iteration protocol
    print("\n1. Iteration protocol:")
    nums = [1, 2, 3]
    iterator = iter(nums)
    print(f"   next(): {next(iterator)}")
    print(f"   next(): {next(iterator)}")
    print(f"   next(): {next(iterator)}")
    
    # Custom iterator
    print("\n2. Custom MyRange(1, 5):")
    for n in MyRange(1, 5):
        print(f"   {n}")
    
    # Generator equivalent
    print("\n3. Generator count_up(1, 5):")
    for n in count_up(1, 5):
        print(f"   {n}")
    
    # DataLoader
    print("\n4. ML DataLoader:")
    loader = DataLoader(range(10), batch_size=3)
    for batch in loader:
        print(f"   Batch: {batch}")
    
    print("\n" + "="*60)