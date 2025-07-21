"""
Write a program that prompts the user for two positive numbers (floating-point),
then prints the results of the following operations on those two numbers:
addition, subtraction, product, quotient, floor quotient, remainder, and power.
Do not worry about validating the input.

==> Enter the first number:
3.141592
==> Enter the second number:
2.718282
==> 3.141592 + 2.718282 = 5.859811
==> 3.141592 - 2.718282 = 0.42324699999999993
==> 3.141592 * 2.718282 = 8.539561733178
==> 3.141592 / 2.718282 = 1.1557038600115808
==> 3.141592 // 2.718282 = 1.0
==> 3.141592 % 2.718282 = 0.42324699999999993
==> 3.141592 ** 2.718282 = 22.45792517468373
"""

# ==========
# My Solution
# ==========
# import operator

# def calculate(number1, number2):
#     operations = {'+': operator.add,
#                   '-': operator.sub,
#                   '*': operator.mul,
#                   '/': operator.truediv,
#                   '//': operator.floordiv,
#                   '%': operator.mod,
#                   '**': operator.pow
#     }
#     for calculation in operations.values():
#         print(calculation(number1, number2))

# number1 = float(input("Enter a positive number: "))
# number2 = float(input("Enter another positive number: "))

# calculate(number1, number2)


def calculate(number1, number2, operator):
    match operator:
        case '+': return number1 + number2
        case '-': return number1 - number2
        case '*': return number1 * number2
        case '/': return number1 / number2
        case '//': return number1 // number2
        case '%': return number1 % number2
        case '**': return number1 ** number2

number1 = float(input("Enter a positive number: "))
number2 = float(input("Enter another positive number: "))

for operator in ['+', '-', '*', '/', '//', '%', '**']:
    result = calculate(number1, number2, operator)
    print(f">>> {number1} {operator} {number2} = {result}")


