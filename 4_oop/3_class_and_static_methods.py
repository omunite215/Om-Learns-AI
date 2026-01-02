"""
================================================================================
PYTHON OOP: CLASS METHODS & STATIC METHODS
================================================================================
Day: 16

Description:
    Complete guide to class methods and static methods in Python. Covers
    @classmethod decorator, @staticmethod decorator, alternative constructors,
    utility functions, and when to use each type of method.

Learning Objectives:
    - Understand the difference between instance, class, and static methods
    - Create class methods with @classmethod decorator
    - Create static methods with @staticmethod decorator
    - Use class methods as alternative constructors
    - Know when to use each type of method

Prerequisites:
    - Classes and Instances (Day 15)
    - Class Variables (Day 16 Part 1)
================================================================================
"""

import datetime

# =============================================================================
# 1. THREE TYPES OF METHODS
# =============================================================================

"""
INSTANCE METHODS (Regular methods):
- First parameter: self (the instance)
- Can access/modify instance AND class state
- Most common type of method

CLASS METHODS:
- Decorated with @classmethod
- First parameter: cls (the class)
- Can access/modify CLASS state only
- Common for: alternative constructors, class-level operations

STATIC METHODS:
- Decorated with @staticmethod
- NO automatic first parameter
- Cannot access instance OR class state directly
- Common for: utility functions that belong to the class logically
"""


# =============================================================================
# 2. BASE EMPLOYEE CLASS
# =============================================================================

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        Employee.num_of_emps += 1
    
    # --- Instance method ---
    def fullname(self):
        """Instance method - has access to self"""
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        """Instance method - modifies instance state"""
        self.pay = int(self.pay * self.raise_amount)
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


# =============================================================================
# 3. CLASS METHODS (@classmethod)
# =============================================================================

"""
Class methods receive the CLASS as first argument (cls), not the instance.
Use cases:
- Modify class state that applies to all instances
- Alternative constructors (create instances in different ways)
- Factory methods
"""

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        Employee.num_of_emps += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # --- Class method to modify class variable ---
    @classmethod
    def set_raise_amt(cls, amount):
        """
        Set raise amount for ALL employees.
        cls = the class (Employee), not an instance
        """
        cls.raise_amount = amount
    
    # --- Class method as alternative constructor ---
    @classmethod
    def from_string(cls, emp_str):
        """
        Create Employee from string 'First-Last-Pay'.
        Convention: from_* for alternative constructors
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))  # cls() creates instance!
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


# --- Using class method to modify class state ---
print("=== CLASS METHOD: MODIFY CLASS STATE ===")

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(f"Before: Employee.raise_amount = {Employee.raise_amount}")
print(f"        emp_1.raise_amount = {emp_1.raise_amount}")
print(f"        emp_2.raise_amount = {emp_2.raise_amount}")

# Call class method on CLASS
Employee.set_raise_amt(1.05)

print(f"\nAfter Employee.set_raise_amt(1.05):")
print(f"        Employee.raise_amount = {Employee.raise_amount}")
print(f"        emp_1.raise_amount = {emp_1.raise_amount}")
print(f"        emp_2.raise_amount = {emp_2.raise_amount}")

# Can also call on instance (still modifies class!)
emp_1.set_raise_amt(1.06)

print(f"\nAfter emp_1.set_raise_amt(1.06):")
print(f"        Employee.raise_amount = {Employee.raise_amount}")
# Note: calling on emp_1 still modified the CLASS variable!


# --- Using class method as alternative constructor ---
print("\n=== CLASS METHOD: ALTERNATIVE CONSTRUCTOR ===")

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-80000'
emp_str_3 = 'Jane-Wilson-90000'

# Instead of parsing manually each time:
# first, last, pay = emp_str_1.split('-')
# new_emp = Employee(first, last, int(pay))

# Use the class method!
new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(f"From string '{emp_str_1}':")
print(f"  {new_emp_1}")
print(f"  Email: {new_emp_1.email}")
print(f"  Pay: ${new_emp_1.pay:,}")

print(f"\nTotal employees: {Employee.num_of_emps}")


# =============================================================================
# 4. WHY USE cls() INSTEAD OF ClassName()?
# =============================================================================

"""
Using cls() instead of Employee() in class methods enables proper inheritance!
"""

class Manager(Employee):
    """Manager is a type of Employee"""
    
    def __init__(self, first, last, pay, department):
        super().__init__(first, last, pay)
        self.department = department
    
    @classmethod
    def from_string(cls, mgr_str):
        """Override to handle department"""
        first, last, pay, dept = mgr_str.split('-')
        return cls(first, last, int(pay), dept)

print("\n=== WHY cls() MATTERS ===")

# Because Employee.from_string uses cls(), subclasses work correctly!
# If it used Employee() directly, it would always create Employee, not Manager

mgr_str = 'Alice-Johnson-100000-Engineering'
mgr = Manager.from_string(mgr_str)
print(f"Manager: {mgr.fullname()}")
print(f"Department: {mgr.department}")
print(f"Type: {type(mgr)}")  # <class 'Manager'>, not Employee!


# =============================================================================
# 5. STATIC METHODS (@staticmethod)
# =============================================================================

"""
Static methods don't receive self OR cls automatically.
They're essentially regular functions that belong to a class namespace.

