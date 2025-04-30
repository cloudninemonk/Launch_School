# Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

# My response:

def multiply(x, y):
    print(float(x) * float(y))

num1, num2 = [input('Enter the first number: '), input('Enter the second number: ')] # Ask user for two numbers.
multiply(num1, num2) # Invoke the function multiply by passing the two arguments.


# Launch School's answer including my comments:

def multiply(left, right):
    return left * right

def get_number(prompt):     # Function get_number with the parameter, prompt. Accepts the arguments first_number and second_number.
    entry = input(prompt)   # Variable entry asking the user for their input.
    return float(entry)     # Returns the float of the user's input.

first_number = get_number('Enter the first number: ')   # Variable, first_number, invoking function get_number.
second_number = get_number('Enter the second number: ') # Variable, second_number, invoking function get_number.
product = multiply(first_number, second_number)         # Variable, product, invoking function multiply and passing the arguments first_number and second_number.
print(f'{first_number} * {second_number} = {product}')  # Print f-string of the three declared variables: first_number, second_number and product.

# COMMENTS AFTER THE EXERCISE
# I did not completely answer the question as I did not output the two numbers and answer into a simple formula.
# I could have spread out line 9 variable declaration over multiple lines.

