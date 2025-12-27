"""
================================================================================
PYTHON FUNDAMENTALS: FILE HANDLING
================================================================================
Day: 12

Description:
    Complete guide to file operations in Python. Covers reading, writing,
    binary files, file modes, context managers, file positioning, and
    practical patterns for data processing in ML/AI workflows.

Learning Objectives:
    - Open, read, write, and close files properly
    - Understand file modes (r, w, a, rb, wb, etc.)
    - Use context managers for safe file handling
    - Work with text and binary files
    - Navigate files with seek() and tell()
    - Process large files efficiently with chunking
    - Handle CSV, JSON, and other common formats

Prerequisites:
    - Basic Python syntax
    - OS module basics (Day 10)
================================================================================
"""

import os

# =============================================================================
# 1. WHAT IS FILE HANDLING?
# =============================================================================

"""
File handling allows Python to read from and write to files on disk.

Why is it essential for AI/ML?
- Loading and saving datasets (CSV, JSON, text)
- Saving model weights and checkpoints
- Writing training logs and metrics
- Processing configuration files
- Handling large datasets that don't fit in memory

Key concepts:
- File objects: Python's interface to files
- File modes: How to open files (read, write, append)
- Context managers: Safe and automatic file closing
- Encoding: How text is converted to/from bytes
"""


# =============================================================================
# 2. OPENING AND CLOSING FILES
# =============================================================================

# --- Basic open and close (NOT RECOMMENDED) ---
# f = open("demo.txt", 'r')
# print(f.name)      # Filename
# print(f.mode)      # Mode opened with
# print(f.closed)    # Is file closed?
# f.close()          # Must close manually!
# print(f.closed)    # True after closing

"""
Problems with manual close:
- Easy to forget
- Exceptions may skip close()
- Resource leaks
"""

# --- Context manager (ALWAYS USE THIS) ---
# with open("demo.txt", 'r') as f:
#     content = f.read()
#     # File automatically closed when block exits
# print(f.closed)  # True - automatically closed!

"""
Benefits of context managers:
- Automatic closing (even on exceptions)
- Cleaner code
- Resource safety
- Exception handling built-in
"""


# =============================================================================
# 3. FILE MODES
# =============================================================================

"""
FILE MODES - How to open a file:

TEXT MODES:
'r'  - Read (default). File must exist.
'w'  - Write. Creates new or TRUNCATES existing!
'a'  - Append. Creates new or adds to end.
'x'  - Exclusive create. Fails if file exists.
'r+' - Read and write. File must exist.
'w+' - Write and read. Creates/truncates.
'a+' - Append and read. Creates or appends.

BINARY MODES (add 'b'):
'rb'  - Read binary
'wb'  - Write binary
'ab'  - Append binary
'r+b' - Read/write binary

IMPORTANT:
- 'w' mode DESTROYS existing content!
- Binary mode for images, audio, models, pickles
- Text mode for .txt, .csv, .json, .py
"""

# --- Demonstrate modes ---
# Create a test file
test_file = "test_modes.txt"

