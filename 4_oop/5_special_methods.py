"""
================================================================================
PYTHON OOP: SPECIAL (DUNDER) METHODS
================================================================================
Day: 18

Description:
    Complete guide to Python's special methods (also called magic methods or
    dunder methods). Covers object representation, operator overloading,
    comparison, container emulation, and context managers.

Learning Objectives:
    - Understand what special/dunder methods are
    - Implement __repr__ and __str__ for object representation
    - Overload operators (+, -, *, /, ==, <, etc.)
    - Make objects callable, iterable, and indexable
    - Create context managers with __enter__ and __exit__
    - Apply special methods in ML/AI contexts

Prerequisites:
    - Classes and Instances (Day 15)
    - Inheritance (Day 17)
================================================================================
"""

# =============================================================================
# 1. WHAT ARE SPECIAL METHODS?
# =============================================================================

"""
SPECIAL METHODS (Dunder Methods):
- Methods surrounded by double underscores: __method__
- "Dunder" = Double UNDERscore
- Define how objects behave with built-in functions and operators
- Called implicitly by Python (not directly by you usually)

Examples:
- __init__: Called when creating object
- __str__: Called by str() and print()
- __add__: Called by + operator
- __len__: Called by len()

Why they matter for AI/ML:
- Custom tensor/matrix operations
- Dataset iteration and indexing
- Model comparison and sorting
- Clean API design for ML libraries
"""

# Built-in types use special methods too!
print("=== SPECIAL METHODS IN BUILT-INS ===")
print(f"1 + 2 = {1 + 2}")
print(f"int.__add__(1, 2) = {int.__add__(1, 2)}")  # Same thing!

print(f"\n'a' + 'b' = {'a' + 'b'}")
print(f"str.__add__('a', 'b') = {str.__add__('a', 'b')}")  # Same thing!

print(f"\nlen('hello') = {len('hello')}")
print(f"'hello'.__len__() = {'hello'.__len__()}")  # Same thing!


# =============================================================================
# 2. OBJECT REPRESENTATION: __repr__ AND __str__
# =============================================================================

"""
__repr__: Official/unambiguous representation (for developers)
- Goal: Ideally eval(repr(obj)) should recreate the object
- Used by: repr(), interactive interpreter, debugging
- Fallback for __str__ if not defined

__str__: Informal/readable representation (for users)
- Goal: Human-friendly output
- Used by: str(), print()
"""

class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first.lower()}.{last.lower()}@email.com"
        self.pay = pay
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self):
        """Developer-friendly representation"""
        # Goal: Could copy-paste to recreate object
        return f"Employee('{self.first}', '{self.last}', {self.pay})"
    
    def __str__(self):
        """User-friendly representation"""
        return f"{self.fullname()} - {self.email}"


print("\n=== __repr__ AND __str__ ===")

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# __repr__ - for developers
print(f"repr(emp_1): {repr(emp_1)}")
print(f"emp_1.__repr__(): {emp_1.__repr__()}")

# __str__ - for users
print(f"\nstr(emp_1): {str(emp_1)}")
print(f"emp_1.__str__(): {emp_1.__str__()}")

# print() uses __str__, falls back to __repr__
print(f"\nprint(emp_1): {emp_1}")

# In interactive interpreter, __repr__ is shown
# >>> emp_1
# Employee('Corey', 'Schafer', 50000)


# =============================================================================
# 3. ARITHMETIC OPERATORS
# =============================================================================

