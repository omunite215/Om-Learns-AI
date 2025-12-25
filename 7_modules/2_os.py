"""
================================================================================
PYTHON FUNDAMENTALS: THE OS MODULE
================================================================================
Day: 10

Description:
    Complete guide to Python's os module for operating system interactions.
    Covers file/directory operations, path manipulation, environment variables,
    directory traversal, and cross-platform best practices essential for
    data pipelines and ML workflows.

Learning Objectives:
    - Navigate and manipulate the file system programmatically
    - Work with file and directory paths cross-platform
    - Access and modify environment variables
    - Traverse directory trees efficiently
    - Get file metadata and information
    - Build robust file handling for data science projects

Prerequisites:
    - Basic Python syntax
    - Imports and modules (Day 5)
================================================================================
"""

import os
from datetime import datetime

# =============================================================================
# 1. WHAT IS THE OS MODULE?
# =============================================================================

"""
The OS module provides a portable way to use operating system functionality.

Why is it important for AI/ML?
- Loading datasets from various directories
- Organizing model checkpoints and outputs
- Managing experiment logs and results
- Creating data pipelines
- Automating file preprocessing

Key submodules:
- os.path: Path manipulation utilities
- os.environ: Environment variables
"""

print(f"Operating System: {os.name}")
# Output: 'posix' (Linux/Mac) or 'nt' (Windows)


# =============================================================================
# 2. CURRENT WORKING DIRECTORY
# =============================================================================

# --- Get current working directory ---
cwd = os.getcwd()
print(f"Current directory: {cwd}")
# Output: /home/user/projects/python_course

# --- Change directory ---
# os.chdir("/path/to/directory")
# os.chdir("..")          # Go up one level
# os.chdir("subfolder")   # Go into subfolder

# Example: Navigate relative to current location
original_dir = os.getcwd()
# os.chdir("./../1_basics")  # Go up, then into 1_basics
# print(f"New directory: {os.getcwd()}")
# os.chdir(original_dir)     # Return to original

# --- Why this matters for ML ---
"""
When loading data, always be aware of your working directory:
- Relative paths depend on where script is run from
- Use absolute paths or os.path for reliability
"""


# =============================================================================
# 3. ENVIRONMENT VARIABLES
# =============================================================================

# --- Access environment variables ---
home_dir = os.environ.get("HOME")  # Linux/Mac
# home_dir = os.environ.get("USERPROFILE")  # Windows
print(f"Home directory: {home_dir}")

# --- Get with default value (recommended) ---
python_path = os.environ.get("PYTHONPATH", "Not set")
print(f"Python path: {python_path}")

# --- Access directly (raises KeyError if not exists) ---
# path = os.environ["PATH"]  # Use with caution

# --- Set environment variable (current process only) ---
os.environ["MY_PROJECT_DIR"] = "/path/to/project"
os.environ["MODEL_VERSION"] = "v2.1"
print(f"Model version: {os.environ.get('MODEL_VERSION')}")

# --- Delete environment variable ---
# del os.environ["MY_PROJECT_DIR"]

# --- List all environment variables ---
# for key, value in os.environ.items():
#     print(f"{key}: {value}")

# --- Common ML/AI environment variables ---
"""
Useful environment variables for AI projects:
- CUDA_VISIBLE_DEVICES: Control GPU visibility
- PYTHONPATH: Additional module search paths
- MODEL_PATH: Where to save/load models
- DATA_DIR: Dataset location
- LOG_LEVEL: Logging verbosity
"""


# =============================================================================
# 4. LISTING DIRECTORY CONTENTS
# =============================================================================

# --- List all items in directory ---
contents = os.listdir(".")  # Current directory
print(f"Directory contents: {contents}")
# Output: ['file1.py', 'file2.py', 'subfolder', ...]

# --- List specific directory ---
# home_contents = os.listdir(os.environ.get("HOME"))

# --- Filter by file type ---
all_files = os.listdir(".")
py_files = [f for f in all_files if f.endswith(".py")]
print(f"Python files: {py_files}")

