# The following code uses the randrange function from Python's random library to obtain and print a random integer within a given range. 
# Using a while loop, it keeps running until it finds a random number that matches the last number in the range. 
# Refactor the code so it doesn't require two different invocations of randrange.

# import random

# highest = 10
# number = random.randrange(highest + 1)
# print(number)

# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)


# My response:

import random

highest = 10
number = 0

while number != highest:
    number = random.randrange(highest + 1)
    print(number)
    continue


# Launch School's answer:

import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

# The ideal do/while loop use case occurs when you need to execute some code at least once. We need to do that here. 
# However, Python doesn't have a do/while loop. Instead, we can combine a while True loop with a break statement.