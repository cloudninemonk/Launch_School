'''
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
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
- function return -> string
- program output -> boolean

Rules (Explicit):
-

Rules (Implicit/Inferred):
- string can be empty
- characters can be anything

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

Edge Cases:
-

D: Data Structures
-------------------------
-

Notes
-------------------------
- generator
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Return the joining of the generator where each charater is multiplied by 2.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def repeater(text):
    return ''.join(char * 2 for char in text)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")

# ==========
# LS Solution
# ==========
def repeater(string):
    return ''.join([char * 2 for char in string])