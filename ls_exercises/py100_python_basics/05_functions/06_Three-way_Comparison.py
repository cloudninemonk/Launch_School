# 6. Three-way Comparison
"""

Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 
1 if the second string is shorter, and 0 if they're of equal length. For example:

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0

"""

# My response:

def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        print(-1)
    elif len(str1) > len(str2):
        print(1)
    else:
        print(0)


compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0

# Comments:
"""

# The question specifically asks for the result to be returned, rather than printed within the function.

"""

# Launch School's solution:

"""

def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        return 0

"""