Use when:
- Function is logically related to the class
- But doesn't need access to instance or class state
- Could be a standalone function but belongs with the class
"""

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"
        Employee.num_of_emps += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    
    # --- Static methods ---
    @staticmethod
    def is_workday(day):
        """
        Check if given date is a workday.
        No self or cls - doesn't need instance/class data!
        """
        # Monday = 0, Sunday = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    @staticmethod
    def validate_email(email):
        """Validate email format"""
        return '@' in email and '.' in email.split('@')[-1]
    
    @staticmethod
    def calculate_bonus(salary, performance_rating):
        """Calculate bonus based on salary and rating"""
        bonus_rates = {5: 0.20, 4: 0.15, 3: 0.10, 2: 0.05, 1: 0.0}
        rate = bonus_rates.get(performance_rating, 0)
        return salary * rate
    
    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


# --- Using static methods ---
print("\n=== STATIC METHODS ===")

# Check workday - call on class
my_date = datetime.date(2016, 7, 11)  # Monday
print(f"Is {my_date} ({my_date.strftime('%A')}) a workday? {Employee.is_workday(my_date)}")

saturday = datetime.date(2016, 7, 9)
print(f"Is {saturday} ({saturday.strftime('%A')}) a workday? {Employee.is_workday(saturday)}")

# Can also call on instance (but doesn't use instance data)
emp = Employee('Test', 'User', 50000)
sunday = datetime.date(2016, 7, 10)
print(f"Via instance - Is {sunday} a workday? {emp.is_workday(sunday)}")

# Other static methods
print(f"\nValidate 'test@company.com': {Employee.validate_email('test@company.com')}")
print(f"Validate 'invalid-email': {Employee.validate_email('invalid-email')}")

print(f"\nBonus for $50000 salary, rating 5: ${Employee.calculate_bonus(50000, 5):,.2f}")
print(f"Bonus for $50000 salary, rating 3: ${Employee.calculate_bonus(50000, 3):,.2f}")


# =============================================================================
# 6. WHEN TO USE WHICH METHOD?
# =============================================================================

"""
Decision guide:

1. Does it need access to instance data (self)?
   YES → Instance method
   NO → Continue to 2

2. Does it need access to class data (cls)?
   YES → Class method
   NO → Continue to 3

3. Is it logically related to the class?
   YES → Static method
   NO → Regular function outside class

