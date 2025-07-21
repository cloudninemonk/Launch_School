"""
Write a function that takes a number as an argument. If the argument is a
positive number, return the negative of that number. If the argument is a
negative number, return it as-is.

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
"""
# ==========
# My Solution
# ==========
def negative(number):
    return - abs(number)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
print(negative(-5.34342834732) == -5.34342834732)
print(negative(3945864398564389576432895243) == -3945864398564389576432895243)