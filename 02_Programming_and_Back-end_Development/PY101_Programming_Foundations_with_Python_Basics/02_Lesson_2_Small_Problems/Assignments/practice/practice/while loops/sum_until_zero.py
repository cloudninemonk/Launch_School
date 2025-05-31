# 2. Sum Until Zero
# Continuously accept numbers and sum them until the user enters 0.

user_number = float(input('Enter a number: '))
  
while user_number == 0:
    user_number = float(input('Enter a number that is not equal to 0: '))

sum_numbers = user_number 

while user_number != 0:
    user_number = float(input('Enter another number that is not equal to zero, otherwise I will sum all: '))
    sum_numbers += user_number
print(f'The sum of the numbers you entered is {sum_numbers}')
