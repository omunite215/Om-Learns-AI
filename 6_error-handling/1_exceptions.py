"""
================================================================================
PYTHON FUNDAMENTALS: ERROR HANDLING & EXCEPTIONS
================================================================================
Day: 13

Description:
    Complete guide to error handling in Python using exceptions. Covers
    try/except blocks, exception hierarchy, raising exceptions, custom
    exceptions, and best practices for robust ML/AI applications.

Learning Objectives:
    - Understand what exceptions are and why they matter
    - Handle errors gracefully with try/except/else/finally
    - Catch specific vs general exceptions
    - Raise and re-raise exceptions appropriately
    - Create custom exception classes
    - Apply error handling patterns in ML/AI workflows

Prerequisites:
    - Basic Python syntax
    - Functions and classes
    - File handling (Day 12)
================================================================================
"""

import os
import sys

# =============================================================================
# 1. WHAT ARE EXCEPTIONS?
# =============================================================================

"""
EXCEPTIONS are events that disrupt the normal flow of a program.

Why proper error handling matters for AI/ML:
- Training runs can take hours/days - crashes waste resources
- Data pipelines must handle corrupt/missing files gracefully
- API calls and network operations can fail
- GPU memory errors need proper cleanup
- Models should fail gracefully in production

Types of errors:
1. Syntax Errors: Code won't run (caught before execution)
2. Exceptions: Runtime errors (caught during execution)

Exception vs Error:
- All errors are exceptions in Python
- "Error" suffix = serious issues (MemoryError, SystemError)
- "Exception" suffix = recoverable issues (ValueError, KeyError)
"""

# --- What happens without handling ---
# print(1/0)  # ZeroDivisionError: division by zero
# print(int("hello"))  # ValueError: invalid literal
# print(undefined_var)  # NameError: name not defined

# Program crashes and stops execution!


# =============================================================================
# 2. BASIC TRY/EXCEPT
# =============================================================================

# --- Simple exception handling ---
try:
    result = 10 / 0
except:
    print("An error occurred!")
# Output: An error occurred!
# Program continues running!

# --- Catch specific exception type ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# --- Access exception information ---
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print(f"Error args: {e.args}")

# --- Your original example enhanced ---
try:
    f = open("no_file.txt")
except FileNotFoundError as e:
    print("Sorry Bro!! File not found!!")
    print(f"Details: {e}")
except Exception as e:
    print("Something went wrong!!")
    print(f"Error: {e}")


# =============================================================================
# 3. MULTIPLE EXCEPT BLOCKS
# =============================================================================

"""
Order matters! Python checks from top to bottom.
Put specific exceptions BEFORE general ones.
"""

def divide_from_input():
    """Demonstrate multiple exception handling"""
    try:
        num1 = int(input("Enter first number: ") or "10")
        num2 = int(input("Enter second number: ") or "0")
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Unexpected error: {e}")

# --- Catch multiple exceptions in one block ---
try:
    # Some risky operation
    value = int("hello")
except (ValueError, TypeError) as e:
    print(f"Value or Type error: {e}")

# --- Different handling for each ---
def process_data(data):
    try:
        result = data['value'] / data['divisor']
        return result
    except KeyError as e:
        print(f"Missing key: {e}")
        return None
    except TypeError:
        print("Invalid data types")
        return None
    except ZeroDivisionError:
        print("Divisor cannot be zero")
        return float('inf')


# =============================================================================
# 4. ELSE AND FINALLY CLAUSES
# =============================================================================

"""
Complete try structure:
try:
    # Code that might raise exception
except ExceptionType:
    # Handle exception
else:
    # Runs ONLY if no exception occurred
finally:
    # ALWAYS runs (cleanup code)
"""

# --- else clause ---
def read_file_safely(filepath):
    """else runs only when try succeeds"""
    try:
        f = open(filepath, 'r')
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    else:
        # Only runs if open() succeeded
        content = f.read()
        f.close()
        print("File read successfully!")
        return content

