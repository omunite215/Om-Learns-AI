"""
================================================================================
PYTHON OOP: CLASS VARIABLES
================================================================================
Day: 16

Description:
    Deep dive into class variables (class attributes) in Python. Covers the
    difference between class and instance variables, how Python looks up
    attributes, and practical patterns for shared state across instances.

Learning Objectives:
    - Understand class variables vs instance variables
    - Know how attribute lookup works in Python
    - Use class variables for shared state and counters
    - Understand when modifying via self creates instance attributes
    - Apply class variables in ML/AI contexts

Prerequisites:
    - Classes and Instances (Day 15)
    - Basic OOP concepts
================================================================================
"""

# =============================================================================
# 1. WHAT ARE CLASS VARIABLES?
# =============================================================================

"""
CLASS VARIABLES:
- Defined in class body (outside any method)
- Shared by ALL instances of the class
- Belong to the class itself, not individual objects
- Accessed via ClassName.var or self.var

INSTANCE VARIABLES:
- Defined in __init__ with self.var
- Unique to each instance
- Each object has its own copy

Why class variables matter for AI/ML:
- Track total models trained
- Share configuration across instances
- Define default hyperparameters
- Count dataset samples processed
- Maintain global registries
"""


# =============================================================================
# 2. BASIC CLASS VARIABLES
# =============================================================================

class Employee:
    # Class variables - shared by all instances
    num_of_emps = 0
    raise_amount = 1.04  # 4% raise
    company_name = "TechCorp"
    
    def __init__(self, first, last, pay):
        # Instance variables - unique to each instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        
        # Increment class variable
        Employee.num_of_emps += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        # Using self.raise_amount allows per-instance override
        self.pay = int(self.pay * self.raise_amount)
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

# --- Check count before creating instances ---
print("=== CLASS VARIABLE: EMPLOYEE COUNTER ===")
print(f"Employees before: {Employee.num_of_emps}")  # 0

# --- Create instances ---
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(f"Employees after: {Employee.num_of_emps}")   # 2

# Each instance creation incremented the counter!


# =============================================================================
# 3. ACCESSING CLASS VARIABLES
# =============================================================================

print("\n=== ACCESSING CLASS VARIABLES ===")

# --- Access via class name (preferred for reading class vars) ---
print(f"Employee.raise_amount: {Employee.raise_amount}")
print(f"Employee.company_name: {Employee.company_name}")
print(f"Employee.num_of_emps: {Employee.num_of_emps}")

# --- Access via instance (falls back to class) ---
print(f"\nemp_1.raise_amount: {emp_1.raise_amount}")
print(f"emp_2.raise_amount: {emp_2.raise_amount}")

# Both ways work! But why?


# =============================================================================
# 4. ATTRIBUTE LOOKUP ORDER (IMPORTANT!)
# =============================================================================

"""
When you access obj.attribute, Python looks in this order:
1. Instance's __dict__ (instance attributes)
2. Class's __dict__ (class attributes)
3. Parent class's __dict__ (inherited attributes)

If found in step 1, returns that value.
If not found, moves to next step.
"""

print("\n=== ATTRIBUTE LOOKUP ===")

# Instance namespace - only has instance attributes
print(f"emp_1.__dict__: {emp_1.__dict__}")
# Output: {'first': 'Corey', 'last': 'Schafer', 'pay': 50000, 'email': '...'}
# Note: NO raise_amount here!

# Class namespace - has class attributes
print(f"\nEmployee.__dict__ (partial):")
for key in ['num_of_emps', 'raise_amount', 'company_name']:
    print(f"  {key}: {Employee.__dict__[key]}")

# When we do emp_1.raise_amount:
# 1. Python checks emp_1.__dict__ - not found
# 2. Python checks Employee.__dict__ - found! Returns 1.04


# =============================================================================
# 5. MODIFYING CLASS VARIABLES
# =============================================================================

print("\n=== MODIFYING CLASS VARIABLES ===")

# --- Modify via CLASS (affects all instances) ---
print("Before modification:")
print(f"  Employee.raise_amount: {Employee.raise_amount}")
print(f"  emp_1.raise_amount: {emp_1.raise_amount}")
print(f"  emp_2.raise_amount: {emp_2.raise_amount}")

Employee.raise_amount = 1.05  # Change for ALL

print("\nAfter Employee.raise_amount = 1.05:")
print(f"  Employee.raise_amount: {Employee.raise_amount}")  # 1.05
print(f"  emp_1.raise_amount: {emp_1.raise_amount}")        # 1.05
print(f"  emp_2.raise_amount: {emp_2.raise_amount}")        # 1.05

# --- Modify via INSTANCE (CREATES instance attribute!) ---
emp_1.raise_amount = 1.10  # This creates an INSTANCE attribute!

print("\nAfter emp_1.raise_amount = 1.10:")
print(f"  Employee.raise_amount: {Employee.raise_amount}")  # 1.05 (class)
print(f"  emp_1.raise_amount: {emp_1.raise_amount}")        # 1.10 (instance!)
print(f"  emp_2.raise_amount: {emp_2.raise_amount}")        # 1.05 (class)

