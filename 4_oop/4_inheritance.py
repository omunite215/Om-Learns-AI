"""
================================================================================
PYTHON OOP: INHERITANCE
================================================================================
Day: 17

Description:
    Complete guide to inheritance in Python. Covers creating subclasses,
    method overriding, super() function, multiple inheritance, method
    resolution order (MRO), and composition patterns for ML/AI applications.

Learning Objectives:
    - Understand inheritance and the "is-a" relationship
    - Create subclasses that extend parent classes
    - Override methods and class variables
    - Use super() to call parent methods
    - Understand Method Resolution Order (MRO)
    - Know when to use inheritance vs composition
    - Apply inheritance in ML/AI architectures

Prerequisites:
    - Classes and Instances (Day 15)
    - Class Variables and Methods (Day 16)
================================================================================
"""

# =============================================================================
# 1. WHAT IS INHERITANCE?
# =============================================================================

"""
INHERITANCE allows a class to inherit attributes and methods from another class.

Terminology:
- Parent/Base/Super class: The class being inherited from
- Child/Derived/Sub class: The class that inherits

Benefits:
- Code reuse: Don't repeat common functionality
- Logical hierarchy: Model real-world relationships
- Extensibility: Add features without modifying original
- Polymorphism: Treat different types uniformly

"is-a" relationship:
- Developer IS AN Employee
- Manager IS AN Employee
- Cat IS AN Animal

Why inheritance matters for AI/ML:
- Base Model class with common train/predict methods
- Specialized models inherit and override
- Custom layers extend base layer classes
- Dataset classes with common loading logic
"""


# =============================================================================
# 2. BASIC INHERITANCE
# =============================================================================

class Employee:
    """Base class for all employees"""
    raise_amt = 1.04  # 4% raise
    
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
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


# --- Simple inheritance (no customization) ---
class Developer(Employee):
    """Developer inherits everything from Employee"""
    pass  # Inherits all attributes and methods

# Developer has access to all Employee functionality!
dev = Developer('John', 'Doe', 50000)
print("=== BASIC INHERITANCE ===")
print(f"Developer: {dev.fullname()}")
print(f"Email: {dev.email}")
print(f"Pay: ${dev.pay:,}")

# --- Check inheritance ---
print(f"\nIs dev an Employee? {isinstance(dev, Employee)}")  # True
print(f"Is dev a Developer? {isinstance(dev, Developer)}")  # True
print(f"Is Developer subclass of Employee? {issubclass(Developer, Employee)}")  # True


# =============================================================================
# 3. OVERRIDING CLASS VARIABLES
# =============================================================================

class Employee:
    raise_amt = 1.04  # 4% default raise
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first.lower()}.{last.lower()}@email.com"
        self.pay = pay
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        # Uses self.raise_amt - allows subclass override!
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.first}', '{self.last}', {self.pay})"


class Developer(Employee):
    """Developers get a higher raise"""
    raise_amt = 1.10  # 10% raise for developers!


print("\n=== OVERRIDING CLASS VARIABLES ===")

emp = Employee('Regular', 'Employee', 50000)
dev = Developer('Dev', 'Developer', 50000)

print(f"Employee raise_amt: {Employee.raise_amt}")  # 1.04
print(f"Developer raise_amt: {Developer.raise_amt}")  # 1.10

print(f"\nBefore raise:")
print(f"  emp pay: ${emp.pay:,}")
print(f"  dev pay: ${dev.pay:,}")

emp.apply_raise()  # Uses 1.04
dev.apply_raise()  # Uses 1.10

print(f"\nAfter raise:")
print(f"  emp pay: ${emp.pay:,} (4% raise)")
print(f"  dev pay: ${dev.pay:,} (10% raise)")


# =============================================================================
# 4. EXTENDING __init__ WITH super()
# =============================================================================

