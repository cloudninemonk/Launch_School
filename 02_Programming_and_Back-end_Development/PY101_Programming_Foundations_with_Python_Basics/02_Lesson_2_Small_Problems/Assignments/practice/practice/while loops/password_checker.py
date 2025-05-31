# 3. Password Checker
# Keep asking for a password until the user gets it right.

user_input = input('Enter your password: ')

while user_input != 'open123':
    user_input = input('Incorrect. Reenter your password: ')

print(f'Correct. Your password is {user_input}')