# Check emp_1's namespace now
print(f"\nemp_1.__dict__: {emp_1.__dict__}")
# Now contains 'raise_amount': 1.10!

# emp_2 still doesn't have instance attribute
print(f"emp_2.__dict__: {emp_2.__dict__}")
# No raise_amount - still uses class variable


# =============================================================================
# 6. APPLYING RAISES WITH DIFFERENT RATES
# =============================================================================

print("\n=== APPLYING RAISES ===")

# Reset for clean demo
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
Employee.raise_amount = 1.04

# Give emp_1 a special raise rate
emp_1.raise_amount = 1.10  # 10% for emp_1 only

print("Before raise:")
print(f"  emp_1: ${emp_1.pay:,} (rate: {emp_1.raise_amount})")
print(f"  emp_2: ${emp_2.pay:,} (rate: {emp_2.raise_amount})")

# apply_raise uses self.raise_amount
emp_1.apply_raise()  # Uses 1.10 (instance)
emp_2.apply_raise()  # Uses 1.04 (class)

print("\nAfter raise:")
print(f"  emp_1: ${emp_1.pay:,} (10% raise)")
print(f"  emp_2: ${emp_2.pay:,} (4% raise)")


# =============================================================================
# 7. WHEN TO USE self VS ClassName
# =============================================================================

"""
Use ClassName.class_var when:
- MODIFYING and want to affect ALL instances
- The value should never be overridden per-instance
- Incrementing counters: Employee.num_of_emps += 1

Use self.class_var when:
- READING the value (allows per-instance override)
- You want subclasses to potentially override
- You want flexibility for special cases
"""

class Counter:
    """Demonstrates proper usage of class vs instance reference"""
    total_count = 0  # Shared across ALL counters
    
    def __init__(self, name):
        self.name = name
        self.count = 0  # Per-instance counter
    
    def increment(self):
        self.count += 1           # Instance only - use self
        Counter.total_count += 1  # All instances - use ClassName!
    
    def __repr__(self):
        return f"Counter('{self.name}', count={self.count})"

print("\n=== COUNTER EXAMPLE ===")
c1 = Counter("Counter1")
c2 = Counter("Counter2")

c1.increment()
c1.increment()
c1.increment()
c2.increment()

print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"Total across all counters: {Counter.total_count}")


# =============================================================================
# 8. PRACTICAL ML/AI EXAMPLES
# =============================================================================

class Model:
    """ML Model with class-level tracking"""
    
    # Class variables
    models_created = 0
    models_trained = 0
    default_learning_rate = 0.01
    default_epochs = 100
    
    def __init__(self, name, learning_rate=None, epochs=None):
        self.name = name
        self.learning_rate = learning_rate or Model.default_learning_rate
        self.epochs = epochs or Model.default_epochs
        self.is_trained = False
        self.accuracy = None
        
        Model.models_created += 1
        self.model_id = Model.models_created
    
    def train(self, X, y):
        """Simulate training"""
        print(f"Training {self.name}...")
        self.is_trained = True
        self.accuracy = 0.85 + (self.model_id * 0.01)  # Simulated
        Model.models_trained += 1
    
    @classmethod
    def get_stats(cls):
        """Get class-level statistics"""
        return {
            'created': cls.models_created,
            'trained': cls.models_trained,
            'untrained': cls.models_created - cls.models_trained
        }
    
    def __repr__(self):
        status = f"acc={self.accuracy:.2%}" if self.is_trained else "untrained"
        return f"Model('{self.name}', {status})"

print("\n=== ML MODEL TRACKING ===")

# Create models
model1 = Model("ClassifierA")
model2 = Model("ClassifierB", learning_rate=0.001)
model3 = Model("ClassifierC", epochs=200)

print(f"Models created: {Model.models_created}")
print(f"Models trained: {Model.models_trained}")

# Train some models
model1.train(None, None)
model3.train(None, None)

print(f"\nAfter training:")
print(f"Stats: {Model.get_stats()}")
print(f"model1: {model1}")
print(f"model2: {model2}")
print(f"model3: {model3}")


class Dataset:
    """Dataset class with shared configuration"""
    
    # Class variables for defaults
    default_train_ratio = 0.8
    default_shuffle = True
    total_samples_processed = 0
    
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.size = len(data)
        
        Dataset.total_samples_processed += self.size
    
    def split(self, ratio=None):
        """Split into train/test"""
        ratio = ratio or Dataset.default_train_ratio
        split_idx = int(self.size * ratio)
        return self.data[:split_idx], self.data[split_idx:]
    
    @classmethod
    def set_defaults(cls, train_ratio=None, shuffle=None):
        """Update default settings for all future datasets"""
        if train_ratio is not None:
            cls.default_train_ratio = train_ratio
        if shuffle is not None:
            cls.default_shuffle = shuffle

print("\n=== DATASET CLASS VARIABLES ===")
ds1 = Dataset("Dataset1", list(range(100)))
ds2 = Dataset("Dataset2", list(range(50)))

