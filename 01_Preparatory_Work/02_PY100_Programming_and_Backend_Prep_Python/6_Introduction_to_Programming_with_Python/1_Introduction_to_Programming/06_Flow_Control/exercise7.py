# Write a function that takes a single integer argument and prints a message that describes whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0


# My response:

def single_int(inter):
    if (inter >= 0) and (inter <= 50):
        print ('the value is between 0 and 50 (inclusive)')
    elif (inter >= 51) and (inter <=100):
        print('the value is between 51 and 100 (inclusive)')
    elif (inter > 100):
        print('the value is greater than 100')
    else:
        print('the value is less than 0')


single_int(-8)


# Launch School's answer:

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')


# Comments:

# Whilst both mine and LS's code is very similar. LS's is more efficient considering there is only one logical expression
# on line 27, 29 and 31. Whereas my code had two on each of those lines.

