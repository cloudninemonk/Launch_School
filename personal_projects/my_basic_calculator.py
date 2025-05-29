"""
This code is a command line calculator that performs simple arithmetic: multiplication, 
division, addition and subtraction of two numbers that are input by the user.
"""

def multiply(num1, num2):
    result = num1 * num2
    print(f'{num1}*{num2} = {result}')

def division(num1, num2):
    result = num1 / num2
    print(f'{num1}/{num2} = {result}')

def addition(num1, num2):
    result = num1 + num2
    print(f'{num1}+{num2} = {result}')

def subtraction(num1, num2):
    result = num1 - num2
    print(f'{num1}-{num2} = {result}')


calc_options = ['m', 'd', 'a', 's']
calc_to_perform = ''

while calc_to_perform not in calc_options:
    print("""
What sort of calculation would you like to perform?

multiplication (m)
division (d)
addition (a)
subtraction (s)       
""")
    calc_to_perform = input().lower()
    if calc_to_perform not in calc_options:
        print('Invalid input. Choose m, d, a or s')


print('\nEnter a number:')
num1 = int(input())
print('Enter another number:')
num2 = int(input()) 


if calc_to_perform == 'm':
    multiply(num1, num2)
elif calc_to_perform == 'd':
    division(num1, num2)
elif calc_to_perform == 'a':
    addition(num1, num2)
elif calc_to_perform == 's':
    subtraction(num1, num2)

    

def bottom():
    print('Reached the bottom')
    
def top():
    bottom()

top()


    


    