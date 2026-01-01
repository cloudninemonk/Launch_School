'''
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True
'''
# ==========
# My Solution
# ==========
def keep_keys(input_dict, keys):
    return {key: input_dict[key] for key in keys if key in input_dict}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# ==========
# LS Solution
# ==========

# solution 1 - traditional loop
def keep_keys(my_dict, key_list):
    new_dict = {}
    for key in key_list:
        if key in my_dict:
            new_dict[key] = my_dict[key]

    return new_dict

# solution 2 - dictionary comprehension
def keep_keys(my_dict, key_list):
    return {key: my_dict[key]
            for key in key_list
            if key in my_dict}
