# 4. Input Validator
# Ask for a number between 1 and 10. Repeat until valid.

user_input = float(input('Enter a number between 1 and 10: '))

while user_input <=1 or user_input >= 10:
    user_input = float(input(f'''The number you entered is not between 1 and 10.
    Try again: '''))

print(f'You entered a valid number: {user_input}')
