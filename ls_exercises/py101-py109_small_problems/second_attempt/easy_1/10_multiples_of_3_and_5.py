"""
Write a function that computes the sum of all numbers between 1 and some other
number, inclusive, that are multiples of 3 or 5. For instance, if the supplied
number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
"""
# ==========
# My Solution
# ==========

def multisum(integer):
    result = 0
    for number in range(1, integer + 1):
        if number % 3 == 0 or number % 5 == 0:
            result += number
    return result

print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)

# ==========
# LS Solution
# ==========

def is_multiple(number, divisor):
    return number % divisor == 0

def multisum(max_value):
    total_sum = 0
    for number in range(1, max_value + 1):
        if is_multiple(number, 3) or is_multiple(number, 5):
            total_sum += number
    return total_sum

# Discussion

# The solution begins with an is_multiple function that returns True
# if the given number is a multiple of the divisor, or False if it is not. This
# function isn't entirely necessary, but it makes the main function more
# readable.

# The main function, multisum, adds each appropriate value in the range to our sum variable.
