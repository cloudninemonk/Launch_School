# The following function returns a list of the remainders of dividing the numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at least one number 
# that is not evenly divisible by 3 (that is, the remainder is not 0):

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

# Note: when working with integers, a value of 0 is "falsy"; all other integers are "truthy".

# My response:

# determines if any of the collection's elements are truthy
if (any(remainders_3(numbers_1))): 
    print('numbers_1 contains at least one number that is not divisible by 3')
if (any(remainders_3(numbers_2))):
    print('numbers_2 contains at least one number that is not divisible by 3')
if (any(remainders_3(numbers_3))):
    print('numbers_3 contains at least one number that is not divisible by 3')
if (any(remainders_3(numbers_4))):
    print('numbers_4 contains at least one number that is not divisible by 3')


# Launch School's answer:

print(any(remainders_3(numbers_1)))     # True
print(any(remainders_3(numbers_2)))     # True
print(any(remainders_3(numbers_3)))     # False
print(any(remainders_3(numbers_4)))     # False

# remainders_3 returns a list of integers between 0 and 2, inclusive. 
# A value of 0 means the corresponding number is divisible by 3, 
# while a value of 1 or 2 means the number is not divisible by 3. 
# Since 0 is falsy and 1 and 2 are truthy, we can use any to determine 
# whether any of the numbers are non-zero.