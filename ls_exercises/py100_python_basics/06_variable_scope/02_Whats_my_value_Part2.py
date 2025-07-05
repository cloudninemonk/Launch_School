# 2. What's my value? (Part 2)

"""

What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    
    x = x + 5
    print(x)

my_function()

"""

# My response:

"""

The global variable x is accessible anywhere within the code, including the function definitions. Considering such,
The code will output 15.

"""

# Comments:

"""

My repsonse was incorrect. 

My solution doesn't correctly predict the behavior of the given code. The code would not output 15 as you 
suggested but would raise an UnboundLocalError. This is an important concept in Python variable scope that's 
worth understanding fully.

The line x = x + 5 inside the function attempts to use x before it's been defined locally, which causes the 
error. Python sees the assignment and marks x as a local variable for the entire function, but then tries to 
reference its value before it's been initialized.

For the code to correctly execute and output 15, you would implement a global x into the function defintion:

x = 10

def my_function():
    global x  # This tells Python that x refers to the global variable
    x = x + 5
    print(x)

my_function()

"""