# value = int(input('Enter a number: ')) # prints 3 if the value entered is 3

# if value == 3:
#     print('value is 3')


# value = int(input('Enter a number: '))

# if value == 3:
#     print('value is 3')           # prints 3 if the value entered is 3
# else:
#     print('value is NOT 3')       # prints value is NOT 3 for any value entered that is not 3


value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')                   # prints 3 if the value entered is 3
else:
    if value == 4:
        print('value is 4')               # prints 4 if the value entered is 4
    else:
        print('value is NOT 3 or 4')      # prints value is NOT 3 or 4 for any value entered that is not 3 or 4


if value == 3:
    print('value is 3')
elif value == 4:                        # can implement an elif (else if) to reduce the code from 2 lines to 1 line.
    print('value is 4')
else:
    print('value is NOT 3 or 4')