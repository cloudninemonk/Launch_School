# Without running this code, what will it print? Why?

# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = dict(dict1)
# dict1['a'][1] = 42
# print(dict2['a'])


# My response:

# [1, 2, 3]


# Launch School's answer:

# [1, 42, 3]

# As in the previous exercise, the constructor invocation dict(dict1) creates a new dict that contains the 
# same key/value pairs as dict1. Thus, dict2 is not the same object as dict1.

# On line 7, we reassign dict1['a'][1] to 42. Since dict1 and dict2 are different dicts, 
# you might expect that mutating one of dict1's values would not impact dict2. However, that is not the case. 
# The dicts are different objects but share value components since the dict constructor creates a shallow copy. 
# Thus, mutations to dict1['a'] can be seen in dict2['a'].

# This code demonstrates that two dicts with equal-value objects associated with every key may also share those objects. 
# That isn't always the case, but you must understand what's happening in your code.