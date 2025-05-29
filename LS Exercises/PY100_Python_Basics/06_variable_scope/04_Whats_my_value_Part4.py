# 4. What's my value? (Part 4)

"""

What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()

"""

# My response:

"""

The code would output 1. The global variable a is accessing within the function as it is not attempting to use it
aside from merely printing it. 

"""

# Comments:

"""

If the function tried to modify the variable a (rather than just print it), you would need to use the global 
keyword to indicate that you want to modify the global variable rather than create a new local one.

"""