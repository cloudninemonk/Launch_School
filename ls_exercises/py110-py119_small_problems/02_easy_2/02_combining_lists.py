'''
Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- 2 x lists

Output:
- Function returned value -> a set of the union of the two lists
- Program output -> boolean

Rules (Explicit):
-

Rules (Implicit/Inferred):
- lists cannot contain non-hashable datatypes

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

Edge Cases:
-

D: Data Structures
-------------------------
- set constructor

Notes
-------------------------
- union method
- | operator

A: Algorithm (Step-by-step)
-------------------------
1. Pass the two sets to the function union
2. Return the set of the union of the two lists

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def union(list1, list2):
    return set(list1) | set(list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# or

def union(list1, list2):
    return set(list1).union(list2) # union can have any iterable type as an argument

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# ==========
# LS Solution
# ==========

# Solution 1:

def copy_non_dups_to(result_set, lst):
    for value in lst:
        result_set.add(value)

def union(list1, list2):
    result_set = set()
    copy_non_dups_to(result_set, list1)
    copy_non_dups_to(result_set, list2)
    return result_set

# Solution 2:

def union(list1, list2):
    return set(list1).union(set(list2))