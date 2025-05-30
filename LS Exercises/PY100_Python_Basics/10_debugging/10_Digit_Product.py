# 10. Digit Product

"""
You've been asked to implement a function called digit_product that takes a string of 
digits as an argument and returns the product of all the digits in the string.

When testing the function, you find that it returns 0, which is not what you expect. 
Can you identify the issue and correct the code?

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 0

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0

"""

# My response:

def digit_product(str_num):
    digits = list(str_num) # creates a list of strings ['1', '2', '3', '4', '5']
    product = 1 # product initalised to 1 as 0 will always result in 0.

    for digit in digits:
        product *= int(digit)   # each string element is converted to an integer

    return product

result = digit_product('12345')
print(result)  # 120

