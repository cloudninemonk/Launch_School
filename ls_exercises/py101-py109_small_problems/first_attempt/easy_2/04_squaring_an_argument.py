"""
Using the multiply function from the "Multiplying Two Numbers" exercise, write a
function that computes the square of its argument (the square is the result of
multiplying a number by itself).

Examples:
    print(square(5) == 25)   # True
    print(square(-8) == 64)  # True
"""

# def square(number):
#     """Returns the square as a float or integer depending on the input."""
#     if '.' in number:
#         return f"{(float(number) ** 2):.2f}"
#     return int(number) ** 2

# number = input("Enter a number: ")

# print(f"The square of your number is {square(number)}.")

def multiply(number1, number2):
    """Returns the multiplication as a float or integer depending on the input."""
    if '.' in number1 or '.' in number2:
        return float(number1) * float(number2)
    return int(number1) * int(number2)

def square(number):
    """Returns the square of a number."""
    return multiply(number, number)

number1 = input("Enter a number: ")
number2 = input("Enter a number: ")

print(f"The square of your first number is {square(number1)}.")
print(f"The square of your first number is {square(number2)}.")
