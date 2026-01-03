"""
================================================================================
PYTHON OOP: PROPERTY DECORATORS (GETTERS, SETTERS, DELETERS)
================================================================================
Day: 18 (Part 2)

Description:
    Complete guide to Python property decorators. Covers @property for getters,
    @name.setter for setters, @name.deleter for deleters, computed properties,
    validation, and encapsulation patterns for ML/AI applications.

Learning Objectives:
    - Understand why properties are useful
    - Create read-only properties with @property
    - Create settable properties with @name.setter
    - Create deletable properties with @name.deleter
    - Implement validation and computed attributes
    - Apply properties in ML/AI contexts

Prerequisites:
    - Classes and Instances (Day 15)
    - Decorators concept
================================================================================
"""

# =============================================================================
# 1. THE PROBLEM: CHANGING IMPLEMENTATION
# =============================================================================

"""
Consider this scenario:
1. You create a class with public attributes
2. Users access attributes directly: emp.first, emp.last
3. Later, you need to add validation or compute values
4. Problem: Can't change without breaking existing code!

Solution: Properties allow you to add getter/setter logic
while maintaining the same attribute-style access.
"""

# --- The Problem Illustrated ---
class EmployeeBad:
    """Class with potential issue"""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Email computed once at init - what if name changes?
        self.email = f"{first.lower()}.{last.lower()}@email.com"
    
    def fullname(self):
        return f"{self.first} {self.last}"


print("=== THE PROBLEM ===")

emp = EmployeeBad('John', 'Smith')
print(f"Name: {emp.first} {emp.last}")
print(f"Email: {emp.email}")

# What happens when we change the name?
emp.first = 'Jim'
print(f"\nAfter changing first name to 'Jim':")
print(f"Name: {emp.first} {emp.last}")
print(f"Email: {emp.email}")  # Still john.smith@email.com! BUG!

# The email wasn't updated because it was computed once in __init__


# =============================================================================
# 2. THE SOLUTION: @property DECORATOR
# =============================================================================

"""
@property turns a method into a "getter" that's accessed like an attribute.
- No parentheses needed when accessing
- Computed on-the-fly each time
- Can add logic without changing interface
"""

class Employee:
    """Fixed class using @property"""
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Remove email from __init__ - make it a property instead!
    
    @property
    def email(self):
        """Email is computed dynamically"""
        return f"{self.first.lower()}.{self.last.lower()}@email.com"
    
    @property
    def fullname(self):
        """Full name is also a property"""
        return f"{self.first} {self.last}"


print("\n=== @property SOLUTION ===")

emp = Employee('John', 'Smith')
print(f"Name: {emp.fullname}")    # No parentheses!
print(f"Email: {emp.email}")      # No parentheses!

# Now changing the name updates email automatically!
emp.first = 'Jim'
print(f"\nAfter changing first name to 'Jim':")
print(f"Name: {emp.fullname}")    # Jim Smith
print(f"Email: {emp.email}")      # jim.smith@email.com - FIXED!


# =============================================================================
# 3. SETTERS WITH @name.setter
# =============================================================================

"""
@name.setter allows you to set a property value.
The setter method must have the SAME NAME as the property.

IMPORTANT: You must define @property BEFORE @name.setter!
"""

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        """Getter for email"""
        return f"{self.first.lower()}.{self.last.lower()}@email.com"
    
    @property
    def fullname(self):
        """Getter for fullname"""
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        """Setter for fullname - parses and sets first/last"""
        first, last = name.split(' ')
        self.first = first
        self.last = last


print("\n=== @property.setter ===")

emp = Employee('John', 'Smith')
print(f"Initial: {emp.fullname}")
print(f"Email: {emp.email}")

# Use the setter - looks like normal assignment!
emp.fullname = "Om Patel"

print(f"\nAfter emp.fullname = 'Om Patel':")
print(f"First: {emp.first}")      # Om
print(f"Last: {emp.last}")        # Patel
print(f"Fullname: {emp.fullname}") # Om Patel
print(f"Email: {emp.email}")      # om.patel@email.com


# =============================================================================
# 4. DELETERS WITH @name.deleter
# =============================================================================

"""
@name.deleter defines what happens when you use 'del' on a property.
Useful for cleanup or resetting values.
"""

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        if self.first and self.last:
            return f"{self.first.lower()}.{self.last.lower()}@email.com"
        return None
    
    @property
    def fullname(self):
        if self.first and self.last:
            return f"{self.first} {self.last}"
        return None
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        """Called when: del emp.fullname"""
        print("Deleting name!")
        self.first = None
        self.last = None


print("\n=== @property.deleter ===")

