# Write a find_integers function that returns a list of all the integers from my_tuple:

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

# You can use the expression type(object) is int to determine whether an object is an integer. 
# For instance:

# print(type(True) is int)      # False (boolean)
# print(type([1, 2, 3]) is int) # False (list)
# print(type(3.141592) is int)  # False (float)
# print(type(77) is int)        # True

# You may receive a SyntaxWarning warning message from the last two examples. You can ignore that warning.


# My response:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(my_things):                       # parameter my_things accepts the argument my_tuple
    my_ints = []    
    for i in my_things:
        if type(i) is int:
            my_ints.append(i)
    return my_ints
        
integers = find_integers(my_tuple) 
print(integers)                    # [1, 3, -4]

# Comments:
# This is an ideal scenario to use comprehensions. 
# [ element for element in iterable if condition ]


# Launch School's answer:

# def find_integers(things):
#     return [ element
#              for element in things
#              if type(element) is int ]

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)
# integers = find_integers(my_tuple)
# print(integers)                    # [1, 3, -4]

# Our solution uses a list comprehension to iterate through the elements in the things argument and create a new list.

# It's worth noting that we used a list comprehension to iterate over the tuple.
# The main reason for that choice is that find_integers is expected to return a list, not a tuple.
# However, an even more important reason is that there is no such thing as a "tuple comprehension".
# Comprehensions don't care what kind of collection you're iterating, but the result must always be a list, set, or dictionary.