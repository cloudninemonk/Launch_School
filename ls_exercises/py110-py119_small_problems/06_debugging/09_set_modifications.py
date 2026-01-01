'''
We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?

data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
'''
# The set length changed during the loop, causing a RuntimeError. Could fix this issue by not mutating the set within the loop, rather creating a new set to add values to.

# using traditional loop
data_set = {1, 2, 3, 4, 5}
new_data_set = set()
for item in data_set:
    if item % 2 == 0:
        new_data_set.add(item)

# using set comprehension

data_set = {1, 2, 3, 4, 5}
new_data_set = {item for item in data_set if item % 2 == 0