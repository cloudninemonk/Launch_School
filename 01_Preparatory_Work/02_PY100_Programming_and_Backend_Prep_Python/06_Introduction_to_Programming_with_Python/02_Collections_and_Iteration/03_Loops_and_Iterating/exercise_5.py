# Print all of the even numbers in the following list of nested lists. Don't use any while loops.

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# Expected output
# 6
# 4
# 2
# 4
# 16
# 0

# My response:

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for i in my_list:
    for j in i:
        if j % 2 == 0:
            print(j)

# Comments:
# Use better naming for objects. i.e. nest_list rather than i and number rather than j.

# Launch School's answer:

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for nested_list in my_list:
    for number in nested_list:
        if number % 2 == 0:
            print(number)

# That may not have been too easy. Nested loops are hard to think about, but you'll encounter them often enough to have dreams about them.
# We start by iterating over the nested lists inside my_list.
# That means nested_list takes on the values [1, 3, 6, 11], [4, 2, 4], and [9, 7, 16, 0] as the iteration proceeds.
# We then iterate over the numbers in the current nested list during each iteration.
# Finally, we print the even numbers.