def multiply(left, right):                                  
    return left * right                                     

def get_num(prompt):                                       
    return float(input(prompt))                             

first_number = get_num('Enter the first number: ')          
second_number = get_num('Enter the second number: ')        
product = multiply(first_number, second_number)             
print(f'{first_number} * {second_number} = {product}')  

# Identify all of the identifiers on each line of the code above.


# My response:

# def multiply(left, right):                                  # multiply, left, right
#     return left * right                                     # left, right

# def get_num(prompt):                                        # get_num, prompt
#     return float(input(prompt))                             # prompt

# first_number = get_num('Enter the first number: ')          # first_number, get_num
# second_number = get_num('Enter the second number: ')        # second_number, get_num
# product = multiply(first_number, second_number)             # product, multiply, first_number, second_number
# print(f'{first_number} * {second_number} = {product}')      # first_number, secodn_number, product


# Launch School's answer:

# The identifiers in this code are multiply, left, right, first_number, second_number, 
# get_num, prompt, float, input, product, and print. 
# The following table shows where each identifier appears in the code.

# Identifier	    Appears on these lines
# multiply	        1, 9
# left	            1, 2
# right	            1, 2
# first_number	    7, 9, 10
# second_number	    8, 9, 10
# get_num	        4, 7, 8
# prompt	        4, 5
# float	            5
# input	            5
# product	        9, 10
# print	            10


# Comments:

# I did not recognise that input, float and print are all identifiers. 
# The reason they are identifier is because input, float and print are 
# all functions. 