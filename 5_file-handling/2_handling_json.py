"""
================================================================================
PYTHON FILE HANDLING: WORKING WITH JSON
================================================================================
Day: 19

Description:
    Complete guide to JSON handling in Python. Covers parsing JSON strings,
    reading/writing JSON files, serialization/deserialization, custom encoders,
    and practical patterns for configuration files and data exchange.

Learning Objectives:
    - Understand JSON format and its Python equivalents
    - Parse JSON strings with json.loads()
    - Convert Python objects to JSON with json.dumps()
    - Read and write JSON files with json.load()/json.dump()
    - Handle complex objects with custom encoders/decoders
    - Apply JSON in ML/AI configuration and data pipelines

Prerequisites:
    - File handling basics (Day 12)
    - Python data structures (lists, dicts)
================================================================================
"""

import json
from datetime import datetime, date
from typing import Any, Dict, List

# =============================================================================
# 1. WHAT IS JSON?
# =============================================================================

"""
JSON (JavaScript Object Notation):
- Lightweight data interchange format
- Human-readable text format
- Language-independent (works everywhere)
- Native support in Python via 'json' module

JSON ↔ Python Type Mapping:
JSON            Python
----            ------
object          dict
array           list
string          str
number (int)    int
number (float)  float
true            True
false           False
null            None

Why JSON matters for AI/ML:
- Configuration files for models/experiments
- API data exchange
- Saving/loading model metadata
- Logging training results
- Dataset annotations (COCO, etc.)
"""


# =============================================================================
# 2. PARSING JSON STRINGS (json.loads)
# =============================================================================

"""
json.loads() = Load String
Converts JSON string → Python object
"""

# --- JSON string example ---
people_string = """
{
  "people": [
    {
      "name": "Om",
      "emails": [
        "omunite21@gmail.com",
        "patel.omm@northeastern.edu"
      ],
      "has_license": false
    },
    {
      "name": "Omi",
      "emails": [
        "mypiano21502@gmail.com",
        "random@northeastern.edu"
      ],
      "has_license": true
    }
  ]
}
"""

# --- Parse JSON string to Python dict ---
data = json.loads(people_string)

print("=== json.loads() - Parse JSON String ===")
print(f"Type: {type(data)}")  # <class 'dict'>
print(f"Keys: {data.keys()}")

# --- Access nested data ---
print("\nPeople in data:")
for person in data['people']:
    print(f"  Name: {person['name']}")
    print(f"  Emails: {person['emails']}")
    print(f"  Has License: {person['has_license']}")
    print()

# --- Access specific fields ---
print("Email addresses:")
for person in data['people']:
    for email in person['emails']:
        print(f"  - {email}")


# =============================================================================
# 3. CONVERTING TO JSON STRINGS (json.dumps)
# =============================================================================

"""
json.dumps() = Dump String
Converts Python object → JSON string

Parameters:
- indent: Pretty print with indentation
- sort_keys: Sort dictionary keys
- separators: Custom separators (compact output)
- ensure_ascii: Escape non-ASCII characters
"""

# --- Basic conversion ---
python_dict = {
    "name": "Om Patel",
    "age": 22,
    "skills": ["Python", "ML", "Deep Learning"],
    "is_student": True,
    "gpa": None
}

json_string = json.dumps(python_dict)
print("\n=== json.dumps() - Convert to JSON String ===")
print(f"Basic: {json_string}")

# --- Pretty print with indent ---
pretty_json = json.dumps(python_dict, indent=2)
print(f"\nPretty (indent=2):\n{pretty_json}")

# --- Sort keys ---
sorted_json = json.dumps(python_dict, indent=2, sort_keys=True)
print(f"\nSorted keys:\n{sorted_json}")

# --- Compact output ---
compact_json = json.dumps(python_dict, separators=(',', ':'))
print(f"\nCompact: {compact_json}")

# --- Handle non-ASCII characters ---
unicode_dict = {"name": "北京", "city": "東京", "emoji": "🐍"}
ascii_json = json.dumps(unicode_dict, ensure_ascii=True)
unicode_json = json.dumps(unicode_dict, ensure_ascii=False)
print(f"\nASCII escaped: {ascii_json}")
print(f"Unicode preserved: {unicode_json}")


# =============================================================================
# 4. READING JSON FILES (json.load)
# =============================================================================

"""
json.load() = Load from File
Reads JSON file → Python object
"""

# --- Read JSON file ---
print("\n=== json.load() - Read JSON File ===")

