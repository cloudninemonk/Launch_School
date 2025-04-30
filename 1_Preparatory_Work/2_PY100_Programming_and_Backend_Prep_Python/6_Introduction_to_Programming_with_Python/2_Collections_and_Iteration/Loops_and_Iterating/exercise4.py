# Use a while loop to print all numbers in my_list with even values, one number per line. 
# Then, print the odd numbers using a ' for' loop.

# my_list = [6, 3, 0, 11, 20, 4, 17]

# Expected Even Values

# 6
# 0
# 20
# 4

# Exepected Odd Values

# 3
# 11
# 17


# My response:

my_list = [6, 3, 0, 11, 20, 4, 17]

# My even numbers:
i = 0

while i < len(my_list):
    if my_list[i] % 2 == 0:
        print(my_list[i])
    i += 1

# My odd numbers:
j = 0

for j in my_list:
    if j % 2 != 0:
        print(j)
        continue

# Comments
# No need to implement continue in the for loop


# Launch School's answer:

# while loop
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    # Even numbers are exactly divisible by 2
    if number % 2 == 0:
        print(number)

    index += 1

# for loop
my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    # Odd numbers are not exactly divisible by 2
    if number % 2 != 0:
        print(number)

# Our solutions both rely on using the % operator to determine whether a number is exactly divisible by 2. 
# Even numbers are; odd numbers aren't. In both cases, we only need to compare the result of element % 2 with 0.
# 'If number % 2 is 0, the number is even. Otherwise, it is odd.

# As with the previous problem, we needed indexing to control the while loop. 
# However, the for loop led to code that is easier to read.
