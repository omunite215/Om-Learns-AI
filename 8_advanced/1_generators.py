"""
================================================================================
PYTHON ADVANCED: GENERATORS
================================================================================
Day: 14

Description:
    Complete guide to Python generators for memory-efficient iteration.
    Covers generator functions, generator expressions, yield statement,
    send/throw methods, and practical patterns for processing large datasets.

Learning Objectives:
    - Understand what generators are and how they work
    - Create generators using yield and generator expressions
    - Understand lazy evaluation and memory efficiency
    - Use send(), throw(), and close() methods
    - Chain generators with yield from
    - Apply generators in ML/AI data pipelines

Prerequisites:
    - Functions (Day 3-4)
    - Iterators and iterables
    - List comprehensions
================================================================================
"""

import sys
import time
import random

# =============================================================================
# 1. WHAT ARE GENERATORS?
# =============================================================================

"""
GENERATORS are functions that produce a sequence of values lazily (on-demand).

Regular function:
- Computes all values at once
- Stores everything in memory
- Returns complete result

Generator function:
- Produces one value at a time
- Pauses between yields
- Resumes where it left off
- Memory efficient!

Why generators matter for AI/ML:
- Process datasets larger than memory
- Stream data during training
- Efficient data augmentation pipelines
- Real-time data processing
- Batch generation for training
"""

# --- The problem: Memory with large data ---
def square_numbers_list(nums):
    """Regular function - stores all results in memory"""
    result = []
    for i in nums:
        result.append(i * i)
    return result

# For 10 million numbers: creates list of 10M items in memory!
# my_nums = square_numbers_list(range(10_000_000))  # ~400MB memory!

# --- The solution: Generators ---
def square_numbers_generator(nums):
    """Generator function - yields one value at a time"""
    for i in nums:
        yield i * i

# For 10 million numbers: only ONE value in memory at a time!
# my_nums = square_numbers_generator(range(10_000_000))  # ~0MB extra memory!


# =============================================================================
# 2. CREATING GENERATORS WITH YIELD
# =============================================================================

# --- Basic generator function ---
def count_up_to(n):
    """Generator that counts from 1 to n"""
    i = 1
    while i <= n:
        yield i  # Pause here, return i, resume on next call
        i += 1

# Using the generator
counter = count_up_to(5)
print(f"Generator object: {counter}")
print(f"Type: {type(counter)}")

# Get values one at a time with next()
print(f"First: {next(counter)}")   # 1
print(f"Second: {next(counter)}")  # 2
print(f"Third: {next(counter)}")   # 3

# Or iterate with for loop
print("\nIterating remaining values:")
for num in counter:
    print(num)  # 4, 5

# --- How yield works ---
def simple_generator():
    """Demonstrates yield behavior"""
    print("Starting generator")
    yield 1
    print("Resuming after first yield")
    yield 2
    print("Resuming after second yield")
    yield 3
    print("Generator exhausted")

gen = simple_generator()
print("Generator created (nothing printed yet!)")
print(f"First next(): {next(gen)}")
print(f"Second next(): {next(gen)}")
print(f"Third next(): {next(gen)}")
# next(gen)  # Would raise StopIteration

# --- Multiple yields in loop ---
def fibonacci(limit):
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("\nFibonacci up to 100:")
print(list(fibonacci(100)))


# =============================================================================
# 3. GENERATOR EXPRESSIONS
# =============================================================================

"""
Generator expressions = Compact generator syntax
Like list comprehensions but with () instead of []
"""

# --- List comprehension vs Generator expression ---
# List comprehension - creates list in memory
squares_list = [x * x for x in range(10)]
print(f"List: {squares_list}")
print(f"List size: {sys.getsizeof(squares_list)} bytes")

# Generator expression - creates generator object
squares_gen = (x * x for x in range(10))
print(f"Generator: {squares_gen}")
print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")

# Both can be iterated
print(f"From generator: {list(squares_gen)}")

# --- Memory comparison ---
# List of 1 million integers
list_size = sys.getsizeof([x for x in range(1_000_000)])
print(f"\nList (1M items): {list_size:,} bytes ({list_size/1024/1024:.1f} MB)")

# Generator for 1 million integers
gen_size = sys.getsizeof(x for x in range(1_000_000))
print(f"Generator (1M items): {gen_size} bytes")

# --- Generator expressions with conditions ---
evens = (x for x in range(20) if x % 2 == 0)
print(f"\nEven numbers: {list(evens)}")

# Nested generator expression
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = (num for row in matrix for num in row)
print(f"Flattened: {list(flattened)}")

