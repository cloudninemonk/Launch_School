# X Ask the user for the first number.
# X Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform th eoperation on the two numbers.
# Print the result to the terminal.

print('Welcome to Calculator!')

response = True

while response:
    print("What's the first number?")
    number1 = float(input())
    print("What's the second number?")
    number2 = float(input())

    print('What operation would you like to perform?\n'
          '1) Add 2) Subtract 3) Multiply 4) Divide 5) Exponential')
    operation = input()

    def calculate(number1, number2):

        if operation == '1':
            result = number1 + number2 # Adds number1 to number2
            return result
        elif operation == '2':
            result = number1 - number2 # Subtracts number2 from number1
            return result
        elif operation == '3':
            result = number1 * number2 # Multiplies number1 by number2
            return result
        elif operation == '4':
            if number2 == 0.0:
                print("You cannot have a denominator with a value of zero")
                result = 'invalid'
            else:
                result = number1 / number2 # Divides number1 by number2
            return result
        elif operation == '5':
            result = number1 ** number2 # Raise number to the power of number2
            return result

    print(f'The result is: {calculate(number1, number2)}')
    print('Would you like to perform another calculation? y/n')
    
    response = input()
    if response == 'y':
        continue
    else: 
        break