# Write mode - creates/overwrites
with open(test_file, 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Append mode - adds to end
with open(test_file, 'a') as f:
    f.write("Line 3 (appended)\n")

# Read mode - read content
with open(test_file, 'r') as f:
    print(f.read())

# Clean up
os.remove(test_file)


# =============================================================================
# 4. READING FILES
# =============================================================================

# Create sample file for examples
sample_file = "sample_read.txt"
with open(sample_file, 'w') as f:
    f.write("Line 1: Hello World\n")
    f.write("Line 2: Python is great\n")
    f.write("Line 3: File handling\n")
    f.write("Line 4: Machine Learning\n")
    f.write("Line 5: Deep Learning\n")

# --- read() - Read entire file ---
with open(sample_file, 'r') as f:
    content = f.read()
    print("=== read() ===")
    print(content)
    print(f"Type: {type(content)}")  # str

# --- read(n) - Read n characters ---
with open(sample_file, 'r') as f:
    chunk = f.read(10)  # First 10 characters
    print(f"=== read(10) ===")
    print(f"'{chunk}'")

# --- readline() - Read one line ---
with open(sample_file, 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print("=== readline() ===")
    print(f"Line 1: {line1}", end='')
    print(f"Line 2: {line2}", end='')

# --- readlines() - Read all lines as list ---
with open(sample_file, 'r') as f:
    lines = f.readlines()
    print("=== readlines() ===")
    print(f"Type: {type(lines)}")  # list
    print(f"Count: {len(lines)} lines")
    print(f"First: {lines[0]}", end='')

# --- Iterate over file (MEMORY EFFICIENT - RECOMMENDED) ---
print("=== Iterating ===")
with open(sample_file, 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"{line_num}: {line.strip()}")

# --- Read with stripping newlines ---
with open(sample_file, 'r') as f:
    lines = [line.strip() for line in f]
    print(f"Stripped lines: {lines}")

# Clean up
os.remove(sample_file)


# =============================================================================
# 5. WRITING FILES
# =============================================================================

# --- write() - Write string ---
with open("write_demo.txt", 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")
    # Note: write() doesn't add newlines automatically!

# --- writelines() - Write list of strings ---
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("write_demo.txt", 'w') as f:
    f.writelines(lines)
    # Note: Must include \n in each string!

# --- Better writelines with join ---
lines = ["Apple", "Banana", "Cherry"]
with open("write_demo.txt", 'w') as f:
    f.write('\n'.join(lines) + '\n')

# --- print() to file ---
with open("write_demo.txt", 'w') as f:
    print("Using print function", file=f)
    print("Another line", file=f)
    print(f"Value: {42}", file=f)

# Verify
with open("write_demo.txt", 'r') as f:
    print(f.read())

# Clean up
os.remove("write_demo.txt")


# =============================================================================
# 6. FILE POSITION - tell() AND seek()
# =============================================================================

"""
Files have an internal cursor/position pointer:
- tell(): Returns current position (bytes from start)
- seek(offset, whence): Move to position

seek() whence values:
- 0: From beginning (default)
- 1: From current position
- 2: From end of file
"""

# Create test file
with open("position_demo.txt", 'w') as f:
    f.write("ABCDEFGHIJ")  # 10 characters

# --- Demonstrate positioning ---
with open("position_demo.txt", 'r') as f:
    print(f"Initial position: {f.tell()}")  # 0
    
    content = f.read(5)
    print(f"Read 5 chars: '{content}'")
    print(f"Position now: {f.tell()}")  # 5
    
    # Go back to start
    f.seek(0)
    print(f"After seek(0): {f.tell()}")  # 0
    
    # Go to position 3
    f.seek(3)
    print(f"After seek(3): '{f.read(4)}'")  # DEFG
    
    # Go to end
    f.seek(0, 2)  # 2 = from end
    print(f"At end: {f.tell()}")  # 10

# --- Practical: Overwrite part of file ---
with open("position_demo.txt", 'r+') as f:
    f.seek(0)       # Go to start
    f.write("XXX")  # Overwrite first 3 chars

with open("position_demo.txt", 'r') as f:
    print(f"Modified: {f.read()}")  # XXXDEFGHIJ

# Clean up
os.remove("position_demo.txt")


# =============================================================================
# 7. COPYING FILES
# =============================================================================

# Create source file
with open("source.txt", 'w') as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# --- Simple copy (small files) ---
with open("source.txt", 'r') as rf:
    with open("copy_simple.txt", 'w') as wf:
        wf.write(rf.read())

# --- Line by line copy (medium files) ---
with open("source.txt", 'r') as rf:
    with open("copy_lines.txt", 'w') as wf:
        for line in rf:
            wf.write(line)

# --- Using shutil (RECOMMENDED for most cases) ---
import shutil

shutil.copy("source.txt", "copy_shutil.txt")      # Copy content + permissions
shutil.copy2("source.txt", "copy_shutil2.txt")    # Copy content + all metadata

# Clean up
for f in ["source.txt", "copy_simple.txt", "copy_lines.txt", 
          "copy_shutil.txt", "copy_shutil2.txt"]:
    if os.path.exists(f):
        os.remove(f)


# =============================================================================
# 8. BINARY FILES
# =============================================================================

"""
Binary mode ('b') for:
- Images (jpg, png, gif)
- Audio/Video (mp3, mp4)
- Compiled files (exe, pyc)
- Serialized data (pickle, model weights)
- Any non-text file

NEVER use text mode for binary files - it corrupts data!
"""

# --- Write binary data ---
binary_data = bytes([0, 1, 2, 3, 255, 254, 253])
with open("binary_demo.bin", 'wb') as f:
    f.write(binary_data)

# --- Read binary data ---
with open("binary_demo.bin", 'rb') as f:
    data = f.read()
    print(f"Binary data: {data}")
    print(f"Type: {type(data)}")  # bytes
    print(f"First byte: {data[0]}")  # 0

# --- Copy binary file (e.g., image) ---
# with open("sample.jpg", 'rb') as rf:
#     with open("sample_copy.jpg", 'wb') as wf:
#         wf.write(rf.read())

# Clean up
os.remove("binary_demo.bin")


# =============================================================================
# 9. CHUNKED READING (LARGE FILES)
# =============================================================================

"""
For large files (GBs), reading all at once causes memory issues.
Solution: Read in chunks!

Essential for:
- Processing large datasets
- Copying large model files
- Log file analysis
- Streaming data processing
"""

# Create a larger test file
with open("large_file.txt", 'w') as f:
    for i in range(1000):
        f.write(f"Line {i}: This is test data for chunked reading demo\n")

# --- Chunked text reading ---
chunk_size = 1024  # 1KB chunks
with open("large_file.txt", 'r') as f:
    chunk_count = 0
    while True:
        chunk = f.read(chunk_size)
        if not chunk:  # Empty string = EOF
            break
        chunk_count += 1
        # Process chunk here
    print(f"Processed {chunk_count} chunks")

# --- Chunked binary copy (from your original code) ---
def copy_binary_chunked(src, dst, chunk_size=4096):
    """Copy binary file in chunks - memory efficient"""
    bytes_copied = 0
    with open(src, 'rb') as rf:
        with open(dst, 'wb') as wf:
            while True:
                chunk = rf.read(chunk_size)
                if not chunk:
                    break
                wf.write(chunk)
                bytes_copied += len(chunk)
    return bytes_copied

# --- Generator for line-by-line processing ---
def read_lines_chunked(filepath, chunk_size=8192):
    """Generator that yields lines from large file"""
    with open(filepath, 'r') as f:
        buffer = ''
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                if buffer:
                    yield buffer
                break
            buffer += chunk
            lines = buffer.split('\n')
            buffer = lines.pop()  # Keep incomplete line
            for line in lines:
                yield line

# Usage:
# for line in read_lines_chunked("huge_file.txt"):
#     process(line)

# Clean up
os.remove("large_file.txt")


# =============================================================================
# 10. ENCODING
# =============================================================================

"""
Encoding defines how text is converted to/from bytes.

Common encodings:
- utf-8: Universal, supports all languages (DEFAULT, recommended)
- ascii: English only, 7-bit
- latin-1: Western European
- utf-16: Windows default for some files
- cp1252: Windows Western European

Always specify encoding explicitly for portability!
"""

# --- Write with encoding ---
with open("encoded.txt", 'w', encoding='utf-8') as f:
    f.write("Hello, 世界! 🌍\n")  # English, Chinese, emoji
    f.write("Ñoño, café, naïve\n")  # Special characters

# --- Read with encoding ---
with open("encoded.txt", 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# --- Handle encoding errors ---
with open("encoded.txt", 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()  # Replaces bad chars with ?

# errors options: 'strict' (default), 'ignore', 'replace', 'backslashreplace'

# --- Detect encoding (using chardet) ---
"""
pip install chardet

import chardet

with open("unknown.txt", 'rb') as f:
    raw = f.read()
    result = chardet.detect(raw)
    print(result)  # {'encoding': 'utf-8', 'confidence': 0.99}
"""

# Clean up
os.remove("encoded.txt")


# =============================================================================
# 11. WORKING WITH CSV FILES
# =============================================================================

import csv

# --- Write CSV ---
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'San Francisco'],
    ['Charlie', 35, 'Chicago']
]

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# --- Read CSV ---
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# --- CSV with headers (DictReader/DictWriter) ---
# Write
with open('data_dict.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30, 'city': 'NYC'})
    writer.writerow({'name': 'Bob', 'age': 25, 'city': 'SF'})

# Read
with open('data_dict.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is {row['age']} years old")

# Clean up
os.remove('data.csv')
os.remove('data_dict.csv')


# =============================================================================
# 12. WORKING WITH JSON FILES
# =============================================================================

import json

# --- Write JSON ---
data = {
    'name': 'Model_v1',
    'accuracy': 0.95,
    'epochs': 100,
    'layers': [64, 128, 64],
    'params': {
        'learning_rate': 0.001,
        'batch_size': 32
    }
}

with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)  # indent for pretty print

# --- Read JSON ---
with open('config.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print(f"Model: {loaded_data['name']}")
    print(f"Accuracy: {loaded_data['accuracy']}")

# --- JSON string operations ---
json_string = json.dumps(data, indent=2)  # To string
data_back = json.loads(json_string)        # From string

# Clean up
os.remove('config.json')


# =============================================================================
# 13. PRACTICAL ML/AI FILE UTILITIES
# =============================================================================

def safe_read_file(filepath, encoding='utf-8'):
    """Read file with error handling"""
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except PermissionError:
        print(f"Permission denied: {filepath}")
        return None
    except UnicodeDecodeError:
        print(f"Encoding error, trying latin-1: {filepath}")
        with open(filepath, 'r', encoding='latin-1') as f:
            return f.read()


def safe_write_file(filepath, content, encoding='utf-8'):
    """Write file with directory creation"""
    os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
    with open(filepath, 'w', encoding=encoding) as f:
        f.write(content)
    return True


def append_to_log(filepath, message, timestamp=True):
    """Append message to log file with optional timestamp"""
    from datetime import datetime
    with open(filepath, 'a', encoding='utf-8') as f:
        if timestamp:
            ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{ts}] {message}\n")
        else:
            f.write(f"{message}\n")


def count_lines(filepath):
    """Count lines in file efficiently"""
    count = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        for _ in f:
            count += 1
    return count


def head(filepath, n=10):
    """Return first n lines of file (like Unix head)"""
    lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            lines.append(line.rstrip())
    return lines


def tail(filepath, n=10):
    """Return last n lines of file (like Unix tail)"""
    from collections import deque
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(deque(f, maxlen=n))


def file_checksum(filepath, algorithm='md5'):
    """Calculate file checksum for data integrity"""
    import hashlib
    hash_func = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()


class DataLogger:
    """Log training metrics to file"""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.headers_written = False
    
    def log(self, metrics_dict):
        """Log metrics as CSV row"""
        mode = 'a' if self.headers_written else 'w'
        with open(self.filepath, mode, newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=metrics_dict.keys())
            if not self.headers_written:
                writer.writeheader()
                self.headers_written = True
            writer.writerow(metrics_dict)
    
    def read_all(self):
        """Read all logged metrics"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))


class ConfigManager:
    """Manage JSON configuration files"""
    
    def __init__(self, config_path):
        self.path = config_path
        self.config = self._load()
    
    def _load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save()


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Always Use Context Managers
   with open(file, mode) as f:
       # File auto-closes when block exits

2. File Modes
   - 'r': Read (default)
   - 'w': Write (overwrites!)
   - 'a': Append
   - 'b': Binary mode (add to above)
   - '+': Read and write

3. Reading Methods
   - read(): Entire file as string
   - read(n): n characters
   - readline(): One line
   - readlines(): All lines as list
   - Iterate: for line in f (memory efficient)

4. Writing Methods
   - write(str): Write string
   - writelines(list): Write list of strings
   - print(..., file=f): Print to file

5. File Position
   - tell(): Current position
   - seek(offset, whence): Move position

6. Large Files
   - Read in chunks to save memory
   - Use generators for line processing

7. Always Specify Encoding
   open(file, 'r', encoding='utf-8')

8. Common Formats
   - csv module for CSV files
   - json module for JSON files
   - pickle for Python objects
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Word Counter [EASY]
# Read a text file and count:
# - Total lines, words, characters
# TODO: Write your code here

# Solution:
# def count_file_stats(filepath):
#     with open(filepath, 'r', encoding='utf-8') as f:
#         content = f.read()
#         lines = content.count('\n') + 1
#         words = len(content.split())
#         chars = len(content)
#     return {'lines': lines, 'words': words, 'chars': chars}


# Exercise 2: Log Writer [EASY]
# Create function that appends timestamped entries to log file
# Format: [YYYY-MM-DD HH:MM:SS] level: message
# TODO: Write your code here

# Solution:
# from datetime import datetime
# def log_entry(filepath, level, message):
#     ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     with open(filepath, 'a', encoding='utf-8') as f:
#         f.write(f"[{ts}] {level.upper()}: {message}\n")


# Exercise 3: CSV Processor [MEDIUM]
# Read CSV, filter rows where column > value, write to new CSV
# TODO: Write your code here

# Solution:
# def filter_csv(input_path, output_path, column, threshold):
#     with open(input_path, 'r', encoding='utf-8') as rf:
#         reader = csv.DictReader(rf)
#         rows = [r for r in reader if float(r[column]) > threshold]
#     
#     if rows:
#         with open(output_path, 'w', newline='', encoding='utf-8') as wf:
#             writer = csv.DictWriter(wf, fieldnames=rows[0].keys())
#             writer.writeheader()
#             writer.writerows(rows)
#     return len(rows)


# Exercise 4: File Merger [MEDIUM]
# Merge multiple text files into one, with separators
# TODO: Write your code here

# Solution:
# def merge_files(input_files, output_file, separator="\n---\n"):
#     with open(output_file, 'w', encoding='utf-8') as wf:
#         for i, input_file in enumerate(input_files):
#             if i > 0:
#                 wf.write(separator)
#             with open(input_file, 'r', encoding='utf-8') as rf:
#                 wf.write(rf.read())


# Exercise 5: Binary File Comparator [MEDIUM]
# Compare two binary files, return True if identical
# TODO: Write your code here

# Solution:
# def files_identical(file1, file2, chunk_size=8192):
#     with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
#         while True:
#             chunk1 = f1.read(chunk_size)
#             chunk2 = f2.read(chunk_size)
#             if chunk1 != chunk2:
#                 return False
#             if not chunk1:
#                 return True


# Exercise 6: Config File System [CHALLENGE]
# Create class that manages nested config with dot notation
# config.get("model.layers.0"), config.set("training.epochs", 100)
# TODO: Write your code here

# Solution:
# class NestedConfig:
#     def __init__(self, filepath):
#         self.filepath = filepath
#         self.data = self._load()
#     
#     def _load(self):
#         if os.path.exists(self.filepath):
#             with open(self.filepath, 'r') as f:
#                 return json.load(f)
#         return {}
#     
#     def save(self):
#         with open(self.filepath, 'w') as f:
#             json.dump(self.data, f, indent=2)
#     
#     def get(self, key_path, default=None):
#         keys = key_path.split('.')
#         value = self.data
#         for key in keys:
#             if isinstance(value, dict) and key in value:
#                 value = value[key]
#             elif isinstance(value, list) and key.isdigit():
#                 value = value[int(key)]
#             else:
#                 return default
#         return value
#     
#     def set(self, key_path, value):
#         keys = key_path.split('.')
#         data = self.data
#         for key in keys[:-1]:
#             if key not in data:
#                 data[key] = {}
#             data = data[key]
#         data[keys[-1]] = value
#         self.save()


# Exercise 7: Large File Processor [CHALLENGE]
# Process large CSV in chunks, compute running statistics
# (mean, min, max) without loading entire file
# TODO: Write your code here

# Solution:
# def streaming_stats(filepath, column, chunk_lines=1000):
#     total = 0
#     count = 0
#     min_val = float('inf')
#     max_val = float('-inf')
#     
#     with open(filepath, 'r', encoding='utf-8') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             val = float(row[column])
#             total += val
#             count += 1
#             min_val = min(min_val, val)
#             max_val = max(max_val, val)
#     
#     return {
#         'mean': total / count if count else 0,
#         'min': min_val,
#         'max': max_val,
#         'count': count
#     }


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting to close files
   ❌ f = open('file.txt'); data = f.read()
   ✅ with open('file.txt') as f: data = f.read()

2. Using 'w' mode accidentally (destroys data!)
   ❌ with open('important.txt', 'w') as f: content = f.read()
   ✅ with open('important.txt', 'r') as f: content = f.read()

3. Not specifying encoding
   ❌ open('file.txt', 'r')
   ✅ open('file.txt', 'r', encoding='utf-8')

4. Text mode for binary files
   ❌ open('image.jpg', 'r')
   ✅ open('image.jpg', 'rb')

5. Reading large files entirely into memory
   ❌ data = open('huge.csv').read()
   ✅ for line in open('huge.csv'): process(line)

6. Forgetting newline in write()
   ❌ f.write("line1"); f.write("line2")  # Results: line1line2
   ✅ f.write("line1\n"); f.write("line2\n")

7. Not handling file not found
   ❌ with open('maybe.txt') as f: ...
   ✅ try: with open('maybe.txt') as f: ...
      except FileNotFoundError: ...

8. Windows CSV line ending issues
   ❌ open('data.csv', 'w')
   ✅ open('data.csv', 'w', newline='')
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("FILE HANDLING DEMONSTRATION")
    print("="*60)
    
    # Create demo file
    demo_file = "demo_output.txt"
    
    # Write
    print("\n1. Writing to file...")
    with open(demo_file, 'w', encoding='utf-8') as f:
        f.write("Hello, World!\n")
        f.write("Python File Handling Demo\n")
        f.write("Line 3 of the file\n")
    print(f"   Created: {demo_file}")
    
    # Read
    print("\n2. Reading from file...")
    with open(demo_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            print(f"   Line {i}: {line.strip()}")
    
    # Append
    print("\n3. Appending to file...")
    with open(demo_file, 'a', encoding='utf-8') as f:
        f.write("This line was appended!\n")
    
    # File info
    print(f"\n4. File size: {os.path.getsize(demo_file)} bytes")
    
    # Clean up
    os.remove(demo_file)
    print(f"\n5. Cleaned up: {demo_file}")
    
    print("\n" + "="*60)
    print("Run the exercises to practice!")
    print("="*60)