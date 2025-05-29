# 7. First Multiple of 7 and 13
# Find the first number greater than 1 that is divisible by both 7 and 13.


my_num = 2

while my_num % 7 != 0 or my_num % 13 != 0:
    my_num += 1
print(f'The first number divisible by 7 and 13 is: {my_num}')