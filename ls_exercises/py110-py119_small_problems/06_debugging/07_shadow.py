'''
We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
'''
# The built-in sum function identifier is the same as the custom function identifier sum. For the return line, the sum function is attempting to call the function it is contained within. To avoid this behaviour, ensure unique identifier name for the custom function e.g., total_sum

# ==========
# My Solution
# ==========
def total_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(total_sum(numbers, 2) == 20)

# ==========
# LS Solution
# ==========
def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20) # True
