# X Ask the user for the first number.
# X Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform th eoperation on the two numbers.
# Print the result to the terminal.
# Ask the user if they would like to perform another calculation.

print('Welcome to Calculator!')

def calculate(number1, number2, operation):

    if operation == '1':
        return number1 + number2
    elif operation == '2':
        return number1 - number2
    elif operation == '3':
        return number1 * number2
    elif operation == '4':
        if number2:
            return number1 / number2
        else:
            print("You cannot have a denominator with a value of zero")
            return 'invalid'   
    elif operation == '5':
        return number1 ** number2

response = True

while response:
    try:
        print("What's the first number?")
        number1 = float(input())
        print("What's the second number?")
        number2 = float(input())
    except ValueError:
        print("You did not enter a valid number.")

    operation = ''
    while operation not in ['1', '2', '3', '4', '5']:
        print('What operation would you like to perform?\n'
            '1) Add 2) Subtract 3) Multiply 4) Divide 5) Exponential')
        operation = input()

    print(f'The result is: {calculate(number1, number2, operation)}')
    response = input('Would you like to perform another calculation? y/n \n').lower()
    if response in ['y', 'yes', 'yeah', 'yeh']:
        continue
    else: 
        break
    

