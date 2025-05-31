# 6. Digit Counter
# Count how many digits are in an integer without converting it to a string.

user_input = int(input('Enter an integer: '))
iterator = 0
counter = 0

if user_input == 0:
    print('The number of digits is 1.')
while user_input > 0:
    user_input //= 10
    counter += 1
print(counter)