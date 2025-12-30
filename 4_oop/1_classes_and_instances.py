"""
================================================================================
PYTHON OOP: CLASSES AND INSTANCES
================================================================================
Day: 15

Description:
    Complete introduction to Object-Oriented Programming in Python. Covers
    classes, objects, instances, attributes, methods, constructors, and
    the foundations needed for building ML models and data pipelines.

Learning Objectives:
    - Understand OOP concepts: classes, objects, instances
    - Create classes with __init__ constructor
    - Define instance attributes and methods
    - Understand the 'self' parameter
    - Differentiate instance vs class attributes
    - Apply OOP principles in ML/AI contexts

Prerequisites:
    - Functions (Day 3-4)
    - Data structures (lists, dicts)
================================================================================
"""

# =============================================================================
# 1. WHAT IS OBJECT-ORIENTED PROGRAMMING?
# =============================================================================

"""
OOP is a programming paradigm based on "objects" containing data and code.

Key Concepts:
- CLASS: A blueprint/template for creating objects
- OBJECT: An instance of a class
- ATTRIBUTE: Data stored in an object (variables)
- METHOD: Functions that belong to an object

Why OOP matters for AI/ML:
- Organize complex ML pipelines
- Create reusable model components
- Build custom layers and architectures
- Encapsulate data preprocessing logic
- Design clean APIs for your models

Real-world analogy:
- Class = Cookie cutter (blueprint)
- Object = Cookie (actual instance)
- Attributes = Size, flavor, color (properties)
- Methods = eat(), crumble(), dip() (actions)
"""


# =============================================================================
# 2. CREATING A BASIC CLASS
# =============================================================================

# --- Simplest possible class ---
class Employee:
    pass  # Empty class (placeholder)

# Creating instances (objects)
emp_1 = Employee()
emp_2 = Employee()

print(f"emp_1: {emp_1}")
print(f"emp_2: {emp_2}")
print(f"Same object? {emp_1 is emp_2}")  # False - different instances

# --- Adding attributes manually (NOT RECOMMENDED) ---
emp_1.first = 'Om'
emp_1.last = 'Patel'
emp_1.email = 'om.patel@company.com'
emp_1.pay = 50000

print(f"Employee: {emp_1.first} {emp_1.last}")
print(f"Email: {emp_1.email}")

# Problem: emp_2 has no attributes!
# print(emp_2.first)  # AttributeError!

"""
Problems with manual attribute assignment:
- Inconsistent objects (some have attrs, some don't)
- No validation
- Easy to forget attributes
- No documentation of expected structure
"""


# =============================================================================
# 3. THE __init__ METHOD (CONSTRUCTOR)
# =============================================================================

"""
__init__ is the constructor - called automatically when creating an instance.
Use it to initialize attributes consistently for every object.
"""

class Employee:
    def __init__(self, first, last, pay):
        """Initialize employee with required attributes"""
        # 'self' refers to the instance being created
        self.first = first
        self.last = last
        self.pay = pay
        # Derived attribute
        self.email = f"{first.lower()}.{last.lower()}@company.com"

