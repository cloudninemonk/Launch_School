print('What is your name? ')    # prints the question
name = input()                  # input from user required
print(f'Good Morning, {name}!') # f-string (interpolated string)

name = input("What's your name? ")  # input from user will have a space after the ?
print(f'Good Morning, {name}!')     # f-string (interpolated string)

name = input("What's your name?\n") # input from user is on a new line
print(f'Good morning, {name}!')     # f-string (interpolated string)
      