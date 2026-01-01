'''
Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- list of integers

Output:
- function return => integer

Rules (Explicit):
- average rounded down to the integer component of the average
- list is never empty
- element will always be positive integers

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

Edge Cases:
-

D: Data Structures
-------------------------
- int

Notes
-------------------------
- import statistics
- statistics.mean()
- sum function

A: Algorithm (Step-by-step)
-------------------------
1. Import statistics
2. Pass the list numbers to the function average
3. Return the integer of the average using the statistics.mean function

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

import statistics

def average(numbers):
    return int(statistics.mean(numbers))

# or

def average(numbers):
    return sum(numbers) // len(numbers) # // results in an integer value being calculated

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

# ==========
# LS Solution
# ==========

def average(numbers):
    total = sum(numbers)
    return total // len(numbers)