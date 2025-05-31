# 5. Guess the Number
# User keeps guessing a number until it's correct. Provide "too high/low" hints.

correct_number = 10.0
user_input = float(input('Guess the number: '))

while user_input != correct_number:
    if user_input > correct_number:
        user_input = float(input('Too high, try again: '))
    else:
        user_input = float(input('Too low, try again: '))

print(f'You got it, the correct number is: {user_input}')