# Now every employee MUST have these attributes
emp_1 = Employee('Om', 'Patel', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(f"\nEmployee 1: {emp_1.first} {emp_1.last}")
print(f"Email: {emp_1.email}")
print(f"Pay: ${emp_1.pay:,}")

print(f"\nEmployee 2: {emp_2.first} {emp_2.last}")
print(f"Email: {emp_2.email}")

# --- What happens during instantiation ---
"""
Employee('Om', 'Patel', 60000) does:
1. Creates new empty Employee object
2. Calls __init__(self, 'Om', 'Patel', 60000)
3. self = the new object
4. Attributes are set on self
5. Returns the initialized object
"""


# =============================================================================
# 4. UNDERSTANDING 'self'
# =============================================================================

"""
'self' is a reference to the current instance.
- First parameter of every instance method
- Python passes it automatically
- By convention named 'self' (could be anything)
"""

class Demo:
    def __init__(self, value):
        print(f"self is: {self}")
        self.value = value
    
    def show(self):
        print(f"self is: {self}")
        print(f"value is: {self.value}")

obj = Demo(42)
print(f"obj is: {obj}")
obj.show()

# self and obj are the SAME object!

# --- Why self is needed ---
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1  # Which object's count? self.count!
    
    def get_count(self):
        return self.count

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print(f"\nc1 count: {c1.get_count()}")  # 2
print(f"c2 count: {c2.get_count()}")  # 1
# Each instance has its OWN count!


# =============================================================================
# 5. INSTANCE METHODS
# =============================================================================

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
    
    def fullname(self):
        """Return employee's full name"""
        return f"{self.first} {self.last}"
    
    def apply_raise(self, percentage):
        """Apply percentage raise to salary"""
        self.pay = int(self.pay * (1 + percentage / 100))
    
    def __str__(self):
        """String representation for print()"""
        return f"Employee({self.first} {self.last}, ${self.pay:,})"

emp_1 = Employee('Om', 'Patel', 60000)

# --- Calling methods ---
# Method 1: On instance (common)
print(f"\nFull name: {emp_1.fullname()}")

# Method 2: On class (must pass instance)
print(f"Full name: {Employee.fullname(emp_1)}")

# Both are equivalent! Python converts:
# emp_1.fullname() → Employee.fullname(emp_1)

# --- Methods that modify state ---
print(f"\nBefore raise: ${emp_1.pay:,}")
emp_1.apply_raise(10)  # 10% raise
print(f"After raise: ${emp_1.pay:,}")

# --- Using __str__ ---
print(f"\nEmployee: {emp_1}")


# =============================================================================
# 6. INSTANCE VS CLASS ATTRIBUTES
# =============================================================================

"""
Instance attributes: Unique to each instance (defined in __init__ with self)
Class attributes: Shared by ALL instances (defined in class body)
"""

class Employee:
    # Class attributes - shared by all instances
    company = "TechCorp"
    raise_amount = 1.04  # 4% default raise
    employee_count = 0
    
    def __init__(self, first, last, pay):
        # Instance attributes - unique to each instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        
        # Modify class attribute
        Employee.employee_count += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        # Access class attribute through self (allows override)
        self.pay = int(self.pay * self.raise_amount)

# --- Class attribute access ---
print(f"\nCompany: {Employee.company}")
print(f"Default raise: {Employee.raise_amount}")

emp_1 = Employee('Om', 'Patel', 60000)
emp_2 = Employee('Test', 'User', 50000)

print(f"Employee count: {Employee.employee_count}")  # 2

# Access class attribute through instance
print(f"emp_1 company: {emp_1.company}")
print(f"emp_2 company: {emp_2.company}")

# --- Attribute lookup order ---
"""
When you access obj.attribute, Python looks:
1. Instance's __dict__ (instance attributes)
2. Class's __dict__ (class attributes)
3. Parent classes (inheritance - Day 16)
"""

print(f"\nemp_1.__dict__: {emp_1.__dict__}")
print(f"Employee.__dict__: {list(Employee.__dict__.keys())}")

# --- Overriding class attribute on instance ---
emp_1.raise_amount = 1.10  # Creates INSTANCE attribute!

print(f"\nemp_1.raise_amount: {emp_1.raise_amount}")  # 1.10 (instance)
print(f"emp_2.raise_amount: {emp_2.raise_amount}")  # 1.04 (class)
print(f"Employee.raise_amount: {Employee.raise_amount}")  # 1.04 (class)

emp_1.apply_raise()  # Uses 1.10
emp_2.apply_raise()  # Uses 1.04

print(f"emp_1 pay after raise: ${emp_1.pay:,}")
print(f"emp_2 pay after raise: ${emp_2.pay:,}")


# =============================================================================
# 7. DEFAULT AND OPTIONAL PARAMETERS
# =============================================================================

class Employee:
    def __init__(self, first, last, pay=50000, department=None):
        """
        Initialize employee with optional parameters.
        
        Args:
            first: First name (required)
            last: Last name (required)
            pay: Annual salary (default: 50000)
            department: Department name (default: None)
        """
        self.first = first
        self.last = last
        self.pay = pay
        self.department = department or "Unassigned"
        self.email = f"{first.lower()}.{last.lower()}@company.com"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

# Various ways to create instances
emp_1 = Employee('Om', 'Patel', 60000, 'Engineering')
emp_2 = Employee('Jane', 'Doe', department='Marketing')  # Default pay
emp_3 = Employee('John', 'Smith')  # All defaults

print(f"\n{emp_1.first}: ${emp_1.pay:,}, {emp_1.department}")
print(f"{emp_2.first}: ${emp_2.pay:,}, {emp_2.department}")
print(f"{emp_3.first}: ${emp_3.pay:,}, {emp_3.department}")


# =============================================================================
# 8. PRACTICAL EXAMPLE: ML MODEL CLASS
# =============================================================================

import random

class SimpleModel:
    """A simple ML model class demonstrating OOP concepts"""
    
    # Class attributes
    model_count = 0
    
    def __init__(self, name, learning_rate=0.01, epochs=100):
        """Initialize model with hyperparameters"""
        self.name = name
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.is_trained = False
        self.history = {'loss': [], 'accuracy': []}
        
        SimpleModel.model_count += 1
        self.model_id = SimpleModel.model_count
    
    def summary(self):
        """Print model summary"""
        print(f"\n{'='*40}")
        print(f"Model: {self.name} (ID: {self.model_id})")
        print(f"{'='*40}")
        print(f"Learning Rate: {self.learning_rate}")
        print(f"Epochs: {self.epochs}")
        print(f"Trained: {self.is_trained}")
        if self.is_trained:
            print(f"Final Loss: {self.history['loss'][-1]:.4f}")
            print(f"Final Accuracy: {self.history['accuracy'][-1]:.2%}")
    
    def train(self, X, y, verbose=True):
        """Simulate model training"""
        if verbose:
            print(f"\nTraining {self.name}...")
        
        # Simulate training
        self.weights = [random.random() for _ in range(len(X[0]) if X else 1)]
        
        for epoch in range(self.epochs):
            # Simulated metrics
            loss = 1.0 / (epoch + 1) + random.random() * 0.1
            accuracy = min(0.5 + epoch * 0.005 + random.random() * 0.05, 0.99)
            
            self.history['loss'].append(loss)
            self.history['accuracy'].append(accuracy)
            
            if verbose and (epoch + 1) % 25 == 0:
                print(f"  Epoch {epoch+1}/{self.epochs} - "
                      f"Loss: {loss:.4f}, Accuracy: {accuracy:.2%}")
        
        self.is_trained = True
        if verbose:
            print(f"Training complete!")
    
    def predict(self, X):
        """Make predictions"""
        if not self.is_trained:
            raise RuntimeError("Model must be trained before prediction!")
        # Simulated predictions
        return [random.choice([0, 1]) for _ in range(len(X))]
    
    def save(self, filepath):
        """Save model to file"""
        import json
        model_data = {
            'name': self.name,
            'learning_rate': self.learning_rate,
            'epochs': self.epochs,
            'weights': self.weights,
            'is_trained': self.is_trained
        }
        with open(filepath, 'w') as f:
            json.dump(model_data, f, indent=2)
        print(f"Model saved to {filepath}")
    
    def __str__(self):
        status = "trained" if self.is_trained else "untrained"
        return f"SimpleModel('{self.name}', {status})"
    
    def __repr__(self):
        return f"SimpleModel('{self.name}', lr={self.learning_rate}, epochs={self.epochs})"

# --- Using the model class ---
print("\n" + "="*50)
print("ML MODEL CLASS DEMONSTRATION")
print("="*50)

# Create models
model1 = SimpleModel("ClassifierV1", learning_rate=0.001, epochs=100)
model2 = SimpleModel("ClassifierV2", learning_rate=0.01, epochs=50)

print(f"\nModels created: {SimpleModel.model_count}")
print(f"model1: {model1}")
print(f"model2: {repr(model2)}")

# Train model
X_train = [[1, 2], [3, 4], [5, 6]]
y_train = [0, 1, 0]

model1.train(X_train, y_train, verbose=True)
model1.summary()


# =============================================================================
# 9. MUTABLE DEFAULT ARGUMENTS (GOTCHA!)
# =============================================================================

"""
NEVER use mutable defaults (list, dict) directly!
They're shared across ALL instances!
"""

# --- WRONG way ---
class WrongExample:
    def __init__(self, items=[]):  # DANGER!
        self.items = items

wrong1 = WrongExample()
wrong2 = WrongExample()

wrong1.items.append("A")
print(f"wrong1.items: {wrong1.items}")  # ['A']
print(f"wrong2.items: {wrong2.items}")  # ['A'] - Same list!

# --- CORRECT way ---
class CorrectExample:
    def __init__(self, items=None):
        self.items = items if items is not None else []
        # Or: self.items = items or []
        # Or: self.items = list(items) if items else []

correct1 = CorrectExample()
correct2 = CorrectExample()

correct1.items.append("A")
print(f"\ncorrect1.items: {correct1.items}")  # ['A']
print(f"correct2.items: {correct2.items}")  # [] - Separate list!


# =============================================================================
# 10. DATA CLASSES (PYTHON 3.7+)
# =============================================================================

"""
dataclass decorator auto-generates __init__, __repr__, __eq__, etc.
Perfect for simple data containers!
"""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Employee:
    first: str
    last: str
    pay: int = 50000
    department: str = "Unassigned"
    skills: List[str] = field(default_factory=list)  # Mutable default done right!
    
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

# Auto-generated __init__!
emp = Employee("Om", "Patel", 60000, "Engineering", ["Python", "ML"])

print(f"\nDataclass Employee:")
print(f"  {emp}")  # Auto-generated __repr__!
print(f"  Email: {emp.email}")
print(f"  Skills: {emp.skills}")

# Auto-generated __eq__!
emp2 = Employee("Om", "Patel", 60000, "Engineering", ["Python", "ML"])
print(f"  emp == emp2: {emp == emp2}")  # True!

# --- Dataclass for ML config ---
@dataclass
class ModelConfig:
    """Configuration for ML model"""
    name: str
    learning_rate: float = 0.001
    epochs: int = 100
    batch_size: int = 32
    hidden_layers: List[int] = field(default_factory=lambda: [64, 32])
    dropout: float = 0.2
    optimizer: str = "adam"

config = ModelConfig("MyModel", epochs=200)
print(f"\nModel Config: {config}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Class Basics
   - class ClassName: defines a class
   - Instance = object created from class
   - __init__ = constructor, initializes attributes

2. self Parameter
   - First parameter of instance methods
   - References the current instance
   - Python passes it automatically

3. Attributes
   - Instance attributes: unique to each object (self.attr)
   - Class attributes: shared by all instances (ClassName.attr)
   - Lookup order: instance → class → parent classes

4. Methods
   - Instance methods: take self, operate on instance
   - Called as obj.method() or Class.method(obj)

5. Best Practices
   - Initialize ALL attributes in __init__
   - Use None for mutable defaults
   - Use descriptive names
   - Add docstrings
   - Consider dataclasses for simple data containers

6. ML/AI Applications
   - Model classes encapsulate weights, hyperparameters
   - Config classes hold experiment settings
   - Pipeline classes organize data flow
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Basic Class [EASY]
# Create a Book class with title, author, pages, and current_page
# Add methods: read(pages), get_progress(), reset()
# TODO: Write your code here

# Solution:
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.current_page = 0
#     
#     def read(self, pages):
#         self.current_page = min(self.current_page + pages, self.pages)
#     
#     def get_progress(self):
#         return self.current_page / self.pages * 100
#     
#     def reset(self):
#         self.current_page = 0
#     
#     def __str__(self):
#         return f"{self.title} by {self.author} ({self.get_progress():.1f}% complete)"


# Exercise 2: Bank Account [EASY]
# Create BankAccount class with balance, deposit(), withdraw(), get_balance()
# Prevent negative balance
# TODO: Write your code here

# Solution:
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         return False
#     
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             return True
#         return False
#     
#     def get_balance(self):
#         return self.balance


# Exercise 3: Shopping Cart [MEDIUM]
# Create Cart class with items list
# Methods: add_item(name, price, qty), remove_item(name), total(), clear()
# TODO: Write your code here

# Solution:
# class Cart:
#     def __init__(self):
#         self.items = []
#     
#     def add_item(self, name, price, qty=1):
#         self.items.append({'name': name, 'price': price, 'qty': qty})
#     
#     def remove_item(self, name):
#         self.items = [i for i in self.items if i['name'] != name]
#     
#     def total(self):
#         return sum(i['price'] * i['qty'] for i in self.items)
#     
#     def clear(self):
#         self.items = []
#     
#     def __len__(self):
#         return sum(i['qty'] for i in self.items)


# Exercise 4: Dataset Class [MEDIUM]
# Create Dataset class for ML with features (X) and labels (y)
# Methods: split(ratio), shuffle(), get_batch(size), __len__
# TODO: Write your code here

# Solution:
# class Dataset:
#     def __init__(self, X, y):
#         self.X = list(X)
#         self.y = list(y)
#     
#     def __len__(self):
#         return len(self.X)
#     
#     def shuffle(self):
#         import random
#         combined = list(zip(self.X, self.y))
#         random.shuffle(combined)
#         self.X, self.y = zip(*combined)
#         self.X, self.y = list(self.X), list(self.y)
#     
#     def split(self, ratio=0.8):
#         idx = int(len(self) * ratio)
#         train = Dataset(self.X[:idx], self.y[:idx])
#         test = Dataset(self.X[idx:], self.y[idx:])
#         return train, test
#     
#     def get_batch(self, size):
#         for i in range(0, len(self), size):
#             yield self.X[i:i+size], self.y[i:i+size]


# Exercise 5: Experiment Tracker [MEDIUM]
# Create class to track ML experiments
# Store: name, hyperparams, metrics, timestamps
# Methods: log_metric(), get_best(), summary()
# TODO: Write your code here

# Solution:
# from datetime import datetime
# class ExperimentTracker:
#     def __init__(self, name):
#         self.name = name
#         self.created_at = datetime.now()
#         self.hyperparams = {}
#         self.metrics = {}
#     
#     def set_params(self, **params):
#         self.hyperparams.update(params)
#     
#     def log_metric(self, name, value, step=None):
#         if name not in self.metrics:
#             self.metrics[name] = []
#         self.metrics[name].append({'value': value, 'step': step})
#     
#     def get_best(self, metric, mode='max'):
#         values = [m['value'] for m in self.metrics.get(metric, [])]
#         if not values:
#             return None
#         return max(values) if mode == 'max' else min(values)
#     
#     def summary(self):
#         print(f"Experiment: {self.name}")
#         print(f"Params: {self.hyperparams}")
#         for metric, values in self.metrics.items():
#             print(f"{metric}: {[v['value'] for v in values[-5:]]}")


# Exercise 6: Neural Network Layer [CHALLENGE]
# Create Layer class with input_size, output_size, activation
# Methods: forward(x), backward(grad), init_weights()
# TODO: Write your code here

# Solution:
# import random
# import math
# class Layer:
#     def __init__(self, input_size, output_size, activation='relu'):
#         self.input_size = input_size
#         self.output_size = output_size
#         self.activation = activation
#         self.weights = None
#         self.bias = None
#         self.last_input = None
#         self.init_weights()
#     
#     def init_weights(self):
#         scale = math.sqrt(2.0 / self.input_size)
#         self.weights = [[random.gauss(0, scale) for _ in range(self.output_size)]
#                        for _ in range(self.input_size)]
#         self.bias = [0.0] * self.output_size
#     
#     def forward(self, x):
#         self.last_input = x
#         output = []
#         for i in range(self.output_size):
#             val = sum(x[j] * self.weights[j][i] for j in range(self.input_size))
#             val += self.bias[i]
#             if self.activation == 'relu':
#                 val = max(0, val)
#             output.append(val)
#         return output


# Exercise 7: Model Registry [CHALLENGE]
# Create singleton-like registry for managing multiple models
# Methods: register(), get(), list_models(), delete()
# TODO: Write your code here

# Solution:
# class ModelRegistry:
#     _models = {}  # Class-level storage
#     
#     def __init__(self):
#         pass
#     
#     @classmethod
#     def register(cls, name, model):
#         if name in cls._models:
#             raise ValueError(f"Model '{name}' already exists")
#         cls._models[name] = model
#     
#     @classmethod
#     def get(cls, name):
#         return cls._models.get(name)
#     
#     @classmethod
#     def list_models(cls):
#         return list(cls._models.keys())
#     
#     @classmethod
#     def delete(cls, name):
#         if name in cls._models:
#             del cls._models[name]


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting self
   ❌ def fullname(): return first + last
   ✅ def fullname(self): return self.first + self.last

2. Mutable default arguments
   ❌ def __init__(self, items=[]):
   ✅ def __init__(self, items=None): self.items = items or []

3. Modifying class attribute through instance
   ❌ self.class_list.append(x)  # Modifies for ALL instances!
   ✅ self.instance_list = self.class_list.copy(); self.instance_list.append(x)

4. Not initializing attributes in __init__
   ❌ Setting attributes only in some methods
   ✅ Initialize ALL attributes in __init__ (even as None)

5. Confusing class and instance
   ❌ Employee.pay = 60000  # Changes class attribute!
   ✅ emp.pay = 60000  # Changes instance attribute

6. Calling method without parentheses
   ❌ emp.fullname  # Returns method object!
   ✅ emp.fullname()  # Calls the method

7. Not using __str__ for debugging
   ❌ print(emp)  # <__main__.Employee object at 0x...>
   ✅ Define __str__ for readable output

8. Circular references
   ❌ self.parent = parent; parent.child = self  # Memory leak!
   ✅ Use weakref for bidirectional references
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CLASSES AND INSTANCES DEMONSTRATION")
    print("="*60)
    
    # Basic class usage
    print("\n1. Creating Employee instances:")
    
    class Employee:
        company = "TechCorp"
        
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
        
        def fullname(self):
            return f"{self.first} {self.last}"
        
        def __str__(self):
            return f"Employee({self.fullname()}, ${self.pay:,})"
    
    emp1 = Employee('Om', 'Patel', 60000)
    emp2 = Employee('Jane', 'Doe', 55000)
    
    print(f"   {emp1}")
    print(f"   {emp2}")
    print(f"   Company: {Employee.company}")
    
    # Method calls
    print("\n2. Method calls:")
    print(f"   emp1.fullname(): {emp1.fullname()}")
    print(f"   Employee.fullname(emp1): {Employee.fullname(emp1)}")
    
    # Instance vs class attributes
    print("\n3. Instance vs Class attributes:")
    print(f"   emp1.__dict__: {emp1.__dict__}")
    print(f"   Class attributes: company='{Employee.company}'")
    
    print("\n" + "="*60)
    print("Run the exercises to practice!")
    print("="*60)