# --- Separate files and directories ---
items = os.listdir(".")
files = [f for f in items if os.path.isfile(f)]
dirs = [d for d in items if os.path.isdir(d)]
print(f"Files: {files}")
print(f"Directories: {dirs}")


# =============================================================================
# 5. PATH OPERATIONS (os.path)
# =============================================================================

"""
os.path provides utilities for manipulating file paths in a cross-platform way.
ALWAYS use os.path instead of string concatenation for paths!
"""

# --- Join paths (ESSENTIAL - use this always!) ---
# ❌ Wrong: path = "folder" + "/" + "file.txt"
# ✅ Correct:
path = os.path.join("data", "raw", "dataset.csv")
print(f"Joined path: {path}")
# Output: data/raw/dataset.csv (Linux) or data\raw\dataset.csv (Windows)

# Multiple components
model_path = os.path.join("models", "v2", "checkpoints", "best_model.h5")
print(f"Model path: {model_path}")

# --- Split path into directory and filename ---
full_path = "/home/user/data/train.csv"
directory, filename = os.path.split(full_path)
print(f"Directory: {directory}")   # /home/user/data
print(f"Filename: {filename}")     # train.csv

# --- Get just the filename ---
print(f"Basename: {os.path.basename(full_path)}")
# Output: train.csv

# --- Get just the directory ---
print(f"Dirname: {os.path.dirname(full_path)}")
# Output: /home/user/data

# --- Split filename and extension ---
name, ext = os.path.splitext("model_v2.tar.gz")
print(f"Name: {name}, Extension: {ext}")
# Output: Name: model_v2.tar, Extension: .gz

# Better for multiple extensions
filename = "archive.tar.gz"
print(f"Full extension handling: {filename.replace('.tar.gz', '')}")

# --- Get absolute path ---
relative = "./data/file.csv"
absolute = os.path.abspath(relative)
print(f"Absolute path: {absolute}")

# --- Get real path (resolves symlinks) ---
real = os.path.realpath(relative)
print(f"Real path: {real}")

# --- Normalize path (clean up redundant separators) ---
messy_path = "data//raw/../processed/./file.csv"
clean_path = os.path.normpath(messy_path)
print(f"Normalized: {clean_path}")
# Output: data/processed/file.csv

# --- Check path properties ---
test_path = "sample_module.py"
print(f"Exists: {os.path.exists(test_path)}")
print(f"Is file: {os.path.isfile(test_path)}")
print(f"Is directory: {os.path.isdir(test_path)}")
print(f"Is absolute: {os.path.isabs(test_path)}")

# --- Common path for ML projects ---
"""
project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── models/
│   └── checkpoints/
├── notebooks/
├── src/
└── logs/

Access pattern:
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
MODEL_DIR = os.path.join(BASE_DIR, "models")
"""


# =============================================================================
# 6. CREATING DIRECTORIES
# =============================================================================

# --- Create single directory ---
# os.mkdir("new_folder")  # Fails if parent doesn't exist

# --- Create nested directories (RECOMMENDED) ---
os.makedirs("data/processed/images", exist_ok=True)
# exist_ok=True: Don't raise error if directory exists

# --- Practical ML example ---
def setup_project_structure(base_path):
    """Create standard ML project directory structure"""
    directories = [
        "data/raw",
        "data/processed",
        "data/external",
        "models/checkpoints",
        "logs/training",
        "logs/evaluation",
        "notebooks",
        "src/utils",
        "outputs/figures",
        "outputs/predictions"
    ]
    
    for dir_path in directories:
        full_path = os.path.join(base_path, dir_path)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created: {full_path}")

# setup_project_structure("my_ml_project")


# =============================================================================
# 7. REMOVING FILES AND DIRECTORIES
# =============================================================================

# --- Remove a file ---
# os.remove("file_to_delete.txt")  # Raises error if doesn't exist

# Safe removal
def safe_remove(filepath):
    """Remove file if it exists"""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed: {filepath}")
    else:
        print(f"File not found: {filepath}")

# --- Remove empty directory ---
# os.rmdir("empty_folder")  # Only works if directory is empty

# --- Remove directory with contents ---
import shutil
# shutil.rmtree("folder_with_contents")  # BE CAREFUL - no undo!

