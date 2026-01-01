'''
Given a dictionary, return its keys sorted by the values associated with each key.

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- dictionary

Output:
- list of the input dictionary's keys

Rules (Explicit):
- output list should be sorted based on the values of the input dictionary's items

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- sorted function
- key function
- dictionary view object

A: Algorithm (Step-by-step)
-------------------------
1. Initialise the dictionary my_dict
2. Initialise the expected return list keys
3. Define the function order_by_value that receives the argument my_dict
4. Initialise the variable my_keys to contain the keys from my_dict
5. Return the sorted my_keys by sorting based on the key function my_value

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def my_value(key):
    return my_dict[key]

def order_by_value(my_dict):
    my_keys = list(my_dict)
    return sorted(my_keys, key = my_value)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

#alternatively

def order_by_value(my_dict):
    my_keys = list(my_dict)
    return sorted(my_keys, key = my_dict.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

# ==========
# LS Solution
# ==========

def sort_key(item):
    return item[1]

def order_by_value(d):
    sorted_items = sorted(d.items(), key=sort_key)
    return [key for key, value in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True