"""
super() returns a proxy object that delegates method calls to the parent class.
Use it to extend (not replace) parent functionality.
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
        return f"{self.__class__.__name__}('{self.first}', '{self.last}', {self.pay})"


class Developer(Employee):
    """Developer with programming language specialty"""
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        # Call parent __init__ first
        super().__init__(first, last, pay)
        # Then add child-specific attributes
        self.prog_lang = prog_lang
    
    def __repr__(self):
        return f"Developer('{self.first}', '{self.last}', {self.pay}, '{self.prog_lang}')"


print("\n=== EXTENDING __init__ WITH super() ===")

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(f"dev_1: {dev_1}")
print(f"  Email: {dev_1.email}")           # Inherited
print(f"  Language: {dev_1.prog_lang}")    # New attribute

print(f"\ndev_2: {dev_2}")
print(f"  Language: {dev_2.prog_lang}")

# --- Why use super() instead of Parent.__init__()? ---
"""
super().__init__(...)  vs  Employee.__init__(self, ...)

super() is better because:
1. Works correctly with multiple inheritance
2. Follows Method Resolution Order (MRO)
3. More maintainable - doesn't hardcode parent class name
4. Enables cooperative multiple inheritance
"""


# =============================================================================
# 5. ADDING NEW METHODS TO SUBCLASSES
# =============================================================================

class Manager(Employee):
    """Manager who supervises other employees"""
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Handle mutable default argument properly!
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        """Add employee to manager's team"""
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        """Remove employee from manager's team"""
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        """Print all employees under this manager"""
        print(f"\n{self.fullname()}'s team:")
        for emp in self.employees:
            print(f"  --> {emp.fullname()}")
    
    def get_team_size(self):
        """Return number of direct reports"""
        return len(self.employees)
    
    def get_team_payroll(self):
        """Calculate total team payroll"""
        return sum(emp.pay for emp in self.employees) + self.pay


print("\n=== MANAGER CLASS WITH NEW METHODS ===")

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# Create manager with initial team
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(f"Manager: {mgr_1.fullname()}")
print(f"Email: {mgr_1.email}")  # Inherited!

# Use new methods
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print(f"\nTeam size: {mgr_1.get_team_size()}")
print(f"Team payroll: ${mgr_1.get_team_payroll():,}")

# Remove employee
mgr_1.remove_emp(dev_2)
print(f"\nAfter removing dev_2:")
mgr_1.print_emps()


# =============================================================================
# 6. OVERRIDING METHODS
# =============================================================================

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def get_info(self):
        """Base info method"""
        return f"{self.fullname()} - ${self.pay:,}"


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    
    # Override get_info to include programming language
    def get_info(self):
        """Extended info with programming language"""
        # Can call parent method if needed
        base_info = super().get_info()
        return f"{base_info} [{self.prog_lang}]"


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees or []
    
    # Override get_info to include team size
    def get_info(self):
        """Extended info with team size"""
        base_info = super().get_info()
        return f"{base_info} (Team: {len(self.employees)})"


print("\n=== OVERRIDING METHODS ===")

emp = Employee('Regular', 'Employee', 50000)
dev = Developer('Dev', 'Person', 60000, 'Python')
mgr = Manager('Manager', 'Boss', 90000, [emp, dev])

# Same method name, different behavior!
print(f"Employee: {emp.get_info()}")
print(f"Developer: {dev.get_info()}")
print(f"Manager: {mgr.get_info()}")


# =============================================================================
# 7. isinstance() AND issubclass()
# =============================================================================

print("\n=== isinstance() AND issubclass() ===")

emp = Employee('Regular', 'Employee', 50000)
dev = Developer('Dev', 'Person', 60000, 'Python')
mgr = Manager('Sue', 'Smith', 90000)

# isinstance() - check if object is instance of class
print("isinstance() checks:")
print(f"  isinstance(dev, Developer): {isinstance(dev, Developer)}")  # True
print(f"  isinstance(dev, Employee): {isinstance(dev, Employee)}")    # True (inheritance!)
print(f"  isinstance(dev, Manager): {isinstance(dev, Manager)}")      # False