# --- Using generator in functions ---
# Many functions accept generators directly
print(f"Sum of squares: {sum(x*x for x in range(10))}")
print(f"Max square: {max(x*x for x in range(10))}")
print(f"Any > 50: {any(x*x > 50 for x in range(10))}")


# =============================================================================
# 4. GENERATOR METHODS: send(), throw(), close()
# =============================================================================

# --- send() - Send value INTO generator ---
def accumulator():
    """Generator that accumulates sent values"""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

acc = accumulator()
print(f"\nAccumulator:")
print(f"Initial: {next(acc)}")      # Must call next() first!
print(f"Send 10: {acc.send(10)}")   # 10
print(f"Send 20: {acc.send(20)}")   # 30
print(f"Send 5: {acc.send(5)}")     # 35

# --- Coroutine pattern with send() ---
def running_average():
    """Calculate running average of sent values"""
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        if value is not None:
            total += value
            count += 1
            average = total / count

avg = running_average()
next(avg)  # Prime the generator
print(f"\nRunning average:")
print(f"Send 10: {avg.send(10)}")  # 10.0
print(f"Send 20: {avg.send(20)}")  # 15.0
print(f"Send 30: {avg.send(30)}")  # 20.0

# --- throw() - Throw exception into generator ---
def careful_generator():
    """Generator that handles thrown exceptions"""
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        yield "Caught ValueError!"
    yield "Continuing..."

gen = careful_generator()
print(f"\nthrow() example:")
print(next(gen))  # 1
print(gen.throw(ValueError))  # "Caught ValueError!"
print(next(gen))  # "Continuing..."

# --- close() - Stop generator ---
def infinite_counter():
    """Generator that counts forever"""
    i = 0
    try:
        while True:
            yield i
            i += 1
    except GeneratorExit:
        print("Generator closed!")

gen = infinite_counter()
print(f"\nclose() example:")
print(next(gen))  # 0
print(next(gen))  # 1
gen.close()  # Prints "Generator closed!"


# =============================================================================
# 5. YIELD FROM - DELEGATING TO SUB-GENERATORS
# =============================================================================

"""
yield from delegates to another iterable/generator
Cleaner than nested loops, passes values through
"""

# --- Without yield from ---
def chain_manually(*iterables):
    """Chain iterables without yield from"""
    for iterable in iterables:
        for item in iterable:
            yield item

# --- With yield from (cleaner!) ---
def chain(*iterables):
    """Chain iterables with yield from"""
    for iterable in iterables:
        yield from iterable

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print(f"\nChained: {list(chain(list1, list2, list3))}")

