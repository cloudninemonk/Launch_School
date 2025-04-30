# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])


# My response:

# It outputs Empty. The argument [] is passed to the function parameter my_list. 
# The if statement determines if something is True. Considering an empty list is considered Falsey,
# if my_list: is false and hence else: is True. 


# Launch School's answer:

# The output is Empty since an empty list like [] is falsy. As a result, 
# my_list on line 2 is falsy, so the else block runs instead of the if block.
