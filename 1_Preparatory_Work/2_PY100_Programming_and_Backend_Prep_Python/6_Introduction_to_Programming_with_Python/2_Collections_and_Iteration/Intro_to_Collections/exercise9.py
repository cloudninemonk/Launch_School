my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# 1. Are the lists assigned to my_list and another_list equal?
# 2. Are the lists assigned to my_list and another_list the same object?
# 3. Are the nested lists at index 3 of my_list and another_list equal?
# 4. Are the nested lists at index 3 of my_list and another_list the same object?


# My response:

# 1. Yes, as they are shallow copied from my_list to another_list.
# 2. No, they are different objects with the same value.
# 3. Yes, as they are shallow copied from my_list to another_list.
# 4. Yes, they are the same object unless the nested list is reassigned.


# Launch School's answer:
# 1. The two lists are equal: they are both lists with the same elements.
# 2. The two lists are not the same object: The list constructor creates a new object.
# 3. The two nested lists are equal: they are both lists that have the same elements.
# 4. The two nested lists are the same object: the list constructor creates a shallow copy 
#    of the iterable passed as an argument. Shallow copies don't create new nested lists.
#    Instead, only a reference to the nested list gets copied.
