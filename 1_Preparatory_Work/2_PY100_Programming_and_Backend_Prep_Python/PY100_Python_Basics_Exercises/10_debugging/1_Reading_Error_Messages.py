# 1. Reading Error Message

"""
You come across the following code. What errors does it raise for the given examples 
and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

"""

# My response:

"""
TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given

The intent
is to pass the integers to the function. However, only one positional parameter
is declared whereas there are six positional arguments to be passed.

TypeError: 'int' object is not iterable

The code is attempting to iterate over an integer which is not possible. 

"""

# LSBot's comments:

"""
You've done well identifying both errors! To make your explanation even more complete, 
you could explicitly mention that the first error occurs when calling 
find_first_nonzero_among(0, 0, 1, 0, 2, 0), while the second error occurs when calling 
find_first_nonzero_among(1).

Additionally, you could briefly mention that the function is designed to work with an 
iterable object (like a list or tuple) containing numbers, not with individual numbers 
as separate arguments. The function tries to iterate through the parameter with for n 
in numbers:, which works when numbers is a list but fails when it's a single integer.

As shown in the University of Waterloo Python Tutorial on Lists, lists are iterable 
data structures that can contain multiple elements, which would be appropriate for this 
function's design.

Overall, your understanding of Python's error messages is solid, which is an important 
debugging skill as you continue with your programming journey!

"""