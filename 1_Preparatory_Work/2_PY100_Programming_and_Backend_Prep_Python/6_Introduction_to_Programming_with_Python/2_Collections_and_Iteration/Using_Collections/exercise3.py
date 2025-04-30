# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. 
# It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).

# My response:

my_tup = (1, 2, 3, 4, 5)
my_tup1 = my_tup[::-1][1:len(my_tup)-1]

# alternatively,

my_tup = (1, 2, 3, 4, 5)
my_tup_rev = my_tup[::-1]
my_tup1 = my_tup_rev[1:len(my_tup_rev)-1]

# Comments:

# Rather than using len(my_tup)-1 to stipulate the second last index. Cleaner way would be to use -1. 
# i.e. [1:-1] to get second to second last elements


# Launch School's answer:

# Solution 1

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
result = tuple(my_list[1:4])
print(result)       # (4, 3, 2)

# Solution 2

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)       # (4, 3, 2)

# Solution 3

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]
print(result)       # (4, 3, 2)

# There are several ways to solve this problem. Your first inclination may have been to use the reverse method, as in Solution 1. 
# However, reverse only works with lists, so we must first convert the tuple to a list. 
# Even so, we have to slice the list, though the slice is a little cleaner.

# Solutions 2 and 3 use the same approach by extracting a reversed slice. 
# The only difference is how we specify the start and stop values for the slice. 
# What makes these tricky is that the element indexed by the stop value is not included in the result. 
# If you used one of these solutions, you likely started with an off-by-one bug.