"""
Write a function that takes one integer argument and returns True when the
number's absolute value is odd, False otherwise.
"""
# ==========
# My Solution
# ==========

def is_odd(number):
    return abs(number) % 2 != 0

print(is_odd(-7))
print(is_odd(8))
print(is_odd(0))

# ==========
# LS Solution
# ==========

def is_odd(number):
    return abs(number) % 2 == 1

# The abs function returns the absolute value of the argument, ensuring it's
# positive. We then check whether the resulting number modulo 2 equals 1, which
# would indicate it's odd.

# It's actually not necessary to use abs here; when evaluating n % d where n is
# an integer and d is 1, -1, or 2, it doesn't matter whether n is positive or
# negative. However, if disn't 1, -1, or 2, it does matter. To make the code as
# clear as possible, using abs is a good idea.

# ==========
# LS Bot Solution
# ==========