# --- finally clause ---
def read_with_finally(filepath):
    """finally ALWAYS runs - perfect for cleanup"""
    f = None
    try:
        f = open(filepath, 'r')
        content = f.read()
        return content
    except FileNotFoundError:
        print("File not found!")
        return None
    finally:
        # Always executes - even if return happens!
        if f:
            f.close()
            print("File closed in finally block")
        print("Cleanup complete")

# --- Complete example (from your code) ---
try:
    f = open("test_file.txt", 'w')
    f.write("Test content")
except IOError as e:
    print(f"IO Error: {e}")
else:
    print("Write successful!")
    print(f.read() if f.readable() else "File not readable in write mode")
finally:
    if 'f' in dir() and not f.closed:
        f.close()
    print("Operation completed...")
    # Clean up test file
    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")

# --- finally with return ---
def test_finally_return():
    """finally runs even when returning"""
    try:
        return "try"
    finally:
        print("finally executed!")  # Still prints!

# result = test_finally_return()  # Prints "finally executed!"


# =============================================================================
# 5. EXCEPTION HIERARCHY
# =============================================================================

"""
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   ├── TimeoutError
    │   └── ConnectionError
    ├── RuntimeError
    │   └── RecursionError
    ├── TypeError
    └── ValueError
        └── UnicodeError

IMPORTANT:
- Catch specific exceptions first
- Catching 'Exception' catches most errors
- Avoid catching 'BaseException' (includes SystemExit, KeyboardInterrupt)
"""

# --- Why order matters ---
try:
    d = {}
    value = d['key']
except LookupError:
    print("LookupError caught")  # This catches KeyError too!
except KeyError:
    print("KeyError caught")  # Never reached!

# --- Better approach ---
try:
    d = {}
    value = d['key']
except KeyError:
    print("KeyError caught")  # Specific first
except LookupError:
    print("Other LookupError caught")


# =============================================================================
# 6. RAISING EXCEPTIONS
# =============================================================================

"""
raise - Explicitly throw an exception
Use when:
- Input validation fails
- Preconditions not met
- Signaling error conditions
"""

# --- Raise built-in exceptions ---
def validate_age(age):
    """Raise exception for invalid age"""
    if not isinstance(age, (int, float)):
        raise TypeError(f"Age must be a number, got {type(age).__name__}")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

# Test
try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# --- Raise with custom message ---
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Custom message: Division by zero not allowed!")
    return a / b

# --- Re-raise exception (after logging, etc.) ---
def process_with_logging(data):
    try:
        result = risky_operation(data)
    except Exception as e:
        print(f"Logging error: {e}")  # Log it
        raise  # Re-raise the same exception

# --- Raise different exception ---
def get_config_value(config, key):
    try:
        return config[key]
    except KeyError:
        raise ValueError(f"Required config key missing: {key}")


# =============================================================================
# 7. EXCEPTION CHAINING
# =============================================================================

"""
Python 3 supports exception chaining:
- raise ... from e: Explicit chaining
- raise ... from None: Suppress original
"""

# --- Explicit chaining (raise from) ---
def load_config(filepath):
    try:
        with open(filepath, 'r') as f:
            import json
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file missing: {filepath}") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in config") from e

# --- Suppress original exception ---
def get_value(data, key):
    try:
        return data[key]
    except KeyError:
        raise ValueError(f"Key '{key}' not found") from None

# --- Access chained exceptions ---
try:
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Math failed") from e
except ValueError as e:
    print(f"Caught: {e}")
    print(f"Caused by: {e.__cause__}")


# =============================================================================
# 8. CUSTOM EXCEPTIONS
# =============================================================================

"""
Create custom exceptions for:
- Domain-specific errors
- Better error categorization
- Cleaner API design
"""

# --- Simple custom exception ---
class ValidationError(Exception):
    """Raised when validation fails"""
    pass