# Safe directory removal
def safe_rmtree(dirpath):
    """Remove directory tree if it exists"""
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)
        print(f"Removed directory: {dirpath}")
    else:
        print(f"Directory not found: {dirpath}")


# =============================================================================
# 8. RENAMING AND MOVING
# =============================================================================

# --- Rename file or directory ---
# os.rename("old_name.txt", "new_name.txt")

# --- Move file (rename with path) ---
# os.rename("file.txt", "subfolder/file.txt")

# --- Safe rename with existence check ---
def safe_rename(src, dst):
    """Rename file with error handling"""
    if not os.path.exists(src):
        print(f"Source not found: {src}")
        return False
    if os.path.exists(dst):
        print(f"Destination exists: {dst}")
        return False
    os.rename(src, dst)
    print(f"Renamed: {src} -> {dst}")
    return True

# --- Replace (overwrites destination if exists) ---
# os.replace("source.txt", "destination.txt")

# --- Using shutil for more options ---
# shutil.move("source.txt", "dest_folder/")  # Move
# shutil.copy("source.txt", "copy.txt")       # Copy
# shutil.copy2("source.txt", "copy.txt")      # Copy with metadata


# =============================================================================
# 9. FILE INFORMATION AND METADATA
# =============================================================================

# --- Get file size ---
file_path = "os.py"  # Use an existing file
if os.path.exists(file_path):
    size_bytes = os.path.getsize(file_path)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    print(f"File size: {size_bytes} bytes ({size_kb:.2f} KB)")

# --- Get modification time ---
if os.path.exists(file_path):
    mtime = os.path.getmtime(file_path)  # Unix timestamp
    modified = datetime.fromtimestamp(mtime)
    print(f"Last modified: {modified}")

# --- Get creation time ---
if os.path.exists(file_path):
    ctime = os.path.getctime(file_path)
    created = datetime.fromtimestamp(ctime)
    print(f"Created: {created}")

# --- Get access time ---
if os.path.exists(file_path):
    atime = os.path.getatime(file_path)
    accessed = datetime.fromtimestamp(atime)
    print(f"Last accessed: {accessed}")

# --- Complete file stats ---
if os.path.exists(file_path):
    stats = os.stat(file_path)
    print(f"\nComplete file stats for {file_path}:")
    print(f"  Size: {stats.st_size} bytes")
    print(f"  Mode: {oct(stats.st_mode)}")
    print(f"  Modified: {datetime.fromtimestamp(stats.st_mtime)}")


# =============================================================================
# 10. WALKING DIRECTORY TREES (os.walk)
# =============================================================================

"""
os.walk() recursively traverses directory trees.
Essential for processing datasets spread across folders!
"""

# --- Basic usage ---
def list_all_files(directory):
    """List all files in directory tree"""
    all_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            all_files.append(filepath)
    return all_files

# --- Find specific file types ---
def find_files_by_extension(directory, extension):
    """Find all files with given extension"""
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(extension):
                filepath = os.path.join(root, filename)
                matching_files.append(filepath)
    return matching_files

# Example: Find all Python files
# python_files = find_files_by_extension(".", ".py")
# print(f"Found {len(python_files)} Python files")

# --- Find all images for ML dataset ---
def find_images(directory):
    """Find all image files in directory"""
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")
    images = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(image_extensions):
                images.append(os.path.join(root, filename))
    return images

# --- Calculate directory size ---
def get_directory_size(directory):
    """Calculate total size of directory"""
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.exists(filepath):
                total_size += os.path.getsize(filepath)
    return total_size

# size = get_directory_size(".")
# print(f"Directory size: {size / (1024*1024):.2f} MB")

# --- Skip certain directories ---
def find_files_skip_dirs(directory, extension, skip_dirs=None):
    """Find files but skip certain directories"""
    if skip_dirs is None:
        skip_dirs = {"__pycache__", ".git", "node_modules", "venv"}
    
    matching = []
    for root, dirs, files in os.walk(directory):
        # Modify dirs in-place to skip directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for filename in files:
            if filename.endswith(extension):
                matching.append(os.path.join(root, filename))
    return matching


