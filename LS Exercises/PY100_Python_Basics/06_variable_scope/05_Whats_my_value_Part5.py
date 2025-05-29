# 5. What's my value? (Part 5)

"""

What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

"""

# My response:

"""

The code would output 1 and reassign the value of 2 to the variable a.
As the variable a is not defined locally, the code looks for a globally. 
After the code prints the value assigned to a, it then locally reassigns
the value of 2 to a. Globally, a still remains equal to 1.

"""

# Comments:

"""
My answer is incorrect as the code would actually raise an UnboundLocalError rather 
than successfully printing the value of a. This error occurs because Python's scope 
rules are different from what I described, particularly when a variable is 
assigned within a function.

In Python, when a variable is assigned anywhere within a function, 
that variable is treated as local to the function for its entire scope - even 
before the assignment occurs.

Python sees the assignment a = 2 and declares a as a local variable for the entire 
function. When print(a) is executed before the assignment,Python tries to access the
local variable a, which hasn't been assigned a value yet, resulting in the 
UnboundLocalError.

If you want to access a global variable and also assign to it within a function, you'd need to use the global keyword:

a = 1

def my_function():
    global a  # Declare we want to use the global 'a'
    print(a)  # Now this works and prints 1
    a = 2     # This modifies the global 'a'

my_function()

"""