emp = Employee('John', 'Smith')
print(f"Before delete: {emp.fullname}")

# Use the deleter
del emp.fullname

print(f"After delete: {emp.fullname}")  # None
print(f"Email: {emp.email}")            # None


# =============================================================================
# 5. VALIDATION WITH SETTERS
# =============================================================================

"""
Setters are perfect for validating data before assignment.
"""

class Employee:
    def __init__(self, first, last, pay):
        # These go through the setters!
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, value):
        if not value or not value.strip():
            raise ValueError("First name cannot be empty")
        self._first = value.strip().title()
    
    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, value):
        if not value or not value.strip():
            raise ValueError("Last name cannot be empty")
        self._last = value.strip().title()
    
    @property
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Pay must be a number")
        if value < 0:
            raise ValueError("Pay cannot be negative")
        self._pay = value
    
    @property
    def email(self):
        return f"{self._first.lower()}.{self._last.lower()}@email.com"
    
    @property
    def fullname(self):
        return f"{self._first} {self._last}"


print("\n=== VALIDATION WITH SETTERS ===")

emp = Employee('  john  ', 'SMITH', 50000)
print(f"Name: {emp.fullname}")  # John Smith (cleaned!)
print(f"Pay: ${emp.pay:,}")

# Valid changes
emp.pay = 60000
print(f"New pay: ${emp.pay:,}")

# Invalid changes
try:
    emp.pay = -1000
except ValueError as e:
    print(f"Error: {e}")

try:
    emp.first = ""
except ValueError as e:
    print(f"Error: {e}")


# =============================================================================
# 6. READ-ONLY PROPERTIES
# =============================================================================

"""
Properties without setters are read-only.
Attempting to set them raises AttributeError.
"""