# =============================================================================
# 11. EXECUTING SYSTEM COMMANDS
# =============================================================================

"""
os.system() can run shell commands, but subprocess is preferred for new code.
"""

# --- os.system (simple but limited) ---
# exit_code = os.system("ls -la")  # Linux/Mac
# exit_code = os.system("dir")     # Windows

# --- Better: subprocess module ---
import subprocess

# Run command and capture output
# result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
# print(result.stdout)

# --- Get terminal size ---
try:
    terminal_size = os.get_terminal_size()
    print(f"Terminal: {terminal_size.columns}x{terminal_size.lines}")
except OSError:
    print("Not running in terminal")


# =============================================================================
# 12. CROSS-PLATFORM CONSIDERATIONS
# =============================================================================

"""
Write code that works on Windows, Mac, and Linux!
"""

# --- Path separator ---
print(f"Path separator: {os.sep}")
# Output: / (Linux/Mac) or \ (Windows)

# --- Line separator ---
print(f"Line separator: {repr(os.linesep)}")
# Output: \n (Linux/Mac) or \r\n (Windows)

# --- Always use os.path.join ---
# ❌ path = "data/" + filename
# ✅ path = os.path.join("data", filename)

# --- Home directory cross-platform ---
def get_home_directory():
    """Get home directory cross-platform"""
    return os.path.expanduser("~")

print(f"Home: {get_home_directory()}")

# --- Expand user in paths ---
config_path = os.path.expanduser("~/.config/myapp")
print(f"Config path: {config_path}")

# --- Expand environment variables ---
path_with_var = os.path.expandvars("$HOME/data")
print(f"Expanded path: {path_with_var}")


# =============================================================================
# 13. PRACTICAL ML/AI UTILITIES
# =============================================================================

def ensure_dir(directory):
    """Ensure directory exists, create if not"""
    os.makedirs(directory, exist_ok=True)
    return directory


def get_latest_file(directory, pattern="*"):
    """Get most recently modified file in directory"""
    import glob
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def get_unique_filename(filepath):
    """Generate unique filename if file exists"""
    if not os.path.exists(filepath):
        return filepath
    
    base, ext = os.path.splitext(filepath)
    counter = 1
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    return f"{base}_{counter}{ext}"


def clean_old_files(directory, days=30, pattern="*.log"):
    """Remove files older than specified days"""
    import glob
    import time
    
    cutoff = time.time() - (days * 24 * 60 * 60)
    removed = 0
    
    for filepath in glob.glob(os.path.join(directory, pattern)):
        if os.path.getmtime(filepath) < cutoff:
            os.remove(filepath)
            removed += 1
    
    return removed


class ProjectPaths:
    """Manage paths for ML project"""
    
    def __init__(self, base_dir=None):
        if base_dir is None:
            base_dir = os.getcwd()
        self.base = os.path.abspath(base_dir)
        
    @property
    def data(self):
        return ensure_dir(os.path.join(self.base, "data"))
    
    @property
    def raw_data(self):
        return ensure_dir(os.path.join(self.data, "raw"))
    
    @property
    def processed_data(self):
        return ensure_dir(os.path.join(self.data, "processed"))
    
    @property
    def models(self):
        return ensure_dir(os.path.join(self.base, "models"))
    
    @property
    def logs(self):
        return ensure_dir(os.path.join(self.base, "logs"))
    
    @property
    def outputs(self):
        return ensure_dir(os.path.join(self.base, "outputs"))

# Usage:
# paths = ProjectPaths("/path/to/project")
# data_file = os.path.join(paths.raw_data, "dataset.csv")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Directory Navigation
   - os.getcwd(): Get current directory
   - os.chdir(): Change directory
   - os.listdir(): List contents

2. Path Manipulation (ALWAYS use os.path!)
   - os.path.join(): Combine paths (cross-platform)
   - os.path.split(): Split into dir and file
   - os.path.basename(): Get filename
   - os.path.dirname(): Get directory
   - os.path.exists(): Check existence
   - os.path.isfile()/isdir(): Check type

