"""Write a function that takes one integer argument and returns True when the
number's absolute value is odd, False otherwise."""

def is_odd(number):
    """This function determines if a number is odd."""
    if number % 2 != 0:
        return "Your number is odd."
    return "Your number is even."

your_number = float(input("Enter a number: "))
print(is_odd(your_number))
