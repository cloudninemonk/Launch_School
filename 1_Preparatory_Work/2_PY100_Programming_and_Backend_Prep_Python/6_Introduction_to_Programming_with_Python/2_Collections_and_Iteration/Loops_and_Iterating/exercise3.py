# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

# my_list = [6, 3, 0, 11, 20, 4, 17]

# Expected output
# 6
# 3
# 0
# 11
# 20
# 4
# 17

# My response:

my_list = [6, 3, 0, 11, 20, 4, 17]

# while loop
i = 0

while i < len(my_list):
    print(my_list[i])
    i = i + 1

# Comments
# Better to use i += 1

# for loop
for j in my_list:
    print(j)

# Launch School's answer:

# while loop
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    print(number)
    index += 1

# for loop
my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    print(number)

# Our solution using a while loop uses indexing to control iteration and to access the list members. 
# Note that we start by setting index to 0 and then iterate while index is less than the list length.

# The solution using a for loop is clearly easier to understand -- we don't have to mess around with indexing;
# 'we only need to iterate over the list elements.


