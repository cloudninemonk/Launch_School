'''
Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting number of a sequence that your function will create. The function should return a list containing the same number of elements as the count argument. The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0. The starting number can be any integer. If the count is 0, the function should return an empty list.

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- integers

Output:
- function return -> list
- program output -> boolean

Rules (Explicit):
- count always greater than or equal to 0
- starting integer can be of any value - positive or negative or 0.
- count of 0, results in an empty list

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

Edge Cases:
-

D: Data Structures
-------------------------
- range
- list

Notes
-------------------------
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Pass the integers count and start to the function sequence.
2. Iterate through a range count as the end value
3. On each iteration, add the result of the iteration counter + 1 by the start number to the list numbers
4. Return numbers

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def sequence(count, start):
    return [i * start for i in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

# ==========
# LS Solution
# ==========

def sequence(count, start_num):
    return [start_num * num for num in range(1, count + 1)]