# --- Custom exception with attributes ---
class ModelTrainingError(Exception):
    """Raised when model training fails"""
    
    def __init__(self, message, epoch=None, loss=None):
        self.message = message
        self.epoch = epoch
        self.loss = loss
        super().__init__(self.message)
    
    def __str__(self):
        details = [self.message]
        if self.epoch is not None:
            details.append(f"epoch={self.epoch}")
        if self.loss is not None:
            details.append(f"loss={self.loss:.4f}")
        return " | ".join(details)

# Usage
try:
    raise ModelTrainingError("Loss exploded", epoch=42, loss=float('inf'))
except ModelTrainingError as e:
    print(f"Training failed: {e}")
    print(f"Failed at epoch: {e.epoch}")

# --- Exception hierarchy for ML project ---
class MLPipelineError(Exception):
    """Base exception for ML pipeline"""
    pass

class DataLoadError(MLPipelineError):
    """Error loading data"""
    pass

class PreprocessingError(MLPipelineError):
    """Error in data preprocessing"""
    pass

class TrainingError(MLPipelineError):
    """Error during training"""
    pass

class InferenceError(MLPipelineError):
    """Error during inference"""
    pass

# Now you can catch all pipeline errors or specific ones
def run_pipeline():
    try:
        # pipeline code
        pass
    except DataLoadError:
        print("Failed to load data")
    except MLPipelineError:
        print("Pipeline failed")


# =============================================================================
# 9. ASSERTIONS
# =============================================================================

"""
assert - Debug-time checks
- Disabled with python -O (optimized mode)
- Use for "this should NEVER happen" conditions
- NOT for user input validation!
"""

# --- Basic assertion ---
def calculate_mean(numbers):
    assert len(numbers) > 0, "Cannot calculate mean of empty list"
    return sum(numbers) / len(numbers)

# --- Assertion with message ---
def set_learning_rate(lr):
    assert 0 < lr < 1, f"Learning rate must be between 0 and 1, got {lr}"
    return lr

# --- When to use assert vs raise ---
"""
assert: Internal consistency checks (developer errors)
raise: Runtime errors, user input validation (user errors)

❌ assert user_input > 0  # User can trigger this!
✅ if user_input <= 0: raise ValueError("Must be positive")

✅ assert self._initialized  # Internal state check
"""


# =============================================================================
# 10. CONTEXT MANAGERS FOR ERROR HANDLING
# =============================================================================

"""
Context managers (with statement) provide:
- Automatic setup and cleanup
- Exception handling built-in
- Resource management
"""

# --- File handling (safe even on error) ---
with open("test.txt", 'w') as f:
    f.write("test")
# File closed automatically, even if error occurs!

# Clean up
os.remove("test.txt")

# --- Custom context manager ---
class ErrorLogger:
    """Log exceptions that occur in context"""
    
    def __init__(self, log_file):
        self.log_file = log_file
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            with open(self.log_file, 'a') as f:
                f.write(f"{exc_type.__name__}: {exc_val}\n")
        return False  # Don't suppress exception

# Usage:
# with ErrorLogger("errors.log"):
#     risky_operation()

# --- Using contextlib ---
from contextlib import contextmanager

@contextmanager
def timer(name):
    """Context manager for timing code blocks"""
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name}: {elapsed:.4f} seconds")

# Usage:
# with timer("Training"):
#     train_model()

# --- Suppress specific exceptions ---
from contextlib import suppress

# Instead of:
try:
    os.remove("maybe_exists.txt")
except FileNotFoundError:
    pass

# Use:
with suppress(FileNotFoundError):
    os.remove("maybe_exists.txt")


# =============================================================================
# 11. COMMON EXCEPTIONS REFERENCE
# =============================================================================