# issubclass() - check class hierarchy
print("\nissubclass() checks:")
print(f"  issubclass(Developer, Employee): {issubclass(Developer, Employee)}")  # True
print(f"  issubclass(Manager, Employee): {issubclass(Manager, Employee)}")      # True
print(f"  issubclass(Developer, Manager): {issubclass(Developer, Manager)}")    # False
print(f"  issubclass(Employee, object): {issubclass(Employee, object)}")        # True!

# --- Practical use: Type checking ---
def process_employee(emp):
    """Process based on employee type"""
    if isinstance(emp, Manager):
        print(f"Processing manager with {len(emp.employees)} reports")
    elif isinstance(emp, Developer):
        print(f"Processing developer who knows {emp.prog_lang}")
    else:
        print(f"Processing regular employee")

process_employee(dev)
process_employee(mgr)
process_employee(emp)


# =============================================================================
# 8. METHOD RESOLUTION ORDER (MRO)
# =============================================================================

"""
MRO determines the order in which base classes are searched when looking for a method.
Python uses C3 linearization algorithm.
"""

print("\n=== METHOD RESOLUTION ORDER (MRO) ===")

print(f"Developer MRO: {Developer.__mro__}")
# (Developer, Employee, object)

print(f"\nManager MRO: {Manager.__mro__}")
# (Manager, Employee, object)

# When you call dev.fullname():
# 1. Python looks in Developer - not found
# 2. Python looks in Employee - found!
# 3. (Would look in object if not found)

# You can also use .mro() method
print(f"\nUsing .mro(): {Developer.mro()}")


# =============================================================================
# 9. MULTIPLE INHERITANCE
# =============================================================================

"""
Python supports multiple inheritance - a class can inherit from multiple parents.
Use with caution! Can lead to complexity.
"""

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"


class Worker:
    def __init__(self, job):
        self.job = job
    
    def work(self):
        return f"I work as a {self.job}"


class Employee(Person, Worker):
    """Employee inherits from both Person and Worker"""
    
    def __init__(self, name, job, salary):
        Person.__init__(self, name)  # Initialize Person
        Worker.__init__(self, job)   # Initialize Worker
        self.salary = salary
    
    def get_info(self):
        return f"{self.greet()}. {self.work()}. Salary: ${self.salary:,}"


print("\n=== MULTIPLE INHERITANCE ===")

emp = Employee('John', 'Developer', 75000)
print(emp.get_info())
print(f"MRO: {Employee.__mro__}")


# --- Diamond Problem ---
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(f"\nDiamond Problem - D().method(): {D().method()}")  # Returns 'B'
print(f"D MRO: {D.__mro__}")
# D -> B -> C -> A -> object (follows MRO)


# =============================================================================
# 10. INHERITANCE VS COMPOSITION
# =============================================================================

"""
INHERITANCE: "is-a" relationship
- Developer IS AN Employee
- Use when subclass is a specialized version of parent

COMPOSITION: "has-a" relationship  
- Manager HAS employees
- Use when one class contains another as a component

Prefer composition over inheritance when:
- Relationship is "has-a" not "is-a"
- You need more flexibility
- You want to avoid deep inheritance hierarchies
"""

# --- Composition Example ---
class Salary:
    """Salary component"""
    def __init__(self, base, bonus_rate=0.1):
        self.base = base
        self.bonus_rate = bonus_rate
    
    def calculate_total(self):
        return self.base * (1 + self.bonus_rate)


class Address:
    """Address component"""
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class EmployeeComposition:
    """Employee using composition instead of inheritance"""
    
    def __init__(self, name, salary_base, address_info):
        self.name = name
        # Has-a Salary
        self.salary = Salary(salary_base)
        # Has-a Address
        self.address = Address(**address_info)
    
    def get_info(self):
        return f"{self.name} - ${self.salary.calculate_total():,.0f} - {self.address}"


print("\n=== COMPOSITION EXAMPLE ===")