"""
Operator    Method              Reverse Method
+           __add__             __radd__
-           __sub__             __rsub__
*           __mul__             __rmul__
/           __truediv__         __rtruediv__
//          __floordiv__        __rfloordiv__
%           __mod__             __rmod__
**          __pow__             __rpow__
@           __matmul__          __rmatmul__

In-place operators (+=, -=, etc.):
+=          __iadd__
-=          __isub__
*=          __imul__
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"
    
    def __add__(self, other):
        """Add salaries when adding two employees"""
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented
    
    def __mul__(self, other):
        """Multiply salary by a number"""
        if isinstance(other, (int, float)):
            return self.pay * other
        return NotImplemented
    
    def __rmul__(self, other):
        """Handle number * employee"""
        return self.__mul__(other)


print("\n=== ARITHMETIC OPERATORS ===")

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Using __add__
print(f"emp_1 + emp_2 = {emp_1 + emp_2}")  # Combined salary: 110000

# Using __mul__
print(f"emp_1 * 2 = {emp_1 * 2}")  # Double salary: 100000
print(f"2 * emp_1 = {2 * emp_1}")  # Uses __rmul__


# --- Vector Example (more practical) ---
class Vector:
    """2D Vector with operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Scalar multiplication"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def __neg__(self):
        """Unary negation: -v"""
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        """Magnitude: abs(v)"""
        return (self.x**2 + self.y**2) ** 0.5
    
    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y


