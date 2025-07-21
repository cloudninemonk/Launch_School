"""
Build a program that randomly generates and prints Teddy's age. To get the age,
you should generate a random number between 20 and 100, inclusive.

Teddy is 69 years old!
"""
# ==========
# # My Solution
# # ==========
# import random

# print(f"Teddy is {random.randint(20,100)} years old.")

# # ==========
# # LS Solution
# # ==========
# import random

# age = random.randint(20, 100)
# print(f"Teddy is {age} years old!")

# Discussion
#
# Our solution uses the randint function from the random module,
# which lets you generate a random integer between two inclusive bounds.

# The use of a range to limit the output value is an enormous help here, so we
# use it to generate Teddy's age. Afterward, all we have to do is print the
# result.

# Note that randint generates integers between the two numbers, inclusive of
# both.

# Further Exploration Modify this program to ask for a name, then print the age
# for that person. For an extra challenge, use "Teddy" as the name if no name is
# entered.

# ==========
# My Solution
# ==========
import random

name = input("What is your name? ")
if not name:
    name = 'Teddy'

age = random.randint(20, 100)

print(f"{name} is {age} years old!")