emp = EmployeeComposition(
    "John Doe",
    50000,
    {"street": "123 Main St", "city": "Boston", "country": "USA"}
)
print(emp.get_info())


# =============================================================================
# 11. ML/AI INHERITANCE PATTERNS
# =============================================================================

class BaseModel:
    """Base class for ML models"""
    
    default_epochs = 100
    default_lr = 0.01
    
    def __init__(self, name, epochs=None, learning_rate=None):
        self.name = name
        self.epochs = epochs or self.default_epochs
        self.learning_rate = learning_rate or self.default_lr
        self.is_trained = False
        self.history = {'loss': [], 'accuracy': []}
    
    def train(self, X, y):
        """To be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement train()")
    
    def predict(self, X):
        """To be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement predict()")
    
    def summary(self):
        """Print model summary"""
        status = "trained" if self.is_trained else "untrained"
        print(f"Model: {self.name} ({status})")
        print(f"  Epochs: {self.epochs}")
        print(f"  Learning Rate: {self.learning_rate}")
    
    def save(self, filepath):
        """Save model - common functionality"""
        import json
        with open(filepath, 'w') as f:
            json.dump({
                'name': self.name,
                'epochs': self.epochs,
                'learning_rate': self.learning_rate,
                'is_trained': self.is_trained
            }, f)
        print(f"Model saved to {filepath}")


class LinearRegression(BaseModel):
    """Linear Regression model"""
    
    def __init__(self, name="LinearRegression", **kwargs):
        super().__init__(name, **kwargs)
        self.weights = None
        self.bias = None
    
    def train(self, X, y):
        """Simplified training"""
        print(f"Training {self.name} for {self.epochs} epochs...")
        # Simulated training
        self.weights = [0.5] * len(X[0]) if X else [0.5]
        self.bias = 0.1
        self.is_trained = True
        self.history['loss'] = [1.0 / (i+1) for i in range(self.epochs)]
    
    def predict(self, X):
        if not self.is_trained:
            raise RuntimeError("Model must be trained first!")
        # Simplified prediction
        return [sum(x) * 0.5 + self.bias for x in X]


class NeuralNetwork(BaseModel):
    """Neural Network model"""
    
    default_epochs = 200  # Override parent default
    
    def __init__(self, name="NeuralNetwork", layers=None, **kwargs):
        super().__init__(name, **kwargs)
        self.layers = layers or [64, 32]
    
    def train(self, X, y):
        """Simplified training"""
        print(f"Training {self.name} with layers {self.layers}...")
        self.is_trained = True
        self.history['loss'] = [1.0 / (i+1) for i in range(self.epochs)]
        self.history['accuracy'] = [min(0.5 + i*0.005, 0.99) for i in range(self.epochs)]
    
    def predict(self, X):
        if not self.is_trained:
            raise RuntimeError("Model must be trained first!")
        return [1 if sum(x) > 0 else 0 for x in X]
    
    def summary(self):
        """Override to include layer info"""
        super().summary()  # Call parent summary
        print(f"  Layers: {self.layers}")


print("\n=== ML MODEL INHERITANCE ===")

# Create models
lr_model = LinearRegression(epochs=50)
nn_model = NeuralNetwork(layers=[128, 64, 32], epochs=100)

# Both share common interface
lr_model.summary()
print()
nn_model.summary()

# Train and predict
X_train = [[1, 2], [3, 4], [5, 6]]
y_train = [3, 7, 11]

lr_model.train(X_train, y_train)
nn_model.train(X_train, y_train)

print(f"\nLR predictions: {lr_model.predict([[2, 3], [4, 5]])}")
print(f"NN predictions: {nn_model.predict([[2, 3], [-1, -2]])}")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Basic Inheritance
   class Child(Parent):
   - Child inherits all attributes and methods from Parent
   - Use isinstance() to check type
   - Use issubclass() to check class hierarchy

2. super() Function
   - super().__init__() calls parent constructor
   - super().method() calls parent method
   - Follows Method Resolution Order (MRO)
   - Preferred over Parent.__init__(self)