try:
    with open('5_file-handling/states.json', 'r', encoding='utf-8') as f:
        states_data = json.load(f)
    
    print(f"Loaded {len(states_data.get('states', []))} states")
    
    # Access data
    for state in states_data['states'][:3]:  # First 3 states
        print(f"  {state['name']} ({state['abbreviation']})")
    print("  ...")
    
except FileNotFoundError:
    print("states.json not found - creating sample data...")
    states_data = {
        "states": [
            {"name": "California", "abbreviation": "CA", "area_codes": ["209", "213"]},
            {"name": "Texas", "abbreviation": "TX", "area_codes": ["210", "214"]},
            {"name": "New York", "abbreviation": "NY", "area_codes": ["212", "315"]}
        ]
    }

# --- Safe JSON loading with error handling ---
def load_json_safe(filepath, default=None):
    """Load JSON file with error handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return default
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filepath}: {e}")
        return default


# =============================================================================
# 5. WRITING JSON FILES (json.dump)
# =============================================================================

"""
json.dump() = Dump to File
Writes Python object → JSON file
"""

print("\n=== json.dump() - Write JSON File ===")

# --- Modify and write data ---
# Remove area_codes from states
if 'states' in states_data:
    modified_data = {'states': []}
    for state in states_data['states']:
        new_state = {k: v for k, v in state.items() if k != 'area_codes'}
        modified_data['states'].append(new_state)
    
    # Write to new file
    with open('5_file-handling/new_states.json', 'w', encoding='utf-8') as f:
        json.dump(modified_data, f, indent=2)
    
    print("Created new_states.json (without area_codes)")

# --- Write with all options ---
config = {
    "model": "ResNet50",
    "epochs": 100,
    "learning_rate": 0.001,
    "batch_size": 32
}

with open('5_file-handling/config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, sort_keys=True)
print("Created config.json")


# =============================================================================
# 6. HANDLING COMPLEX TYPES (Custom Encoders)
# =============================================================================

"""
JSON doesn't support datetime, sets, custom objects by default.
Solution: Custom JSONEncoder or default function.
"""

# --- The Problem ---
complex_data = {
    "name": "Experiment",
    "created": datetime.now(),
    "tags": {"ml", "python", "training"}  # set
}

try:
    json.dumps(complex_data)
except TypeError as e:
    print(f"\n=== Custom Encoders ===")
    print(f"Error: {e}")

# --- Solution 1: default function ---
def json_serializer(obj):
    """Custom serializer for non-JSON types"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, set):
        return list(obj)
    elif hasattr(obj, '__dict__'):
        return obj.__dict__
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

json_string = json.dumps(complex_data, default=json_serializer, indent=2)
print(f"With custom serializer:\n{json_string}")

# --- Solution 2: Custom JSONEncoder class ---
class CustomEncoder(json.JSONEncoder):
    """Custom JSON encoder for complex types"""
    
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return {'__datetime__': obj.isoformat()}
        elif isinstance(obj, set):
            return {'__set__': list(obj)}
        elif hasattr(obj, 'to_dict'):
            return obj.to_dict()
        return super().default(obj)

json_string = json.dumps(complex_data, cls=CustomEncoder, indent=2)
print(f"\nWith CustomEncoder:\n{json_string}")


# =============================================================================
# 7. CUSTOM DECODERS (Object Hook)
# =============================================================================

"""
Use object_hook to convert JSON back to Python objects.
"""

def json_deserializer(dct):
    """Custom deserializer for complex types"""
    if '__datetime__' in dct:
        return datetime.fromisoformat(dct['__datetime__'])
    elif '__set__' in dct:
        return set(dct['__set__'])
    return dct

# Round-trip example
original = {
    "event": "Training Started",
    "timestamp": datetime(2024, 12, 17, 14, 30, 0),
    "tags": {"ml", "experiment"}
}

# Encode
encoded = json.dumps(original, cls=CustomEncoder)
print(f"\n=== Custom Decoder ===")
print(f"Encoded: {encoded}")

# Decode
decoded = json.loads(encoded, object_hook=json_deserializer)
print(f"Decoded timestamp type: {type(decoded.get('timestamp', {}).get('__datetime__', 'N/A'))}")


# =============================================================================
# 8. JSON VALIDATION AND SCHEMA
# =============================================================================

