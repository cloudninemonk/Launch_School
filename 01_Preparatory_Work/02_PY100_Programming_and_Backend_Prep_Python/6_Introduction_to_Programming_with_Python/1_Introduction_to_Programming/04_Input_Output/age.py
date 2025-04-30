# age = input('How old are you? ')
# print(f'You are {age}')
# print(f'In 10 years, you will be {int(age) + 10} years old.')
# print(f'In 20 years, you will be {int(age) + 20} years old.')
# print(f'In 30 years, you will be {int(age) + 30} years old.')
# print(f'In 40 years, you will be {int(age) + 40} years old.')

age = int(input('How old are you? '))
print(f'You are {age}.')
i = 0
j = 0
for i in range(4):
    j = 10 * (i+1)
    age += 10
    print(f'In {j} years, you will be {age} years old.')