"""
MOST COMMON EXCEPTIONS IN PYTHON:

ValueError
    - Wrong value type/range
    - int("hello"), list.remove(not_in_list)

TypeError  
    - Wrong type for operation
    - "hello" + 5, len(42)

KeyError
    - Dictionary key not found
    - d = {}; d['missing']

IndexError
    - List index out of range
    - lst = [1,2,3]; lst[10]

AttributeError
    - Object doesn't have attribute
    - "hello".nonexistent()

NameError
    - Variable not defined
    - print(undefined_variable)

FileNotFoundError
    - File doesn't exist
    - open("nonexistent.txt")

PermissionError
    - No permission to access file
    - open("/root/secret.txt")

ImportError / ModuleNotFoundError
    - Module not found
    - import nonexistent_module

ZeroDivisionError
    - Division by zero
    - 10 / 0

MemoryError
    - Out of memory
    - [0] * (10 ** 12)

RecursionError
    - Max recursion depth exceeded
    - def f(): f(); f()

StopIteration
    - Iterator exhausted
    - next(iter([]))

AssertionError
    - Assert statement failed
    - assert False

TimeoutError
    - Operation timed out
    - Network/API calls

ConnectionError
    - Network connection failed
    - API/database connections
"""


# =============================================================================
# 12. PRACTICAL ML/AI ERROR HANDLING
# =============================================================================

def safe_import(module_name, package_name=None):
    """Safely import module with helpful error message"""
    try:
        return __import__(module_name)
    except ImportError:
        pkg = package_name or module_name
        print(f"Module '{module_name}' not found.")
        print(f"Install with: pip install {pkg}")
        return None


def load_data_safely(filepath, loader_func):
    """Load data with comprehensive error handling"""
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Data file not found: {filepath}")
        
        data = loader_func(filepath)
        
        if data is None or len(data) == 0:
            raise ValueError("Loaded data is empty")
        
        return data
    
    except FileNotFoundError as e:
        print(f"[ERROR] {e}")
        return None
    except PermissionError:
        print(f"[ERROR] No permission to read: {filepath}")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")
        return None


class TrainingCheckpoint:
    """Save training state for recovery"""
    
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(checkpoint_dir, exist_ok=True)
    
    def save(self, epoch, model_state, optimizer_state, loss):
        """Save checkpoint"""
        import json
        checkpoint = {
            'epoch': epoch,
            'loss': loss,
            'model_state': str(model_state),  # Simplified
            'optimizer_state': str(optimizer_state)
        }
        path = os.path.join(self.checkpoint_dir, f'checkpoint_epoch_{epoch}.json')
        with open(path, 'w') as f:
            json.dump(checkpoint, f)
        return path
    
    def load_latest(self):
        """Load most recent checkpoint"""
        import glob
        import json
        checkpoints = glob.glob(os.path.join(self.checkpoint_dir, 'checkpoint_*.json'))
        if not checkpoints:
            return None
        latest = max(checkpoints, key=os.path.getmtime)
        with open(latest, 'r') as f:
            return json.load(f)