class Circle:
    """Circle with read-only computed properties"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def diameter(self):
        """Read-only: computed from radius"""
        return self._radius * 2
    
    @property
    def area(self):
        """Read-only: computed from radius"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """Read-only: computed from radius"""
        import math
        return 2 * math.pi * self._radius


print("\n=== READ-ONLY PROPERTIES ===")

circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")

# Can set radius (has setter)
circle.radius = 10
print(f"\nAfter radius = 10:")
print(f"Diameter: {circle.diameter}")  # Automatically updates!
print(f"Area: {circle.area:.2f}")

# Can't set diameter (no setter)
try:
    circle.diameter = 20
except AttributeError as e:
    print(f"\nError setting diameter: {e}")


# =============================================================================
# 7. CACHING EXPENSIVE PROPERTIES
# =============================================================================

"""
For expensive computations, cache the result until invalidated.
"""

class Dataset:
    """Dataset with cached statistics"""
    
    def __init__(self, data):
        self._data = list(data)
        self._stats_cache = None  # Cache for statistics
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = list(value)
        self._stats_cache = None  # Invalidate cache!
    
    @property
    def stats(self):
        """Cached statistics - computed once until data changes"""
        if self._stats_cache is None:
            print("Computing statistics...")  # Only printed once!
            self._stats_cache = {
                'count': len(self._data),
                'sum': sum(self._data),
                'mean': sum(self._data) / len(self._data) if self._data else 0,
                'min': min(self._data) if self._data else None,
                'max': max(self._data) if self._data else None
            }
        return self._stats_cache


print("\n=== CACHED PROPERTIES ===")

ds = Dataset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Stats: {ds.stats}")  # Computes
print(f"Stats again: {ds.stats}")  # Uses cache (no "Computing...")

# Change data - invalidates cache
ds.data = [10, 20, 30]
print(f"\nAfter changing data:")
print(f"Stats: {ds.stats}")  # Recomputes


# =============================================================================
# 8. PROPERTY() FUNCTION (ALTERNATIVE SYNTAX)
# =============================================================================

"""
Properties can also be created using the property() function.
Less common but useful to know.
"""

class Employee:
    def __init__(self, first, last):
        self._first = first
        self._last = last
    
    def get_first(self):
        return self._first
    
    def set_first(self, value):
        self._first = value
    
    def del_first(self):
        self._first = None
    
    # Create property using property() function
    first = property(get_first, set_first, del_first, "First name property")


print("\n=== property() FUNCTION ===")

emp = Employee('John', 'Smith')
print(f"First: {emp.first}")

emp.first = 'Jane'
print(f"After set: {emp.first}")

# Access docstring
print(f"Property doc: {Employee.first.__doc__}")


# =============================================================================
# 9. ML/AI PRACTICAL EXAMPLES
# =============================================================================

class Model:
    """ML Model with property-based state management"""
    
    def __init__(self, name):
        self._name = name
        self._weights = None
        self._is_trained = False
        self._history = {'loss': [], 'accuracy': []}
    
    @property
    def name(self):
        return self._name
    
    @property
    def weights(self):
        return self._weights
    
    @weights.setter
    def weights(self, value):
        self._weights = value
        # Mark as trained when weights are set
        self._is_trained = value is not None
    
    @property
    def is_trained(self):
        """Read-only: derived from weights"""
        return self._weights is not None
    
    @property
    def history(self):
        """Read-only copy of training history"""
        return self._history.copy()
    
    @property
    def num_params(self):
        """Read-only: count parameters"""
        if self._weights is None:
            return 0
        return sum(len(w) if isinstance(w, list) else 1 for w in self._weights)
    
    @property
    def best_accuracy(self):
        """Read-only: best accuracy from history"""
        if not self._history['accuracy']:
            return None
        return max(self._history['accuracy'])
    
    def train(self, X, y, epochs=10):
        """Simulate training"""
        self._weights = [[0.1, 0.2], [0.3, 0.4]]
        for epoch in range(epochs):
            loss = 1.0 / (epoch + 1)
            acc = min(0.5 + epoch * 0.05, 0.99)
            self._history['loss'].append(loss)
            self._history['accuracy'].append(acc)


print("\n=== ML MODEL WITH PROPERTIES ===")

model = Model("Classifier")
print(f"Is trained: {model.is_trained}")  # False
print(f"Num params: {model.num_params}")  # 0

model.train(None, None, epochs=10)
print(f"\nAfter training:")
print(f"Is trained: {model.is_trained}")  # True
print(f"Num params: {model.num_params}")  # 4
print(f"Best accuracy: {model.best_accuracy:.2%}")


class Hyperparameters:
    """Hyperparameters with validation"""
    
    def __init__(self):
        self._learning_rate = 0.01
        self._batch_size = 32
        self._epochs = 100
        self._dropout = 0.0
    
    @property
    def learning_rate(self):
        return self._learning_rate
    
    @learning_rate.setter
    def learning_rate(self, value):
        if not 0 < value < 1:
            raise ValueError("Learning rate must be between 0 and 1")
        self._learning_rate = value
    
    @property
    def batch_size(self):
        return self._batch_size
    
    @batch_size.setter
    def batch_size(self, value):
        if value <= 0 or not isinstance(value, int):
            raise ValueError("Batch size must be positive integer")
        # Recommend power of 2
        if value & (value - 1) != 0:
            print(f"Warning: batch_size {value} is not a power of 2")
        self._batch_size = value
    
    @property
    def epochs(self):
        return self._epochs
    
    @epochs.setter
    def epochs(self, value):
        if value <= 0:
            raise ValueError("Epochs must be positive")
        self._epochs = int(value)
    
    @property
    def dropout(self):
        return self._dropout
    
    @dropout.setter
    def dropout(self, value):
        if not 0 <= value < 1:
            raise ValueError("Dropout must be between 0 and 1")
        self._dropout = value
    
    def __repr__(self):
        return (f"Hyperparameters(lr={self._learning_rate}, "
                f"batch={self._batch_size}, epochs={self._epochs}, "
                f"dropout={self._dropout})")


print("\n=== HYPERPARAMETERS WITH VALIDATION ===")

hp = Hyperparameters()
print(hp)

hp.learning_rate = 0.001
hp.batch_size = 64
hp.dropout = 0.5
print(f"After updates: {hp}")

# Validation in action
try:
    hp.learning_rate = 5.0
except ValueError as e:
    print(f"Error: {e}")

try:
    hp.dropout = -0.1
except ValueError as e:
    print(f"Error: {e}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. @property Decorator
   - Turns method into a "getter"
   - Access like attribute: obj.property (no parentheses)
   - Computed on every access

2. @name.setter Decorator
   - Defines how to set a property
   - Must define @property FIRST!
   - Access like attribute: obj.property = value

3. @name.deleter Decorator
   - Defines cleanup for: del obj.property
   - Less commonly used

4. Use Cases
   - Computed attributes (email from first + last)
   - Validation (ensure positive values)
   - Read-only attributes (no setter)
   - Caching expensive computations
   - Backward compatibility (add logic without changing interface)

5. Naming Convention
   - Public property: name
   - Private backing store: _name

6. Best Practices
   - Use properties for computed values
   - Add validation in setters
   - Cache expensive computations
   - Keep getters simple and fast
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Temperature Class [EASY]
# Create class that stores Celsius
# Properties: celsius (getter/setter), fahrenheit (computed), kelvin (computed)
# TODO: Write your code here

# Solution:
# class Temperature:
#     def __init__(self, celsius=0):
#         self._celsius = celsius
#     
#     @property
#     def celsius(self):
#         return self._celsius
#     
#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature below absolute zero")
#         self._celsius = value
#     
#     @property
#     def fahrenheit(self):
#         return self._celsius * 9/5 + 32
#     
#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.celsius = (value - 32) * 5/9
#     
#     @property
#     def kelvin(self):
#         return self._celsius + 273.15


# Exercise 2: Rectangle Class [EASY]
# Properties: width, height (with validation > 0)
# Read-only: area, perimeter, is_square
# TODO: Write your code here

# Solution:
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     
#     @property
#     def width(self):
#         return self._width
#     
#     @width.setter
#     def width(self, value):
#         if value <= 0:
#             raise ValueError("Width must be positive")
#         self._width = value
#     
#     @property
#     def height(self):
#         return self._height
#     
#     @height.setter
#     def height(self, value):
#         if value <= 0:
#             raise ValueError("Height must be positive")
#         self._height = value
#     
#     @property
#     def area(self):
#         return self._width * self._height
#     
#     @property
#     def perimeter(self):
#         return 2 * (self._width + self._height)
#     
#     @property
#     def is_square(self):
#         return self._width == self._height


# Exercise 3: BankAccount [MEDIUM]
# balance with validation (no negative)
# Read-only: is_overdrawn, account_status
# TODO: Write your code here

# Solution:
# class BankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.owner = owner
#         self._balance = initial_balance
#     
#     @property
#     def balance(self):
#         return self._balance
#     
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#         self._balance = value
#     
#     @property
#     def account_status(self):
#         if self._balance >= 10000:
#             return "Gold"
#         elif self._balance >= 1000:
#             return "Standard"
#         else:
#             return "Basic"


# Exercise 4: ML Config [MEDIUM]
# learning_rate (0-1), epochs (positive int), model_type (valid types only)
# Read-only: config_dict
# TODO: Write your code here


# Exercise 5: Lazy Loading [CHALLENGE]
# Create property that loads data only when first accessed
# Cache the result for subsequent accesses
# TODO: Write your code here

# Solution:
# class LazyDataset:
#     def __init__(self, filepath):
#         self._filepath = filepath
#         self._data = None
#     
#     @property
#     def data(self):
#         if self._data is None:
#             print(f"Loading data from {self._filepath}...")
#             # Simulate loading
#             self._data = [1, 2, 3, 4, 5]
#         return self._data
#     
#     def reload(self):
#         self._data = None


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Defining setter before property
   ❌ @fullname.setter before @property
   ✅ @property first, then @fullname.setter

2. Forgetting underscore for backing store
   ❌ @property
      def name(self): return self.name  # Infinite recursion!
   ✅ @property
      def name(self): return self._name

3. Heavy computation in getter
   ❌ @property
      def result(self): return expensive_operation()  # Called every access!
   ✅ Cache the result, invalidate when needed

4. Not validating in __init__
   ❌ def __init__(self, x): self._x = x  # Bypasses validation!
   ✅ def __init__(self, x): self.x = x  # Goes through setter

5. Returning mutable objects
   ❌ @property
      def items(self): return self._items  # Can be modified externally!
   ✅ @property
      def items(self): return self._items.copy()

6. Making getter have side effects
   - Getters should be pure - no modifications!
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("PROPERTY DECORATORS DEMONSTRATION")
    print("="*60)
    
    class Employee:
        def __init__(self, first, last):
            self.first = first
            self.last = last
        
        @property
        def email(self):
            return f"{self.first.lower()}.{self.last.lower()}@email.com"
        
        @property
        def fullname(self):
            return f"{self.first} {self.last}"
        
        @fullname.setter
        def fullname(self, name):
            first, last = name.split(' ')
            self.first = first
            self.last = last
        
        @fullname.deleter
        def fullname(self):
            print("Deleting name!")
            self.first = None
            self.last = None
    
    emp = Employee('John', 'Smith')
    
    print(f"\n1. Initial state:")
    print(f"   Name: {emp.fullname}")
    print(f"   Email: {emp.email}")
    
    print(f"\n2. Using setter (emp.fullname = 'Om Patel'):")
    emp.fullname = "Om Patel"
    print(f"   First: {emp.first}")
    print(f"   Last: {emp.last}")
    print(f"   Email: {emp.email}")
    
    print(f"\n3. Using deleter (del emp.fullname):")
    del emp.fullname
    print(f"   First: {emp.first}")
    print(f"   Last: {emp.last}")
    
    print("\n" + "="*60)