Common patterns:
- Instance method: modify/read object state
- Class method: alternative constructors (from_*), modify class state
- Static method: utility/helper functions, validation
"""

print("\n=== METHOD TYPE COMPARISON ===")

class Demo:
    class_var = "I am a class variable"
    
    def __init__(self, value):
        self.instance_var = value
    
    def instance_method(self):
        """Access instance AND class"""
        return f"Instance: {self.instance_var}, Class: {Demo.class_var}"
    
    @classmethod
    def class_method(cls):
        """Access class only"""
        return f"Class: {cls.class_var}"
    
    @staticmethod
    def static_method(x, y):
        """Access neither - just a function"""
        return f"Sum: {x + y}"

d = Demo("Hello")

print(f"Instance method: {d.instance_method()}")
print(f"Class method (via class): {Demo.class_method()}")
print(f"Class method (via instance): {d.class_method()}")
print(f"Static method: {Demo.static_method(5, 3)}")


# =============================================================================
# 7. PRACTICAL ML/AI EXAMPLES
# =============================================================================

class Model:
    """ML Model with various method types"""
    
    models_created = 0
    default_config = {
        'learning_rate': 0.01,
        'epochs': 100,
        'batch_size': 32
    }
    
    def __init__(self, name, config=None):
        self.name = name
        self.config = config or Model.default_config.copy()
        self.is_trained = False
        self.metrics = {}
        
        Model.models_created += 1
    
    # Instance method - works with this specific model
    def train(self, X, y):
        """Train this specific model"""
        print(f"Training {self.name}...")
        self.is_trained = True
        self.metrics['accuracy'] = 0.85
    
    # Class method - alternative constructor
    @classmethod
    def from_config_file(cls, filepath):
        """Create model from config file"""
        import json
        with open(filepath, 'r') as f:
            config = json.load(f)
        name = config.pop('name', 'unnamed_model')
        return cls(name, config)
    
    @classmethod
    def create_ensemble(cls, base_name, n_models):
        """Create multiple models"""
        return [cls(f"{base_name}_{i}") for i in range(n_models)]
    
    @classmethod
    def set_default_config(cls, **kwargs):
        """Update default config for future models"""
        cls.default_config.update(kwargs)
    
    # Static method - utility functions
    @staticmethod
    def calculate_accuracy(y_true, y_pred):
        """Calculate accuracy metric"""
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_true) if y_true else 0
    
    @staticmethod
    def split_data(data, ratio=0.8):
        """Split data into train/test"""
        split_idx = int(len(data) * ratio)
        return data[:split_idx], data[split_idx:]
    
    @staticmethod
    def is_valid_config(config):
        """Validate model configuration"""
        required = ['learning_rate', 'epochs', 'batch_size']
        return all(key in config for key in required)
    
    def __repr__(self):
        status = "trained" if self.is_trained else "untrained"
        return f"Model('{self.name}', {status})"

print("\n=== ML MODEL EXAMPLE ===")

# Using instance method
model1 = Model("Classifier_v1")
print(f"Created: {model1}")

# Using class method - alternative constructor
ensemble = Model.create_ensemble("ensemble_model", 3)
print(f"Ensemble: {ensemble}")

# Using class method - modify defaults
Model.set_default_config(epochs=200, batch_size=64)
model2 = Model("Classifier_v2")
print(f"model2 config: {model2.config}")

# Using static methods
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 0]
print(f"\nAccuracy: {Model.calculate_accuracy(y_true, y_pred):.2%}")

config = {'learning_rate': 0.01, 'epochs': 100}
print(f"Valid config? {Model.is_valid_config(config)}")


# --- DataProcessor with multiple constructors ---
class DataProcessor:
    """Data processor with various loading methods"""
    
    supported_formats = ['csv', 'json', 'parquet']
    
    def __init__(self, data, name="unnamed"):
        self.data = data
        self.name = name
        self.processed = False
    
    @classmethod
    def from_csv(cls, filepath):
        """Load from CSV file"""
        import csv
        with open(filepath, 'r') as f:
            data = list(csv.DictReader(f))
        return cls(data, name=filepath)
    
    @classmethod
    def from_json(cls, filepath):
        """Load from JSON file"""
        import json
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls(data, name=filepath)
    
    @classmethod
    def from_dict(cls, data_dict):
        """Load from dictionary"""
        return cls(data_dict.get('data', []), name=data_dict.get('name', 'dict_data'))
    
    @staticmethod
    def is_supported(filepath):
        """Check if file format is supported"""
        ext = filepath.split('.')[-1].lower()
        return ext in DataProcessor.supported_formats
    
    @staticmethod
    def validate_data(data):
        """Validate data structure"""
        if not isinstance(data, (list, dict)):
            return False
        if isinstance(data, list) and len(data) == 0:
            return False
        return True


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Instance Methods
   - def method(self):
   - Access instance (self) and class
   - Most common type

2. Class Methods (@classmethod)
   - def method(cls):
   - Access class only, not instance
   - Use for: alternative constructors (from_*), modify class state
   - Use cls() not ClassName() for inheritance support

3. Static Methods (@staticmethod)
   - def method():
   - No access to instance or class
   - Use for: utility functions, validation, calculations
   - Could be standalone but logically belongs to class

4. Method Selection Guide
   - Need self? → Instance method
   - Need cls for constructors/class state? → Class method
   - Utility function related to class? → Static method

5. Naming Conventions
   - from_* for alternative constructors
   - is_* for boolean checks
   - validate_* for validation
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Person with Multiple Constructors [EASY]
# Create Person class with from_string, from_dict class methods
# TODO: Write your code here

# Solution:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     
#     @classmethod
#     def from_string(cls, s, sep=','):
#         name, age = s.split(sep)
#         return cls(name.strip(), int(age))
#     
#     @classmethod
#     def from_dict(cls, d):
#         return cls(d['name'], d['age'])


# Exercise 2: Temperature Class [EASY]
# Create class with from_celsius, from_fahrenheit class methods
# Static method for conversion formula
# TODO: Write your code here

# Solution:
# class Temperature:
#     def __init__(self, kelvin):
#         self.kelvin = kelvin
#     
#     @classmethod
#     def from_celsius(cls, c):
#         return cls(c + 273.15)
#     
#     @classmethod
#     def from_fahrenheit(cls, f):
#         return cls((f - 32) * 5/9 + 273.15)
#     
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return c * 9/5 + 32


# Exercise 3: Validator Class [MEDIUM]
# Create class with only static methods for validation
# email, phone, password, username
# TODO: Write your code here

# Solution:
# class Validator:
#     @staticmethod
#     def is_valid_email(email):
#         return '@' in email and '.' in email.split('@')[-1]
#     
#     @staticmethod
#     def is_valid_phone(phone):
#         digits = ''.join(c for c in phone if c.isdigit())
#         return len(digits) == 10
#     
#     @staticmethod
#     def is_valid_password(password):
#         return (len(password) >= 8 and
#                 any(c.isupper() for c in password) and
#                 any(c.isdigit() for c in password))


# Exercise 4: Date Class [MEDIUM]
# from_string, from_timestamp, today class methods
# is_leap_year, days_in_month static methods
# TODO: Write your code here

# Solution:
# class Date:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     
#     @classmethod
#     def from_string(cls, s, fmt='%Y-%m-%d'):
#         import datetime
#         dt = datetime.datetime.strptime(s, fmt)
#         return cls(dt.year, dt.month, dt.day)
#     
#     @classmethod
#     def today(cls):
#         import datetime
#         t = datetime.date.today()
#         return cls(t.year, t.month, t.day)
#     
#     @staticmethod
#     def is_leap_year(year):
#         return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#     
#     @staticmethod
#     def days_in_month(year, month):
#         if month in [4, 6, 9, 11]: return 30
#         if month == 2: return 29 if Date.is_leap_year(year) else 28
#         return 31


# Exercise 5: ML Metrics Class [MEDIUM]
# Create class with static methods for ML metrics
# accuracy, precision, recall, f1, mse, rmse
# TODO: Write your code here

# Solution:
# class Metrics:
#     @staticmethod
#     def accuracy(y_true, y_pred):
#         return sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)
#     
#     @staticmethod
#     def mse(y_true, y_pred):
#         return sum((t - p)**2 for t, p in zip(y_true, y_pred)) / len(y_true)
#     
#     @staticmethod
#     def rmse(y_true, y_pred):
#         return Metrics.mse(y_true, y_pred) ** 0.5


# Exercise 6: Config Manager [CHALLENGE]
# Singleton-like config with class methods
# load, save, get, set class methods
# TODO: Write your code here

# Solution:
# class Config:
#     _config = {}
#     _filepath = None
#     
#     @classmethod
#     def load(cls, filepath):
#         import json
#         cls._filepath = filepath
#         try:
#             with open(filepath) as f:
#                 cls._config = json.load(f)
#         except FileNotFoundError:
#             cls._config = {}
#     
#     @classmethod
#     def save(cls):
#         if cls._filepath:
#             import json
#             with open(cls._filepath, 'w') as f:
#                 json.dump(cls._config, f, indent=2)
#     
#     @classmethod
#     def get(cls, key, default=None):
#         return cls._config.get(key, default)
#     
#     @classmethod
#     def set(cls, key, value):
#         cls._config[key] = value


# =============================================================================
# COMMON MISTAKES TO AVOID
# =============================================================================
"""
1. Forgetting cls parameter in class methods
   ❌ @classmethod
      def method(): ...
   ✅ @classmethod
      def method(cls): ...