def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """Decorator to retry failed operations"""
    import time
    from functools import wraps
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    print(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

# Usage:
# @retry(max_attempts=3, delay=2, exceptions=(ConnectionError,))
# def fetch_data_from_api():
#     ...


class GracefulTrainer:
    """Training loop with error handling"""
    
    def __init__(self, model, data, epochs):
        self.model = model
        self.data = data
        self.epochs = epochs
        self.best_loss = float('inf')
    
    def train(self):
        """Train with graceful error handling"""
        try:
            for epoch in range(self.epochs):
                try:
                    loss = self._train_epoch(epoch)
                    self._save_if_best(epoch, loss)
                except MemoryError:
                    print(f"OOM at epoch {epoch}, reducing batch size")
                    self._reduce_batch_size()
                except KeyboardInterrupt:
                    print(f"\nTraining interrupted at epoch {epoch}")
                    self._save_checkpoint(epoch, "interrupted")
                    break
        except Exception as e:
            print(f"Training failed: {e}")
            self._save_checkpoint(0, "failed")
            raise
        finally:
            self._cleanup()
    
    def _train_epoch(self, epoch):
        # Simulated training
        return 0.5
    
    def _save_if_best(self, epoch, loss):
        if loss < self.best_loss:
            self.best_loss = loss
            print(f"New best: {loss:.4f}")
    
    def _save_checkpoint(self, epoch, status):
        print(f"Saving checkpoint: epoch={epoch}, status={status}")
    
    def _reduce_batch_size(self):
        print("Reducing batch size...")
    
    def _cleanup(self):
        print("Cleaning up resources...")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Try/Except Structure
   try:
       risky_code()
   except SpecificError:
       handle_specific()
   except Exception as e:
       handle_general(e)
   else:
       on_success()
   finally:
       always_cleanup()

2. Exception Handling Rules
   - Catch specific exceptions first
   - Avoid bare except:
   - Don't catch Exception unless re-raising
   - Use finally for cleanup

3. Raising Exceptions
   - raise ValueError("message")
   - raise CustomError() from original
   - Just 'raise' to re-raise current

4. Custom Exceptions
   - Inherit from Exception
   - Add helpful attributes
   - Create hierarchy for your domain

5. Best Practices
   - Handle errors at appropriate level
   - Log before re-raising
   - Fail fast, fail clearly
   - Provide helpful error messages

6. ML/AI Specific
   - Save checkpoints for recovery
   - Handle OOM gracefully
   - Catch KeyboardInterrupt for early stopping
   - Validate data before training
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Safe Division [EASY]
# Create function that divides two numbers safely
# Return None for invalid operations, log the error
# TODO: Write your code here

# Solution:
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero")
#         return None
#     except TypeError:
#         print("Error: Invalid types for division")
#         return None


# Exercise 2: Input Validator [EASY]
# Create function that validates user input is positive integer
# Raise appropriate exceptions for invalid input
# TODO: Write your code here

# Solution:
# def get_positive_int(prompt):
#     try:
#         value = int(input(prompt))
#         if value <= 0:
#             raise ValueError("Value must be positive")
#         return value
#     except ValueError as e:
#         raise ValueError(f"Invalid input: {e}")


# Exercise 3: File Reader with Retry [MEDIUM]
# Create function that retries reading file up to 3 times
# Handle FileNotFoundError and PermissionError differently
# TODO: Write your code here

# Solution:
# def read_file_retry(filepath, max_retries=3):
#     import time
#     for attempt in range(max_retries):
#         try:
#             with open(filepath, 'r') as f:
#                 return f.read()
#         except FileNotFoundError:
#             raise  # Don't retry - file won't appear
#         except PermissionError:
#             if attempt < max_retries - 1:
#                 print(f"Permission denied, retrying... ({attempt + 1})")
#                 time.sleep(1)
#             else:
#                 raise


# Exercise 4: Custom Exception Hierarchy [MEDIUM]
# Create exception hierarchy for a data processing pipeline:
# - DataPipelineError (base)
# - DataValidationError (with invalid_fields attribute)
# - DataTransformError (with transform_name attribute)
# TODO: Write your code here

# Solution:
# class DataPipelineError(Exception):
#     """Base exception for data pipeline"""
#     pass
# 
# class DataValidationError(DataPipelineError):
#     def __init__(self, message, invalid_fields=None):
#         self.invalid_fields = invalid_fields or []
#         super().__init__(message)
# 
# class DataTransformError(DataPipelineError):
#     def __init__(self, message, transform_name=None):
#         self.transform_name = transform_name
#         super().__init__(message)


# Exercise 5: Robust Config Loader [MEDIUM]
# Load JSON config with defaults for missing keys
# Handle file not found, invalid JSON, missing keys
# TODO: Write your code here

# Solution:
# import json
# def load_config(path, defaults=None):
#     defaults = defaults or {}
#     try:
#         with open(path, 'r') as f:
#             config = json.load(f)
#     except FileNotFoundError:
#         print(f"Config not found, using defaults")
#         return defaults.copy()
#     except json.JSONDecodeError as e:
#         raise ValueError(f"Invalid JSON in config: {e}")
#     
#     # Merge with defaults
#     result = defaults.copy()
#     result.update(config)
#     return result


# Exercise 6: Exception Logger Decorator [CHALLENGE]
# Create decorator that logs all exceptions to file
# Include timestamp, function name, args, exception details
# TODO: Write your code here

# Solution:
# from functools import wraps
# from datetime import datetime
# 
# def log_exceptions(log_file):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except Exception as e:
#                 with open(log_file, 'a') as f:
#                     ts = datetime.now().isoformat()
#                     f.write(f"[{ts}] {func.__name__}\n")
#                     f.write(f"  Args: {args}, Kwargs: {kwargs}\n")
#                     f.write(f"  Error: {type(e).__name__}: {e}\n\n")
#                 raise
#         return wrapper
#     return decorator


# Exercise 7: Fault-Tolerant Batch Processor [CHALLENGE]
# Process list of items, continue on individual failures
# Return successful results and list of failures
# TODO: Write your code here

# Solution:
# def process_batch(items, processor_func, max_failures=None):
#     results = []
#     failures = []
#     
#     for i, item in enumerate(items):
#         try:
#             result = processor_func(item)
#             results.append((i, item, result))
#         except Exception as e:
#             failures.append((i, item, str(e)))
#             if max_failures and len(failures) >= max_failures:
#                 print(f"Max failures ({max_failures}) reached, stopping")
#                 break
#     
#     return {
#         'successful': results,
#         'failed': failures,
#         'success_rate': len(results) / len(items) if items else 0
#     }


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Bare except clause
   ❌ except:
   ✅ except Exception as e:

2. Catching too broad
   ❌ except Exception:  # Hides bugs!
   ✅ except (ValueError, KeyError):

3. Silencing exceptions
   ❌ except: pass
   ✅ except Error: log_error(); raise

4. Not using context managers
   ❌ f = open(); try: ... finally: f.close()
   ✅ with open() as f: ...

5. Using assert for validation
   ❌ assert user_input > 0  # Disabled in production!
   ✅ if user_input <= 0: raise ValueError(...)

6. Catching and not re-raising
   ❌ except: print("error")  # Swallows exception
   ✅ except: print("error"); raise

7. Wrong exception order
   ❌ except Exception: ... except ValueError:  # Never reached!
   ✅ except ValueError: ... except Exception:

8. Forgetting exception info
   ❌ except ValueError: print("Error")
   ✅ except ValueError as e: print(f"Error: {e}")

9. Raising strings (Python 2 habit)
   ❌ raise "Something went wrong"
   ✅ raise ValueError("Something went wrong")

10. Not cleaning up resources
    ❌ try: f = open(); process()  # Leak on error!
    ✅ try: f = open(); process() finally: f.close()
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("ERROR HANDLING DEMONSTRATION")
    print("="*60)
    
    # Example 1: Basic exception handling
    print("\n1. Basic exception handling:")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"   Caught: {type(e).__name__}: {e}")
    
    # Example 2: Multiple exceptions
    print("\n2. Multiple exceptions:")
    for value in ["hello", None, 0]:
        try:
            result = 100 / int(value) if value else 100 / value
        except (ValueError, TypeError) as e:
            print(f"   {value}: ValueError/TypeError - {e}")
        except ZeroDivisionError:
            print(f"   {value}: ZeroDivisionError")
    
    # Example 3: Custom exception
    print("\n3. Custom exception:")
    try:
        raise ModelTrainingError("Gradient explosion", epoch=15, loss=1e10)
    except ModelTrainingError as e:
        print(f"   {e}")
    
    # Example 4: else and finally
    print("\n4. else and finally:")
    try:
        x = 1 + 1
    except:
        print("   Error occurred")
    else:
        print("   Success! No errors")
    finally:
        print("   Finally always runs")
    
    # Example 5: Validation
    print("\n5. Validation with raise:")
    try:
        validate_age(-10)
    except ValueError as e:
        print(f"   Validation failed: {e}")
    
    print("\n" + "="*60)
    print("Run the exercises to practice!")
    print("="*60)