"""A simple calculator module for basic arithmetic operations."""


def prompt(message):
    """Prepend the passed strings with ==>"""
    print(f'==> {message}')

def invalid_number(number_str):
    """Check if the input string is not a valid integer.
    Args:
        number_str (str): The string to validate as an integer.
    Returns:
        bool: True if the string is not a valid integer, False otherwise.
    """
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt("""What operation would you like to perform?"
       1) Add 2) Subtract 3) Multiply 4) Divide""")
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

prompt(f"The result is: {output}")