print("\n=== VECTOR OPERATIONS ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"-v1 = {-v1}")
print(f"abs(v1) = {abs(v1)}")  # Magnitude: 5.0


# =============================================================================
# 4. COMPARISON OPERATORS
# =============================================================================

"""
Operator    Method
==          __eq__
!=          __ne__
<           __lt__
<=          __le__
>           __gt__
>=          __ge__

Note: If you define __eq__, also define __hash__ for hashability
      (or set __hash__ = None to make unhashable)
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"
    
    def __eq__(self, other):
        """Equal if same name and pay"""
        if isinstance(other, Employee):
            return (self.first == other.first and 
                    self.last == other.last and 
                    self.pay == other.pay)
        return NotImplemented
    
    def __lt__(self, other):
        """Less than based on pay"""
        if isinstance(other, Employee):
            return self.pay < other.pay
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Employee):
            return self.pay <= other.pay
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.pay > other.pay
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Employee):
            return self.pay >= other.pay
        return NotImplemented
    
    def __hash__(self):
        """Make hashable (for use in sets/dicts)"""
        return hash((self.first, self.last, self.pay))


print("\n=== COMPARISON OPERATORS ===")

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
emp_3 = Employee('Corey', 'Schafer', 50000)

print(f"emp_1 == emp_3: {emp_1 == emp_3}")  # True (same values)
print(f"emp_1 == emp_2: {emp_1 == emp_2}")  # False
print(f"emp_1 < emp_2: {emp_1 < emp_2}")    # True (50000 < 60000)
print(f"emp_1 > emp_2: {emp_1 > emp_2}")    # False

# Can now sort employees!
employees = [emp_2, emp_1, Employee('Alice', 'Jones', 55000)]
sorted_emps = sorted(employees)
print(f"\nSorted by pay: {sorted_emps}")


# =============================================================================
# 5. LEN AND OTHER BUILT-INS
# =============================================================================

"""
__len__     len(obj)
__bool__    bool(obj), if obj:
__hash__    hash(obj)
__call__    obj()
__contains__ item in obj
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"
    
    def __len__(self):
        """Length of full name"""
        return len(self.fullname())
    
    def __bool__(self):
        """Employee is 'truthy' if they have positive pay"""
        return self.pay > 0


print("\n=== __len__ AND __bool__ ===")

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Unpaid', 'Intern', 0)

print(f"len(emp_1) = {len(emp_1)}")  # Length of 'Corey Schafer' = 13

print(f"bool(emp_1) = {bool(emp_1)}")  # True (pay > 0)
print(f"bool(emp_2) = {bool(emp_2)}")  # False (pay = 0)

# In conditionals
if emp_1:
    print("emp_1 has pay!")
if not emp_2:
    print("emp_2 has no pay!")


# =============================================================================
# 6. MAKING OBJECTS CALLABLE: __call__
# =============================================================================

"""
__call__ makes instances callable like functions.
Useful for:
- Function-like objects with state
- Neural network layers (forward pass)
- Decorators as classes
"""

class Counter:
    """Callable counter object"""
    def __init__(self, start=0):
        self.count = start
    
    def __call__(self, increment=1):
        """Called when instance is used as function"""
        self.count += increment
        return self.count
    
    def __repr__(self):
        return f"Counter({self.count})"


print("\n=== __call__ (Callable Objects) ===")

counter = Counter(10)
print(f"Initial: {counter}")

# Call the object like a function!
print(f"counter() = {counter()}")      # 11
print(f"counter() = {counter()}")      # 12
print(f"counter(5) = {counter(5)}")    # 17
print(f"Final: {counter}")


# --- Neural Network Layer Example ---
class DenseLayer:
    """Simple dense layer - callable for forward pass"""
    
    def __init__(self, input_size, output_size, activation='relu'):
        self.input_size = input_size
        self.output_size = output_size
        self.activation = activation
        # Simulated weights
        self.weights = [[0.1] * output_size for _ in range(input_size)]
        self.bias = [0.0] * output_size
    
    def __call__(self, inputs):
        """Forward pass - called like layer(x)"""
        outputs = []
        for j in range(self.output_size):
            value = sum(inputs[i] * self.weights[i][j] for i in range(self.input_size))
            value += self.bias[j]
            # Apply activation
            if self.activation == 'relu':
                value = max(0, value)
            outputs.append(value)
        return outputs
    
    def __repr__(self):
        return f"DenseLayer({self.input_size}, {self.output_size}, '{self.activation}')"


layer = DenseLayer(3, 2)
print(f"\n{layer}")
print(f"layer([1, 2, 3]) = {layer([1, 2, 3])}")  # Call like function!


# =============================================================================
# 7. CONTAINER METHODS: __getitem__, __setitem__, __iter__
# =============================================================================

"""
__getitem__     obj[key]
__setitem__     obj[key] = value
__delitem__     del obj[key]
__iter__        iter(obj), for x in obj
__next__        next(obj)
__contains__    item in obj
"""

class DataBatch:
    """Custom container with indexing and iteration"""
    
    def __init__(self, data):
        self._data = list(data)
    
    def __repr__(self):
        return f"DataBatch({self._data})"
    
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        """Enable indexing: batch[0], batch[1:3]"""
        return self._data[index]
    
    def __setitem__(self, index, value):
        """Enable assignment: batch[0] = value"""
        self._data[index] = value
    
    def __delitem__(self, index):
        """Enable deletion: del batch[0]"""
        del self._data[index]
    
    def __iter__(self):
        """Enable iteration: for item in batch"""
        return iter(self._data)
    
    def __contains__(self, item):
        """Enable 'in' operator: item in batch"""
        return item in self._data


print("\n=== CONTAINER METHODS ===")

batch = DataBatch([10, 20, 30, 40, 50])

print(f"batch = {batch}")
print(f"len(batch) = {len(batch)}")
print(f"batch[0] = {batch[0]}")
print(f"batch[1:3] = {batch[1:3]}")  # Slicing works!
print(f"30 in batch: {30 in batch}")

# Iteration
print("Iterating:", end=" ")
for item in batch:
    print(item, end=" ")
print()

# Modification
batch[0] = 100
print(f"After batch[0] = 100: {batch}")


# =============================================================================
# 8. CONTEXT MANAGERS: __enter__ AND __exit__
# =============================================================================

"""
Context managers handle setup/cleanup with 'with' statement.
__enter__: Called when entering 'with' block
__exit__: Called when exiting 'with' block (even on exception!)
"""

class FileManager:
    """Custom file manager context manager"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Open file and return it"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close file (always called, even on exception)"""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        # Return True to suppress exceptions
        return False


print("\n=== CONTEXT MANAGERS ===")

# with FileManager('test.txt', 'w') as f:
#     f.write('Hello, World!')
# File automatically closed!


class Timer:
    """Context manager for timing code blocks"""
    
    def __init__(self, name="Timer"):
        self.name = name
        self.start = None
        self.elapsed = None
    
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, *args):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"{self.name}: {self.elapsed:.4f} seconds")
        return False

