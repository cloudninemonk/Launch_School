# 1. First Element

"""
Write a function that returns the first element of a list provided as an argument. For example:

print(first(['Earth', 'Moon', 'Mars']))  # Earth

Be sure to handle the case where the input list is empty.
"""

# My response:

def first(planets):
    if planets:
        return planets[0]
    else:
        return

print(first([]))  # None
print(first(['Earth', 'Moon', 'Mars'])) # Earth

# LSBot comments:
"""
When you use return without a value in Python, it implicitly returns None. 
This works correctly but it might be more explicit to return None directly.

def first(lst):
    if lst:  # Using Python's truthiness to check if list is not empty
        return lst[0]
    else:
        return None  # Explicitly returning None for empty lists
"""