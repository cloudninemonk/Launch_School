'''
Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
'''

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- two lists

Output:
- function return -> list
- program output -> boolean

Rules (Explicit):
- lists are non-empty
- list contains same number of elements

Rules (Implicit/Inferred):
- lists can contain any type of element

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- for loop
- enumerate function

A: Algorithm (Step-by-step)
-------------------------
1. Pass two lists list1 and list2 to the function interleave
2. Initialise an empty list combined_list
3. Loop through each list and append the value at the index of each list of the current loop iteration to combined_list. list1 before list2
4. Return the combined list

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def interleave(list1, list2):
    combined_list = []

    for idx in range(len(list1)):
        combined_list.extend([list1[idx], list2[idx]])

    return combined_list

# or

def interleave(list1, list2):
    combined_list = []

    for value1, value2 in zip(list1, list2):
        combined_list.extend([value1, value2])

    return combined_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

# ==========
# LS Solution
# ==========
def interleave(list1, list2):
    new_list = []
    for idx in range(len(list1)):
        new_list.extend([list1[idx], list2[idx]])

    return new_list