# Usage:
with Timer("Sum calculation"):
    total = sum(range(1000000))
print(f"Total: {total}")


# =============================================================================
# 9. ATTRIBUTE ACCESS: __getattr__, __setattr__, __delattr__
# =============================================================================

"""
__getattr__:    Called when attribute not found normally
__setattr__:    Called on every attribute assignment
__delattr__:    Called on attribute deletion
__getattribute__: Called on EVERY attribute access (use carefully!)
"""

class FlexibleObject:
    """Object that returns default for missing attributes"""
    
    def __init__(self):
        self._data = {}
    
    def __getattr__(self, name):
        """Called when attribute not found"""
        print(f"Accessing missing attribute: {name}")
        return self._data.get(name, None)
    
    def __setattr__(self, name, value):
        """Called on every attribute assignment"""
        if name.startswith('_'):
            # Use object's __setattr__ for private attrs
            object.__setattr__(self, name, value)
        else:
            print(f"Setting {name} = {value}")
            self._data[name] = value


print("\n=== ATTRIBUTE ACCESS ===")

obj = FlexibleObject()
obj.name = "Test"  # Calls __setattr__
obj.value = 42     # Calls __setattr__

print(f"obj.name = {obj.name}")
print(f"obj.missing = {obj.missing}")  # Calls __getattr__


# =============================================================================
# 10. ML/AI PRACTICAL EXAMPLES
# =============================================================================

class Tensor:
    """Simple tensor class with operator overloading"""
    
    def __init__(self, data, requires_grad=False):
        self.data = data if isinstance(data, list) else [data]
        self.requires_grad = requires_grad
        self.grad = None
        self.shape = self._get_shape(self.data)
    
    def _get_shape(self, data):
        if not isinstance(data, list):
            return ()
        if not data:
            return (0,)
        return (len(data),) + self._get_shape(data[0])
    
    def __repr__(self):
        return f"Tensor({self.data}, shape={self.shape})"
    
    def __add__(self, other):
        if isinstance(other, Tensor):
            result = [a + b for a, b in zip(self.data, other.data)]
        else:
            result = [x + other for x in self.data]
        return Tensor(result)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, Tensor):
            result = [a * b for a, b in zip(self.data, other.data)]
        else:
            result = [x * other for x in self.data]
        return Tensor(result)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __neg__(self):
        return Tensor([-x for x in self.data])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def mean(self):
        return self.sum() / len(self)


print("\n=== TENSOR CLASS ===")

t1 = Tensor([1, 2, 3, 4])
t2 = Tensor([5, 6, 7, 8])

print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t1 + t2 = {t1 + t2}")
print(f"t1 * 2 = {t1 * 2}")
print(f"t1 * t2 = {t1 * t2}")
print(f"t1[0] = {t1[0]}")
print(f"t1.sum() = {t1.sum()}")
print(f"t1.mean() = {t1.mean()}")


class Model:
    """ML Model with special methods"""
    
    def __init__(self, name, layers=None):
        self.name = name
        self.layers = layers or []
        self.is_trained = False
    
    def __repr__(self):
        return f"Model('{self.name}', layers={len(self.layers)})"
    
    def __call__(self, X):
        """Forward pass - model(X)"""
        output = X
        for layer in self.layers:
            output = layer(output)
        return output
    
    def __len__(self):
        """Number of layers"""
        return len(self.layers)
    
    def __getitem__(self, index):
        """Get layer by index"""
        return self.layers[index]
    
    def __iter__(self):
        """Iterate over layers"""
        return iter(self.layers)
    
    def __bool__(self):
        """True if model has layers"""
        return len(self.layers) > 0


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Object Representation
   - __repr__: Unambiguous, for developers (eval-able if possible)
   - __str__: Readable, for users

2. Operator Overloading
   - Arithmetic: __add__, __sub__, __mul__, __truediv__
   - Comparison: __eq__, __lt__, __gt__, __le__, __ge__
   - Unary: __neg__, __abs__, __pos__