print(f"Total samples processed: {Dataset.total_samples_processed}")
print(f"Default train ratio: {Dataset.default_train_ratio}")

# Change default for all future datasets
Dataset.set_defaults(train_ratio=0.7)
print(f"New default train ratio: {Dataset.default_train_ratio}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Class Variables
   - Defined in class body, outside methods
   - Shared by ALL instances
   - Good for: counters, defaults, configuration

2. Instance Variables
   - Defined with self.var in __init__
   - Unique to each instance
   - Good for: object-specific data

3. Attribute Lookup Order
   instance.__dict__ → class.__dict__ → parent.__dict__

4. Modifying Class Variables
   - ClassName.var = x → Changes for ALL instances
   - self.var = x → Creates INSTANCE attribute (shadows class var)

5. Best Practices
   - Use ClassName.var when modifying shared state
   - Use self.var when reading (allows override)
   - Use class vars for counters, defaults, constants
   - Be careful: self.list.append() modifies shared list!
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Instance Counter [EASY]
# Create class that tracks how many instances exist
# Add class variable and increment in __init__
# TODO: Write your code here

# Solution:
# class Product:
#     count = 0
#     
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.count += 1


# Exercise 2: Default Configuration [EASY]
# Create class with default values that can be overridden per-instance
# TODO: Write your code here

# Solution:
# class APIClient:
#     default_timeout = 30
#     default_retries = 3
#     
#     def __init__(self, url, timeout=None, retries=None):
#         self.url = url
#         self.timeout = timeout or APIClient.default_timeout
#         self.retries = retries or APIClient.default_retries


# Exercise 3: Running Statistics [MEDIUM]
# Create class that tracks min, max, sum, count across all instances
# TODO: Write your code here

# Solution:
# class Measurement:
#     count = 0
#     total = 0
#     minimum = float('inf')
#     maximum = float('-inf')
#     
#     def __init__(self, value):
#         self.value = value
#         Measurement.count += 1
#         Measurement.total += value
#         Measurement.minimum = min(Measurement.minimum, value)
#         Measurement.maximum = max(Measurement.maximum, value)
#     
#     @classmethod
#     def average(cls):
#         return cls.total / cls.count if cls.count else 0


# Exercise 4: Model Version Tracker [MEDIUM]
# Track all model versions, allow getting latest version
# TODO: Write your code here

# Solution:
# class ModelVersion:
#     all_versions = []
#     
#     def __init__(self, name, version):
#         self.name = name
#         self.version = version
#         ModelVersion.all_versions.append(self)
#     
#     @classmethod
#     def get_latest(cls, name):
#         versions = [m for m in cls.all_versions if m.name == name]
#         return max(versions, key=lambda m: m.version) if versions else None


# Exercise 5: Shared Cache [CHALLENGE]
# Create class with shared cache across instances
# Each instance can read/write to shared cache
# TODO: Write your code here

# Solution:
# class CachedProcessor:
#     _cache = {}
#     cache_hits = 0
#     cache_misses = 0
#     
#     def __init__(self, name):
#         self.name = name
#     
#     def process(self, key, compute_func):
#         if key in CachedProcessor._cache:
#             CachedProcessor.cache_hits += 1
#             return CachedProcessor._cache[key]
#         else:
#             CachedProcessor.cache_misses += 1
#             result = compute_func()
#             CachedProcessor._cache[key] = result
#             return result


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Modifying class var via self (creates instance attr)
   ❌ self.count += 1  # Creates instance attribute!
   ✅ ClassName.count += 1

2. Mutable class variables (DANGER!)
   ❌ class Foo:
          items = []  # Shared list - all instances modify same list!
   ✅ class Foo:
          def __init__(self):
              self.items = []  # Each instance gets own list

3. Expecting instance modification to affect class
   ❌ emp.raise_amount = 1.1  # Only affects emp, not class
   ✅ Employee.raise_amount = 1.1  # Affects all

4. Not understanding attribute lookup
   - Reading: self.var works (falls back to class)
   - Writing: self.var = x creates instance attr

5. Forgetting class vars are shared in inheritance
   - Subclasses share parent's class vars by reference!
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CLASS VARIABLES DEMONSTRATION")
    print("="*60)
    
    class Employee:
        num_of_emps = 0
        raise_amount = 1.04
        
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            Employee.num_of_emps += 1
        
        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)
    
    print(f"\n1. Before creating employees: {Employee.num_of_emps}")
    
    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'User', 60000)
    
    print(f"2. After creating 2 employees: {Employee.num_of_emps}")
    
    print(f"\n3. Class raise_amount: {Employee.raise_amount}")
    print(f"   emp_1.raise_amount: {emp_1.raise_amount}")
    
    emp_1.raise_amount = 1.10
    print(f"\n4. After emp_1.raise_amount = 1.10:")
    print(f"   Class raise_amount: {Employee.raise_amount}")
    print(f"   emp_1.raise_amount: {emp_1.raise_amount}")
    print(f"   emp_2.raise_amount: {emp_2.raise_amount}")
    
    print("\n" + "="*60)