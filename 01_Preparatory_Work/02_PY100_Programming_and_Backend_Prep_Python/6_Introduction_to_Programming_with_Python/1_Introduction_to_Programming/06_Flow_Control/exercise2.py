# Write a function, even_or_odd, that determines whether its argument is an even or odd number. 
# If it's even, the function should print 'even'; otherwise, it should print 'odd'. 
# Assume the argument is always an integer.


# My response:

def even_or_odd(num):
    if num % 2 == 0:
        print('argument is even')
    else:
        print('argument is odd')

number = int(input('User enter a number: '))
even_or_odd(number)
    

# Launch School's answer:

# solution 1:

# def even_or_odd(number):
#     if number % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# solution 2:

# def even_or_odd(number):
#     print('even' if number % 2 == 0 else 'odd')
