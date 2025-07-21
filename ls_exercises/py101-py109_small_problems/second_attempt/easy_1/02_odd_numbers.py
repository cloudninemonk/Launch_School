"""
Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the odd numbers?

"""

# ==========
# My Solution
# ==========

# 1. No user input

for number in range(1, 100, 2):
    print(number)

# 2. User input

number1 = int(input("Enter the starting number: "))
number2 = int(input("Enter the ending number: "))

for number in range(number1, number2):
    if number % 2 != 0:
        print(number)



# ==========
# LS Solution
# ==========

# for number in range(1, 100):
#     if number % 2 == 1:
#         print(number)

# Discussion
# Our initial solution uses Python's range function to iterate over all numbers
# from 1 to 99. It then checks whether each number is odd using the condition
# number % 2 == 1 before printing it.

# If your approach was different from ours, don't worry. There are several ways
# to solve this problem.

# Bonus question:

# for number in range(1, 100, 2):
#     print(number)

# For the bonus question, we used the range function's third argument (the step)
# to increment by 2, starting from 1. This ensures that we only iterate over odd
# numbers, making the process more efficient.

# Further Exploration Consider adding a way for the user to specify the starting
# and ending values of the odd numbers printed.