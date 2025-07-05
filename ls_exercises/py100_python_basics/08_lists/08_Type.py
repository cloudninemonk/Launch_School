# 8. Type
"""
How can you check if a variable holds a value that is a list? Given two variables, verify whether the values they hold are lists.

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'
"""

# My response:

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

# Determining the class type

type(some_value1) # <class 'list'>
type(some_value2) # <class 'str'>

# Determining the class type name only

type(some_value1).__name__ # 'list'
type(some_value2).__name__ # 'str'

# Determining if the variables are lists using comparison operator

type(some_value1) == list # True
type(some_value2) == list # False

# Determining if the variables are of list instance

isinstance(some_value1, list)   # True
isinstance(some_value2, list)   # False



