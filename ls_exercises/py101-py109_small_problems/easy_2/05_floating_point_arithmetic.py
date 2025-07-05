"""
Write a program that prompts the user for two positive numbers (floating-point),
then prints the results of the following operations on those two numbers: addition,
subtraction, product, quotient, floor quotient, remainder, and power. Do not worry
about validating the input.

Examples:
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
# def addition(number1, number2):
#     """Return the addition of two numbers."""
#     return number1 + number2

# def subtraction(number1, number2):
#     """Return the subtractions of two numbers."""
#     return number1 - number2

# def product(number1, number2):
#     """Return the product of two numbers."""
#     return number1 * number2

# def quotient(number1, number2):
#     """Return the quotient of two numbers."""
#     return number1 / number2

# def floor_quotient(number1, number2):
#     """Return the floor quotient of two numbers."""
#     return number1 // number2

# def remainder(number1, number2):
#     """Return the remainder of two numbers."""
#     return number1 % number2

# def power(number1, number2):
#     """Return the power of two numbers."""
#     return number1 ** number2

# def main():
#     number1 = float(input("Enter a positive number: "))
#     number2 = float(input("Enter another positive number: "))

#     print(addition(number1, number2))
#     print(subtraction(number1, number2))
#     print(product(number1, number2))
#     print(quotient(number1, number2))
#     print(floor_quotient(number1, number2))
#     print(remainder(number1, number2))
#     print(power(number1, number2))

# main()

def calculate(number1, number2, operator):
    "Return the calculation based on the operator argument."
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
    operation = f"{number1} {operator} {number2}"
    result = calculate(number1, number2, operator)
    print(f"==> {operation} = {result}")





