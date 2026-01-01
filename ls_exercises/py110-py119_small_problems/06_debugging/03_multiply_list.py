'''
You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.

def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])
'''
# The for loop is iterating through each element in the list and multiplying it by 2. However, there is no modification to the original list or is there a construction of a new list with the resulting multiplied values. Therefore, the lst return is the same as the original lst argument passed to the function.

# solution 1
def multiply_list(lst):
    for idx, value in enumerate(lst):
        lst[idx] = value * 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# solution 2
def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# ==========
# LS Solution
# ==========
def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])  # True