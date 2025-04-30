# 3. Multiply By Five

"""
When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")

"""

# My response:
"""
The function performs a string concatenation as the input by the user is a string. 
To achieve the intent of multiplying the user input to achieve an output of 50,
the input value should be convereted to an integer int(input()) if only integers
are expected. Otherwise, the user input can be converted to a float, float(input())
"""

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = float(input())

print(f"The result is {multiply_by_five(number)}!")

# LSBot's comments:

"""
I was impressed by your understanding of the type conversion issue and how you provided 
a more flexible solution by using float() instead of just int(). This allows the program 
to handle both whole numbers and decimal inputs. One small consideration would be to add 
error handling for invalid inputs (like letters or symbols), but that's beyond the scope 
of this particular exercise. Your solution is correct and demonstrates a solid grasp of 
Python type handling, which is a foundational concept you'll continue to build upon.
"""