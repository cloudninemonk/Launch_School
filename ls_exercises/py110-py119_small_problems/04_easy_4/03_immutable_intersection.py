'''
Transform two lists into frozen sets and find their common elements.

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- two lists of integers

Output:
- function: frozenset containing a set of integer(s)
- program: boolean

Rules (Explicit):
-

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

Edge Cases:
-

D: Data Structures
-------------------------
- frozenset

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1. Initialise list1 and list2
2. Initialise expected_result to frozenset({8})
3. Define the function intersection that receives list1 and list2
4. Return the frozenset of the intersection of set of list1 and set of list2
5. Test the equality of the returned value to the expected_result

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def intersection(list1, list2):
    return frozenset(set(list1).intersection(set(list2)))

# or

def intersection(list1, list2):
    return frozenset(set(list1)&(set(list2)))

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

# ==========
# LS Solution
# ==========

def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)