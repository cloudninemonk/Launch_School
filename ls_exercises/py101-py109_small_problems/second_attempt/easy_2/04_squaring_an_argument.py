"""
Using the multiply function from the "Multiplying Two Numbers" exercise, write a
function that computes the square of its argument (the square is the result of
multiplying a number by itself).

Examples:

print(square(5) == 25)   # True
print(square(-8) == 64)  # True
"""
# ==========
# My Solution
# ==========
def square(number):
    return multiply(number, number)

def multiply(number1, number2):
    return number1 * number2

print(square(5) == 25)
print(square(-8) == 64)

# ==========
# LS Solution
# ==========
def multiply(num1, num2):
    return num1 * num2

def square(number):
    return multiply(number, number)

# Discussion

# Our implementation relies on the previous exercise's multiply function. The
# return value of multiply is the result of multiplying the arguments together,
# so we just pass it the same number twice. The result is the squared value.

# Further Exploration

# Suppose we want to generalize this function to a "power to
# the n" type function: cubed, to the 4th power, to the 5th, etc. How would we
# go about doing so while still using the multiply function?

# ==========
# My Solution
# ==========
def power(number, n):
    result = 1
    for i in range(n):
        result = multiply(result, number)
    return result

def multiply(number1, number2):
    return number1 * number2

print(power(4, 2))
