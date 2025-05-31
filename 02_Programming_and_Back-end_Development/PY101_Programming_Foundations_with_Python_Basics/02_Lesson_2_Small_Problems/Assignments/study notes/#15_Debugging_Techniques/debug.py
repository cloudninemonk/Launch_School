# debug.py

import pdb

counter = 1

pdb.set_trace()  # Another breakpoint

while counter <= 5:
    print(counter)
    pdb.set_trace()  # Add breakpoint
    counter += 1

numbers = [10, 20, 30, 40]
try:
    index = int(input("Enter an index to access: "))
    element = numbers[index]
    result = 100 / element
except ValueError:
    print('Invalid input. You did not enter a valid number.')
except IndexError:
    print('The number you entered is not a valid index.')
else:
    print(f"Result: {result}")

def lower_first(word):
    # Ensure word is a string
    if type(word) != str:
        return word

    # Ensure word contains at least one character
    if len(word) == 0:
        return word

    # We now know that word is a string that contains
    # at least one character. That means the following
    # code will run without generating an error.
    return word[0].lower() + word[1:]

print(lower_first("FOO"))  # Output: "fOO"
print(lower_first(32))     # Output: 32

def process_user_input():
    try:
        num = int(input('Enter a number: '))
        sq_num = num ** 2
    except ValueError:
        print('You need to enter a valid number.')
    finally:
        return sq_num
	
print(f'The square of your number is {process_user_input()}')
