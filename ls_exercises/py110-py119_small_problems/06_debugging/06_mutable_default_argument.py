'''
We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:
How would you fix this code?

def append_to_list(value, lst=[]):
    lst.append(value)
    print(lst)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
'''

# The function correctly appends and returns [1] for the first function call. However, for the second, as lst = [1] at this point is a shared parameter across all function calls, when the value 2 is passed as an argument to the function, it too is appended to the same lst object, resulting in lst = [1, 2]. Rather, a new local variable should be included in the function rather than a default parameter.

# ==========
# My Solution
# ==========
def append_to_list(value):
    lst = []
    lst.append(value)
    print(lst)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

# ==========
# LS Solution
# ==========
def append_to_list(value, lst=None): # Including a None value for lst allows for a list argument to be passed to the function. Otherwise, lst = None.
    if lst is None:
        lst = []
    lst.append(value)
    return lst
