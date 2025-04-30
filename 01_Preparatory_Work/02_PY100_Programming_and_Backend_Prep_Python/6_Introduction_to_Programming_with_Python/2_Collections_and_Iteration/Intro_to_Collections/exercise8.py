# How would you print all the numbers in the following range?

range(3, 17, 4)


# My response:

for i in range(3,17,4):
     print(i, end=' ')


# Launch School's answer:

# Solution 1

# print(list(range(3, 17, 4)))

# Solution 2

# print(tuple(range(3, 17, 4)))

# Since ranges are lazy sequences, you must either iterate over the range or convert the 
# range to a non-lazy sequence: a list or tuple. Here, we transform the range into a list 
# and a tuple.