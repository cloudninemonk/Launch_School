# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

# Note: when working with integers, a value of 0 is "falsy"; all other integers are "truthy".

# My response:

if (all(remainders_5(numbers_1))): 
    print('numbers_1 does not contain any numbers that are divisible by 5')
if (all(remainders_5(numbers_2))): 
    print('numbers_2 does not contain any numbers that are divisible by 5')
if (all(remainders_5(numbers_3))): 
    print('numbers_3 does not contain any numbers that are divisible by 5')
if (all(remainders_5(numbers_4))): 
    print('numbers_4 does not contain any numbers that are divisible by 5')


# Launch School's answer:

print(all(remainders_5(numbers_1)))     # False
print(all(remainders_5(numbers_2)))     # True
print(all(remainders_5(numbers_3)))     # False
print(all(remainders_5(numbers_4)))     # True

# remainders_5 is similar to remainders_3 in the previous exercise (exercise 18) in that it returns a list of integers. 
# In this list, a value of 0 means the corresponding number is divisible by 5, while a non-zero value 
# means the number is not divisible by 5. Since 0 is falsy and the other integers are truthy, we can use 
# all to determine whether all of the numbers are not divisible by 5.