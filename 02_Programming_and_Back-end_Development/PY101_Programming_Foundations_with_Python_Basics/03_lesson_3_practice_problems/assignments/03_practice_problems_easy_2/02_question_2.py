"""
Given a number and a list, determine whether the number is included in the list.

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
"""
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]
number1 = 8
number2 = 95

try:
    check_value = numbers.index(number1)
    print(True)
except ValueError:
    print(False)

try:
    check_value = numbers.index(number2)
    print(True)
except ValueError:
    print(False)

# Whilst my solution achieves the intended result, it is inefficient.
# Better off using the 'in' expression.

"""
LS Solution
"""
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]
number1 = 8
number2 = 95

number1 in numbers  # False
number2 in numbers  # True

