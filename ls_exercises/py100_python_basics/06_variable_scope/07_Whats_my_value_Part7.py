# 7. What's my value? (Part 7)

"""

What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

"""

# My response:

"""

The code will output 2.
the implementation of global a preceding the assignment of 2 to a within the function
results in global a being reassigned with the value of 2.
print(a) is then printing the reassigned variable a which has a value of 2 assigned to it.

"""