3. Environment Variables
   - os.environ.get("VAR", default): Safe access
   - os.environ["VAR"] = value: Set variable

4. File Operations
   - os.makedirs(path, exist_ok=True): Create directories
   - os.remove(): Delete file
   - os.rename(): Rename/move
   - os.path.getsize(): File size

5. Directory Traversal
   - os.walk(): Recursively traverse directories
   - Perfect for finding datasets/processing files

6. Best Practices
   - Always use os.path.join() for paths
   - Use exist_ok=True with makedirs
   - Handle exceptions for file operations
   - Use expanduser("~") for home directory
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Path Builder [EASY]
# Create paths for a ML project with these directories:
# - data/train, data/test, data/validation
# - models/saved, models/checkpoints
# Use os.path.join and os.makedirs
# TODO: Write your code here

# Solution:
# base = "ml_project"
# dirs = [
#     os.path.join(base, "data", "train"),
#     os.path.join(base, "data", "test"),
#     os.path.join(base, "data", "validation"),
#     os.path.join(base, "models", "saved"),
#     os.path.join(base, "models", "checkpoints")
# ]
# for d in dirs:
#     os.makedirs(d, exist_ok=True)
#     print(f"Created: {d}")


# Exercise 2: Environment Config [EASY]
# Create a function that reads these env vars with defaults:
# - MODEL_PATH (default: "./models")
# - DATA_PATH (default: "./data")
# - LOG_LEVEL (default: "INFO")
# TODO: Write your code here

# Solution:
# def get_config():
#     return {
#         "model_path": os.environ.get("MODEL_PATH", "./models"),
#         "data_path": os.environ.get("DATA_PATH", "./data"),
#         "log_level": os.environ.get("LOG_LEVEL", "INFO")
#     }
# config = get_config()
# print(config)


# Exercise 3: File Finder [MEDIUM]
# Write function to find all CSV files in a directory tree
# Return list of tuples: (filepath, size_mb, modified_date)
# TODO: Write your code here

# Solution:
# def find_csv_files(directory):
#     csv_files = []
#     for root, dirs, files in os.walk(directory):
#         for f in files:
#             if f.endswith(".csv"):
#                 path = os.path.join(root, f)
#                 size = os.path.getsize(path) / (1024 * 1024)
#                 mtime = datetime.fromtimestamp(os.path.getmtime(path))
#                 csv_files.append((path, round(size, 2), mtime))
#     return csv_files


# Exercise 4: Directory Stats [MEDIUM]
# Write function that returns stats about a directory:
# - Total files, total directories
# - Total size (MB)
# - Largest file (name and size)
# - Most common extension
# TODO: Write your code here

# Solution:
# from collections import Counter
# def directory_stats(path):
#     files, dirs, extensions = [], [], []
#     total_size = 0
#     largest = ("", 0)
#     
#     for root, dirnames, filenames in os.walk(path):
#         dirs.extend(dirnames)
#         for f in filenames:
#             fp = os.path.join(root, f)
#             files.append(fp)
#             size = os.path.getsize(fp)
#             total_size += size
#             if size > largest[1]:
#                 largest = (f, size)
#             _, ext = os.path.splitext(f)
#             if ext:
#                 extensions.append(ext)
#     
#     common_ext = Counter(extensions).most_common(1)
#     return {
#         "total_files": len(files),
#         "total_dirs": len(dirs),
#         "total_size_mb": round(total_size / (1024*1024), 2),
#         "largest_file": largest,
#         "common_extension": common_ext[0] if common_ext else None
#     }


# Exercise 5: Backup Creator [MEDIUM]
# Create function that backs up all .py files from source to backup dir
# Maintain directory structure, add timestamp to backup folder name
# TODO: Write your code here

# Solution:
# import shutil
# def backup_python_files(source, backup_base):
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     backup_dir = os.path.join(backup_base, f"backup_{timestamp}")
#     
#     for root, dirs, files in os.walk(source):
#         for f in files:
#             if f.endswith(".py"):
#                 src_path = os.path.join(root, f)
#                 rel_path = os.path.relpath(src_path, source)
#                 dst_path = os.path.join(backup_dir, rel_path)
#                 os.makedirs(os.path.dirname(dst_path), exist_ok=True)
#                 shutil.copy2(src_path, dst_path)
#     return backup_dir


