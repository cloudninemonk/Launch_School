'''
Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
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
- function return -> integer
- program output -> boolean

Rules (Explicit):
- Reverse each digit within the integer
- integer is positive

Rules (Implicit/Inferred):
- integers are at least a single digit

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

Edge Cases:
-

D: Data Structures
-------------------------
- str
- int

Notes
-------------------------
- Reverse slicing

A: Algorithm (Step-by-step)
-------------------------
1. Pass the integer to the function reverse_number
2. Determine the reverse of the str of the integer
3. Return the int of the reversed string

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def reverse_number(number):
    return int(str(number)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

# ==========
# LS Solution
# ==========

def reverse_number(number):
    return int(str(number)[::-1])