2. Using self in static methods
   ❌ @staticmethod
      def method(self): ...
   ✅ @staticmethod
      def method(): ...

3. Using ClassName() instead of cls() in constructors
   ❌ @classmethod
      def from_x(cls, x): return Employee(x)  # Breaks inheritance!
   ✅ @classmethod
      def from_x(cls, x): return cls(x)

4. Using static when class method needed
   ❌ @staticmethod
      def create(): return MyClass()
   ✅ @classmethod
      def create(cls): return cls()

5. Accessing self in class method
   ❌ @classmethod
      def method(cls): return self.attr
   ✅ @classmethod
      def method(cls): return cls.class_attr

6. Overcomplicating with wrong method type
   - Simple utility? → Static
   - Need instance? → Instance method
   - Alternative constructor? → Class method
"""


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("CLASS & STATIC METHODS DEMONSTRATION")
    print("="*60)
    
    class Employee:
        raise_amount = 1.04
        
        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
        
        @classmethod
        def set_raise_amt(cls, amount):
            cls.raise_amount = amount
        
        @classmethod
        def from_string(cls, s):
            first, last, pay = s.split('-')
            return cls(first, last, int(pay))
        
        @staticmethod
        def is_workday(day):
            return day.weekday() < 5
    
    print("\n1. Class method - modify class state:")
    Employee.set_raise_amt(1.05)
    print(f"   raise_amount = {Employee.raise_amount}")
    
    print("\n2. Class method - alternative constructor:")
    emp = Employee.from_string('John-Doe-50000')
    print(f"   Created: {emp.first} {emp.last}, ${emp.pay:,}")
    
    print("\n3. Static method - utility function:")
    import datetime
    today = datetime.date.today()
    print(f"   Is {today} a workday? {Employee.is_workday(today)}")
    
    print("\n" + "="*60)