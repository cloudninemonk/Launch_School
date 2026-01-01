'''
Given the following data structure, write some code that uses comprehensions to define a dictionary where the key is the first item in each sublist, and the value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

Expected result:

# Pretty printed for clarity
{
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}
'''
# ==========
# My Solution
# ==========
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

dict1 = {sublst[0]: sublst[1] for sublst in lst}
print(dict1)

# ==========
# LS Solution
# ==========
dict1 = {item[0]: item[1] for item in lst}
print(dict1)
