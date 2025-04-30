# Find Maximum

"""
Your colleague has implemented a custom function to find the maximum value in a list. 
However, the function sometimes works correctly, but other times it produces incorrect 
results. Can you help your colleague fix the bug?

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

"""

# My response:
"""
As max_number is initialised to 0, if numbers only contains negative numerals,
number in numbers would never > 0, hence return of max_number will be 0.

i.e. the third print statement will output 0 rather than -2.

Below is the amended code to ensure the max number is output.
"""
def find_maximum(numbers):
    if numbers:
        return max(numbers)

print(find_maximum([45, 3, 10, 98, 22]))  # 98
print(find_maximum([-1, 0, 5, 3]))        #  5
print(find_maximum([-10, -3, -20, -2]))   #  -2

# LSBot's comments:

"""
Opportunities for improvement
I was impressed by your ability to correctly identify the bug and provide a working solution! 
For further improvement, I would suggest two approaches:

1. If you want to use Python's built-in max() function, you could simplify your code to:

def find_maximum(numbers):
if not numbers:
    return None
return max(numbers)

2. If you want to implement the algorithm manually (which might have been the intention of the 
exercise), you could initialize max_number to the first element of the list or to negative 
infinity:

def find_maximum(numbers):
if not numbers:
    return None
max_number = numbers[0]  # Start with the first element
for number in numbers:
    if number > max_number:
        max_number = number
return max_number

"""