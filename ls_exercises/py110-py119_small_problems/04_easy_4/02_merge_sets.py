'''
Given two lists, convert them to sets and return a new set which is the union of both sets.

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- two lists containing integers

Output:
- function: a set containing all the integers from the two lists
- program: boolean

Rules (Explicit):
-

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

Edge Cases:
-

D: Data Structures
-------------------------
- set

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1. Initialise the lists list1 and list2
2. Define a function merge_sets for both lists to be passed to.
3. Return the union of the set of list1 and set of list2
4. Test the equality of the returned value with the given {3, 5, 7, 9, 11, 13}

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def merge_sets(list1, list2):
    return set(list1) | set(list2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})

# ==========
# LS Solution
# ==========

def merge_sets(list1, list2):
    return set(list1) | set(list2)