def validate_config(config: dict, schema: dict) -> List[str]:
    """Simple JSON validation against schema"""
    errors = []
    
    # Check required fields
    for field in schema.get('required', []):
        if field not in config:
            errors.append(f"Missing required field: {field}")
    
    # Check types
    for field, expected_type in schema.get('types', {}).items():
        if field in config:
            if not isinstance(config[field], expected_type):
                errors.append(f"Invalid type for {field}: expected {expected_type.__name__}")
    
    # Check ranges
    for field, (min_val, max_val) in schema.get('ranges', {}).items():
        if field in config:
            if not min_val <= config[field] <= max_val:
                errors.append(f"{field} must be between {min_val} and {max_val}")
    
    return errors


print("\n=== JSON Validation ===")

config_schema = {
    'required': ['model', 'epochs', 'learning_rate'],
    'types': {'epochs': int, 'learning_rate': float, 'batch_size': int},
    'ranges': {'epochs': (1, 1000), 'learning_rate': (0, 1)}
}

test_config = {"model": "ResNet", "epochs": 100, "learning_rate": 0.01}
errors = validate_config(test_config, config_schema)
print(f"Valid config errors: {errors}")

bad_config = {"epochs": "100", "learning_rate": 5.0}
errors = validate_config(bad_config, config_schema)
print(f"Bad config errors: {errors}")


# =============================================================================
# 9. PRACTICAL ML/AI UTILITIES
# =============================================================================

class ConfigManager:
    """Manage JSON configuration files"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.config = self._load()
    
    def _load(self) -> dict:
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value):
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            config = config.setdefault(k, {})
        config[keys[-1]] = value
        self.save()


class ExperimentLogger:
    """Log experiment results to JSON"""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.experiments = self._load()
    
    def _load(self) -> list:
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def log(self, name: str, params: dict, metrics: dict):
        experiment = {
            'name': name,
            'timestamp': datetime.now().isoformat(),
            'params': params,
            'metrics': metrics
        }
        self.experiments.append(experiment)
        self._save()
    
    def _save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.experiments, f, indent=2, default=str)
    
    def get_best(self, metric: str, mode: str = 'max') -> dict:
        if not self.experiments:
            return None
        key = lambda x: x['metrics'].get(metric, float('-inf') if mode == 'max' else float('inf'))
        return max(self.experiments, key=key) if mode == 'max' else min(self.experiments, key=key)


def merge_configs(*configs: dict) -> dict:
    """Deep merge multiple config dictionaries"""
    result = {}
    for config in configs:
        for key, value in config.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_configs(result[key], value)
            else:
                result[key] = value
    return result


print("\n=== ML Config Manager ===")
# Example usage (would need actual file)
# config = ConfigManager('config.json')
# config.set('model.layers', [64, 128, 64])
# print(config.get('model.layers'))


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
"""
1. Core Functions
   - json.loads(string): JSON string → Python object
   - json.dumps(obj): Python object → JSON string
   - json.load(file): JSON file → Python object
   - json.dump(obj, file): Python object → JSON file

2. Formatting Options
   - indent: Pretty print
   - sort_keys: Alphabetical order
   - separators: Custom separators
   - ensure_ascii: Handle Unicode

3. Custom Types
   - default parameter or custom JSONEncoder for serialization
   - object_hook for deserialization
   - Handle datetime, sets, custom classes

4. Best Practices
   - Always use 'with' for file operations
   - Use encoding='utf-8' explicitly
   - Handle JSONDecodeError for invalid JSON
   - Validate config before using

5. ML/AI Use Cases
   - Model configuration files
   - Experiment logging
   - Dataset annotations
   - API responses
"""


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

# Exercise 1: Parse and Filter [EASY]
# Parse JSON string, filter items by condition
# TODO: Write your code here

# Exercise 2: Config Merger [MEDIUM]
# Merge base config with overrides from file
# TODO: Write your code here

# Exercise 3: JSON Schema Validator [CHALLENGE]
# Implement more complete schema validation
# TODO: Write your code here


# =============================================================================
# RUN EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("JSON HANDLING DEMONSTRATION")
    print("="*60)
    
    # Quick demo
    sample = {"name": "Test", "values": [1, 2, 3], "active": True}
    
    print("\n1. Python → JSON string:")
    print(f"   {json.dumps(sample)}")
    
    print("\n2. JSON string → Python:")
    json_str = '{"x": 10, "y": 20}'
    print(f"   {json.loads(json_str)}")
    
    print("\n3. Pretty print:")
    print(json.dumps(sample, indent=2))