# --- Recursive generators with yield from ---
def flatten(nested_list):
    """Recursively flatten nested lists"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # Recurse
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(f"Flattened: {list(flatten(nested))}")

# --- yield from with generator functions ---
def numbers(n):
    yield from range(n)
    
def letters(n):
    yield from (chr(ord('a') + i) for i in range(n))

def numbers_and_letters(n):
    yield from numbers(n)
    yield from letters(n)

print(f"Combined: {list(numbers_and_letters(5))}")


# =============================================================================
# 6. GENERATOR STATE AND INSPECTION
# =============================================================================

import inspect

def stateful_generator():
    """Generator with inspectable state"""
    x = 0
    while x < 3:
        x += 1
        yield x

gen = stateful_generator()

# Check generator state
print(f"\nGenerator states:")
print(f"Initial state: {inspect.getgeneratorstate(gen)}")  # GEN_CREATED

next(gen)
print(f"After next(): {inspect.getgeneratorstate(gen)}")   # GEN_SUSPENDED

list(gen)  # Exhaust the generator
print(f"After exhausted: {inspect.getgeneratorstate(gen)}")  # GEN_CLOSED

"""
Generator states:
- GEN_CREATED: Created but not started
- GEN_RUNNING: Currently executing
- GEN_SUSPENDED: Paused at yield
- GEN_CLOSED: Completed or closed
"""


# =============================================================================
# 7. MEMORY COMPARISON: LIST VS GENERATOR
# =============================================================================

"""
Updated version of your original code for Python 3.x
- xrange -> range (xrange doesn't exist in Python 3)
- time.clock() -> time.perf_counter() (clock() removed in Python 3.8)
"""

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    """Create list of people - stores ALL in memory"""
    result = []
    for i in range(num_people):  # Changed from xrange to range
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    """Generate people - yields ONE at a time"""
    for i in range(num_people):  # Changed from xrange to range
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

def measure_memory_and_time(func, num_people, use_generator=False):
    """Measure memory usage and execution time"""
    import tracemalloc
    
    tracemalloc.start()
    t1 = time.perf_counter()  # Changed from time.clock()
    
    result = func(num_people)
    
    # Force evaluation for fair comparison
    if not use_generator:
        # List is already evaluated
        pass
    else:
        # Don't consume generator - that's the point!
        pass
    
    t2 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        'time': t2 - t1,
        'memory_current': current / 1024 / 1024,  # MB
        'memory_peak': peak / 1024 / 1024  # MB
    }

# --- Compare list vs generator ---
print("\n" + "="*60)
print("MEMORY COMPARISON: LIST VS GENERATOR")
print("="*60)

num_people = 100_000

print(f"\nCreating {num_people:,} people records...")

# List approach
print("\n--- List Approach ---")
stats_list = measure_memory_and_time(people_list, num_people, False)
print(f"Time: {stats_list['time']:.4f} seconds")
print(f"Peak Memory: {stats_list['memory_peak']:.2f} MB")

# Generator approach
print("\n--- Generator Approach ---")
stats_gen = measure_memory_and_time(people_generator, num_people, True)
print(f"Time: {stats_gen['time']:.6f} seconds")
print(f"Peak Memory: {stats_gen['memory_peak']:.4f} MB")

print(f"\nMemory savings: {stats_list['memory_peak'] / max(stats_gen['memory_peak'], 0.001):.0f}x less!")


# =============================================================================
# 8. PRACTICAL ML/AI GENERATOR PATTERNS
# =============================================================================

# --- Data Batch Generator ---
def batch_generator(data, batch_size):
    """Generate batches from data"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = list(range(100))
print("\nBatch generator:")
for i, batch in enumerate(batch_generator(data, 15)):
    print(f"Batch {i}: {len(batch)} items, first={batch[0]}, last={batch[-1]}")

# --- Infinite Data Generator (for training) ---
def infinite_batch_generator(data, batch_size, shuffle=True):
    """Infinitely yield batches, shuffling each epoch"""
    while True:
        if shuffle:
            indices = list(range(len(data)))
            random.shuffle(indices)
            shuffled = [data[i] for i in indices]
        else:
            shuffled = data
        
        yield from batch_generator(shuffled, batch_size)

# Usage:
# for step, batch in enumerate(infinite_batch_generator(train_data, 32)):
#     train_step(batch)
#     if step >= max_steps:
#         break

# --- Data Augmentation Pipeline ---
def augmentation_generator(images, augment_func, augments_per_image=3):
    """Generate augmented versions of images"""
    for image in images:
        yield image  # Original
        for _ in range(augments_per_image):
            yield augment_func(image)

# --- File Line Generator (large files) ---
def read_large_file(filepath, chunk_size=8192):
    """Memory-efficient line reading"""
    with open(filepath, 'r', encoding='utf-8') as f:
        buffer = ''
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                if buffer:
                    yield buffer
                break
            buffer += chunk
            lines = buffer.split('\n')
            buffer = lines.pop()
            yield from lines

# --- CSV Row Generator ---
def csv_row_generator(filepath):
    """Generate rows from CSV without loading entire file"""
    import csv
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        yield from reader

# --- Sliding Window Generator ---
def sliding_window(sequence, window_size, step=1):
    """Generate sliding windows over sequence"""
    for i in range(0, len(sequence) - window_size + 1, step):
        yield sequence[i:i + window_size]

print("\nSliding window (size=3, step=1):")
data = [1, 2, 3, 4, 5, 6, 7]
print(list(sliding_window(data, 3)))

# --- Time Series Sequence Generator ---
def sequence_generator(data, seq_length, pred_length=1):
    """Generate (X, y) pairs for time series"""
    for i in range(len(data) - seq_length - pred_length + 1):
        X = data[i:i + seq_length]
        y = data[i + seq_length:i + seq_length + pred_length]
        yield X, y

print("\nTime series sequences (seq=3, pred=1):")
data = [10, 20, 30, 40, 50, 60, 70]
for X, y in sequence_generator(data, 3, 1):
    print(f"X: {X} -> y: {y}")

# --- Progress Generator ---
def progress_generator(iterable, total=None, prefix='Progress'):
    """Wrap generator with progress tracking"""
    if total is None:
        total = len(iterable) if hasattr(iterable, '__len__') else '?'
    
    for i, item in enumerate(iterable, 1):
        print(f"\r{prefix}: {i}/{total}", end='', flush=True)
        yield item
    print()  # Newline at end


# =============================================================================
# 9. GENERATOR PIPELINES
# =============================================================================

"""
Chain generators for efficient data processing pipelines.
Each step processes one item at a time - minimal memory!
"""

def read_data(data):
    """Stage 1: Read data"""
    yield from data

def filter_valid(items, min_value=0):
    """Stage 2: Filter invalid items"""
    for item in items:
        if item >= min_value:
            yield item

def transform(items, func):
    """Stage 3: Transform items"""
    for item in items:
        yield func(item)

def batch(items, size):
    """Stage 4: Batch items"""
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch

# --- Build pipeline ---
raw_data = [-1, 2, -3, 4, 5, -6, 7, 8, 9, 10]

pipeline = batch(
    transform(
        filter_valid(
            read_data(raw_data),
            min_value=0
        ),
        func=lambda x: x * 2
    ),
    size=3
)

print("\nGenerator Pipeline:")
for batch_num, batch_data in enumerate(pipeline):
    print(f"Batch {batch_num}: {batch_data}")

# --- Cleaner pipeline with helper ---
def pipeline(*stages):
    """Chain multiple generators"""
    def run(data):
        result = data
        for stage in stages:
            result = stage(result)
        return result
    return run


# =============================================================================
# 10. ITERTOOLS - GENERATOR UTILITIES
# =============================================================================

import itertools

# --- itertools.count() - Infinite counter ---
print("\nitertools examples:")
counter = itertools.count(start=10, step=2)
print(f"count(10, 2): {[next(counter) for _ in range(5)]}")

# --- itertools.cycle() - Infinite cycling ---
cycler = itertools.cycle(['A', 'B', 'C'])
print(f"cycle: {[next(cycler) for _ in range(7)]}")

# --- itertools.repeat() - Repeat value ---
repeater = itertools.repeat('X', 3)
print(f"repeat: {list(repeater)}")

# --- itertools.chain() - Chain iterables ---
chained = itertools.chain([1, 2], [3, 4], [5, 6])
print(f"chain: {list(chained)}")

# --- itertools.islice() - Slice generator ---
gen = (x * x for x in range(100))
sliced = itertools.islice(gen, 5, 10)
print(f"islice(5, 10): {list(sliced)}")

# --- itertools.takewhile() / dropwhile() ---
nums = [1, 3, 5, 7, 2, 4, 6]
taken = itertools.takewhile(lambda x: x < 6, nums)
print(f"takewhile(<6): {list(taken)}")

# --- itertools.groupby() ---
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('A', 5)]
data_sorted = sorted(data, key=lambda x: x[0])
for key, group in itertools.groupby(data_sorted, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

# --- itertools.tee() - Duplicate generator ---
gen = (x for x in range(5))
gen1, gen2 = itertools.tee(gen, 2)
print(f"tee gen1: {list(gen1)}")
print(f"tee gen2: {list(gen2)}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Generator Basics
   - yield pauses function, returns value
   - next() resumes execution
   - Memory efficient - one value at a time
   - Can only iterate once

2. Creating Generators
   - Generator function: def func(): yield value
   - Generator expression: (x for x in iterable)

3. Generator Methods
   - next(gen): Get next value
   - gen.send(value): Send value into generator
   - gen.throw(exc): Throw exception into generator
   - gen.close(): Stop generator

4. yield from
   - Delegates to sub-generator
   - Cleaner than nested loops
   - Enables recursive generators

5. When to Use Generators
   - Large datasets that don't fit in memory
   - Streaming data processing
   - Infinite sequences
   - Lazy evaluation needed
   - Data pipelines

6. Common Patterns
   - Batch generation for training
   - Sliding windows for sequences
   - Data augmentation pipelines
   - File streaming

7. itertools Module
   - count, cycle, repeat: Infinite iterators
   - chain, islice, tee: Iterator tools
   - takewhile, dropwhile, groupby: Filtering
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Range Generator [EASY]
# Create generator that mimics range(start, stop, step)
# TODO: Write your code here

# Solution:
# def my_range(start, stop=None, step=1):
#     if stop is None:
#         start, stop = 0, start
#     current = start
#     while (step > 0 and current < stop) or (step < 0 and current > stop):
#         yield current
#         current += step


# Exercise 2: File Word Generator [EASY]
# Create generator that yields words from file one at a time
# TODO: Write your code here

# Solution:
# def word_generator(filepath):
#     with open(filepath, 'r') as f:
#         for line in f:
#             for word in line.split():
#                 yield word.strip('.,!?;:')


# Exercise 3: Prime Number Generator [MEDIUM]
# Create infinite generator of prime numbers
# TODO: Write your code here

# Solution:
# def primes():
#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     
#     n = 2
#     while True:
#         if is_prime(n):
#             yield n
#         n += 1


# Exercise 4: Moving Average Generator [MEDIUM]
# Generator that yields moving average of last n values sent to it
# TODO: Write your code here

# Solution:
# def moving_average(window_size):
#     values = []
#     average = None
#     while True:
#         value = yield average
#         if value is not None:
#             values.append(value)
#             if len(values) > window_size:
#                 values.pop(0)
#             average = sum(values) / len(values)


# Exercise 5: Tree Traversal Generator [MEDIUM]
# Yield all values from nested dict structure
# TODO: Write your code here

# Solution:
# def traverse_dict(d, path=''):
#     for key, value in d.items():
#         current_path = f"{path}.{key}" if path else key
#         if isinstance(value, dict):
#             yield from traverse_dict(value, current_path)
#         else:
#             yield (current_path, value)


# Exercise 6: Data Augmentation Generator [CHALLENGE]
# Create generator that yields original + augmented versions
# Augmentations: add noise, scale, shift
# TODO: Write your code here

# Solution:
# def augment_data(data_generator, augments_per_sample=2):
#     for sample in data_generator:
#         yield sample  # Original
#         for _ in range(augments_per_sample):
#             aug_type = random.choice(['noise', 'scale', 'shift'])
#             if aug_type == 'noise':
#                 yield [x + random.gauss(0, 0.1) for x in sample]
#             elif aug_type == 'scale':
#                 factor = random.uniform(0.8, 1.2)
#                 yield [x * factor for x in sample]
#             else:
#                 shift = random.uniform(-0.5, 0.5)
#                 yield [x + shift for x in sample]


# Exercise 7: Async-style Generator Pipeline [CHALLENGE]
# Create a generator-based task scheduler
# TODO: Write your code here

# Solution:
# def task_scheduler(tasks):
#     """Round-robin task scheduler using generators"""
#     task_gens = [task() for task in tasks]
#     while task_gens:
#         for i, gen in enumerate(task_gens[:]):
#             try:
#                 result = next(gen)
#                 yield f"Task {i}: {result}"
#             except StopIteration:
#                 task_gens.remove(gen)


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Trying to reuse exhausted generator
   ❌ gen = (x for x in range(5)); list(gen); list(gen)  # Second is empty!
   ✅ Create new generator or use itertools.tee()

2. Forgetting generators are lazy
   ❌ gen = (print(x) for x in range(5))  # Nothing prints!
   ✅ list(gen)  # Force evaluation

3. Using len() on generator
   ❌ len(x for x in range(10))  # TypeError!
   ✅ sum(1 for x in range(10))  # Count by iterating

4. Modifying list while iterating generator over it
   ❌ gen = (x for x in my_list); my_list.append(6)
   ✅ gen = (x for x in my_list.copy())

5. Forgetting to prime generator before send()
   ❌ gen.send(value)  # TypeError!
   ✅ next(gen); gen.send(value)

6. Memory issues with list() on infinite generator
   ❌ list(itertools.count())  # Infinite memory!
   ✅ list(itertools.islice(itertools.count(), 10))

7. Using return value of yield (it's None unless sent)
   ❌ result = yield value; print(result)  # None unless .send() used
   ✅ Understand bidirectional communication pattern

8. Confusing yield and return
   - yield: Pause and produce value, can resume
   - return: End generator, raise StopIteration
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("GENERATORS DEMONSTRATION")
    print("="*60)
    
    # Example 1: Basic generator
    print("\n1. Basic generator:")
    def simple_gen():
        yield "First"
        yield "Second"
        yield "Third"
    
    for value in simple_gen():
        print(f"   {value}")
    
    # Example 2: Generator expression
    print("\n2. Generator expression:")
    squares = (x**2 for x in range(5))
    print(f"   Squares: {list(squares)}")
    
    # Example 3: Memory efficiency
    print("\n3. Memory comparison:")
    list_mem = sys.getsizeof([x for x in range(10000)])
    gen_mem = sys.getsizeof(x for x in range(10000))
    print(f"   List: {list_mem:,} bytes")
    print(f"   Generator: {gen_mem} bytes")
    print(f"   Ratio: {list_mem/gen_mem:.0f}x")
    
    # Example 4: Practical batch generator
    print("\n4. Batch generator:")
    data = list(range(10))
    for i, batch in enumerate(batch_generator(data, 3)):
        print(f"   Batch {i}: {batch}")
    
    # Example 5: Sliding window
    print("\n5. Sliding window:")
    for window in sliding_window([1,2,3,4,5], 3):
        print(f"   {window}")
    
    print("\n" + "="*60)
    print("Run the exercises to practice!")
    print("="*60)