3. Overriding
   - Class variables can be overridden in subclasses
   - Methods can be overridden (same name, different implementation)
   - Call super().method() to extend rather than replace

4. Method Resolution Order (MRO)
   - Order in which classes are searched for methods
   - View with Class.__mro__ or Class.mro()
   - Important for multiple inheritance

5. Inheritance vs Composition
   - Inheritance: "is-a" relationship
   - Composition: "has-a" relationship
   - Prefer composition for flexibility

6. Best Practices
   - Keep inheritance hierarchies shallow
   - Use abstract base classes for interfaces
   - Override methods to specialize behavior
   - Always call super().__init__() in child __init__
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Vehicle Hierarchy [EASY]
# Create Vehicle base class with Car and Motorcycle subclasses
# Vehicle: make, model, year, start(), stop()
# Car: add num_doors
# Motorcycle: add has_sidecar
# TODO: Write your code here

# Solution:
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.running = False
#     
#     def start(self):
#         self.running = True
#         return f"{self.make} {self.model} started"
#     
#     def stop(self):
#         self.running = False
#         return f"{self.make} {self.model} stopped"
# 
# class Car(Vehicle):
#     def __init__(self, make, model, year, num_doors=4):
#         super().__init__(make, model, year)
#         self.num_doors = num_doors
# 
# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, has_sidecar=False):
#         super().__init__(make, model, year)
#         self.has_sidecar = has_sidecar


# Exercise 2: Shape Hierarchy [EASY]
# Create Shape base with Circle, Rectangle, Triangle
# Each should calculate area() and perimeter()
# TODO: Write your code here

# Solution:
# import math
# class Shape:
#     def area(self):
#         raise NotImplementedError
#     def perimeter(self):
#         raise NotImplementedError
# 
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
#     def perimeter(self):
#         return 2 * math.pi * self.radius
# 
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)


# Exercise 3: Bank Account Hierarchy [MEDIUM]
# BankAccount base with SavingsAccount, CheckingAccount
# SavingsAccount: interest_rate, apply_interest()
# CheckingAccount: overdraft_limit, can handle negative balance
# TODO: Write your code here

# Solution:
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     
#     def deposit(self, amount):
#         self.balance += amount
#     
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return True
#         return False
# 
# class SavingsAccount(BankAccount):
#     def __init__(self, owner, balance=0, interest_rate=0.02):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#     
#     def apply_interest(self):
#         self.balance *= (1 + self.interest_rate)
# 
# class CheckingAccount(BankAccount):
#     def __init__(self, owner, balance=0, overdraft_limit=100):
#         super().__init__(owner, balance)
#         self.overdraft_limit = overdraft_limit
#     
#     def withdraw(self, amount):
#         if amount <= self.balance + self.overdraft_limit:
#             self.balance -= amount
#             return True
#         return False


# Exercise 4: ML Dataset Hierarchy [MEDIUM]
# BaseDataset with ImageDataset, TextDataset, TabularDataset
# Common: load(), split(), shuffle()
# Specific: image augmentation, text tokenization, feature scaling
# TODO: Write your code here

# Solution:
# class BaseDataset:
#     def __init__(self, name):
#         self.name = name
#         self.data = []
#     
#     def load(self, filepath):
#         raise NotImplementedError
#     
#     def split(self, ratio=0.8):
#         idx = int(len(self.data) * ratio)
#         return self.data[:idx], self.data[idx:]
#     
#     def shuffle(self):
#         import random
#         random.shuffle(self.data)
# 
# class ImageDataset(BaseDataset):
#     def __init__(self, name, image_size=(224, 224)):
#         super().__init__(name)
#         self.image_size = image_size
#     
#     def augment(self):
#         print(f"Augmenting images to size {self.image_size}")
# 
# class TextDataset(BaseDataset):
#     def __init__(self, name, vocab_size=10000):
#         super().__init__(name)
#         self.vocab_size = vocab_size
#     
#     def tokenize(self):
#         print(f"Tokenizing with vocab size {self.vocab_size}")


