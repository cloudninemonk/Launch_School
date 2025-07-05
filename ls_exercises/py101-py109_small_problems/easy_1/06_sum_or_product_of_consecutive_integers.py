"""Write a program that asks the user to enter an integer greater than 0,
then asks whether the user wants to determine the sum or the product of
all numbers between 1 and the entered integer, inclusive.

Example 1:
    Please enter an integer greater than 0: 5
    Enter "s" to compute the sum, or "p" to compute the product. s

    The sum of the integers between 1 and 5 is 15.

Example 2:
    Please enter an integer greater than 0: 6
    Enter "s" to compute the sum, or "p" to compute the product. p

    The product of the integers between 1 and 6 is 720.
"""
def calculate_sum(integer):
    """Calculates the sum of integers."""
    result = 1
    for number in range(1, integer + 1):
        result += number
    return result

def calculate_product(integer):
    """Calculates the product of integers."""
    result = 1

    for number in range(1, integer + 1):
        result *= number
    return result

get_integer = int(input("Enter an integer greater than 0: "))
compute = input("Enter 's' to computer the sum, or 'p' to computer the product: ")

if compute == 's':
    get_sum = calculate_sum(get_integer)
    print(f"The sum of the integers between 1 and {get_integer} is {get_sum}.")

if compute == 'p':
    get_product = calculate_product(get_integer)
    print(f"The sum of the integers between 1 and {get_integer} is {get_product}.")
