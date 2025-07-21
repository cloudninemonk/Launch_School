"""
Create a function that takes two arguments, multiplies them together, and returns
the result.

Example:
    print(multiply(5, 3) == 15)  # True
"""

def multiply(number1, number2):
    """Returns the multiplication as a float or integer depending on the input."""
    if '.' in number1 or '.' in number2:
        return float(number1) * float(number2)
    return int(number1) * int(number2)

number1 = input("Enter a number: ")
number2 = input("Enter a number: ")

print(multiply(number1, number2))
