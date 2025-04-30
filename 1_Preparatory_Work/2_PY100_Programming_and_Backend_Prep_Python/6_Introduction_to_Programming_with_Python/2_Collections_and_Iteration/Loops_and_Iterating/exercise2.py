# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code should use a for loop to display the future ages.

# My reponse from age.py

# age = int(input('How old are you? '))
# print(f'You are {age}.')
# i = 0
# j = 0
# for i in range(4):
#     j = 10 * (i+1)
#     age += 10
#     print(f'In {j} years, you will be {age} years old.')


# My response:

age = int(input('How old are you? '))
print(f'You are {age}.')

counter = range(10, 50, 10)

for count in counter:
    print(f'In {count} years, you will be {age + count} years old')


# Launch School's answer:

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')