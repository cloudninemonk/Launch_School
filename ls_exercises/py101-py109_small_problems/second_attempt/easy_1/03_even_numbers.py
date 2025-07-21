"""
Print all even numbers from 1 to 99, inclusive, with each number on a separate
line.

Bonus Question: Can you solve the problem by iterating over just the even
numbers?

"""

# ==========
# My Solution
# ==========

# 1. No user input

for number in range(1, 100):
    if number % 2 == 0:
        print(number)

for number in range(2, 100, 2):
        print(number)

# 2. User input

number1 = int(input("Enter the starting number: "))
number2 = int(input("Enter the ending number: "))

for number in range(number1, number2):
    if number % 2 == 0:
        print(number)

# ==========
# LS Solution
# ==========

# for number in range(1, 100):
#     if number % 2 == 0:
#         print(number)

# # Discussion This is similar to the previous problem, but checks for even
# # numbers instead of odd numbers.

# # Bonus question:

# for number in range(2, 100, 2):
#     print(number)

# This solution directly iterates over the even numbers from 2 to 99 by using
# the range function with a step of 2. This way, there's no need to check
# whether a number is even.