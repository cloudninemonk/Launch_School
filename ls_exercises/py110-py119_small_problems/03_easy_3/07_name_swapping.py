'''
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
'''

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string

Output:
- string

Rules (Explicit):
- the names don't include middle names, initials, or suffixes ("Jr.", "Sr.")
- a single space between first and last name

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- split method

A: Algorithm (Step-by-step)
-------------------------
1. Pass the name to the function swap_name
2. Split the name
3. Join the split of the name with ', ' as a delimiter

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def swap_name(name):
    return ', '.join(name.split()[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# ==========
# LS Solution
# ==========

def swap_name(name):
    return ', '.join(name.split()[::-1])

# or

def swap_name(name):
    first, last = name.split()
    return f"{last}, {first}"