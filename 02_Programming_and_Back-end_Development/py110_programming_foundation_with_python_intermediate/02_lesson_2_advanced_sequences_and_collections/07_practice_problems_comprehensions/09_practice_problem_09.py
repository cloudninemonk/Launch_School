'''
This problem may prove challenging. Try it, but don't stress about it. If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

Expected result:

[{'e': [8], 'f': [6, 10]}]
'''
# ==========
# My Solution
# ==========

def check_for_evens(dict1):
    new_dict = {}
    for key, value in dict1.items():
        counter = 0
        for num in value:
            if num % 2 == 0:
                counter += 1
                continue
            else:
                break
        if counter == len(value):
            new_dict[key] = value
    if len(new_dict) == len(dict1):
        return new_dict
    return False

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

new_lst = [dict1 for dict1 in lst if check_for_evens(dict1)]
print(new_lst)

# using the all function

def check_for_evens(dict1):
    for value in dict1.values():
        if not all([num % 2 == 0 for num in value]):
            return False
    return True

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

new_lst = [dict1 for dict1 in lst if check_for_evens(dict1)]
print(new_lst)

# ==========
# LS Solution
# ==========
# solution 1
def all_even(dictionary):
    for values in dictionary.values():
        if not all([num % 2 == 0 for num in values]):
            return False

    return True

result = [val for val in lst if all_even(val)]
print(result)

# solution 2
def list_is_even(lst):
    return all([num % 2 == 0 for num in lst])

def all_even(dictionary):
    lists_are_even = [list_is_even(list_value)
                      for list_value in dictionary.values()]
    return all(lists_are_even)

result = [dictionary for dictionary in lst
                     if all_even(dictionary)]
print(result)




