'''
Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- integer

Output:
- function return -> list of integers
- program output -> boolean

Rules (Explicit):
- argument integer is positivee

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

Edge Cases:
-

D: Data Structures
-------------------------
- range
- str

Notes
-------------------------
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Iterate through all digits commencing at 1 to the argument number inclusive
2. On each iteration, append the current digit to the list numbers
3. Return numbers

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def sequence(number):
    return list(range(1, number + 1))

print(sequence(-5) == [-1, -2, -3, -4, -5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

# ==========
# LS Solution
# ==========

def sequence(limit):
    return list(range(1, limit + 1))