# Exercise 5: Logger Hierarchy [CHALLENGE]
# BaseLogger with FileLogger, ConsoleLogger, DatabaseLogger
# Support log levels: DEBUG, INFO, WARNING, ERROR
# TODO: Write your code here

# Solution:
# class BaseLogger:
#     LEVELS = {'DEBUG': 0, 'INFO': 1, 'WARNING': 2, 'ERROR': 3}
#     
#     def __init__(self, min_level='INFO'):
#         self.min_level = min_level
#     
#     def _should_log(self, level):
#         return self.LEVELS[level] >= self.LEVELS[self.min_level]
#     
#     def _format(self, level, message):
#         from datetime import datetime
#         return f"[{datetime.now()}] {level}: {message}"
#     
#     def log(self, level, message):
#         raise NotImplementedError
# 
# class ConsoleLogger(BaseLogger):
#     def log(self, level, message):
#         if self._should_log(level):
#             print(self._format(level, message))
# 
# class FileLogger(BaseLogger):
#     def __init__(self, filepath, min_level='INFO'):
#         super().__init__(min_level)
#         self.filepath = filepath
#     
#     def log(self, level, message):
#         if self._should_log(level):
#             with open(self.filepath, 'a') as f:
#                 f.write(self._format(level, message) + '\n')


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting to call super().__init__()
   ❌ def __init__(self, x):
          self.x = x  # Parent not initialized!
   ✅ def __init__(self, x):
          super().__init__()
          self.x = x

2. Using Parent.__init__(self) instead of super()
   ❌ Employee.__init__(self, first, last, pay)
   ✅ super().__init__(first, last, pay)

3. Mutable default arguments
   ❌ def __init__(self, items=[]):
   ✅ def __init__(self, items=None):
          self.items = items if items is not None else []

4. Deep inheritance hierarchies
   ❌ A -> B -> C -> D -> E -> F (too deep!)
   ✅ Keep it shallow, use composition

5. Overriding without calling super()
   ❌ def method(self):
          # Parent method completely replaced
   ✅ def method(self):
          super().method()  # Extend parent
          # Additional functionality

6. Tight coupling between parent and child
   - Child shouldn't depend on internal details of parent
   - Use public interface only

7. "Is-a" vs "Has-a" confusion
   - Stack IS NOT an ArrayList (composition!)
   - Dog IS AN Animal (inheritance!)
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("INHERITANCE DEMONSTRATION")
    print("="*60)
    
    # Setup classes
    class Employee:
        raise_amt = 1.04
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
        def fullname(self):
            return f"{self.first} {self.last}"
        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)
    
    class Developer(Employee):
        raise_amt = 1.10
        def __init__(self, first, last, pay, prog_lang):
            super().__init__(first, last, pay)
            self.prog_lang = prog_lang
    
    class Manager(Employee):
        def __init__(self, first, last, pay, employees=None):
            super().__init__(first, last, pay)
            self.employees = employees or []
        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)
        def print_emps(self):
            for emp in self.employees:
                print(f"  --> {emp.fullname()}")
    
    # Demo
    print("\n1. Creating instances:")
    dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
    dev_2 = Developer('Test', 'Employee', 60000, 'Java')
    mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
    
    print(f"   Developer: {dev_1.fullname()} - {dev_1.prog_lang}")
    print(f"   Manager: {mgr_1.fullname()}")
    
    print("\n2. Manager's team:")
    mgr_1.add_emp(dev_2)
    mgr_1.print_emps()
    
    print("\n3. Different raise amounts:")
    print(f"   Employee raise_amt: {Employee.raise_amt}")
    print(f"   Developer raise_amt: {Developer.raise_amt}")
    
    print("\n4. isinstance checks:")
    print(f"   isinstance(dev_1, Developer): {isinstance(dev_1, Developer)}")
    print(f"   isinstance(dev_1, Employee): {isinstance(dev_1, Employee)}")
    
    print("\n" + "="*60)