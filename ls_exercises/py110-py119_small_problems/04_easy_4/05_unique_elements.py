'''
From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
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
- set

Rules (Explicit):
- Return value to be a set

Rules (Implicit/Inferred):
- Use a function to determine the difference of the two lists

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

Edge Cases:
-

D: Data Structures
-------------------------
-

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1. Pass the two list arguments to the function unique_from_first
2. Return the difference of the set of each list

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def unique_from_first(list1, list2):
    return set(list1) - set(list2)


list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# alternatively

def unique_from_first(list1, list2):
    return set(list1).difference(set(list2))


list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# ==========
# LS Solution
# ==========

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

