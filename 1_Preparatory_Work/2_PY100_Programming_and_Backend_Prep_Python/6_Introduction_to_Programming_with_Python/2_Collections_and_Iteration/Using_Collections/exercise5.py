# Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})

# My response:

'cat'                           # yes - immutable  
(3, 1, 4, 1, 5, 9, 2)           # yes - immutable
['a', 'b']                      # no - mutable
{'a': 1, 'b': 2}                # no - mutable
range(5)                        # yes - immutable
{1, 4, 9, 16, 25}               # no - mutable
3                               # yes - immutable
0.0                             # yes - immutable
frozenset({1, 4, 9, 16, 25})    # yes - immutable


# Launch School's answer:

['a', 'b']
{'a': 1, 'b': 2}
{1, 4, 9, 16, 25}   

# The first value is a list, the second another dict, and the last a set. 
# Since all 3 types are mutable, they can't be used as dict keys. 
# All remaining items are immutable built-in objects; they are acceptable dict keys.