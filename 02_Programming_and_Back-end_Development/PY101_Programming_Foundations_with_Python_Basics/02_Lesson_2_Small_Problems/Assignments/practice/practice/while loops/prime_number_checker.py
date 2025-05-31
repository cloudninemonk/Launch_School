# 10. Prime Number Checker
# Ask for a number and determine if it's prime using a loop (not math libraries).

# num = int(input('Enter a positive integer: '))

# if num == 1:
#     print('Your number is not a prime number.')
# elif num == 2 or num == 3:
#     print('Your number is a prime number!')
# else:
#         count = 0
#         while count * count < num:
#             if num % count == 0:
#                 print('Your number is not a prime number.')
#                 break
#             elif count * count + 1 > num:
#                 print('Your number is a prime number!')
#                 break
#             # elif count * count <= num:
#                 # count += 1
#             else:
#                 print('Your number is a prime number!') 
#                 break
#             count += 1

num = int(input('Enter a positive integer: '))
iterator = 1
count = 0

while iterator ** 2 <= num:
    if num % iterator == 0:
        count += 1
    if count > 1:
        break
    iterator += 1

if count > 1 or num == 1:
    print('Your number is not a prime number')
else:
    print('Your number is a prime number!')





         


        

