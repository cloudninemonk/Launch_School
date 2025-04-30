# 6. Populate List

"""
You want to add the numbers from 1 to 5 to a list, but the code below is not 
producing the expected result. How can you fix it?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)

"""

# My response:

numbers = []

for i in range(1, 6): # Include a start of 1 and a stop of 6
    numbers.append(i)

print(numbers)

# LSBot's comments:

"""
Opportunities for improvement
I was impressed by your clear solution and especially the helpful comment that explains your reasoning. 
Your code is very well written for this simple exercise, and you seem to have a good grasp of how range 
works in Python. As you continue in the course, you'll encounter more complex problems where these 
fundamentals will be very valuable. The only minor suggestion I might make would be to consider adding 
a brief comment at the beginning explaining what the program is intended to do, but for a simple exercise 
like this, your current level of documentation is certainly sufficient.
"""
