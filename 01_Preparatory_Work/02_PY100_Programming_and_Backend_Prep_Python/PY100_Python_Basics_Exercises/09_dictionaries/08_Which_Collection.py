# 8. Which Collection?

"""
Rewrite car as a list of lists in which each nested list contains two elements 
that represent the corresponding key/value pairs.

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

"""

# My response:

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print([list(element) for element in list(car.items())])

# LSBot's comments:

"""
Your solution shows strong Python skills with your use of list comprehensions! 
One small refinement would be to simplify your code by removing the redundant 
outer list() call:

[list(element) for element in car.items()]

Or you could make it even more explicit by unpacking the key-value pairs directly:

[[key, value] for key, value in car.items()]

Either of these approaches would be slightly more efficient and clearer about your 
intentions. Overall though, your solution is effective and shows good understanding 
of Python's data structure conversion techniques.
"""