# Exercise 6: Dataset Organizer [CHALLENGE]
# Given a flat directory of images named "class_001.jpg", "class_002.jpg"
# Organize them into class folders: class/001.jpg, class/002.jpg
# TODO: Write your code here

# Solution:
# def organize_dataset(source_dir, dest_dir):
#     os.makedirs(dest_dir, exist_ok=True)
#     
#     for filename in os.listdir(source_dir):
#         if not filename.endswith(('.jpg', '.png', '.jpeg')):
#             continue
#         
#         name, ext = os.path.splitext(filename)
#         parts = name.rsplit('_', 1)
#         if len(parts) != 2:
#             continue
#         
#         class_name, file_id = parts
#         class_dir = os.path.join(dest_dir, class_name)
#         os.makedirs(class_dir, exist_ok=True)
#         
#         src = os.path.join(source_dir, filename)
#         dst = os.path.join(class_dir, f"{file_id}{ext}")
#         shutil.copy2(src, dst)


# Exercise 7: Smart File Monitor [CHALLENGE]
# Create class that watches a directory and reports:
# - New files added since last check
# - Files modified since last check
# - Files deleted since last check
# TODO: Write your code here

# Solution:
# class DirectoryMonitor:
#     def __init__(self, path):
#         self.path = path
#         self.snapshot = self._get_snapshot()
#     
#     def _get_snapshot(self):
#         snapshot = {}
#         if os.path.exists(self.path):
#             for f in os.listdir(self.path):
#                 fp = os.path.join(self.path, f)
#                 if os.path.isfile(fp):
#                     snapshot[f] = os.path.getmtime(fp)
#         return snapshot
#     
#     def check_changes(self):
#         current = self._get_snapshot()
#         old_files = set(self.snapshot.keys())
#         new_files = set(current.keys())
#         
#         added = new_files - old_files
#         deleted = old_files - new_files
#         modified = {f for f in old_files & new_files 
#                    if current[f] != self.snapshot[f]}
#         
#         self.snapshot = current
#         return {"added": added, "deleted": deleted, "modified": modified}


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. String concatenation for paths
   ❌ path = folder + "/" + filename
   ✅ path = os.path.join(folder, filename)

2. Not handling missing directories
   ❌ os.mkdir("nested/path")  # Fails!
   ✅ os.makedirs("nested/path", exist_ok=True)

3. Assuming working directory
   ❌ open("data.csv")  # Depends on where script runs
   ✅ open(os.path.join(os.path.dirname(__file__), "data.csv"))

4. Hardcoding path separators
   ❌ path = "folder\\file.txt"  # Windows only
   ✅ path = os.path.join("folder", "file.txt")

5. Not checking file existence
   ❌ os.remove("maybe_exists.txt")
   ✅ if os.path.exists("maybe_exists.txt"): os.remove(...)

6. Using os.system for commands
   ❌ os.system("ls -la")  # Limited, insecure
   ✅ subprocess.run(["ls", "-la"], capture_output=True)

7. Forgetting to close files
   ❌ f = open(path); data = f.read()
   ✅ with open(path) as f: data = f.read()

8. Ignoring cross-platform issues
   ❌ path = "C:\\Users\\data"  # Windows only
   ✅ path = os.path.expanduser("~/data")
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("OS MODULE DEMONSTRATION")
    print("="*60)
    
    # Current directory
    print(f"\n1. Current directory: {os.getcwd()}")
    
    # Home directory
    print(f"2. Home directory: {os.path.expanduser('~')}")
    
    # Path joining
    example_path = os.path.join("data", "raw", "file.csv")
    print(f"3. Joined path: {example_path}")
    
    # List Python files
    py_files = [f for f in os.listdir(".") if f.endswith(".py")]
    print(f"4. Python files in current dir: {py_files[:5]}...")
    
    # Environment variable
    print(f"5. PATH exists: {'PATH' in os.environ}")
    
    print("\n" + "="*60)
    print("Run the exercises to practice!")
    print("="*60)