'''
A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
'''
# By iterating through the list to create a new list of all unique numbers.
# ==========
# My Solution
# ==========
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]

unique_data = []
for value in data:
    if value not in unique_data:
        unique_data.append(value)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed

# ==========
# LS Solution
# ==========
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
seen = set()

for item in data:
    if item not in seen:
        seen.add(item)
        unique_data.append(item)

print(unique_data == [4, 2, 1, 3]) # True

