"""Print all even numbers from 1 to 99, inclusive, with each number on a separate line.
Bonus Question: Can you solve the problem by iterating over just the even numbers?"""

def print_even():
    """Print even numbers from 1 to 99, inclusive."""
    number = 1
    while number <= 99:
        if number % 2 == 0:
            print (number)
        number += 1

print_even()

"""An alternative solution by iterating over even numbers only."""

def print_even():
    """Iterates over the even numbers only."""
    for number in range(0, 100, 2):
        if number > 0:
            print(number)

print_even()