3. Container Emulation
   - __len__: len(obj)
   - __getitem__: obj[key]
   - __setitem__: obj[key] = value
   - __iter__: for x in obj
   - __contains__: x in obj

4. Callable Objects
   - __call__: obj() - makes instances callable

5. Context Managers
   - __enter__: Setup (return value used in 'as')
   - __exit__: Cleanup (always runs)

6. Best Practices
   - Always implement __repr__
   - Return NotImplemented for unsupported operations
   - Be consistent (if __eq__, consider __hash__)
   - Don't overuse (only when it makes sense)
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Money Class [EASY]
# Create Money class with amount and currency
# Implement __repr__, __str__, __add__, __eq__
# TODO: Write your code here

# Solution:
# class Money:
#     def __init__(self, amount, currency='USD'):
#         self.amount = amount
#         self.currency = currency
#     def __repr__(self):
#         return f"Money({self.amount}, '{self.currency}')"
#     def __str__(self):
#         return f"${self.amount:.2f} {self.currency}"
#     def __add__(self, other):
#         if isinstance(other, Money) and self.currency == other.currency:
#             return Money(self.amount + other.amount, self.currency)
#         return NotImplemented
#     def __eq__(self, other):
#         if isinstance(other, Money):
#             return self.amount == other.amount and self.currency == other.currency
#         return NotImplemented


# Exercise 2: Polynomial Class [MEDIUM]
# Implement polynomial with coefficients
# __repr__, __str__, __add__, __call__ (evaluate), __eq__
# TODO: Write your code here

# Solution:
# class Polynomial:
#     def __init__(self, coefficients):
#         self.coeffs = coefficients
#     def __repr__(self):
#         return f"Polynomial({self.coeffs})"
#     def __call__(self, x):
#         return sum(c * x**i for i, c in enumerate(self.coeffs))
#     def __add__(self, other):
#         if isinstance(other, Polynomial):
#             max_len = max(len(self.coeffs), len(other.coeffs))
#             c1 = self.coeffs + [0] * (max_len - len(self.coeffs))
#             c2 = other.coeffs + [0] * (max_len - len(other.coeffs))
#             return Polynomial([a + b for a, b in zip(c1, c2)])
#         return NotImplemented


# Exercise 3: Matrix Class [CHALLENGE]
# 2D Matrix with __add__, __mul__ (scalar and matrix), __getitem__
# TODO: Write your code here


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting to return NotImplemented
   ❌ def __add__(self, other): return self.x + other.x
   ✅ def __add__(self, other):
          if isinstance(other, MyClass): return ...
          return NotImplemented

2. Implementing __eq__ without __hash__
   - Makes object unhashable (can't use in sets/dicts)
   ✅ Set __hash__ = None explicitly if mutable

3. Confusing __repr__ and __str__
   - __repr__: For developers, unambiguous
   - __str__: For users, readable

4. Forgetting reverse operators
   - 2 * obj fails if only __mul__ defined
   ✅ Also define __rmul__

5. Infinite recursion in __setattr__
   ❌ def __setattr__(self, name, value): self.name = value
   ✅ def __setattr__(self, name, value): object.__setattr__(self, name, value)
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("SPECIAL METHODS DEMONSTRATION")
    print("="*60)
    
    class Employee:
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
        def fullname(self):
            return f"{self.first} {self.last}"
        def __repr__(self):
            return f"Employee('{self.first}', '{self.last}', {self.pay})"
        def __str__(self):
            return f"{self.fullname()} - ${self.pay:,}"
        def __add__(self, other):
            return self.pay + other.pay
        def __len__(self):
            return len(self.fullname())
    
    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'Employee', 60000)
    
    print(f"\n1. __repr__: {repr(emp_1)}")
    print(f"2. __str__: {str(emp_1)}")
    print(f"3. emp_1 + emp_2: {emp_1 + emp_2}")
    print(f"4. len(emp_1): {len(emp_1)}")
    
    print("\n" + "="*60)