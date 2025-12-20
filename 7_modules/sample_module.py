"""
================================================================================
SAMPLE MODULE - Example Custom Module
================================================================================
Day: 5

Description:
    A sample module demonstrating how to create reusable Python modules.
    This module provides utility functions for working with lists.

Usage:
    import sample_module
    sample_module.find_index(['a', 'b', 'c'], 'b')
    
    # Or import specific functions
    from sample_module import find_index, find_all_indices
================================================================================
"""

# =============================================================================
# MODULE-LEVEL VARIABLES (Constants)
# =============================================================================

# This will print when module is imported (not recommended!)
# Use if __name__ == "__main__" to prevent this
# print("Welcome to sample_module")

# Module constants
MODULE_VERSION = "1.0.0"
MODULE_AUTHOR = "Om"

# A test variable
test = "Test string from sample_module"


# =============================================================================
# FUNCTIONS
# =============================================================================

def find_index(to_search, target):
    """
    Find the index of a target value in a list.
    
    Parameters:
    -----------
    to_search : list
        The list to search through
    target : any
        The value to find
    
    Returns:
    --------
    int
        Index of target if found, -1 otherwise
    
    Examples:
    ---------
    >>> find_index(['a', 'b', 'c'], 'b')
    1
    >>> find_index([1, 2, 3], 5)
    -1
    """
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1


def find_all_indices(to_search, target):
    """
    Find all indices where target appears in a list.
    
    Parameters:
    -----------
    to_search : list
        The list to search through
    target : any
        The value to find
    
    Returns:
    --------
    list
        List of indices where target was found
    
    Examples:
    ---------
    >>> find_all_indices([1, 2, 1, 3, 1], 1)
    [0, 2, 4]
    """
    indices = []
    for i, value in enumerate(to_search):
        if value == target:
            indices.append(i)
    return indices


def count_occurrences(to_search, target):
    """
    Count how many times target appears in a list.
    
    Parameters:
    -----------
    to_search : list
        The list to search through
    target : any
        The value to count
    
    Returns:
    --------
    int
        Number of occurrences
    
    Examples:
    ---------
    >>> count_occurrences([1, 2, 1, 3, 1], 1)
    3
    """
    return len(find_all_indices(to_search, target))


def remove_duplicates(to_clean):
    """
    Remove duplicates from a list while preserving order.
    
    Parameters:
    -----------
    to_clean : list
        The list to clean
    
    Returns:
    --------
    list
        New list with duplicates removed
    
    Examples:
    ---------
    >>> remove_duplicates([1, 2, 2, 3, 1, 4])
    [1, 2, 3, 4]
    """
    seen = set()
    result = []
    for item in to_clean:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten_list(nested_list):
    """
    Flatten a nested list into a single list.
    
    Parameters:
    -----------
    nested_list : list
        A list that may contain nested lists
    
    Returns:
    --------
    list
        Flattened list
    
    Examples:
    ---------
    >>> flatten_list([[1, 2], [3, 4], [5]])
    [1, 2, 3, 4, 5]
    """
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


# =============================================================================
# PRIVATE FUNCTIONS (Convention: prefix with _)
# =============================================================================

def _helper_function():
    """
    This is a private function (by convention).
    It won't be imported with 'from sample_module import *'
    """
    return "I'm a helper function"


# =============================================================================
# MODULE TEST CODE
# =============================================================================

# This code only runs when the module is executed directly,
# NOT when it's imported by another module

if __name__ == "__main__":
    print("=" * 50)
    print("Running sample_module.py directly")
    print("=" * 50)
    
    # Test data
    courses = ['History', 'Math', 'Physics', 'ComSci', 'Math']
    
    # Test find_index
    print(f"\nTesting find_index:")
    print(f"  courses = {courses}")
    print(f"  find_index(courses, 'Math') = {find_index(courses, 'Math')}")
    print(f"  find_index(courses, 'Art') = {find_index(courses, 'Art')}")
    
    # Test find_all_indices
    print(f"\nTesting find_all_indices:")
    print(f"  find_all_indices(courses, 'Math') = {find_all_indices(courses, 'Math')}")
    
    # Test count_occurrences
    print(f"\nTesting count_occurrences:")
    print(f"  count_occurrences(courses, 'Math') = {count_occurrences(courses, 'Math')}")
    
    # Test remove_duplicates
    print(f"\nTesting remove_duplicates:")
    print(f"  remove_duplicates(courses) = {remove_duplicates(courses)}")
    
    # Test flatten_list
    print(f"\nTesting flatten_list:")
    nested = [[1, 2], [3, [4, 5]], [6]]
    print(f"  flatten_list({nested}) = {flatten_list(nested)}")
    
    # Test variable
    print(f"\nModule variables:")
    print(f"  test = '{test}'")
    print(f"  MODULE_VERSION = '{MODULE_VERSION}'")
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)