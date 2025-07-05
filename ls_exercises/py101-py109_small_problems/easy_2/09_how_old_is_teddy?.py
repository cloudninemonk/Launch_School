"""
Build a program that randomly generates and prints Teddy's age. To get the age,
you should generate a random number between 20 and 100, inclusive.

Example Output:
    Teddy is 69 years old!
"""

import random

print(f'Teddy is {random.choice(range(20, 100))} years old!')
print(f'Teddy is {random.randint(20, 100)} years old!')
print(f'Teddy is {random.randrange(20, 101)} years old!')
