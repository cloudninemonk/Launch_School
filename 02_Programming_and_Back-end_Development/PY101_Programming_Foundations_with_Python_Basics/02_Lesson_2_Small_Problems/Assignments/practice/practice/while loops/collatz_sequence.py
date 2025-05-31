user_number = int(input('Enter a positive integer: '))

while user_number != 1:
    if user_number % 2 == 0:
        user_number //= 2
    else:
        user_number = 3 * user_number + 1

    print(f'The current number is: {user_number}')


