# 7. Equality

"""
Predict the output of the code shown below. When you run the code, do you see what you expected? Why or why not?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)
"""

# My response:

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

# The output is True. The value assigned to list1 is equal to the value assigned to list2.

# LSBot's comments:

"""
I was impressed by your correct prediction! To enhance your understanding even further, you could expand 
your explanation to contrast the difference between the == operator (which compares values) and the is 
operator (which compares identity/memory location). For example, you could mention that while list1 == list2 
returns True, list1 is list2 would return False because they are distinct objects in memory despite having 
the same values. This distinction between equality and identity is an important concept in Python that will 
be valuable as you progress in your programming journey.
"""