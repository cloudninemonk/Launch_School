""" Print all odd numbers from 1 to 99, inclusive, with each number on a separate line."""

def print_odd():
    """Prints all odd numbers from 1 to 99, inclusive."""
    number = 1
    while number <= 99:
        if number % 2 != 0:
            print(number)
        number += 1

print_odd()
